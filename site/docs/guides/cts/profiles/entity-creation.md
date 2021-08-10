---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity creation profile

The performance of programmatically creating new entity instances.

The [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) interface for a metadata
repository defines optional methods for creating entity instances:

| Method | Description |
|---|---|
| `addEntity` | adds a new entity instance, where the technology under test is the home repository for that instance |
| `saveEntityReferenceCopy` | adds (or updates) an existing entity instance, where the technology under test is _not_ the home repository for that instance |

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | `repository-entity-creation-performance-addEntity` | Invocation of the `addEntity` method during the profile (see detailed logic below). |
    | `repository-entity-creation-performance-saveEntityReferenceCopy` | Invocation of the `saveEntityReferenceCopy` method during the profile (see detailed logic below). |

For every entity type supported by the technology under test, this profile invokes each of these methods `instancesPerType`
times.

!!! example "Example"
    So, for example, if the technology under test supports 50 entity types, and the `instancesPerType` parameter is set to
    100, then this profile will create 50 (types) x 100 (instances per type) x 2 (home + non-home methods) = 10 000 entity
    instances.

The properties of each of these instances will be fully-populated with:

- Any string properties containing a value representative of the property name itself (and where unique, such as
  `qualifiedName`, they will be made unique through appending a unique sequence)
- Any non-string properties will be randomly generated, in a simple attempt to represent data that is not entirely
  uniform

In addition, these tests will record into the [environment](environment.md) profile the `totalEntitiesCreated`.

--8<-- "snippets/abbr.md"
