---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship delete profile

The performance of programmatically soft-deleting an existing relationship instance.

The [Open Metadata Repository Services (OMRS)](/egeria/services/omrs) interface for a metadata
repository defines an optional method for deleting relationship instances:

| Method | Description |
|---|---|
| `deleteRelationship` | soft-deletes the current version of a relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-delete-performance-deleteRelationship` | See (2) in detailed logic below. |
    | `repository-relationship-purge-performance-deleteRelationship` | See detailed logic of [relationship purge](relationship-purge.md) profile. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` relationships of that type. (This uses `findRelationshipsByProperty` with a condition
   on `metadataCollectionId` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
1. For each of these relationship instances, `deleteRelationship` is called to soft-delete it.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is
    set to 100, then this profile will soft-delete 50 (types) x 100 (instances per type) = 5000
    relationships. (And it will run `findRelationshipsByProperty` 50 times.)

--8<-- "snippets/abbr.md"
