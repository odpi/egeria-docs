<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Cohort Registry Store Connectors

A [cohort registry store connector](/concepts/cohort-registry-store-connector) stores the registration information that the [cohort registry](/concepts/cohort-registry) of a cohort member exchanges with the other members of a cohort.  It holds the local server's own registration, and the registrations of each of the remote members, so that the registrations survive a restart of the server.

The definition of the connector interface for a cohort registry store connector is
defined in the [repository-services-apis :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis){ target=gh } module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.cohortregistrystore :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/cohortregistrystore){ target=gh } Java package.

In that package you will see the following Java classes:

* `OMRSCohortRegistryStore` - the interface for the connector.  Its methods are:
    * `saveLocalRegistration`, `retrieveLocalRegistration` and `removeLocalRegistration` - maintain the registration of the local server.
    * `saveRemoteRegistration`, `retrieveRemoteRegistrations`, `retrieveRemoteRegistration` (by metadata collection id) and `removeRemoteRegistration` - maintain the registrations of the other members of the cohort.
    * `clearAllRegistrations` - removes the local and remote registrations when the local server has unregistered from the cohort.
    * `close` - flushes all changes and closes the store.
* `OMRSCohortRegistryStoreConnectorBase` - the abstract base class for the connector.  It extends `ConnectorBase` and implements `OMRSCohortRegistryStore` and `AuditLoggingComponent`, so the connector receives an audit log for its messages.
* `OMRSCohortRegistryStoreProviderBase` - the abstract base class for the connector provider.  It extends `OpenConnectorProviderBase`.
* The `properties` package contains `MemberRegistration`, which describes the registration of a single cohort member, and `CohortMembership`, which is the structure of the registry store as a whole.

## Example Implementation

An implementation of this connector is located in the
[adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh } module.  The `FileBasedRegistryStoreConnector` stores the registrations in a JSON file.  The name of the file is taken from the network address of the endpoint in its connection, or defaults to `cohort.registry` if no endpoint is supplied.

## Writing the Connector Provider

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

The connector provider for a cohort registry store connector extends `OMRSCohortRegistryStoreProviderBase`.  Egeria's file-based connector is described by `EgeriaOpenConnectorDefinition.JSON_FILE_COHORT_REGISTRY_STORE`.

--8<-- "snippets/abbr.md"
