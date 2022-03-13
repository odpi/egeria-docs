---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Administration services

The administration services support the commands to:

* Configure an [OMAG Server Platform](/concepts/omag-server-platform).
* Configure different types of [OMAG Servers](/concepts/omag-server)
* List the configured OMAG Servers
* Deploy the [configuration document](/concepts/configuration-document) for an OMAG Server to a different OMAG Server Platform.
* Start and stop OMAG Servers
* Retrieve the status of an OMAG Server along with the status of each of its active subsystems and services.

The Java clients for the administration services are located in its `admin-services-client` module.

--8<-- "docs/guides/developer/java-clients/platform-constructor-parameters.md"


## Configuring the OMAG Server Platform

The OMAG Server Platform has two connectors that are configured though the [`OMAGServerPlatformConfigurationClient`](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/OMAGServerPlatformConfigurationClient.html){ target=javadoc }.

* The [Platform Metadata Security Connector](/concepts/platform-metadata-security-connector) that authorizes management and administration request to the platform.
* The [Configuration Document Store Connector](/concepts/configuration-document-store-connector) that managed the storage and retrieval of configuration documents.

![OMAGServerPlatformConfigurationClient](omag-server-platform-configuration-client.svg)
> The OMAGServerPlatformConfigurationClient is responsible for setting up the connectors for the OMAG Server Platform.  This configuration needs to be re-applied each time the platform start up,

The client supports retrieving the connection for either of these connectors, updating it and deleting it.  The example below shows how to retrieve the connections for the platform's two connectors.

??? example "Example: retrieving all available configuration documents"
    ```java linenums="1"
    OMAGServerPlatformConfigurationClient platformConfigurationClient = new OMAGServerPlatformConfigurationClient(clientUserId, platformURLRoot);

    Connection configurationStoreConnection = platformConfigurationClient.getConfigurationStoreConnection();
    Connection platformSecurityConnection   = platformConfigurationClient.getPlatformSecurityConnection();
    ```

The platform's configuration is not stored.  Instead it needs to be added/updated each time the platform starts.

## Configuring an OMAG Server

The Administration Services clients that support the configuration of OMAG Servers are specialized to configure the specific services that each type of OMAG Server supports.  For example, `MetadataAccessStoreConfigurationClient` has all of the methods necessary to configure a [Metadata Access Store](/concepts/metadata-access-store).  Similarly, the `IntegrationDaemonConfigurationClient` has all of the methods necessary to configure an [Integration Daemon](/concepts/integration-daemon). 
Since there are some common services, the clients make use of inheritance to share configuration methods that are common.  The diagram below how they are related.

![OMAG Server configuration client hierarchy](omag-server-configuration-clients.svg)
> The configuration clients for OMAG servers are organized in an inheritance hierarchy to allow them to share common methods.  However, each has all of the method needed to configure its services.

| Java Client | Type of OMAG Server it configures | Javadoc Link |
| :---------- | :-------------------------------- | :----------- |
| MetadataAccessPointConfigurationClient | [Metadata Access Point](/concepts/metadata-access-point) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/MetadataAccessPointConfigurationClient.html){ target=javadoc } |
| MetadataAccessStoreConfigurationClient | [Metadata Access Store](/concepts/metadata-access-store) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/MetadataAccessStoreConfigurationClient.html){ target=javadoc } |
| RepositoryProxyConfigurationClient | [Repository Proxy](/concepts/repository-proxy) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/RepositoryProxyConfigurationClient.html){ target=javadoc } |
| ConformanceTestServerConfigurationClient | [Conformance Test Server](/concepts/conformance-test-server) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/ConformanceTestServerConfigurationClient.html){ target=javadoc } |
| EngineHostConfigurationClient | [Engine Host](/concepts/engine-host) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/EngineHostConfigurationClient.html){ target=javadoc } |
| IntegrationDaemonConfigurationClient | [Integration Daemon](/concepts/integration-daemon) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/IntegrationDaemonConfigurationClient.html){ target=javadoc } |
| ViewServerConfigurationClient | [View Server](/concepts/view-server) | [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/ViewServerConfigurationClient.html){ target=javadoc } |

The configuration for each server is stored in a [configuration document](/concepts/configuration-document).  The Java class that holds the configuration document is called `OMAGServerConfig`. It is a JavaBean and it can be used directly to set up the configuration for a server,
or it can be set up by calling the configuration client APIs.

The sample code below shows a series of calls to the `MetadataAccessStoreConfigurationClient` to set up a Metadata Access Store that is using the in-memory repository and is activating the following access services.

* [Asset Consumer OMAS](/services/omas/asset-consumer/overview)
* [Asset Owner OMAS](/services/omas/asset-owner/overview)
* [Asset Manager OMAS](/services/omas/asset-manager/overview)
* [Data Manager OMAS](/services/omas/data-manager/overview)
* [Digital Architecture OMAS](/services/omas/digital-architecture/overview)
* [Community Profile OMAS](/services/omas/community-profile/overview)
* [Governance Program OMAS](/services/omas/governance-program/overview)

??? example "Example: Methods used to configure a Metadata Access Store"
    ```java linenums="1"
    /**
     * Set up the defaults that are used whenever a topic is configured for a server.
     * Check that the eventBusURLRoot is correct for your Kafka installation.
     *
     * @param client client responsible for the server configuration
     *
     * @throws OMAGNotAuthorizedException the supplied userId is not authorized to issue this command.
     * @throws OMAGInvalidParameterException invalid parameter.
     * @throws OMAGConfigurationErrorException unusual state in the admin server.
     */
    private void setEventBus(OMAGServerConfigurationClient client) throws OMAGNotAuthorizedException,
                                                                          OMAGInvalidParameterException,
                                                                          OMAGConfigurationErrorException
    {
        if (eventBusURLRoot != null)
        {
            Map<String, Object> configurationProperties = new HashMap<>();
            Map<String, Object> producerProperties      = new HashMap<>();
            Map<String, Object> consumerProperties      = new HashMap<>();

            producerProperties.put("bootstrap.servers", eventBusURLRoot);
            consumerProperties.put("bootstrap.servers", eventBusURLRoot);
            consumerProperties.put("auto.commit.interval.ms", "1");

            configurationProperties.put("producer", producerProperties);
            configurationProperties.put("consumer", consumerProperties);

            client.setEventBus(null, // use default - kafka
                               null, // use default - egeria.omag
                               configurationProperties);
        }
    }


    /**
     * Configure a security connector.  The default connector uses the Coco Pharmaceutical users and rules.
     * Change the serverSecurityConnectorProviderClassName to null to turn off security in new servers.
     * Alternatively change the class name for a different connector.
     *
     * @param client client responsible for the server configuration
     *
     * @throws OMAGNotAuthorizedException the supplied userId is not authorized to issue this command.
     * @throws OMAGInvalidParameterException invalid parameter.
     * @throws OMAGConfigurationErrorException unusual state in the admin server.
     */
    private void setSecuritySecurityConnector(OMAGServerConfigurationClient client) throws OMAGNotAuthorizedException,
                                                                                           OMAGInvalidParameterException,
                                                                                           OMAGConfigurationErrorException
    {
        if (serverSecurityConnectorProviderClassName != null)
        {
            Connection    connection    = new Connection();
            ConnectorType connectorType = new ConnectorType();

            connectorType.setConnectorProviderClassName(serverSecurityConnectorProviderClassName);
            connection.setConnectorType(connectorType);

            client.setServerSecurityConnection(connection);
        }
    }


    /**
     * Create a new metadata access store OMAG server with an in-memory repository.
     * If the event bus is not set up, the access services are configured without in and out topics.
     *
     * @param serverName name of the new server
     */
    private void createMetadataStore(String serverName)
    {
        try
        {
            System.out.println("Configuring metadata store: " + serverName);

            MetadataAccessStoreConfigurationClient client = new MetadataAccessStoreConfigurationClient(clientUserId, serverName, platformURLRoot);

            client.setServerDescription("Metadata Access Store called " + serverName + " running on platform " + platformURLRoot);
            client.setServerUserId(serverName + "npa");
            client.setServerType(null); // Let the admin service set up the server types
            client.setOrganizationName(organizationName);
            client.setMaxPageSize(maxPageSize);

            this.setSecuritySecurityConnector(client);
            client.setDefaultAuditLog();

            client.setServerURLRoot(platformURLRoot);
            this.setEventBus(client);

            client.setInMemLocalRepository();
            client.setLocalMetadataCollectionName(serverName + "'s metadata collection");

            List<String> assetLookupZones = new ArrayList<>();

            assetLookupZones.add("data-lake");
            assetLookupZones.add("personal-files");

            List<String> personalFilesZone = new ArrayList<>();

            assetLookupZones.add("personal-files");

            List<String> maintenanceZones = new ArrayList<>();

            maintenanceZones.add("quarantine");
            maintenanceZones.add("trash-can");
            maintenanceZones.add("data-lake");

            List<String> newDataZone = new ArrayList<>();

            newDataZone.add("quarantine");

            Map<String, Object> accessServiceOptions = new HashMap<>();


            if (eventBusURLRoot != null)
            {
                accessServiceOptions.put("SupportedZones", assetLookupZones);
                accessServiceOptions.put("DefaultZones", personalFilesZone);

                client.configureAccessService("asset-consumer", accessServiceOptions);

                accessServiceOptions.put("KarmaPointPlateau", 10);

                client.configureAccessService("community-profile", accessServiceOptions);

                accessServiceOptions = new HashMap<>();
                accessServiceOptions.put("SupportedZones", maintenanceZones);
                accessServiceOptions.put("DefaultZones", newDataZone);
                accessServiceOptions.put("PublishZones", assetLookupZones);

                client.configureAccessService("asset-owner", accessServiceOptions);
                client.configureAccessService("data-manager", accessServiceOptions);
                client.configureAccessService("asset-manager", accessServiceOptions);
                client.configureAccessService("governance-program", accessServiceOptions);
                client.configureAccessService("digital-architecture", accessServiceOptions);
            }
            else // configure the access services without in and out topics
            {
                accessServiceOptions.put("SupportedZones", assetLookupZones);
                accessServiceOptions.put("DefaultZones", personalFilesZone);

                client.configureAccessServiceNoTopics("asset-consumer", accessServiceOptions);

                accessServiceOptions.put("KarmaPointPlateau", 10);

                client.configureAccessServiceNoTopics("community-profile", accessServiceOptions);

                accessServiceOptions = new HashMap<>();
                accessServiceOptions.put("SupportedZones", maintenanceZones);
                accessServiceOptions.put("DefaultZones", newDataZone);
                accessServiceOptions.put("PublishZones", assetLookupZones);

                client.configureAccessServiceNoTopics("asset-owner", accessServiceOptions);
                client.configureAccessServiceNoTopics("data-manager", accessServiceOptions);
                client.configureAccessServiceNoTopics("asset-manager", accessServiceOptions);
                client.configureAccessServiceNoTopics("governance-program", accessServiceOptions);
                client.configureAccessServiceNoTopics("digital-architecture", accessServiceOptions);
            }
        }
        catch (Exception error)
        {
            System.out.println("There was an " + error.getClass().getName() + " exception when calling the platform.  Error message is: " + error.getMessage());
        }
    }

    ```

## Managing configuration documents

The [`ConfigurationManagementClient`](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/ConfigurationManagementClient.html){ target=javadoc } supports the retrieval of a single OMAG Server's configuration document, or all available configuration documents.  It also supports the deployment of configuration documents to different OMAG Server Platforms.

![ConfigurationManagementClient](admin-services-operational-clients.svg)


??? example "Example: retrieving all available configuration documents"
    ```java linenums="1"
    ConfigurationManagementClient configurationManagementClient = new ConfigurationManagementClient(clientUserId, platformURLRoot);
    
    Set<OMAGServerConfig> configuredServers = configurationManagementClient.getAllServerConfigurations();
    ```

## Starting and stopping OMAG Servers

The [`OMAGServerOperationsClient`](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/ConfigurationManagementClient.html){ target=javadoc } supports the starting and stopping of OMAG Servers on an OMAG Server Platform. 

The code sample shows the method calls to start and stop named OMAG Servers.

??? example "Example: starting and stopping servers"
    ```java linenums="1"
    /**
     * Start the named server on the platform.  This will fail if the platform is not running,
     * or if the user is not authorized to issue operations requests to the platform or if the
     * server is not configured.
     *
     * @param serverName string name
     */
    private void startServer(String serverName)
    {
        try
        {
            OMAGServerOperationsClient client = new OMAGServerOperationsClient(clientUserId, serverName, platformURLRoot);
    
            System.out.println("Starting " + serverName + " ...");
            System.out.println(client.activateWithStoredConfig());
        }
        catch (Exception error)
        {
            System.out.println("There was an " + error.getClass().getName() + " exception when calling the platform.  Error message is: " + error.getMessage());
        }
    }
    
    
    /**
     * Stop the requested server.    This will fail if the server or the platform is not running,
     * or if the user is not authorized to issue operations requests to the platform.
     *
     * @param serverName string name
     */
    private void stopServer(String serverName)
    {
        try
        {
            OMAGServerOperationsClient client = new OMAGServerOperationsClient(clientUserId, serverName, platformURLRoot);
 
            System.out.println("Stopping " + serverName + " ...");
 
            client.deactivateTemporarily();
 
            System.out.println(serverName + " stopped.");
        }
        catch (Exception error)
        {
            System.out.println("There was an " + error.getClass().getName() + " exception when calling the platform.  Error message is: " + error.getMessage());
        }
    }
    ```

## Querying the active server status

It is also able to retrieve the status of the services running within an active server.

??? example "Example: retrieving the status of the services in an active server"
    ```java linenums="1"
    OMAGServerOperationsClient serverOperationsClient = new OMAGServerOperationsClient(clientUserId, serverName, platformURLRoot);
    
    ServerStatus adminServerStatus = serverOperationsClient.getServerStatus();
    
    if (adminServerStatus != null)
    {
        System.out.println(adminServerStatus.getServerActiveStatus());
        System.out.println(adminServerStatus.getServerType());
        System.out.println(adminServerStatus.getServices());
    }
    ````

The status of the server (and its nested services) is one of 5 values:

- Unknown - The state of the server is unknown.  This is equivalent to a null value.
- Starting - The server is starting.
- Running - The server has completed start up and is running.
- Stopping - The server has received a request to shutdown.
- Inactive - The server is not running.

The server type is derived by the administration services when it starts the server.  It is based on an assessment of the services requested in the configuration document.

!!! education "Further information"

    * The [administration guide](/guides/admin) describes how to use the administration services to configure OMAG Server Platforms and OMAG Servers.
    * The [operations guide](/guides/operations/guide) describes how to use the administration services to start/stop OMAG Servers on OMAG Server Platforms and retrieve diagnostics.
    
--8<-- "snippets/abbr.md"
