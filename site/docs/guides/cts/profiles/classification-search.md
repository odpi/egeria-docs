---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Classification search profile

The performance of programmatically searching for existing entities based on their classification(s).

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines an optional method for searching for entity instances based on classification:

| Method | Description |
|---|---|
| `findEntitiesByClassification` | searches for entity instances based on specific classifications or properties of classifications with specific values |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-classification-search-performance-findEntitiesByClassification-all` | Repository performs search for both of two classification property values, sorting by most recent update date, of first page of instances for a classification. |
    | `repository-classification-search-performance-findEntitiesByClassification-alone` | Repository performs search by classification alone (no properties), sorting by most recent creation date, of first page of instances for a classification. |
    | `repository-classification-search-performance-findEntitiesByClassification-any` | Repository performs search for either of two classification property values, sorting by oldest update date, of first page of instances for a classification. |
    | `repository-classification-search-performance-findEntitiesByClassification-none` | Repository performs search for neither of two classification property values, sorting by entity GUID, of first page of instances for a classification. |
    | `repository-classification-search-performance-findEntitiesByClassification-one` | Repository performs search by a single classification property value, sorting by oldest creation date, of first page of instances for a classification. |
    | `repository-classification-update-performance-findEntitiesByClassification` | Repository performs search for unordered first instancesPerType instances with a classification. |
    | `repository-entity-declassification-performance-findEntitiesByClassification` | Repository performs search for unordered first instancesPerType instances with a classification. |
    | `repository-entity-declassification-performance-findEntitiesByClassification-rc` | Repository performs search for unordered first instancesPerType reference copy classifications. |

--8<-- "snippets/abbr.md"
