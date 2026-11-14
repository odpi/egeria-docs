<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship Search Profile

The technology under test supports the ability to search for relationnship instances.

## Relationship property search

The technology under test supports the search and retrieval of current relationship instances from its repository based on matching specific property values. This tests the [`findRelationshipsByProperty` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-property-search-02` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | repository does not support an entity type that can be used to test relationship type `<typeName>`. |
    | [`repository-relationship-property-search-04` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-05` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty returned `0` unexpected results using parameters: `...`. |
    | [`repository-relationship-property-search-06` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-07` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty returned `0` unexpected results using parameters: `...`. |
    | [`repository-relationship-property-search-10` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-11` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty returned `0` unexpected results using parameters: `...`. |
    | [`repository-relationship-property-search-105` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty with null match parameters found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-106` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByProperty with null match parameters returned `0` unexpected results using parameters: `...`. |

## Relationship value search

The technology under test supports the search and retrieval of current relationship instances from its repository based on matching any values. This tests the [`findRelationshipsByPropertyValue` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-property-search-08` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByPropertyValue found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-09` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationshipsByPropertyValue found `0` unexpected results using parameters: `...`. |

## Relationship condition search

The technology under test supports the search and retrieval of current metadata instances from its repository based on matching logical combinations of property conditions. This tests the [`findRelationships` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface.

It also tests that paging through the results follows the paging contract: an empty list means the page was filtered empty and the caller should ask for the next page, and null means there are no more results. See the [relationship paging test case](../test-cases/repository-relationship-paging-test-case.md).

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`repository-relationship-property-search-103` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationships found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-104` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationships found `0` unexpected results using parameters: `...`. |
    | [`repository-relationship-property-search-107` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationships with null match parameters found `n/n` expected results using parameters: `...`. |
    | [`repository-relationship-property-search-108` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipSearch.java){ target=gh } | findRelationships with null match parameters returned `0` unexpected results using parameters: `...`. |
    | [`repository-relationship-paging-01` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipPaging.java){ target=gh } | no page of relationships holds more than the page size requested |
    | [`repository-relationship-paging-02` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipPaging.java){ target=gh } | no relationship is returned on more than one page |
    | [`repository-relationship-paging-03` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipPaging.java){ target=gh } | paging through findRelationships reaches every relationship that a single search returns |
    | [`repository-relationship-paging-04` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipPaging.java){ target=gh } | the end of the relationships is signalled by null, not by an empty list |
    | [`repository-relationship-paging-05` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestSupportedRelationshipPaging.java){ target=gh } | a page requested beyond the last relationship is null |
