<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Instance Versions Profile

The technology under test is able to return the list of versions of an instance that are stored.  The commands (`getEntityDetailHistory()` and `getRelationshipHistory()`) include a time period to limit the number of versions that the repository needs to return. 

## Get entity instances

The technology under test supports the command to retrieve the versions of an entity.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-lifecycle-32` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions NOT returned before create time |
    | [`repository-entity-lifecycle-33` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions returned after create |
    | [`repository-entity-lifecycle-34` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions returned after update |
    | [`repository-entity-lifecycle-35` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions NOT returned while deleted |
    | [`repository-entity-lifecycle-36` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions returned after restore |
    | [`repository-entity-lifecycle-37` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions are ordered BACKWARDS as requested |
    | [`repository-entity-lifecycle-38` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions NOT returned after purge |
    | [`repository-entity-lifecycle-40` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions not returned during deleted period |
    | [`repository-entity-lifecycle-41` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | `<typeName>` entity versions are ordered FORWARDS as requested |


## Get relationship instances

The technology under test supports the broadcasting of instance re-homed events to other members of the cohort.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-lifecycle-32` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions NOT returned before create time |
    | [`repository-relationship-lifecycle-33` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions returned after create |
    | [`repository-relationship-lifecycle-34` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions returned after update |
    | [`repository-relationship-lifecycle-35` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions NOT returned while deleted |
    | [`repository-relationship-lifecycle-36` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions returned after restore |
    | [`repository-relationship-lifecycle-37` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions are ordered BACKWARDS as requested |
    | [`repository-relationship-lifecycle-38` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions NOT returned after purge |
    | [`repository-relationship-lifecycle-40` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions not returned during deleted period |
    | [`repository-relationship-lifecycle-41` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipLifecycle.java){ target=gh } | `<typeName>` relationship versions are ordered FORWARDS as requested |


