---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity history search profile

The performance of programmatically searching for entity instances as they existed in the past.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata repository defines optional methods for searching for entity instances based on their details in the past, by passing in an `asOfTime` parameter (captured during the execution of the [entity update](entity-update.md) profile):

| Method | Description |
|---|---|
| `findEntities` | arbitrarily complex combinations of search criteria including ranges, nested conditions, etc |
| `findEntitiesByProperty` | searches for entity instances based on specific properties with specific values |
| `findEntitiesByPropertyValue` | searches for entity instances based on text that matches any textual property |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-search-history-performance-findEntities-all-p...` | Interrogates the technology under test for each entity type, by calling `findEntities` for that type GUID with an `asOfTime` using the timestamp captured prior to the execution of the [entity update](entity-update.md) profile. These searches are performed without any explicit sorting of results, and all pages of results are retrieved (the `p...` portion indicates a specific page number): thereby also exercising the efficiency of the technology under test to consistently cycle through pages of results. |
    | `repository-entity-search-history-performance-findEntitiesByPropertyValue-exact` | Repository performs historical search with an exact text value, sorting by oldest creation time, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByPropertyValue-start` | Repository performs historical search with a text value 'starts-with', sorting by newest creation time, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByPropertyValue-contains` | Repository performs historical search with a text value 'contains', sorting by oldest update time, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByPropertyValue-end` | Repository performs historical search with a text value 'ends-with', sorting by newest update time, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByPropertyValue-regex` | Repository performs historical search with a regular expression text value, sorting by GUID, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByProperty-one` | Repository performs historical search by a single property value, sorting by that property, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByProperty-all` | Repository performs historical search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByProperty-any` | Repository performs historical search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-entity-search-history-performance-findEntitiesByProperty-none` | Repository performs historical search by two property value, sorting by the first property, of first page of instances of a type. |
    | `repository-entity-history-retrieval-performance-findEntities` | See the detailed logic of the [entity retrieval](entity-retrieval.md) profile. |
    | `repository-graph-history-query-performance-findEntities` | See the detailed logic of the [graph history query](graph-history-query.md) profile. |

!!! tip "Search variations"
    When `findEntitiesByProperty` is run by the assertions starting with `repository-entity-search-history-performance...`, the tests prefer non-string properties (if any exist for the type) given that the `findEntitiesByPropertyValue` searches will already heavily exercise string-based queries.

--8<-- "snippets/abbr.md"
