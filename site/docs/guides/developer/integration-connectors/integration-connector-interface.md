<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


An integration connector can:

- Listen on a blocking call, waiting for the third party technology to send a notification.
- Register with an external notification service that sends notifications on its own thread.
- Register a listener with its context to act on notifications from the partner OMAS's [Out Topic](/concepts/out-topic).
- Poll the third party technology each time that the integration daemon calls your integration connector's  `refresh()` method.
- Issue queries and maintenance (create, update, delete) requests to the open metadata repositories.

Access to open metadata is provided via a *context* object.  The [Open Metadata Integration Services (OMISs)](/services/omis) each provide a context object that is specialized for a particular category of third party technology in order to provide the most optimal interface to open metadata for your integration connector. This typically includes:

- The ability to register a listener to receive events from the OMAS's [Out Topic](/concepts/out-topic), or send events to the OMAS's [In Topic](/concepts/in-topic).
- The ability to create and update metadata instances.
- For assets, the ability to change an asset's visibility by changing its zone membership using the `publish` and `withdraw` methods.
- The ability to delete metadata.
- Various retrieval methods to help when comparing the metadata in the open metadata repositories with the metadata in the third party technology.

Each integration service defines the base class that an integration connector must implement if they are to run under that service.  The base classes differ only in the type of context object that they support.  Select the integration service, and hence the base class, to use for your integration connector from the table below.

| Integration Service | Type of technology supported | Link to integration connector base class                                                                                                                                                                                                                                                                      |
|---|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [API Integrator OMIS](/services/omis/api-integrator/overview) | API Schemas | [APIIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/api/connector/APIIntegratorConnector.html) class.                                                                                                                                                                                                                                                                             |
| [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) | Assets and related metadata found in an Asset Catalog | [CatalogIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/catalog/connector/CatalogIntegratorConnector.html) class.                             |
| [Database Integrator OMIS](/services/omis/database-integrator/overview) | Databases and their schema | [DatabaseIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/database/connector/DatabaseIntegratorConnector.html) class.                        |
| [Display Integrator OMIS](/services/omis/display-integrator/overview) | Forms, reports and the queries they depend on | [DisplayIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/display/connector/DisplayIntegratorConnector.html) class.                           |
| [Files Integrator OMIS](/services/omis/files-integrator/overview) | Files and their internal structure | [FilesIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/files/connector/FilesIntegratorConnector.html) class.                                   |
| [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) | IT infrastructure landscape such as hosts, platforms and servers | [InfrastructureIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/infrastructure/connector/InfrastructureIntegratorConnector.html) class. |
| [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) | Processes and their execution flow | [LineageIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/lineage/connector/LineageIntegratorConnector.html) class.       |
| [Origanization Integrator OMIS](/services/omis/organization-integrator/overview) | Onboard teams, profiles and users | [OrganizationIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/organization/connector/OrganizationIntegratorConnector.html) |
| [Search Integrator OMIS](/services/omis/search-integrator/overview) | Content for search indexes relating to assets. | [SearchIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/search/connector/SearchIntegratorConnector.html) class.                               |
| [Security Integrator OMIS](/services/omis/security-integrator/overview) | Publishing information about users and resources. | [SecurityIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/security/connector/SecurityIntegratorConnector.html) class.                       |
| [Topic Integrator OMIS](/services/omis/topic-integrator/overview) | Event topics and the structure of the events they share. | [TopicIntegratorConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/integrationservices/topic/connector/TopicIntegratorConnector.html) class.                                   |

The context object is a wrapper around the client of an [Open Metadata Access Service (OMAS)](/services/omas).  It is accessed by the integration connector using the `getContext()` method.  The OMAS supplies the properties, open metadata listener interface and event structures for the API.

![OMIS OMAS Pair](/services/integration-daemon-omis-omas-pair.svg)

Therefore, you need to add dependencies for your selected OMIS's API module and the API module of is partner OMAS.  This is shown in the table below:

| Integration Service | Partner OMAS | Dependencies |
|---|---|---|
| [API Integrator OMIS](/services/omis/api-integrator/overview) | [Data Manager OMAS](/services/omas/data-manager/overview) | api-integrator-api, data-manager-api |
| [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) | [Asset Manager OMAS](/services/omas/asset-manager/overview) | catalog-integrator-api, asset-manager-api |
| [Database Integrator OMIS](/services/omis/database-integrator/overview) | [Data Manager OMAS](/services/omas/data-manager/overview) | database-integrator-api, data-manager-api  |
| [Display Integrator OMIS](/services/omis/display-integrator/overview) | [Data Manager OMAS](/services/omas/data-manager/overview) | display-integrator-api, data-manager-api  |
| [Files Integrator OMIS](/services/omis/files-integrator/overview) | [Data Manager OMAS](/services/omas/data-manager/overview) | files-integrator-api, data-manager-api  |
| [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) | [IT infrastructure OMAS](/services/omas/it-infrastructure/overview) | infrastructure-integrator-api, it-infrastructure-api  |
| [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) | [Asset Manager OMAS](/services/omas/asset-manager/overview) | lineage-integrator-api, asset-manager-api  |
| [Organization Integrator OMIS](/services/omis/organization-integrator/overview) | [Community Profile OMAS](/services/omas/community-profile/overview) | organization-integrator-api, community-profile-api  |
| [Search Integrator OMIS](/services/omis/search-integrator/overview) | [Asset Catalog OMAS](/services/omas/asset-catalog/overview) | search-integrator-api, asset-catalog-api  |
| [Security Integrator OMIS](/services/omis/security-integrator/overview) | [Security Manager OMAS](/services/omas/security-manager/overview) | security-integrator-api, security-manager-api  |
| [Topic Integrator OMIS](/services/omis/topic-integrator/overview) | [Data Manager OMAS](/services/omas/data-manager/overview) | topic-integrator-api, data-manager-api  |

These dependencies are in addition to the standard dependencies for an integration connector:

* [Audit log framework](/frameworks/alf/overview) - for logging audit log messages.
* [Open Connector Framework](/frameworks/ocf/overview) - basic connector interfaces.
* [Integration Daemon API](/services/integration-daemon-services) - for the integration connector base classes.
* [Repository Services APIs](/services/omrs) - for audit log message severities.

??? example "Example of the Maven dependencies for an integration connector ..."
    
    ```xml
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>topic-integrator-api</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>data-manager-api</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
        
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>audit-log-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-connector-framework</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>repository-services-apis</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
            
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>integration-daemon-services-api</artifactId>
                <scope>provided</scope>
                <version>${open-metadata.version}</version>
            </dependency>
    
    ```
    
    !!! tip "Use provided scope ..."

        Notice the `<scope>provided</scope>` setting for the Egeria libraries.  This prevents the Egeria libraries from being included in your connector jar file.  By using the provided scope, your connector can run with any level of Egeria that supports this type of connector.  Without it, duplicate Egeria classes would be loaded into your OMAG Server Platform and if the platform was running at a different level it is not certain which version of the classes would run. (It "may" be ok but experience, as we know, teaches us that "if it can go wrong it will go wrong" so avoiding problems is always preferable :).   

You will also need to add the dependencies for the third party technology that your connector is calling.

All the integration connector base classes inherit from (extend) the [`IntegrationConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/governance-servers/integration-daemon-services/integration-daemon-services-api/src/main/java/org/odpi/openmetadata/governanceservers/integrationdaemonservices/connectors/IntegrationConnectorBase.java){ target=gh }.  This class defines the lifecycle methods of the integration connector.

![Methods implemented by an integration connector](/guides/developer/integration-connectors/integration-connector-methods.svg)
> Methods implemented by an integration connector.  The base class implements the initialize(), setAuditLog(), setConnectorName(), and setContext() methods.  Your integration connector only needs to supply the start, refresh and disconnect method.  It implements the engage method only if it needs to issue a blocking call.

- `initialize` is a standard method for all connectors that is called by the [connector broker](/concepts/connector-broker) when a request is made to create an instance of the connector. The connector broker uses the initialize method to pass the [connection](/concepts/connection) object used to create the connector instance and a unique identifier for this instance of the connector. This method is provided by the integration connector's base class.  Your code can access the connection properties via the `connectionProperties` variable and the connector's unique identifier via the `connectorInstanceId` variable.

- `setAuditLog` provides an [Audit Log Framework (ALF)](/frameworks/alf/overview) compatible logging destination. This method is provided by the integration connector's base class.  Your code can access the audit log via the `auditLog` variable.

- `setConnectorName` provides the name of the connector from the configuration, so it can be used for logging. This method is provided by the integration connector's base class.  Your code can access your integration connector's name via the `connectorName` variable.

- `initializeEmbeddedConnectors` saves the optional list of embedded connectors that were defined in the connection object for your integration connector when it was configured.  These connectors are [digital resource connectors](/concepts/digital-resource-connector) for use by your integration connector to [call the third party technology](/guides/developer/integration-connectors/overview/#three-patterns-for-connections). This method is provided by the integration connector's base class.  Your code can access the embedded connector's via the `embeddedConnectors` variable.

- `setContext` sets up the integration service specific context object. This method is also provided by the integration connector's base class.  Your code can access the connector's name via the `context` variable.  However, it is recommended that because it is set to null after the `disconnect` method (described below), your connector should use the `super.getContext()` method to access the context, particularly if your connector operates in multiple threads.
    
- `start` indicates that the connector is completely configured (that is all the methods listed above have been called) and it can begin processing. This call is where the configuration properties are extracted from the connection object. It can also be used to register with non-blocking services. For example, it can register a listener for events from the OMAS [Out Topic](/concepts/out-topic) through the context.

- `engage` is used when the connector is configured to need to issue blocking calls to wait for new metadata. It is called from its own thread. It is recommended that the `engage()` method returns when each blocking call completes. The integration daemon will pause a second and then call `engage()` again. This pattern enables the calling thread to detect the shutdown of its hosting integration daemon server.  This method is implemented by the integration connector's base class to do nothing.  You only need to override it if your integration connector is issuing blocking calls. 

- `refresh` requests that the connector does a comparison of the metadata in the third party technology and open metadata repositories. Refresh is called:

    1. when the integration connector first starts and then
    1. at intervals defined in the connector's configuration as well as
    1. any external REST API calls to explicitly refresh the connector.
    
- `disconnect` is called when the server is shutting down. The connector should free up any resources that it holds since it is not needed any more.  Once disconnect has been called the context is no longer valid.

Therefore, you are looking to implement the `start`, `refresh` and `disconnect` methods in your integration connector, and optionally overriding the `engage` method if your connector issues blocking calls.
