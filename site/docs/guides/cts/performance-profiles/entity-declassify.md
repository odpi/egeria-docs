---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity declassification profile

The performance of programmatically declassifying existing entity instances from existing classifications.

The [Open Metadata Repository Services (OMRS)](/services/omrs) interface for a metadata repository defines optional methods for declassifying entity instances:

| Method | Description |
|---|---|
| `declassifyEntity` | removes a classification from an existing entity instance, where the technology under test is the home repository for that classification |
| `purgeClassificationReferenceCopy` | removes a classification from an existing entity instance, where the technology under test is _not_ the home repository for that classification |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-declassification-performance-declassifyEntity` | See (2) in detailed logic below. |
    | `repository-entity-declassification-performance-purgeClassificationReferenceCopy` | See (4) in detailed logic below. |

For every classification type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entities homed in the technology under test with the classification. (This uses `findEntitiesByClassification` with a condition on `metadataCollectionId` and its performance is recorded as part of the [classification search](classification-search.md) profile.)
1. For each of these entity instances, `declassifyEntity` is called to remove the classification of this type from that instance.
1. Searches for `instancesPerType` reference copy entities with the classification. (This uses `findEntitiesByClassification` with a condition on `metadataCollectionId` and its performance is recorded as part of the [classification search](classification-search.md) profile.)
1. For each of these reference copy entity instances, `purgeClassificationReferenceCopy` is called to remove the reference copy classification of this type from that instance.

!!! example "Example"
    So, for example, if the technology under test supports 50 classification types, and the `instancesPerType` parameter is set to 100, then this profile will remove 50 (types) x 100 (instances per type) x 2 (home + reference copy methods) = 10 000 classifications. (And it will run `findEntitiesByClassification` 100 times.)

--8<-- "snippets/abbr.md"
