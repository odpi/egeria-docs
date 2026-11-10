<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Writing Cohort Member Client Connectors

A [cohort member client connector](/concepts/cohort-member-client-connector) is used by the [Open Metadata Repository Services (OMRS)](/services/omrs) to issue federated queries to the other members of a [cohort](/concepts/cohort-member).  Each cohort member advertises the connection for its client connector when it registers with the cohort, and the other members use this connection to create the connector that calls it.

Egeria's OMRS provides a default REST API implementation and a corresponding client:

* [REST Cohort Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/omrs-rest-repository-connector){ target=gh } supports remote calls to the OMRS REST API.  Its connector provider is `OMRSRESTRepositoryConnectorProvider`, its connector is `OMRSRESTRepositoryConnector` and its metadata collection is `OMRSRESTMetadataCollection`.

The connection for this connector is configured in the `localRepositoryRemoteConnection` property of the cohort member's `LocalRepositoryConfig` in its [configuration document](/concepts/configuration-document).  It is set up automatically when the local repository is configured - see [Repository Services Section](/guides/admin/servers/by-section/repository-services-section).

The definition of the cohort member client connector interface is
defined in the [repository-services-apis :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis){ target=gh } module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector){ target=gh } Java package.
It is the same interface - the `OMRSRepositoryConnector` abstract class and the `OMRSMetadataCollection` it returns - as the [repository connectors](/concepts/repository-connector) that are used to provide the local repository to a metadata access store,
so that the OMRS
issues calls to the same interface irrespective of whether the call is to the local repository or to a remote cohort member.  See [Writing Repository Connectors](/guides/developer/repository-connectors/overview) for details of this interface.

---8<-- "snippets/abbr.md"
