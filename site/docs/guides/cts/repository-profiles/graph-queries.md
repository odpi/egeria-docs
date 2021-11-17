<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Graph Queries Profile

The technology under test supports graph-like queries that return collections of metadata instances.

## Entity neighborhood

The technology under test supports the ability to query metadata instances that radiate from a specific entity instance through multiple hops. This tests the [`getEntityNeighborhood` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-graph-queries-01` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned a result. |
    | [`repository-graph-queries-02` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned the expected number of entities. |
    | [`repository-graph-queries-03` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned all the expected entities. |
    | [`repository-graph-queries-04` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned the expected number of relationships. |
    | [`repository-graph-queries-05` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned all the expected relationships. |
    | [`repository-graph-queries-14` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | repository supports getEntityNeighborhood |

## Connected entities

The technology under test supports the ability to query the entity instances that are connected to a specific entity instance. This tests the [`getRelatedEntities` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-graph-queries-06` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned the expected number of related entities. |
    | [`repository-graph-queries-07` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned all the expected related entities. |
    | [`repository-graph-queries-15` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | repository supports getRelatedEntities |

## Linked entities

The technology under test supports the ability to locate the metadata instances that connect two entity instances together. This tests the [`getLinkingEntities` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-graph-queries-08` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | getLinkedEntities found `n/n` expected entities using parameters: `...` |
    | [`repository-graph-queries-09` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned all the expected entities. |
    | [`repository-graph-queries-10` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned the expected number of relationships. |
    | [`repository-graph-queries-11` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | graph query returned all the expected relationships. |
    | [`repository-graph-queries-16` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestGraphQueries.java){ target=gh } | repository supports getRelatedEntities |
