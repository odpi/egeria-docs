---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship restore profile

The performance of programmatically reversing the latest soft-delete of an existing relationship instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for reverting soft-deletes on relationship instances:

| Method | Description |
|---|---|
| `restoreRelationship` | reverts the last soft-delete that was made to a relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-restore-performance-restoreRelationship` | See (2) in detailed logic below. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` relationship GUIDs of that type that have been soft-deleted. (This uses `findRelationshipsByProperty`
   with a condition to limit to the status `DELETED` only and its performance is recorded as part of the [relationship
   search](relationship-search.md) profile.)
1. For each of these relationship GUIDs, `restoreRelationship` is called to revert the soft-delete and make the relationship
   active again.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is
    set to 100, then this profile will re-activate 50 (types) x 100 (instances per type) = 5000
    relationships. (And it will run `findRelationshipsByProperty` 50 times.)

--8<-- "snippets/abbr.md"
