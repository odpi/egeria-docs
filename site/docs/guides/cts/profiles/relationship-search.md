---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship search profile

The performance of programmatically searching for existing relationship instances.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines optional methods for searching for relationship instances:

| Method | Description |
|---|---|
| `findRelationships` | arbitrarily complex combinations of search criteria including ranges, nested conditions, etc |
| `findRelationshipsByProperty` | searches for relationship instances based on specific properties with specific values |
| `findRelationshipsByPropertyValue` | searches for relationship instances based on text that matches any textual property |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-relationship-search-performance-findRelationships-all-p...` | This profile begins by interrogating the technology under test in its entirety, to discover every existing relationship instance of every type known to Egeria. The total count of these is tallied to report later under the [environment](environment.md) profile. In this way, even for repositories that do not support write operations, we can still calculate some metrics about read performance (including search) while being able to understand that information in light of the volumes of metadata in the repository while the test was executed. These searches are also performed with basic sorting of results, and all pages of results are retrieved (the `p...` portion indicates a specific page number): thereby also exercising the efficiency of the technology under test to both sort and cycle through pages of results. |
    | `repository-relationship-search-performance-findRelationshipsByPropertyValue-exact` | Repository performs search with an exact text value, sorting by oldest creation time, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByPropertyValue-start` | Repository performs search with a text value 'starts-with', sorting by newest creation time, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByPropertyValue-contains` | Repository performs search with a text value 'contains', sorting by oldest update time, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByPropertyValue-end` | Repository performs search with a text value 'ends-with', sorting by newest update time, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByPropertyValue-regex` | Repository performs search with a regular expression text value, sorting by GUID, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByProperty-one` | Repository performs search by a single property value, sorting by that property, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByProperty-all` | Repository performs search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByProperty-any` | Repository performs search by two property values, sorting by the second property, of first page of instances of a type. |
    | `repository-relationship-search-performance-findRelationshipsByProperty-none` | Repository performs search by two property value, sorting by the first property, of first page of instances of a type. |
    | `repository-relationship-delete-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship delete](relationship-delete.md) profile. |
    | `repository-relationship-purge-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship purge](relationship-purge.md) profile. |
    | `repository-relationship-purge-performance-findRelationshipsByProperty-rc` | See the detailed logic of the [relationship purge](relationship-purge.md) profile. |
    | `repository-relationship-re-home-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship re-home](relationship-re-home.md) profile. |
    | `repository-relationship-re-identify-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship re-identify](relationship-re-identify.md) profile. |
    | `repository-relationship-restore-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship restore](relationship-restore.md) profile. |
    | `repository-relationship-retrieval-performance-findRelationships` | See the detailed logic of the [relationship retrieval](relationship-retrieval.md) profile. |
    | `repository-relationship-retype-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship retype](relationship-retype.md) profile. |
    | `repository-relationship-undo-performance-findRelationships` | See the detailed logic of the [relationship undo](relationship-undo.md) profile. |
    | `repository-relationship-update-performance-findRelationshipsByProperty` | See the detailed logic of the [relationship update](relationship-update.md) profile. |

In addition, these tests will record into the Environment profile the `totalRelationshipsFound`.

!!! tip "Search variations"
    When `findRelationshipsByProperty` is run by the assertions starting with `repository-relationship-search-performance...`,
    the tests prefer non-string properties (if any exist for the type) given that the `findRelationshipsByPropertyValue`
    searches will already heavily exercise string-based queries.

    Note that the various other assertions (that do _not_ start with `repository-relationship-search-performance...`) will
    search on various other properties than those listed: in particular, including header properties like
    `metadataCollectionId`, `version`, and others.

--8<-- "snippets/abbr.md"
