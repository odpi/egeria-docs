<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Rehome Instance Profile

The technology under test supports the command to update the metadata collection id for a metadata instance.

## Update instance home

The technology under test supports the command to update the metadata collection id for a metadata instance.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-reference-copy-lifecycle-18` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityReferenceCopyLifecycle.java){ target=gh } | reference entity re-homed. This tests the [`reHomeEntity` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-reference-copy-lifecycle-19` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityReferenceCopyLifecycle.java){ target=gh } | rehomed master entity has been retrieved. This tests the [`getEntityDetail` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-entity-reference-copy-lifecycle-20` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityReferenceCopyLifecycle.java){ target=gh } | rehomed master entity has correct home metadataCollectionId. This tests the [`getEntityDetail` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-relationship-reference-copy-lifecycle-17` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipReferenceCopyLifecycle.java){ target=gh } | reference relationship re-homed. This tests the [`reHomeRelationship` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-relationship-reference-copy-lifecycle-18` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipReferenceCopyLifecycle.java){ target=gh } | rehomed master relationship has been retrieved. This tests the [`getRelationship` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |
    | [`repository-relationship-reference-copy-lifecycle-19` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipReferenceCopyLifecycle.java){ target=gh } | rehomed master relationship has correct home metadataCollectionId. This tests the [`getRelationship` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. |

## Send re-homed event

The technology under test supports the broadcasting of instance re-homed events to other members of the cohort.

!!! attention "Not yet implemented"

## Process re-homed event

The technology under test supports the receipt/processing of instance re-homed events from other members of the cohort.

!!! attention "Not yet implemented"
