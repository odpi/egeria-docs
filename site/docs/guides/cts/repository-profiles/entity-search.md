<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Search Profile

The technology under test supports the ability to search for entity instances.

## Entity property search

The technology under test supports the search and retrieval of current metadata instances from its repository based on matching specific property values. This tests the [`findEntitiesByProperty` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-property-search-101FEBP` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty is supported |
    | [`repository-entity-property-search-03` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-04` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty returned `0` unexpected results using parameters: `...` |
    | [`repository-entity-property-search-05` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-06` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty returned `0` unexpected results using parameters: `...` |
    | [`repository-entity-property-search-09` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-10` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty returned `0` unexpected results using parameters: `...` |
    | [`repository-entity-property-search-105` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty with null match parameters found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-106` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty with null match parameters returned `0` unexpected results using parameters: `...` |

## Entity value search

The technology under test supports the search and retrieval of current metadata instances from its repository based on matching any values. This tests the [`findEntitiesByPropertyValue` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-property-search-101FEBPV` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue is supported |
    | [`repository-entity-property-search-07` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-08` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue returned `0` unexpected results using parameters: `...` |

## Entity condition search

The technology under test supports the search and retrieval of current metadata instances from its repository based on matching logical combinations of property conditions. This tests the [`findEntities` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-property-search-101FE` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntities using SearchProperties is supported |
    | [`repository-entity-property-search-103` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntities using SearchProperties with general regex found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-104` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntities using SearchProperties with general regex returned `0` unexpected results using parameters: `...` |
    | [`repository-entity-property-search-107` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntities with null match parameters found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-108` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntities with null match parameters returned `0` unexpected results using parameters: `...` |
