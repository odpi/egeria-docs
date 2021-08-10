---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity re-identify profile

The performance of programmatically changing the GUID of an existing entity instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for changing the GUID of entity instances:

| Method | Description |
|---|---|
| `reIdentifyEntity` | changes the GUID of an existing entity |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-re-identify-performance-reIdentifyEntity` | See (2) in detailed logic below. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` homed entity GUIDs of that type. (This uses `findEntitiesByProperty`
   with a condition on `metadataCollectionId` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity GUIDs, `reIdentifyEntity` is called to change the GUID of the entity to a new random GUID.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is
    set to 100, then this profile will re-identify 50 (types) x 100 (instances per type) = 5000
    entities. (And it will run `findEntitiesByProperty` 50 times.)

--8<-- "snippets/abbr.md"
