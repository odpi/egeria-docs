#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright Contributors to the Egeria project.
"""
Example housekeeping script: permanently remove (purge) soft-deleted metadata
from an Egeria metadata access store once it is older than a retention period.

When Egeria soft-deletes an element, the repository keeps it (with status
DELETED) so that it can be restored if it was deleted in error.  Over time these
elements build up.  This script finds soft-deleted entities and relationships
that belong to the server's own metadata collection, checks how long ago each
one was deleted against a retention policy, and purges those that are past it.

It is an EXAMPLE to download and adapt.  Your organization decides which types
of element are purged and how long they are kept - edit RETENTION_POLICY below,
or supply a JSON file with --policy.

Safety:
  * It runs as a DRY RUN unless --purge is given: it reports what it would purge.
  * Only types named in the policy are purged ("*" matches every other type).
  * Only elements whose home is this server's metadata collection are purged;
    reference copies from other cohort members are left alone.
  * Elements archived with a Memento classification (to preserve lineage) are
    not in DELETED status, so they are never touched.
  * --max-purges caps the number of purges in one run.
  * Purging cannot be undone.  Take a database backup first.

Run it from cron (or any scheduler), for example nightly at 02:30:

    30 2 * * * EGERIA_USER=garygeeke EGERIA_USER_PASSWORD=... \\
        /usr/bin/python3 /opt/egeria/purge-deleted-elements.py \\
        --platform-url https://egeria.example.com:9443 \\
        --server qs-metadata-store --policy /opt/egeria/retention.json --purge \\
        >> /var/log/egeria/purge.log 2>&1

The exit code is 0 on success and 1 if any purge failed, so a scheduler can alert.

Requires Python 3.9+ and nothing outside the standard library.
"""

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------------------------------
# Retention policy: open metadata type name -> days to keep after deletion.
# Subtypes are included, so "Referenceable" covers most entity types.
# "*" applies to any type not named.  Remove "*" to purge only named types.
# Relationship types use the same table.
# ---------------------------------------------------------------------------
RETENTION_POLICY = {
    "SearchKeyword": 30,
    "SearchKeywordLink": 30,
    "*": 365,
}

PAGE_SIZE = 500


class EgeriaClient:
    """Minimal REST client for the repository services of one metadata access store."""

    def __init__(self, platform_url, server, user_id, password, verify_tls):
        self.platform_url = platform_url.rstrip("/")
        self.user_id = user_id
        self.base = (f"{self.platform_url}/servers/{server}"
                     f"/open-metadata/repository-services/users/{user_id}")
        self.ssl_context = ssl.create_default_context()
        if not verify_tls:
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE
        self.token = self._post(f"{self.platform_url}/api/token",
                                {"userId": user_id, "password": password},
                                raw=True)

    def _post(self, url, body, raw=False):
        headers = {"Content-Type": "application/json"}
        if not raw:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                                         headers=headers, method="POST")
        with urllib.request.urlopen(request, context=self.ssl_context, timeout=300) as response:
            text = response.read().decode("utf-8")
        if raw:
            return text.strip()
        result = json.loads(text) if text else {}
        if result.get("relatedHTTPCode", 200) != 200:
            raise RuntimeError(f"{result.get('exceptionClassName')}: {result.get('exceptionErrorMessage')}")
        return result

    def metadata_collection_id(self):
        return self._post(f"{self.base}/metadata-collection-id",
                          {"class": "GetRequest"})["metadataCollectionId"]

    def type_def(self, type_name):
        """Return (guid, category) for a type; category is ENTITY_DEF, RELATIONSHIP_DEF or CLASSIFICATION_DEF."""
        result = self._post(f"{self.base}/types/typedef/name/{type_name}", {"class": "GetRequest"})
        return result["typeDef"]["guid"], result["typeDef"]["category"]

    def find_deleted(self, kind, type_guid=None):
        """Yield every soft-deleted entity or relationship (optionally of one type and its subtypes)."""
        request_class = "EntityFindRequest" if kind == "entities" else "RelationshipFindRequest"
        offset = 0
        while True:
            body = {"class": request_class,
                    "limitResultsByStatus": ["DELETED"],
                    "offset": offset,
                    "pageSize": PAGE_SIZE}
            if type_guid:
                body["typeGUID"] = type_guid
            page = self._post(f"{self.base}/instances/{kind}", body).get(kind) or []
            yield from page
            if len(page) < PAGE_SIZE:
                return
            offset += PAGE_SIZE

    def purge(self, kind, instance):
        noun = "entity" if kind == "entities" else "relationship"
        self._post(f"{self.base}/instances/{noun}/{instance['guid']}/purge",
                   {"class": "TypeDefValidationForRequest",
                    "typeDefGUID": instance["type"]["typeDefGUID"],
                    "typeDefName": instance["type"]["typeDefName"]})


def parse_time(value):
    # Egeria returns e.g. 2026-11-10T10:56:25.809+00:00
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main():
    parser = argparse.ArgumentParser(description="Purge soft-deleted Egeria metadata older than a retention period.")
    parser.add_argument("--platform-url", default=os.environ.get("EGERIA_PLATFORM_URL", "https://localhost:9443"))
    parser.add_argument("--server", default=os.environ.get("EGERIA_METADATA_STORE", "qs-metadata-store"),
                        help="the metadata access store whose repository is cleaned")
    parser.add_argument("--user", default=os.environ.get("EGERIA_USER"))
    parser.add_argument("--policy", help="JSON file mapping type name to days to keep; overrides the built-in policy")
    parser.add_argument("--purge", action="store_true", help="actually purge; without this the script is a dry run")
    parser.add_argument("--max-purges", type=int, default=10000, help="stop after this many purges in one run")
    parser.add_argument("--insecure", action="store_true", help="do not verify the platform's TLS certificate")
    args = parser.parse_args()

    password = os.environ.get("EGERIA_USER_PASSWORD")
    if not args.user or password is None:
        parser.error("set EGERIA_USER and EGERIA_USER_PASSWORD (or use --user) - "
                     "the password is only read from the environment")

    policy = RETENTION_POLICY
    if args.policy:
        with open(args.policy, encoding="utf-8") as policy_file:
            policy = json.load(policy_file)

    mode = "PURGE" if args.purge else "DRY RUN"
    now = datetime.now(timezone.utc)
    print(f"{now.isoformat()} {mode} on {args.server} at {args.platform_url}, policy {policy}")

    client = EgeriaClient(args.platform_url, args.server, args.user, password, not args.insecure)
    home_collection = client.metadata_collection_id()

    # One search per named type (which also returns its subtypes), in the order the
    # policy lists them, then one search for everything else if "*" is present.
    # An element takes the retention of its own type if that is named; otherwise that
    # of the first search that found it - so list specific types before general ones.
    searches = {"entities": [], "relationships": []}
    for type_name in policy:
        if type_name == "*":
            continue
        guid, category = client.type_def(type_name)
        if category == "ENTITY_DEF":
            searches["entities"].append((type_name, guid))
        elif category == "RELATIONSHIP_DEF":
            searches["relationships"].append((type_name, guid))
        else:
            print(f"Ignoring {type_name}: classifications are removed with their entity")
    if "*" in policy:
        for kind in searches:
            searches[kind].append(("*", None))

    purged, failed, kept, skipped = 0, 0, 0, 0
    # Relationships first: purging an entity also removes its relationships.
    for kind in ("relationships", "entities"):
        if purged + failed >= args.max_purges:
            break
        seen = set()
        candidates = []
        for policy_type, type_guid in searches[kind]:
            for instance in client.find_deleted(kind, type_guid):
                if instance["guid"] in seen:
                    continue
                seen.add(instance["guid"])
                if instance.get("metadataCollectionId") != home_collection:
                    skipped += 1          # a reference copy - its home server owns it
                    continue
                days = policy.get(instance["type"]["typeDefName"], policy[policy_type])
                deleted_at = parse_time(instance.get("updateTime") or instance["createTime"])
                if now - deleted_at < timedelta(days=days):
                    kept += 1
                    continue
                candidates.append(instance)

        for instance in candidates:
            if purged + failed >= args.max_purges:
                print(f"Reached --max-purges {args.max_purges}; stopping")
                break
            label = f"{instance['type']['typeDefName']} {instance['guid']} deleted {instance.get('updateTime')}"
            if not args.purge:
                print(f"would purge {label}")
                purged += 1
                continue
            try:
                client.purge(kind, instance)
                print(f"purged {label}")
                purged += 1
            except (RuntimeError, urllib.error.URLError) as error:
                # For example, the element was restored, or already purged with its entity.
                print(f"FAILED {label}: {error}", file=sys.stderr)
                failed += 1

    verb = "purged" if args.purge else "to purge"
    print(f"{datetime.now(timezone.utc).isoformat()} done: {purged} {verb}, {kept} within retention, "
          f"{skipped} reference copies skipped, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
