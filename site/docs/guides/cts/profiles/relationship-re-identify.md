---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship re-identify profile

The performance of programmatically changing the GUID of an existing relationship instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for changing the GUID of relationship instances:

| Method | Description |
|---|---|
| `reIdentifyRelationship` | changes the GUID of an existing relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-re-identify-performance-reIdentifyRelationship` | See (2) in detailed logic below. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` homed relationship GUIDs of that type. (This uses `findRelationshipsByProperty`
   with a condition on `metadataCollectionId` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
1. For each of these relationship GUIDs, `reIdentifyRelationship` is called to change its GUID to a new random GUID.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is
    set to 100, then this profile will re-identify 50 (types) x 100 (instances per type) = 5000
    relationships. (And it will run `findRelationshipsByProperty` 50 times.)

--8<-- "snippets/abbr.md"
