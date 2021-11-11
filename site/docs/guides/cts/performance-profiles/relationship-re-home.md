---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship Re-Home Profile

The performance of programmatically changing the home repository of an existing relationship instance.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for changing the home repository of relationship instances:

| Method | Description |
|---|---|
| `reHomeRelationship` | changes the home repository of a relationship |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-re-home-performance-reHomeRelationship` | See (2) in detailed logic below. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` reference copy relationship GUIDs of that type. (This uses `findRelationshipsByProperty` with a condition on `metadataCollectionId` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
1. For each of these relationship GUIDs, `reHomeEntity` is called to change the home repository to the technology under test's `metadataCollectionId`.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is set to 100, then this profile will re-home 50 (types) x 100 (instances per type) = 5000 relationships. (And it will run `findRelationshipsByProperty` 50 times.)

--8<-- "snippets/abbr.md"
