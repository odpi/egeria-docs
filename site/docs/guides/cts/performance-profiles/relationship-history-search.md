---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship History Search Profile

The performance of programmatically searching for relationship instances as they existed in the past.

The [Open Metadata Repository Services (OMRS)](/services/omrs) interface for a metadata repository defines optional methods for searching for relationship instances based on their details in the past, by passing in an `asOfTime` parameter (captured during the execution of the [relationship update](relationship-update.md) profile):

| Method | Description |
|---|---|
| `findRelationships` | arbitrarily complex combinations of search criteria including ranges, nested conditions, etc |
| `findRelationshipsByProperty` | searches for relationship instances based on specific properties with specific values |
| `findRelationshipsByPropertyValue` | searches for relationship instances based on text that matches any textual property |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-search-history-performance-findRelationships-all-p...` | Interrogates the technology under test for each relationship type, by calling `findRelationships` for that type GUID with an `asOfTime` using the timestamp captured prior to the execution of the [relationship update](relationship-update.md) profile. These tests are performed without any explicit sorting of results, and all pages of results are retrieved (the `p...` portion indicates a specific page number): thereby also exercising the efficiency of the technology under test to consistently cycle through pages of results. |
    | `repository-relationship-search-history-performance-findRelationshipsByPropertyValue-exact` | Repository performs historical search with an exact text value, sorting by oldest creation time, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByPropertyValue-start` | Repository performs historical search with a text value 'starts-with', sorting by newest creation time, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByPropertyValue-contains` | Repository performs historical search with a text value 'contains', sorting by oldest update time, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByPropertyValue-end` | Repository performs historical search with a text value 'ends-with', sorting by newest update time, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByPropertyValue-regex` | Repository performs historical search with a regular expression text value, sorting by GUID, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByProperty-one` | Repository performs historical search by a single property value, sorting by that property, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByProperty-all` | Repository performs historical search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByProperty-any` | Repository performs historical search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-relationship-search-history-performance-findRelationshipsByProperty-none` | Repository performs historical search by two property value, sorting by the first property, of first page of instances of a type. |
    | `repository-relationship-history-retrieval-performance-findRelationships` | See the detailed logic of the [relationship retrieval](relationship-retrieval.md) profile. |

!!! tip "Search variations"
    When `findRelationshipsByProperty` is run by the assertions starting with `repository-relationship-search-history-performance...`, the tests prefer non-string properties (if any exist for the type) given that the `findRelationshipsByPropertyValue` searches will already heavily exercise string-based queries.

--8<-- "snippets/abbr.md"
