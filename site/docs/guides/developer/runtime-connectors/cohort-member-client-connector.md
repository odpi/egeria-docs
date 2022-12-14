<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Writing Cohort Member Client Connectors

---8<-- "docs/connectors/runtime/cohort-member-client-connector-intro.md"

Egeria's [Open Metadata Repository Services (OMRS)](/services/omrs) provides a default REST API implementation and a corresponding client:

* [REST Cohort Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/omrs-rest-repository-connector){ target=gh }
  supports remote calls to the OMRS REST API.
  
The connection for this connector is configured in the `LocalRepositoryRemoteConnection` property of the
cohort member's [Local Repository Configuration](/user/guides/admin/servers/configuring-a-metadata-access-point/#configure-the-local-repository).

The definition of the connector interface for these connectors is
defined in the [repository-services-api :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis){ target=gh } module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector){ target=gh } Java package.
It is the same interface as the [repository connectors](/concepts/repository-connector) that are used to provide the local repository to a metadata server
so that the Open Metadata Repository Services (OMRS)
issue calls to the same interface irrespective of whether the call is to the local repository or a remote cohort member.

---8<-- "snippets/abbr.md"
