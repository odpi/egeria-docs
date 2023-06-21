<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Administration services

The configuration for an [OMAG Server](/concepts/omag-server) is maintained in a [Configuration Document](/concepts/configuration-document) and these configuration documents are stored in a *configuration document store*.  The implementation for the configuration document store is plugged into the [OMAG Server Platform](/concepts/omag-server-platform) as a [configuration document store connector](/concepts/configuration-document-store-connector).


The administration services support the commands to:

* Configure an [OMAG Server Platform](/concepts/omag-server-platform)'s configuration document store connector.
* Configure different types of [OMAG Servers](/concepts/omag-server)
* List the configured OMAG Servers
* Deploy the [configuration document](/concepts/configuration-document) for an OMAG Server to a different OMAG Server Platform.

The Java clients for the administration services are located in its `admin-services-client` module.

--8<-- "docs/guides/developer/java-clients/platform-constructor-parameters.md"


## Dynamically configuring the Configuration Document Store Connector

The [Configuration Document Store Connector](/concepts/configuration-document-store-connector)  manage the storage and retrieval of configuration documents.  This connector can be configured though the [`OMAGServerPlatformConfigurationClient`](https://odpi.github.io/egeria/org/odpi/openmetadata/adminservices/client/OMAGServerPlatformConfigurationClient.html){ target=javadoc }.

![OMAGServerPlatformConfigurationClient](omag-server-platform-configuration-client.svg)
> The OMAGServerPlatformConfigurationClient is responsible for setting up the configuration document store connector for the OMAG Server Platform.  This configuration needs to be re-applied each time the platform starts up

The client supports retrieving the connection for either of these connectors, updating it and deleting it.  The example below shows how to retrieve the connections for the platform's two connectors.
The platform's configuration is not stored - it needs to be added/updated each time the platform starts.

??? example "Example: retrieving all available configuration documents"

    ==== "Java"

        ```java linenums="1"
        OMAGServerPlatformConfigurationClient platformConfigurationClient = new OMAGServerPlatformConfigurationClient(clientUserId, platformURLRoot);
    
        Connection configurationStoreConnection = platformConfigurationClient.getConfigurationStoreConnection();
        Connection platformSecurityConnection   = platformConfigurationClient.getPlatformSecurityConnection();
        ```

    ==== "REST API"

        !!! post "POST - configure the configuration document store connector"
            ```
            {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/stores/connection
            ```
        
            The request body should be a connection object used to create the connector to the configuration
            document store.
        
        !!! attention "Ensure the connector is available in the classpath"
            In order to use any connector other than the default, you need to also ensure that the Connector and its ConnectorProvider class are available to the server platform (i.e. the jar file containing them is available in the `LOADER_PATH` location of the server platform).
        
        ??? example "Example: (unencrypted) file store connector"
            For example, this connection would set up the (unencrypted) file store connector:
        
            ```json linenums="1"
            {
                "class": "Connection",
                "connectorType": {
                    "class": "ConnectorType",
                    "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.file.FileBasedServerConfigStoreProvider"
                },
                "endpoint": {
                    "class": "Endpoint",
                    "address": "omag.server.{0}.config"
                }
            }
            ```
        
        ??? example "Example: encrypted JSON file store, non-default location"
            As another example, this connection uses the default encrypted JSON file store, but the files are stored in a different location (`/my-config/omag.server.{0}.config`).
        
            ```json linenums="1"
            {
                "class": "Connection",
                "connectorType": {
                    "class": "ConnectorType",
                    "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.encryptedfile.EncryptedFileBasedServerConfigStoreProvider"
                },
                "endpoint": {
                    "class": "Endpoint",
                    "address": "/my-config/omag.server.{0}.config"
                }
            }
            ```

#### Determine configured store

It is possible to query the setting of the configuration document store connector using the following command:

!!! get "GET - retrieve configured configuration document store"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/stores/connection
    ```

??? success "Response indicating default configuration store (encrypted JSON file store)"
    ```json
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200
    }
    ```

??? success "Response indicating a specific connector"
    If the response looks more like the JSON below, a connector is configured. The `connectorProviderClassName` tells you which connector is being used and the `address` shows where the configuration documents are stored.

    ```json hl_lines="8 12"
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200,
        "connection": {
            "class": "Connection",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.adminservices.configurationstore.file.FileBasedServerConfigStoreProvider"
            },
            "endpoint": {
                "class": "Endpoint",
                "address": "omag.server.{0}.config"
            }
        }
    }
    ```

#### Remove configured store

It is also possible to remove the configuration for the connector using the following command:

!!! delete "DELETE - remove configured configuration store"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/stores/connection
    ```

This reverts the store to the default encrypted JSON file store.

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

--8<-- "snippets/abbr.md"
