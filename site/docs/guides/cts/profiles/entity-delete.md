---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity delete profile

The performance of programmatically soft-deleting an existing entity instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for deleting entity instances:

| Method | Description |
|---|---|
| `deleteEntity` | soft-deletes the current version of an entity |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-delete-performance-deleteEntity` | See (2) in detailed logic below. |
    | `repository-entity-purge-performance-deleteEntity` | See detailed logic of [entity purge](entity-purge.md) profile. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entities of that type. (This uses `findEntitiesByProperty` with a condition
   on `metadataCollectionId` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity instances, `deleteEntity` is called to soft-delete it.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is
    set to 100, then this profile will soft-delete 50 (types) x 100 (instances per type) = 5000
    entities. (And it will run `findEntitiesByProperty` 50 times.)

--8<-- "snippets/abbr.md"
