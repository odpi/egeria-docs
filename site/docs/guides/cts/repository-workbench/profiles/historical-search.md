<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Historical Search Profile

The technology under test supports search for the state of the metadata instances at a specific time in the past.

## Historical property queries

The technology under test supports the point in time search and retrieval of metadata instances from its repository based on specific property values. Currently, this only tests the [`getEntityDetail` and `getRelationship` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } methods of the `OMRSMetadataCollection` interface (with a historical timestamp).

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-lifecycle-27` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | historical retrieval returned correct version of entity |
    | [`repository-entity-lifecycle-31` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | repository supports historic retrieval |
    | [`repository-relationship-lifecycle-25` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | historical retrieval returned correct version relationship |
    | [`repository-relationship-lifecycle-31` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntityLifecycle.java){ target=gh } | repository supports historic retrieval |

## Historical value queries

The technology under test supports the point in time search and retrieval of metadata instances from its repository based on arbitrary values.

!!! attention "Not yet implemented"
