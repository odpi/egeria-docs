<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Servers are configured through the [Administration Services](/services/admin-services/overview/#configure-an-omag-server){ target=dojo-support }.  It involves a sequence of calls that sets up its name and properties, the registered services that it will run along with the connectors that it will host.

??? beginner "Setting up `ServerConfig`"

    In `egeria-dev-projects` is a module called `egeria-config-utility`.  It contains a utility called `ServerConfig` that includes the method calls to create different types of servers, to make changes to a server's configuration and to delete a server's configuration. Navigate to the `ServerConfig` class and run it using the right-mouse menu as before.
    
    ![egeria-config-utility module](/education/egeria-dojo/developer/egeria-config-utility-module.png)
    
    It will also fail with the certificate error.  Edit `ServerConfig`'s newly created configuration and add `-Dstrict.ssl=false` to the `VM Options` and click `OK` to save the configuration to turn off the need for a certificate. 
    
    ![egeria-config-utility configuration](/education/egeria-dojo/developer/egeria-config-utility-configuration.png)
               
    When you restart `ServerConfig`, it displays a menu:
    
    ```bash
    /Library/Java/JavaVirtualMachines/temurin-11.jdk/Contents/Home/bin/java -Dstrict.ssl=false ... org.odpi.openmetadata.devprojects.utilities.serverconfig.ServerConfig
    ===============================
    OMAG Server Operations Utility:    Mon Feb 14 09:33:07 GMT 2022
    ===============================
    Running against platform: https://localhost:9443 - Egeria OMAG Server Platform (version 3.12)
    Using userId: garygeeke
    
    Enter a command along with the server name and any optional parameters. Press enter to execute request.
      - create-metadata-store     <serverName>  
      - create-integration-daemon <serverName> <metadataStoreServerName> 
      - add-topic-connector       <serverName> <optionalConnectorProviderClassName> 
      - log-event-contents        <serverName> <optionalConnectorProviderClassName> 
      - add-cohort-member         <serverName> <optionalCohortName> 
      - add-startup-archive       <serverName> <archiveFileName>
      - update-server-user-id     <serverName> <newUserId> 
      - delete-server             <serverName>  
      - exit  
    ```

??? beginner "Configuring the `msd1` server"
    Enter `create-metadata-store mds1` in the space under the menu and press return. You should see a message `Configuring metadata store: mds1` and the menu is redisplayed.
    
    ![egeria-config-utility creating mds1](/education/egeria-dojo/developer/egeria-config-utility-creating-mds1.png)
    
    Rerun `EgeriaPlatformReport` (select from the configurations box dropdown) and you notice that the exception relating to the missing configuration directory has gone and the report now displays details of the new `mds1` server. [Markdown version of report for reference](/education/egeria-dojo/developer/egeria-platform-report-mds1-configured).
    
??? beginner "Reviewing the output from `EgeriaPlatformReport`"
    There is a lot of detail in this new report - much of it retrieved from the server's [configuration document](/concepts/configuration-document){ target=dojo-support } that was created when the `mds1` server was configured.

    The [Administration Services' `ConfigurationManagementClient`](/services/admin-services/overview/#managing-configuration-documents){ target=dojo-support } is able to retrieve, update and deploy configuration documents to different OMAG Server Platforms.  `EgeriaPlatformReport` used the following method call to retrieve all of the available configuration documents before printing them out to the report.
    
    ```java linenums="1"
    ConfigurationManagementClient configurationManagementClient = new ConfigurationManagementClient(clientUserId, platformURLRoot);
    
    Set<OMAGServerConfig> configuredServers = configurationManagementClient.getAllServerConfigurations();
    ```
    Particular points to note about the `mds1` server configuration:
    
    * The type of the server is null - this is determined when the server is started and Egeria is interpreting/validating the server's configuration document.  You will see that value filled in at the next step in the dojo.
    * The server is running with a userId of `cocoMDS1npa` and a security connector of `org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider`.  The security connector authorizes requests to Egeria and `cocoMDS1npa` is one of the userIds it recognizes.  You can change these hard-coded values in `ServerConfig` to experiment with different security settings.
    
    ```bash
       Platform servers
          Server: mds1
             Type: <null>
             Description: Metadata Access Store called mds1 running on platform https://localhost:9443
             UserId: cocoMDS1npa
             Security Connector
                Implementation: org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider
                Location: <null>
    ```
    
    * The `mds1` server is using an in-memory local metadata repository.  This means that its metadata repository is emptied each time the server is started up - which is very useful when testing new utilities.  The remote connector for the local repository is the connector that other servers would use to call `mds1`.  It is sent out on [cohort registration exchanges](/features/cohort-operation/overview){ target=dojo-support } whenever `mds1` registers with a [cohort](/concepts/cohort-member){ target=dojo-support }.
    
    ```bash
             Local Repository
                Local Repository Mode: Open Metadata Native
                Local Repository Connector
                   Implementation: org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider
                   Location: <null>
                Local Repository Remote Connector
                   Implementation: org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider
                   Location: https://localhost:9443/servers/mds1
    ```
    
    * Finally, the configured [Open Metadata Access Services (OMASs)](/services/omas){ target=dojo-support } are listed including: [Asset Manager OMAS](/services/omas/asset-manager/overview){ target=dojo-support }, [Community Profile OMAS](/services/omas/community-profile/overview){ target=dojo-support }, [Data Manager OMAS](/services/omas/data-manager/overview){ target=dojo-support }, [Digital Architecture OMAS](/services/omas/digital-architecture/overview){ target=dojo-support }, [Asset Consumer OMAS](/services/omas/asset-consumer/overview){ target=dojo-support }, [Governance Program OMAS](/services/omas/governance-program/overview){ target=dojo-support } and [Asset Owner OMAS](/services/omas/asset-owner/overview){ target=dojo-support }.  Below is a snippet from the report showing Asset Manager OMAS.
    
    ```bash
             Services
                Service: Asset Manager OMAS
                   Service Options
                      SupportedZones: [quarantine, trash-can, data-lake]
                      PublishZones: [data-lake, personal-files, personal-files]
                      DefaultZones: [quarantine]
                   Connectors
                      InTopic
                         Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                         Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                         Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=fab57cdc-e7fb-4f23-8237-376c9fda492b, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
                      OutTopic
                         Implementation: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
                         Location: egeria.omag.server.mds1.omas.assetmanager.inTopic
                         Configuration Properties: {producer={bootstrap.servers=localhost:9092}, local.server.id=fab57cdc-e7fb-4f23-8237-376c9fda492b, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
    ```
    The `Service Options` control the behaviour of the OMAS.  
    
    * `SupportedZones` defines the [governance zones that an asset must belong](/features/governance-zoning/overview){ target=dojo-support } to in order to be retrievable through the OMAS.  
    * `DefaultZones` defines the governance zones assigned to a new asset created through this interface.
    * `PublishZones` are the governance zones that are set in the asset when the publishXXX() method is called (more later).
    
    You can also see from the implementation that the Asset Manager OMAS is configured to use Apache Kafka for its [In Topic](/concepts/in-topic){ target=dojo-support } and [Out Topic](/concepts/out-topic){ target=dojo-support }.

