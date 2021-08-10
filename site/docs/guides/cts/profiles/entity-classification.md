---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity classification profile

The performance of programmatically classifying existing entity instances with new classifications.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines optional methods for classifying entity instances:

| Method | Description |
|---|---|
| `classifyEntity` | adds a new classification to an existing entity instance, where the technology under test is the home repository for that classification |
| `saveEntityReferenceCopy` | adds (or updates) an entity instance with a classification, where the technology under test is _not_ the home repository for that classification |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-classification-performance-classifyEntity` | See (2) in detailed logic below. |
    | `repository-entity-classification-performance-saveClassificationReferenceCopy` | See (4) in detailed logic below. |

For every classification type supported by the technology under test, this profile does the following (in order):

1. Searches for `instancesPerType` entities of a type that is valid for the classification. (This uses `findEntities`
   and its performance is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these entity instances, `classifyEntity` is called to add a new classification of this type to that
   instance, using a generated set of properties.
1. Searches for `instancesPerType` entities of a type that is valid for the classification, and where the entity is a
   reference copy. (This uses `findEntitiesByProperty` with a condition on `metadataCollectionId` and its performance
   is recorded as part of the [entity search](entity-search.md) profile.)
1. For each of these reference copy entity instances, `saveClassificationReferenceCopy` is called to add reference copy
   classification of this type to that instance, using a generated set of properties.

!!! example "Example"
    So, for example, if the technology under test supports 50 classification types, and the `instancesPerType` parameter is
    set to 100, then this profile will create 50 (types) x 100 (instances per type) x 2 (home + reference copy methods) = 10 000
    classifications. (And it will run `findEntities` 50 times, and `findEntitiesByProperty` 50 times.)

The properties of each of these instances will be fully-populated with:

- Any string properties containing a value representative of the property name itself (and where unique,
  they will be made unique through appending a unique sequence)
- Any non-string properties will be randomly generated, in a simple attempt to represent data that is not entirely
  uniform

--8<-- "snippets/abbr.md"
