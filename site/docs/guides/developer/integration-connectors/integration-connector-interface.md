<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


An integration connector can:

- Listen on a blocking call, waiting for the third party technology to send a notification.
- Register with an external notification service that sends notifications on its own thread.
- Register a listener with its context to act on notifications from the partner OMAS's [Out Topic](/concepts/out-topic).
- Poll the third party technology each time that the `refresh()` method is called.

The [Open Metadata Integration Services (OMISs)](/services/omis) each define the interface that an integration connector must implements if they are to run under that service.  The interfaces for each integration service is listed in the table below.

| Integration Service | Type of technology supported | Link to integration connector base class |
|---|---|---|
| [Analytics Integrator OMIS](/services/omis/analytics-integrator/overview) | Data Assets and Glossary Terms | [`AnalyticsIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/analytics-integrator/analytics-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/analytics/connector){ target=gh } class. |
| [API Integrator OMIS](/services/omis/api-integrator/overview) | API Schemas | [`APIIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/api-integrator/api-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/api/connector){ target=gh } class. |
| [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) | Assets and related metadata found in an Asset Catalog | [`CatalogIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/catalog-integrator/catalog-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/catalog/connector){ target=gh } class. |
| [Database Integrator OMIS](/services/omis/database-integrator/overview) | Databases and their schema | [`DatabaseIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/database-integrator/database-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/database/connector){ target=gh } class. |
| [Display Integrator OMIS](/services/omis/display-integrator/overview) | Forms, reports and the queries they depend on | [`DisplayIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/display-integrator/display-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/display/connector){ target=gh } class. |
| [Files Integrator OMIS](/services/omis/files-integrator/overview) | Files and their internal structure | [`FilesIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/files-integrator/files-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/files/connector){ target=gh } class. |
| [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) | IT infrastructure landscape such as hosts, platforms and servers | [`InfrastructureIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/infrastructure-integrator/infrastructure-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/infrastructure/connector){ target=gh } class. |
| [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) | Processes and their execution flow | [`LineageIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/lineage-integrator/lineage-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/lineage/connector){ target=gh } class. |
| [Organization Integrator OMIS](/services/omis/organization-integrator/overview) | People, teams, roles  and user identities | [`OrganizationIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/organization-integrator/organization-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/organization/connector){ target=gh } class. |
| [Search Integrator OMIS](/services/omis/search-integrator/overview) | Content for search indexes relating to assets. | [`SearchIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/search-integrator/search-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/search/connector){ target=gh } class. |
| [Security Integrator OMIS](/services/omis/security-integrator/overview) | Publishing information about users and resources. | [`SecurityIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/security-integrator/security-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/security/connector){ target=gh } class. |
| [Topic Integrator OMIS](/services/omis/topic-integrator/overview) | Event topics and the structure of the events they share. | [`TopicIntegratorConnector` :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/topic-integrator/topic-integrator-api/src/main/java/org/odpi/openmetadata/integrationservices/topic/connector){ target=gh } class. |

All of these base classes define the shape of the context object that the integration connector uses to query and maintain open metadata. They also all inherit from (extend) the [`IntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/governance-servers/integration-daemon-services/integration-daemon-services-api/src/main/java/org/odpi/openmetadata/governanceservers/integrationdaemonservices/connectors/IntegrationConnectorBase.java){ target=gh }.  This interface defines the lifecycle methods of the integration connector that are summarized in figure 1.

![Figure 1](/guides/developer/integration-connectors/integration-connector-methods.svg)
> **Figure 1:** Methods implemented by an integration connector

- `initialize` is a standard method for all connectors that is called by the [connector broker](/concepts/connector-broker) when a request is made to create an instance of the connector. The connector broker uses the initialize method to pass the [connection](/concepts/connection) object used to create the connector instance and a unique identifier for this instance of the connector.

- `setAuditLog` provides a [Audit Log Framework (ALF)](/frameworks/alf/overview) compatible logging destination.

- `setConnectorName` provides the name of the connector from the configuration so it can be used for logging.

- `setContext` sets up the integration service specific context object. This provides an interface to the services of the OMAS that the integration service is paired with. Although the interfaces vary from integration service to integration service, they typically offer the following types of method call for each type of metadata it supports:

    - The ability to register a listener to receive events from the OMAS's [Out Topic](/concepts/out-topic), or send events to the OMAS's [In Topic](/concepts/in-topic).
    - The ability to create and update metadata instances.
    - For assets, the ability to change an asset's visibility by changing its zone membership using the `publish` and `withdraw` methods.
    - The ability to delete metadata.
    - Various retrieval methods to help when comparing the metadata in the open metadata repositories with the metadata in the third party technology.
    
- `start` indicates that the connector is completely configured and can begin processing. This call can be used to register with non-blocking services. For example, it can register a listener for events from the OMAS [Out Topic](/concepts/out-topic) through the context.

- `engage` is used when the connector is configured to need to issue blocking calls to wait for new metadata. It is called from its own thread. It is recommended that the `engage()` method returns when each blocking call completes. The integration daemon will pause a second and then call `engage()` again. This pattern enables the calling thread to detect the shutdown of its hosting integration daemon server.

- `refresh` requests that the connector does a comparison of the metadata in the third party technology and open metadata repositories. Refresh is called:

    1. when the integration connector first starts and then
    1. at intervals defined in the connector's configuration as well as
    1. any external REST API calls to explicitly refresh the connector.
    
- `disconnect` is called when the server is shutting down. The connector should free up any resources that it holds since it is not needed any more.  Once disconnect has been called the context is no longer valid.

