---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Graph History Queries Profile

The performance of programmatically retrieving inter-related instances across potentially multiple degrees of separation, for a given point in time.

The [Open Metadata Repository Services (OMRS)](/services/omrs) interface for a metadata repository defines methods for retrieving inter-related metadata instances across several degrees at a given point in time in the past, by passing in an `asOfTime` parameter (captured during the execution of the [entity update](entity-update.md) profile):

| Method | Description |
|---|---|
| `getRelationshipsForEntity` | retrieves the first-degree relationships linked to an entity |
| `getEntityNeighborhood` | retrieves the relationships and entities linked to an entity, up to a specified number of degrees of separation |
| `getRelatedEntities` | retrieves the entities linked to an entity, both directly and indirectly |
| `getLinkingEntities` | retrieves the relationships and entities that exist between (ultimately connecting) two entities |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-graph-history-query-performance-getRelationshipsForEntity` | See (2) in detailed logic below. |
    | `repository-graph-history-query-performance-getEntityNeighborhood-...` | See (3) in detailed logic below. |
    | `repository-graph-history-query-performance-getRelatedEntities` | See (4) in detailed logic below. |
    | `repository-graph-history-query-performance-getLinkingEntities` | See (5) in detailed logic below. |

For every entity type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entity GUIDs of that type. (This uses `findEntities` and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity GUIDs, `getRelationshipsForEntity` is called with an `asOfTime` using the timestamp captured prior to the execution of the [entity update](entity-update.md) profile, to retrieve first-degree relationships.
1. For each of these entity GUIDs, `getEntityNeighborhood` is then called with an `asOfTime` using the timestamp captured prior to the execution of the [entity update](entity-update.md) profile, 3 times to retrieve that entity's 1st, 2nd and 3rd degree relationships.
1. For each of these entity GUIDs, `getRelatedEntities` is then called with an `asOfTime` using the timestamp captured prior to the execution of the [entity update](entity-update.md) profile, to retrieve _all_ the entities that are either directly or indirectly related to this entity. These results, per entity, are stored in a Map for the next step.
1. For each of these entity GUIDs, `getLinkingEntities` is then called with an `asOfTime` using the timestamp captured prior to the execution of the [entity update](entity-update.md) profile, up to 3 times: using the first related entity from the test above, the last related entity from the test above, and an entity from the middle of the list of the results from the test above.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is set to 100, then this profile will run 50 (types) x 100 (instances per type) x 8 (maximum operation variations) = 40 000 (at most) queries. (And it will run the initial `findEntities` 50 times.)

!!! attention "Caveats"
    Note the following caveats:

    - The same GUIDs are used for each retrieval, but each method is run against every GUID before moving onto the next method.
    - The `getLinkingEntities` tests are only run if both the `getRelatedEntities` and `getLinkingEntities` methods are included (not skipped via `methodsToSkip`).

!!! danger "Beware"
    Be aware that the number of relationships quickly increases for operations like `getRelatedEntities`, which furthermore is not paged. For example, even when running at a relatively small 10 `instancesPerType` there will be many instances that individually have more than 1000 related entities. You will therefore probably want to skip this method when running at any `instancesPerType` beyond 10-20 to avoid result sets that will go into the 10 000s.

--8<-- "snippets/abbr.md"
