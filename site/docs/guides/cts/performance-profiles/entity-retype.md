---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Retype Profile

The performance of programmatically changing the type of an existing entity instance.

The [Open Metadata Repository Services (OMRS)](/services/omrs) interface for a metadata repository defines an optional method for changing the type of entity instances:

| Method | Description |
|---|---|
| `reTypeEntity` | changes the type of an existing entity |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-retype-performance-reTypeEntity-toSubtype` | See (3) in detailed logic below. |
    | `repository-entity-retype-performance-reTypeEntity-toSupertype` | See (4) in detailed logic below. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` homed entity GUIDs of that type. (This uses `findEntitiesByProperty`
   with a condition on `metadataCollectionId` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
2. For each of these entity GUIDs, `updateEntityProperties` is called to remove all the entity's properties (so it can be easily retyped), and its performance is recorded as part of the [entity update](entity-update.md) profile.
3. For each of these entity GUIDs, `reTypeEntity` is called to change the type of the entity to one of its subtypes.
4. For each of these entity GUIDs, `reTypeEntity` is then called to change the type of the entity back to its original type.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is set to 100, then this profile will retype 50 (types) x 100 (instances per type) x 2 (operations) = 10 000 entities at most. (And it will run `findEntitiesByProperty` 50 times.)

!!! attention "Caveats"
    Note the following caveats:

    - Instances of a given type will only be retyped if that type has any subtypes: if it has no subtypes, then all retyping operations will be skipped for that type's instances.

--8<-- "snippets/abbr.md"
