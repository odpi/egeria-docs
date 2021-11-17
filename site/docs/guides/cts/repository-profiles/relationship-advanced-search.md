<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship Advanced Search Profile

The technology under test supports the use of regular expressions to search for relationship instances.

## Advanced property search

The technology under test supports the use of regular expressions within match properties to search for relationship instances. This tests the [`findRelationshipsByProperty` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-property-search-14` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty with general regex found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-15` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty with general regex found `0` unexpected results using parameters: `...`. |

## Advanced value search

The technology under test supports the use of regular expressions within value search criteria to search for relationship instances. This tests the [`findRelationshipsByPropertyValue` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-property-search-12` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByPropertyValue with general regex found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-13` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByPropertyValue with general regex found `0` unexpected results using parameters: `...`. |
