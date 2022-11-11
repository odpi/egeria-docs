<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Building Integration Connectors

---8<-- "docs/connectors/integration/integration-connector-intro.md"

The purpose of the integration daemon and its integration services is to minimise the effort required to integrate a third party technology into the open metadata ecosystem.  They handle:

* Management of configuration - including user security information.
* Starting and stopping of your integration logic.
* Thread management and polling.
* Access to the open metadata repositories for query and maintenance of open metadata.
* Ability to write to audit log and maintain measurements for performance metrics.
* Metadata provenance.

This means you can focus on interacting with the third party technology and mapping its metadata to open metadata in your integration connector.


## Integration connector interface

---8<-- "docs/guides/developer/integration-connectors/integration-connector-interface.md"


## Designing your integration connector

There are four main design decisions to make before you start coding:

* How is the work of the connector triggered - explicitly through the connection object contents or by listening for events from either the third party technology or open metadata?
* Which direction the metadata synchronization is going.  Is the third party technology the source of metadata or is metadata the open metadata ecosystem being pushed to the third party technology?  
* How are elements from the third party technology correlated with the elements in open metadata.
* If the third party technology is the source, should the metadata created in the open metadata ecosystem be read-only so that it can not be changed by other tools.  This is achieved using [External source metadata provenance](/features/metadata-provenance/overview).

### Three patterns for connections

Your integration connector is created and initialized with a connection object.  This connection object should contain all the configuration needed by your integration connector.  For example, it may contain configuration properties that can control the behavior of your connector.  When connecting to the third party technology, optional userId and password for the third party technology may be stored in the connection along with endpoint information that defines the network address of its deployment.

![Connection object with an explicit endpoint](explicit-endpoints.svg)
> An explicit endpoint is added to the integration connector's connection in its configuration to provide information on the network location of the third party technology.  This is used to initialize the client libraries needed to call the third party technology.

![A connection with no endpoint](learned-endpoints.svg)
> If no endpoint is configured in the integration connector's connection, the endpoint information can be retrieved from open metadata by calling the context object and/or listening for notifications from the partner OMAS.

An alternative approach to calling the third party technology directly in your integration connector is to use one or more appropriate [digital resource connectors](/concepts/digital-resource-connectors) to call the third party technology.  The connection objects for these digital resource connectors are nested in the connection object for the integration connector.

![A virtual connection include embedded connection](virtual-connector.svg)
> A [Virtual Connection](/concepts/connection/#virtual-connections) is a special type of connection that allows connections for different connectors to be embedded.  This style of connection can be used by an integration connector that is making use of digital resource connectors to call its third party technology.  Typically, there is only one embedded connection, but multiple embedded connections can be used.  Also, the embedded connections themselves may be virtual connections.

### Metadata flow for your connector

The `refresh` method of your connector is called periodically to ensure the metadata in the third party technology is consistent with the metadata in the open metadata ecosystem.  It operates in two phases:

1. Retrieving metadata from the source and ensuring the equivalent metadata is present in the metadata destination.

2. Retrieving metadata from the destination and deleting any elements that are not present in the source.

![Third party technology is the metadata source](third-party-metadata-source.svg)
> When the third party technology is the metadata source (for example, it is a relational database or a file system) the refresh method ensures that the open metadata in Egeria is exactly the same as the metadata in the third party technology.

![Third party technology is the metadata destination](third-party-metadata-source.svg)
> When the open metadata ecosystem is the metadata source and the integration connector is responsible for distributing a subset of the open metadata to the third party technology, the refresh method ensures this subset (and no more) is present in the third party technology.

### Mapping the third party technology to open metadata

Your integration connector needs to be able to map between the elements in the third party technology and in the open metadata ecosystem.  Each will use different unique identifiers that it is unlikely that you can control.  Design the `qualifiedName` of the open metadata elements to be constructable from the identifier of the equivalent metadata element in the third party technology.

??? tip "What if there is not a one-to-one correspondence between elements"
    The [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) supports [external identifiers](/features/external-identifiers/overview) which can help to correlate complex relationships between the third party technology and open metadata.
    
## Controlling external source metadata provenance

The [configuration for an integration connector](/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services) in the Integration Daemon includes a *metadataSourceQualifiedName*.  It specifies the 
Some integration services allow the integration connector to control whether external source metadata provenance is used if it is configured.  If it is set to true, external source metadata provenance is used, otherwise it is local cohort metadata provenance.

| Integration Service | Method to control external source metadata provenance                                                                                         |
|---|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [API Integrator OMIS](/services/omis/api-integrator/overview) | Call `setAPIManagerIsHome()` method to set toggle. Default is `true`, which means external provenance is used if it is configured.            |
| [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview) | Use `assetManagerIsHome` property on method calls.                                                                                            |
| [Database Integrator OMIS](/services/omis/database-integrator/overview) | External source metadata provenance is controlled by the configuration only.                                                                  |
| [Display Integrator OMIS](/services/omis/display-integrator/overview) | Call `setApplicationIsHome()` to set toggle.  Default is `true`, which means external provenance is used if it is configured.                 |
| [Files Integrator OMIS](/services/omis/files-integrator/overview) | External source metadata provenance is controlled by the configuration.                                                                       |
| [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) | Call `setInfrastructureManagerIsHome()` method to set toggle. Default is `true`, which means external provenance is used if it is configured. |
| [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) | Use `assetManagerIsHome` property on method calls.                                                                                            |
| [Organization Integrator OMIS](/services/omis/organization-integrator/overview) | External source metadata provenance is controlled by the configuration only.                                                                  |
| [Search Integrator OMIS](/services/omis/search-integrator/overview) | Not applicable - outbound only.                                                                                                               |
| [Security Integrator OMIS](/services/omis/security-integrator/overview)  | External source metadata provenance is controlled by the configuration only.                                                                  |
| [Topic Integrator OMIS](/services/omis/topic-integrator/overview) | Call `setEventBrokerIsHome()` method to set toggle. Default is `true`, which means external provenance is used if it is configured.                                                                        |


## Writing the connector provider

---8<-- "docs/guides/developer/connector-provider-intro.md"

---8<-- "docs/guides/developer/integration-connectors/implementing-an-integration-connector-provider.md"


!!! example "Example: connector provider for the Kafka Monitor Integration Connector"
    For example, the [`KafkaMonitorIntegrationProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafka/KafkaMonitorIntegrationProvider.java){ target=gh } is used to instantiate connectors that are monitoring an Apache Kafka broker. Therefore, its name and description refer to Kafka, and the connectors it instantiates are of type [`KafkaMonitorIntegrationConnector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafka/KafkaMonitorIntegrationConnector.java){ target=gh }.

## Writing the connector

The connector extends the [appropriate integration connector interface](#integration-connector-interface) and has a default constructor:

```java
public class MyIntegrationConnector extends FilesIntegratorConnector
{

    /**
     * Default constructor used by the connector provider.
     */
    public MyIntegrationConnector()
    {
        super();
    }

}


```

### Accessing configuration properties and the endpoint

The connection object is stored in the `connectionProperties` instance variable defined by the super class.  It is typically accessed in the `start()` method. The code snippet below accesses the endpoint and configuration properties from the connection.  It also uses the audit log to record a start-up message

```java
    /**
     * Indicates that the connector is completely configured and can begin processing.
     * This call can be used to register with non-blocking services.
     *
     * @throws ConnectorCheckedException there is a problem within the connector.
     */
    @Override
    public void start() throws ConnectorCheckedException
    {
        super.start();

        final String methodName = "start";

        /*
         * Extract the configuration
         */
        EndpointProperties  endpoint = connectionProperties.getEndpoint();

        if (endpoint != null)
        {
            myEndpoint = endpoint.getAddress();
        }

        Map<String, Object> configurationProperties = connectionProperties.getConfigurationProperties();

        if (configurationProperties != null)
        {
            :
        }

        /*
         * Record the configuration
         */
        if (auditLog != null)
        {
            auditLog.logMessage(methodName,
                                MyConnectorsAuditCode.CONNECTOR_CONFIGURATION.getMessageDefinition(connectorName,myEndpoint));
        }

        :
    }


```

### Accessing context

The context is retrieved using the `getContext()` method.   This is a synchronized method that can be called from multiple threads, that occurs when the connector is using listeners.

### Registering a listener

An integration connector that is listening for events from the open metadata ecosystem should implement the listener interface for the associated access service.  This interface has a `processEvent()` method that your connector implements.  


| Integration Service                                                                 | Partner OMAS                                                        | Listener Interface                                                                                                                                          |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [API Integrator OMIS](/services/omis/api-integrator/overview)                       | [Data Manager OMAS](/services/omas/data-manager/overview)           | [DataManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/api/DataManagerEventListener.html)                |
| [Catalog Integrator OMIS](/services/omis/catalog-integrator/overview)               | [Asset Manager OMAS](/services/omas/asset-manager/overview)         | [AssetManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetmanager/api/AssetManagerEventListener.html)             |
| [Database Integrator OMIS](/services/omis/database-integrator/overview)             | [Data Manager OMAS](/services/omas/data-manager/overview)           | [DataManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/api/DataManagerEventListener.html)                |
| [Display Integrator OMIS](/services/omis/display-integrator/overview)               | [Data Manager OMAS](/services/omas/data-manager/overview)           | [DataManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/api/DataManagerEventListener.html)                |
| [Files Integrator OMIS](/services/omis/files-integrator/overview)                   | [Data Manager OMAS](/services/omas/data-manager/overview)           | [DataManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/api/DataManagerEventListener.html)                |
| [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) | [IT infrastructure OMAS](/services/omas/it-infrastructure/overview) | [ITInfrastructureEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/itinfrastructure/api/ITInfrastructureEventListener.html) |
| [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview)               | [Asset Manager OMAS](/services/omas/asset-manager/overview)         | [AssetManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetmanager/api/AssetManagerEventListener.html)             |
| [Organization Integrator OMIS](/services/omis/organization-integrator/overview)     | [Community Profile OMAS](/services/omas/community-profile/overview) | [CommunityProfileEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/communityprofile/api/CommunityProfileEventListener.html) |
| [Search Integrator OMIS](/services/omis/search-integrator/overview)                 | [Asset Catalog OMAS](/services/omas/asset-catalog/overview)         | [AssetCatalogEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetcatalog/api/AssetCatalogEventListener.html)             |
| [Security Integrator OMIS](/services/omis/security-integrator/overview)             | [Security Manager OMAS](/services/omas/security-manager/overview)   | [SecurityManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/securitymanager/api/SecurityManagerEventListener.html)    |
| [Topic Integrator OMIS](/services/omis/topic-integrator/overview)                   | [Data Manager OMAS](/services/omas/data-manager/overview)           | [DataManagerEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/datamanager/api/DataManagerEventListener.html)                |

Your integration connector registers itself as a listener in the `start()` method, and the `processEvent()` method is called each time an event occurs.

```java
    /**
     * Indicates that the connector is completely configured and can begin processing.
     *
     * @throws ConnectorCheckedException there is a problem within the connector.
     */
    @Override
    public synchronized void start() throws ConnectorCheckedException
    {
        super.start();

        :
        :
                                
        myContext = super.getContext();

        if (myContext != null)
        {
                myContext.registerListener(this);
        }
    }

```

## Testing your connector

Your integration connector implementation should be built and packaged in a *jar* file.  This jar file contains your connector provider and connector implementation.  It may optionally contain any dependent client libraries to the third party connector that are called directly by your integration connector.  This is necessary if these client libraries are not available in their own jar file.

The connector jar file (and any jar files for the dependent third party client libraries not included in your connector's jar file) need to be added to the [OMAG Server Platform](/concepts/omag-server-platform) class path.  The easiest way to do this is to copy the JAR files into the `lib` directory of your OMAG Server Platform's [install directory](/education/tutorials/installing-egeria-tutorial).

Once you have installed the connector, configure it in the integration daemon, connected to a metadata access store

![Figure 6](testing.svg)

Your connector is then able to start and exchange metadata.

![Figure 7](/services/integration-daemon-internals.svg)

??? education "Further information"
    - [Open Connector Framework (OCF)](/frameworks/ocf/overview) that defines the behavior of all connectors.
    - [Configuring an integration daemon](/guides/admin/servers/configuring-an-integration-daemon) to understand how to set up an integration connector.
    - [Developer guide](/guides/developer) for more information on writing connectors.

--8<-- "snippets/abbr.md"
