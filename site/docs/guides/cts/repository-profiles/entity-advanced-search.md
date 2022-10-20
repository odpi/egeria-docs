<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Advanced Search Profile

The technology under test supports the use of regular expressions to search for metadata instances.

## Advanced property search

The technology under test supports the use of regular expressions within match properties to search for entity instances. This tests the [`findEntitiesByProperty` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-property-search-101FEBPGEN` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty supports general regular expressions |
    | [`repository-entity-property-search-13` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty with general regex found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-14` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByProperty with general regex returned `0` unexpected results using parameters: `...` |

## Advanced value search

The technology under test supports the use of regular expressions within value search criteria to search for entity instances. This tests the [`findEntitiesByPropertyValue` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-entity-property-search-101FEBPVGEN` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue supports general regular expressions |
    | [`repository-entity-property-search-11` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue with general regex found `n/n` expected results using parameters: `...` |
    | [`repository-entity-property-search-12` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedEntitySearch.java){ target=gh } | findEntitiesByPropertyValue with general regex returned `0` unexpected results using parameters: `...` |
