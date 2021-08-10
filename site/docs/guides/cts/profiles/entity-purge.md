---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity purge profile

The performance of programmatically hard-deleting (irreversibly) existing entity instances.

The [Open Metadata Repository Services (OMRS)](/egeria/services/omrs) interface for a metadata
repository defines optional methods for hard-deleting entity instances:

| Method | Description |
|---|---|
| `purgeEntity` | completely removes an entity instance homed in the technology under test (including all of its history) |
| `purgeEntityReferenceCopy` | completely removes an entity instance that is homed somewhere other than the technology under test (including all of its history) |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-purge-performance-purgeEntity` | See (3) in detailed logic below. |
    | `repository-entity-purge-performance-purgeEntityReferenceCopy` | See (5) in detailed logic below. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entity GUIDs homed in the technology under test. (This uses `findEntitiesByProperty`
   with a condition on `metadataCollectionId` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity GUIDs, `deleteEntity` is called to soft-delete the instance. (This is necessary before a
   hard-delete can be done against the instance and its performance is recorded as part of the [entity delete](entity-delete.md) profile.)
1. For each of these entity GUIDs, a `purgeEntity` is then called to hard-delete the instance.
1. Searches for `instancesPerType` reference copy entities. (This uses `findEntitiesByProperty` with a condition on
   `metadataCollectionId` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these reference copy entity instances, `purgeEntityReferenceCopy` is called to remove the reference copy
   instance.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is
    set to 100, then this profile will remove 50 (types) x 100 (instances per type) x 3 (home + reference copy methods) = 15 000
    entities. (And it will run `findEntitiesByProperty` 100 times.)

--8<-- "snippets/abbr.md"
