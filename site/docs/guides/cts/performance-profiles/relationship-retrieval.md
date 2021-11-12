---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship Retrieval Profile

The performance of programmatically retrieving existing relationship instances based on their ID.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata repository defines methods for retrieving relationship instances by their ID:

| Method | Description |
|---|---|
| `isRelationshipKnown` | retrieves a relationship instance's details, if available, or returns null if not |
| `getRelationship` | retrieves a relationship instance's details, if available, or throws an exception if not |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-retrieval-performance-isRelationshipKnown` | See (2) in detailed logic below. |
    | `repository-relationship-retrieval-performance-getRelationship` | See (3) in detailed logic below. |

For every relationship type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` relationship GUIDs of that type. (This uses `findRelationships` and its performance is recorded as part of the [relationship search](relationship-search.md) profile.)
1. For each of these relationship GUIDs, `isRelationshipKnown` is called to retrieve it.
1. For each of these relationship GUIDs, `getRelationship` is then called to retrieve its details.

!!! example "Example"
    So, for example, if the technology under test supports 50 relationship types, and the `instancesPerType` parameter is set to 100, then this profile will retrieve 50 (types) x 100 (instances per type) x 2 (operations) = 10 000 relationships. (And it will run `findRelationships` 50 times.)

!!! attention "Caveats"
    Note the following caveats:

    - The same GUIDs are used for each retrieval, but each method is run against every GUID before moving onto the next method.

--8<-- "snippets/abbr.md"
