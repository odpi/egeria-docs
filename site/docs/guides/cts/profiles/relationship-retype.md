---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship retype profile

The performance of programmatically changing the type of an existing relationship instance.

The [Open Metadata Repository Services (OMRS)](/egeria/services/omrs) interface for a metadata
repository defines an optional method for changing the type of relationship instances:

| Method | Description |
|---|---|
| `reTypeRelationship` | changes the type of an existing relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-retype-performance-reTypeEntity-toSubtype` | See (3) in detailed logic below. |
    | `repository-relationship-retype-performance-reTypeEntity-toSupertype` | See (4) in detailed logic below. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` homed relationship GUIDs of that type. (This uses `findRelationshipsByProperty`
   with a condition on `metadataCollectionId` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
2. For each of these relationship GUIDs, `updateRelationshipProperties` is called to remove all the relationship's properties (so it can be easily retyped),
   and its performance is recorded as part of the [relationship update](relationship-update.md) profile.
3. For each of these relationship GUIDs, `reTypeRelationship` is called to change the type of the relationship to one of its subtypes.
4. For each of these relationship GUIDs, `reTypeRelationship` is then called to change the type of the relationship back to its original type.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is
    set to 100, then this profile will retype 50 (types) x 100 (instances per type) x 2 (operations) = 10 000
    relationships at most. (And it will run `findRelationshipsByProperty` 50 times.)

!!! attention "Caveats"
    Note the following caveats:

    - Instances of a given type will only be retyped if that type has any subtypes: if it has no subtypes, then all
      retyping operations will be skipped for that type's instances.
    - Currently there are no open metadata relationship types that have supertypes or subtypes, so this profile will
      not actually have any metadata instance against which to call `reTypeRelationship`.

--8<-- "snippets/abbr.md"
