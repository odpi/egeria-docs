---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity search profile

The performance of programmatically searching for existing entity instances.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines optional methods for searching for entity instances:

| Method | Description |
|---|---|
| `findEntities` | arbitrarily complex combinations of search criteria including ranges, nested conditions, etc |
| `findEntitiesByProperty` | searches for entity instances based on specific properties with specific values |
| `findEntitiesByPropertyValue` | searches for entity instances based on text that matches any textual property |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-search-performance-findEntities-all-p...` | Interrogates the technology under test in its entirety, to discover every existing entity instance of every type known to Egeria. The total count of these is tallied to report later under the [environment](environment.md) profile. In this way, even for repositories that do not support write operations, we can still calculate some metrics about read performance (including search) while being able to understand that information in light of the volumes of metadata in the repository while the test was executed. These searches are also performed without any explicit sorting of results, and all pages of results are retrieved (the `p...` portion indicates a specific page number): thereby also exercising the efficiency of the technology under test to consistently cycle through pages of results. |
    | `repository-entity-search-performance-findEntitiesByPropertyValue-exact` | Repository performs search with an exact text value, sorting by oldest creation time, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByPropertyValue-start` | Repository performs search with a text value 'starts-with', sorting by newest creation time, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByPropertyValue-contains` | Repository performs search with a text value 'contains', sorting by oldest update time, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByPropertyValue-end` | Repository performs search with a text value 'ends-with', sorting by newest update time, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByPropertyValue-regex` | Repository performs search with a regular expression text value, sorting by GUID, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByProperty-one` | Repository performs search by a single property value, sorting by that property, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByProperty-all` | Repository performs search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByProperty-any` | Repository performs search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-entity-search-performance-findEntitiesByProperty-none` | Repository performs search by two property value, sorting by the first property, of first page of instances of a type. |
    | `repository-entity-classification-performance-findEntities` | See the detailed logic of the [entity classification](entity-classification.md) profile. |
    | `repository-entity-classification-performance-findEntitiesByProperty` | See the detailed logic of the [entity classification](entity-classification.md) profile. |
    | `repository-entity-delete-performance-findEntitiesByProperty` | See the detailed logic of the [entity delete](entity-delete.md) profile. |
    | `repository-entity-purge-performance-findEntitiesByProperty` | See the detailed logic of the [entity purge](entity-purge.md) profile. |
    | `repository-entity-purge-performance-findEntitiesByProperty-rc` | See the detailed logic of the [entity purge](entity-purge.md) profile. |
    | `repository-entity-re-home-performance-findEntitiesByProperty` | See the detailed logic of the [entity re-home](entity-re-home.md) profile. |
    | `repository-entity-re-identify-performance-findEntitiesByProperty` | See the detailed logic of the [entity re-identify](entity-re-identify.md) profile. |
    | `repository-entity-restore-performance-findEntitiesByProperty` | See the detailed logic of the [entity restore](entity-restore.md) profile. |
    | `repository-entity-retrieval-performance-findEntities` | See the detailed logic of the [entity retrieval](entity-retrieval.md) profile. |
    | `repository-entity-retype-performance-findEntitiesByProperty` | See the detailed logic of the [entity retype](entity-retype.md) profile. |
    | `repository-entity-undo-performance-findEntities` | See the detailed logic of the [entity undo](entity-undo.md) profile. |
    | `repository-entity-update-performance-findEntitiesByProperty` | See the detailed logic of the [entity update](entity-update.md) profile. |
    | `repository-graph-query-performance-findEntities` | See the detailed logic of the [graph query](graph-query.md) profile. |
    | `repository-relationship-creation-performance-findEntities` | See the detailed logic of the [relationship creation](relationship-creation.md) profile. |

In addition, these tests will record into the Environment profile the `totalEntitiesFound`.

!!! tip "Search variations"
    When `findEntitiesByProperty` is run by the assertions starting with `repository-entity-search-performance...`,
    the tests prefer non-string properties (if any exist for the type) given that the `findEntitiesByPropertyValue`
    searches will already heavily exercise string-based queries.

    Note that the various other assertions (that do _not_ start with `repository-entity-search-performance...`) will
    search on various other properties than those listed: in particular, including header properties like
    `metadataCollectionId`, `version`, and others.

--8<-- "snippets/abbr.md"
