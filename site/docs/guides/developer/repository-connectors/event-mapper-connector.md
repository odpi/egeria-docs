<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Event mapper connectors

An [event mapper connector](/concepts/event-mapper-connector) runs alongside an adapter [repository connector](/concepts/repository-connector) in a [repository proxy](/concepts/repository-proxy).  It listens for the changes that are made to the metadata in a third party metadata repository through the repository's own interfaces, and converts them into OMRS events that are sent to the other members of the cohort.

## Interface and base classes

The interface and base classes are in the *repository-services-apis* module in the [org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryeventmapper :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryeventmapper){ target=gh } Java package:

* `OMRSRepositoryEventMapper` - the interface for the connector.  The OMRS uses it to pass the connector the information it needs: `initialize` (with the name of the event mapper and the repository connector for the third party repository), `setRepositoryHelper`, `setRepositoryValidator`, `setServerName`, `setServerType`, `setOrganizationName`, `setServerUserId`, `setMetadataCollectionId` and `setRepositoryEventProcessor`.
* `OMRSRepositoryEventMapperBase` - the abstract base class to extend.  It (through `OMRSRepositoryEventMapperConnector`) extends `ConnectorBase` and implements `OMRSRepositoryEventMapper` and `AuditLoggingComponent`.  It saves the values passed by the OMRS in protected variables, such as `repositoryConnector`, `repositoryHelper`, `localMetadataCollectionId`, `localServerName` and `repositoryEventProcessor`.
* `OMRSRepositoryEventMapperProviderBase` - the abstract base class for the connector provider.  It extends `OpenConnectorProviderBase`.
* `OMRSRepositoryEventProcessor` - the abstract class of the component that receives the events from the event mapper.  It implements `OMRSTypeDefEventProcessorInterface` and `OMRSInstanceEventProcessorInterface`.

When the event mapper detects a change in the third party repository, it uses the repository connector to retrieve any additional information it needs, and the repository helper to build the instance, and then calls the matching method on the `repositoryEventProcessor` - for example `processNewEntityEvent`, `processUpdatedEntityEvent`, `processClassifiedEntityEvent`, `processDeletedEntityEvent` or `processNewRelationshipEvent`.  Each method takes the name of the source, the originator's metadata collection id, server name, server type and organization name, followed by the instance.  The event processor that the OMRS supplies sends these events to the cohorts that the repository proxy is registered with.

The event mapper is created and started along with the repository connector.  Use the `start()` method to begin listening to the third party repository, and `disconnect()` to stop.

## Configuring the event mapper

The event mapper is configured in a repository proxy with a `POST` request to `/open-metadata/admin-services/servers/{serverName}/local-repository/event-mapper-details?connectorProvider={connectorProviderClassName}&eventSource={eventSource}`.  The `eventSource` is set as the network address of the endpoint in the event mapper's connection, and the optional request body is a map of configuration properties.  Alternatively, pass a complete connection to `.../local-repository/event-mapper-connection`.  See [Configuring a Repository Proxy](/guides/admin/servers/by-server-type/configuring-a-repository-proxy).

## Implementations

Since each event mapper connector is tied to a third party
technology, core Egeria does not supply any implementations of
this connector.  The [Event mapper for Apache Atlas :material-github:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=gh } was an example; its repository has been archived and is no longer maintained.

--8<-- "snippets/abbr.md"
