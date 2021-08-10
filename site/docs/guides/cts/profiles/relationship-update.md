---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship update profile

The performance of programmatically updating existing relationship instances.

The [Open Metadata Repository Services (OMRS)](/egeria/services/omrs) interface for a metadata
repository defines optional methods for updating relationship instances:

| Method | Description |
|---|---|
| `updateRelationshipProperties` | changes one or more values of the properties on an existing relationship |
| `updateRelationshipStatus` | changes the status of an existing relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-update-performance-updateEntityProperties` | See (2) in detailed logic below. |
    | `repository-relationship-retype-performance-updateEntityProperties-remove` | See the detailed logic of the [relationship retype](relationship-retype.md) profile. |

!!! tip "Captures timestamp for historical metadata profiles"
    Prior to this profile running, a timestamp is captured by the performance workbench to denote a specific date and time
    prior to any updates having been made to the relationships.

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` relationships of that type. (This uses `findRelationshipsByProperty` with a condition on
   `metadataCollectionId` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
1. For each of these relationship instances, `updateRelationshipProperties` is called to update the existing property values of the
   relationship, using a new generated set of properties.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is
    set to 100, then this profile will update 50 (types) x 100 (instances per type) = 5000
    relationships. (And it will run `findRelationshipsByProperty` 50 times.)

The properties of each of these instances will be fully-populated with:

- Any string properties containing a value representative of the property name itself (and where unique,
  they will be made unique through appending a unique sequence)
- Any non-string properties will be randomly generated, in a simple attempt to represent data that is not entirely
  uniform

!!! attention "Caveats"
    Note the following caveats:

    - `updateRelationshipStatus` is currently not tested (there are very few types that support any status that can be updated outside of a delete or restore operation).
    - Relationship type definitions that have no properties will not be updated, since there are no properties to update.

--8<-- "snippets/abbr.md"
