<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Proxies Profile

The technology under test is able to store stubs for entities to use on relationships when the full entity is not available.

## Store entity proxies

The technology under test supports the storage of metadata instances that are proxies for instances from other repositories in the cohort. This tests the [`addEntityProxy` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-proxy-lifecycle-2` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | repository does not support creation of entity proxies for type `<typeName>` |

## Retrieve entity proxies

The technology under test supports the command to retrieve a proxy instance of a metadata instance.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-proxy-lifecycle-03` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | repository supports retrieval of entity proxy as an EntitySummary for type `<typeName>`. This tests the [`getEntitySummary` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-proxy-lifecycle-04` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | repository disallows retrieval of entity proxy as an EntityDetail for type `<typeName>`. This tests the [`getEntityDetail` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-proxy-lifecycle-05` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | repository disallows isEntityKnown for entity proxy for type `<typeName>`. This tests the [`isEntityKnown` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |

## Entity proxy locking

The technology under test ensures metadata instances that are proxies for instances from other repositories can not be updated.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-proxy-lifecycle-09` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | entity proxy status cannot be updated. This tests the [`updateEntityStatus` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-proxy-lifecycle-10` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | entity proxy properties cannot be updated. This tests the [`updateEntityProperties` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-proxy-lifecycle-11` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | entity proxy type cannot be updated. This tests the [`reTypeEntity` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-proxy-lifecycle-12` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | entity proxy identity cannot be updated. This tests the [`reIdentifyEntity` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |

## Entity proxy delete

The technology under test ensures that proxy instances are removed from its repository with integrity when the master copy is deleted. This tests the [`getEntitySummary` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-proxy-lifecycle-08` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityProxyLifecycle.java){ target=gh } | repository supports delete of entity proxy of type |
