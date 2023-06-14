<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# OMAG Server Platform Tutorial

The [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform) is a flexible server platform that can run different types of [OMAG Servers](/concepts/omag-server).  These servers support the open metadata and governance services needed to run the open metadata ecosystem.

## Objectives

At the end of this tutorial you will be able to perform the following tasks.

* Starting the OMAG Server Platform
* Configure open metadata and governance services in an *OMAG Server*.
* Start up the configured server.
* Make calls to the running services.
* Shutdown the server.
* Remove the configuration for the OMAG server.
* Shutdown the platform.
  
## Prerequisite Tasks

* [Download and build Egeria](../building-egeria-tutorial)
* [Familiarize yourself with the Postman test tool](/education/tutorials/postman-tutorial/overview)

## Tutorial Tasks

??? education "Starting the OMAG Server Platform"

    ### Starting the OMAG Server Platform
    
    The [OMAG Server Platform's installation directory](/education/tutorials/building-egeria-tutorial/task-installing-egeria) contains a Java Archive (Jar) file for the [OMAG Server Platform](/concepts/omag-server-platform) itself along with a directory of libraries.
    
    The name of the Java Archive (Jar) file will depend on the release of Egeria that you have installed.  In this example, the release is **4.2**.
    
    ```bash
    $ ls platform
    lib              omag-server-platform-4.2.jar
    ```
    
    The OMAG Server Platform is started with the `java` command.
    
    ??? tip "Checking your Java installation"
        Ensure you have a Java runtime at Version 17 or above installed on your machine. Check the version of Java you have with the command **java -version** and [install the appropriate version](/education/tutorials/building-egeria-tutorial/task-installing-java) if needed. You only need the JRE but select the JDK if you expect to also write some Java code.)
    
    Start the OMAG server platform with the following command:
    
    ```bash
    java -Dloader.path=platform/lib -jar platform/omag-server-platform*.jar
    ```
    
    This starts the platform listening on port `9443`.  Add the `-Dserver.port` parameter before the `-jar` parameter if you wish the platform to listen on a different port. For example, the following command starts the platform listening on port `9444`.  Multiple instances of the same OMAG Server Platform may run in a single machine (or in the same container).  However, they each need to listen on a different port.
    
    ```bash
    java -Dloader.path=platform/lib -Dserver.port=9444 -jar platform/omag-server-platform*.jar
    ```
    
    When the OMAG Server Platform starts up, it displays the `OMAG Server Platform` banner and then details of its configuration.
    
    ```text
     Project Egeria - Open Metadata and Governance
        ____   __  ___ ___    ______   _____                                 ____   _         _     ___
       / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
      / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
     / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
     \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/
    
     :: Powered by Spring Boot (v3.0.6) ::
    
    2023-06-11T13:13:57.959+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 17.0.6 with PID 85411 (/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz/platform/omag-server-platform-4.2-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz)
    2023-06-11T13:13:57.962+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to 1 default profile: "default"
    2023-06-11T13:14:01.186+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
    2023-06-11T13:14:02.400+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Working directory is: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz
    2023-06-11T13:14:02.400+01:00  WARN 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Java trust store 'javax.net.ssl.trustStore' is null - this is needed by Tomcat - using 'server.ssl.trust-store'
    2023-06-11T13:14:04.687+01:00  INFO 85411 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9443 (https) with context path ''
    2023-06-11T13:14:04.704+01:00  INFO 85411 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Started OMAGServerPlatform in 7.591 seconds (process running for 8.325)
    Sun Jun 11 13:14:04 BST 2023 No OMAG servers listed in startup configuration
    Sun Jun 11 13:14:04 BST 2023 OMAG server platform ready for more configuration
    ```
    
    When you see the `OMAG server platform ready for more configuration` message, it means the OMAG Server Platform has completed its start up and it ready to use.
    
    If you get an error that the port is in use, check for any applications using the same port and make sure they are each using unique ports.
    
    Try the following command (replace 9443 accordingly if using a non standard port):
    
    ```bash
    curl --insecure -X GET https://localhost:9443/open-metadata/platform-services/users/test/server-platform/origin
    ```
    Returns
    ```text
    Egeria OMAG Server Platform (version 4.2)
    ```
    
    This calls the OMAG server platform using a REST API call.  The response `Egeria OMAG Server Platform (release X.x)` means the curl command communicated with a running OMAG Server Platform instance.
    
    The OMAG Server Platform has many REST APIs.  Enter **https://localhost:9443/swagger-ui/index.html** into your browser to see the list of available REST APIs.
    
    Broadly speaking, the OMAG Server Platform supports:
    
    * Services to operate the platform.
    * Open metadata and governance services to manage the open metadata ecosystem.
    
    The services operating the platform (primarily the [Administration Services](/services/admin-services/overview) and [Platform Services](/services/platform-services/overview)) are available all the time the OMAG Server Platform is running.  The open metadata and governance services include a server name in the URL and they are routed to the named OMAG Server running on the OMAG Server Platform.
    
    OMAG Servers are started on the OMAG Server Platform through the Platform Services using a [configuration document](/concepts/configuration-document).  This configuration document is configured in the OMAG Server Platform using the Administration Services.
    
    Understanding how to create a configuration document using the administration services is the next task in this tutorial.

??? education "Creating Configuration Documents"
    ### Creating configuration documents for the OMAG Server Platform
    
    The [OMAG Server Platform](/concepts/omag-server-platform) provides a software platform for running [OMAG Servers](/concepts/omag-server).
    
    Each OMAG Server supports selected open metadata and governance services based on its configuration.
    
    #### What is a configuration document?
    
    A [configuration document](/concepts/configuration-document) defines the configuration properties for an OMAG server.  It includes the properties for an OMAG server including the services that it supports.
    
    Configuration documents are typically created using the OMAG Server Platform [Administration Services](/services/admin-services/overview).  In order to experiment with these services, this tutorial uses the [Postman](/education/tutorials/omag-server-tutorial/task-working-with-postman) test tool. This is a tool that enables you to type in REST API calls and execute them against the OMAG server platform.
    
    There is also a postman collection [omag-server-platform-tutorial.postman_collection.json](https://github.com/odpi/egeria-docs/blob/main/site/docs/education/tutorials/omag-server-tutorial/resources/omag-server-platform-tutorial.postman_collection.json) that you can download and import into postman to support this tutorial.  (see **Import** button top left of the Postman user interface).
    
    This tutorial will also use `curl` commands to illustrate calls to the administration services as well as refer to the pre-canned calls in the postman collection.
    
    
    #### Creating the configuration document
    
    Before there is a configuration document, requesting the server configuration creates and returns a default document.  The command is:
    
    ```
    GET {platformURLRoot}/open-metadata/admin-services/users/{adminUserId}/servers/{serverName}/configuration
    ```
    
    where:

    * `{platformURLRoot}` is the host name and port number of the OMAG Server Platform (eg https://localhost:9443).
    * `{adminUserId}` is the user id of the administrator making the calls.
    * `{serverName}` is the name of the OMAG server that is being configured.
    
    Try the following command (this is request **2.** in Postman):
    
    ```
    GET https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/configuration
    ```
    
    The response is in JSON format and contains the following information:
    
    ```json
    {
      "class": "OMAGServerConfigResponse",
      "relatedHTTPCode": 200,
      "omagserverConfig": {
        "class": "OMAGServerConfig",
        "versionId": "V2.0",
        "localServerId": "b49ab686-7b3b-4429-97fd-8d964ef3a4ff",
        "localServerName": "myMetadataServer",
        "localServerType": "Open Metadata and Governance Server",
        "localServerURL": "https://localhost:9443",
        "localServerUserId": "OMAGServer",
        "maxPageSize": 1000
      }
    }
    ```
    
    * The **localServerId** property is a unique identifier given to the server and is used internally to improve the performance of its interaction with external components such as Apache Kafka.
    * The **localServerName** is the name of the OMAG server supplied on the command.
    * The **localServerType**, **localServerURL**, **localServerUserId** and **maxPageSize** are set to their default values and can be changed.
    
    For example, try the following command (this is request **3.** in Postman):
    
    ```
    POST https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/server-type?typeName="Metadata Access Store"
    ```
    
    Then query the configuration again (this is request **2.** in Postman):
    
    ```json
    {
      "class": "OMAGServerConfigResponse",
      "relatedHTTPCode": 200,
      "omagserverConfig": {
        "class": "OMAGServerConfig",
        "versionId": "V2.0",
        "localServerId": "b49ab686-7b3b-4429-97fd-8d964ef3a4ff",
        "localServerName": "myMetadataServer",
        "localServerType": "Metadata Access Store",
        "localServerURL": "https://localhost:9443",
        "localServerUserId": "OMAGServer",
        "maxPageSize": 1000,
        "auditTrail": [
          "Sun Jun 11 20:49:09 BST 2023 garygeeke updated configuration for local server type name to Metadata Access Store."
        ]
      }
    }
    ```
    
    Notice that the localServerType has changed and an audit trail has also appeared.  This allows you to keep track of the changes being made to the configuration document.
    
    The next command configures in type of metadata repository (this is request **4.** in Postman).  In this example, we are using a simple in-memory repository which is useful for testing.
    
    ```
    POST https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/local-repository/mode/in-memory-repository
    ```
    
    This has added the configuration for the local repository using default values. If you query the configuration again (this is request **2.** in Postman) you see a lot has been added.  This includes the definition for the repository as well as a default audit logging destination which ensures that the server writes it audit log messages to the console when it starts up.
    
    ```json
    {
      "class": "OMAGServerConfigResponse",
      "relatedHTTPCode": 200,
      "omagserverConfig": {
        "class": "OMAGServerConfig",
        "versionId": "V2.0",
        "localServerId": "b49ab686-7b3b-4429-97fd-8d964ef3a4ff",
        "localServerName": "myMetadataServer",
        "localServerType": "Metadata Access Store",
        "localServerURL": "https://localhost:9443",
        "localServerUserId": "OMAGServer",
        "maxPageSize": 1000,
        "repositoryServicesConfig": {
          "class": "RepositoryServicesConfig",
          "auditLogConnections": [
            {
              "class": "Connection",
              "headerVersion": 0,
              "qualifiedName": "Console- default",
              "displayName": "Console",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "4afac741-3dcc-4c60-a4ca-a6dede994e3f",
                "qualifiedName": "Egeria:AuditLogDestinationConnector:Console",
                "displayName": "Console Audit Log Destination Connector",
                "description": "Connector supports logging of audit log messages to stdout.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.auditlogstore.console.ConsoleAuditLogStoreProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.auditlogstore.OMRSAuditLogStore"
                ],
                "recognizedConfigurationProperties": [
                  "supportedSeverities"
                ]
              },
              "configurationProperties": {
                "supportedSeverities": [
                  "<Unknown>",
                  "Information",
                  "Event",
                  "Decision",
                  "Action",
                  "Error",
                  "Exception",
                  "Security",
                  "Startup",
                  "Shutdown",
                  "Asset",
                  "Types",
                  "Cohort"
                ]
              }
            }
          ],
          "localRepositoryConfig": {
            "class": "LocalRepositoryConfig",
            "metadataCollectionId": "02694e83-a284-4f03-ac0c-34bfa2ce5c65",
            "localRepositoryMode": "OPEN_METADATA_NATIVE",
            "localRepositoryLocalConnection": {
              "class": "Connection",
              "headerVersion": 0,
              "displayName": "In Memory Local Repository Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "65cc9091-757f-4bcd-b937-426160be8bc2",
                "qualifiedName": "Egeria:OMRSRepositoryConnector:InMemory",
                "displayName": "In Memory OMRS Repository Connector",
                "description": "Native open metadata repository connector that maps open metadata calls to a set of in memory hash maps - demo use only.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector.OMRSMetadataCollectionManager"
                ]
              }
            },
            "localRepositoryRemoteConnection": {
              "class": "Connection",
              "headerVersion": 0,
              "displayName": "Local Repository Remote Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "75ea56d1-656c-43fb-bc0c-9d35c5553b9e",
                "qualifiedName": "Egeria:OMRSRepositoryConnector:CohortMemberClient:REST",
                "displayName": "REST Cohort Member Client Connector",
                "description": "Cohort member client connector that provides access to open metadata located in a remote repository via REST calls.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector.OMRSMetadataCollectionManager"
                ]
              },
              "endpoint": {
                "class": "Endpoint",
                "headerVersion": 0,
                "address": "https://localhost:9443/servers/myMetadataServer"
              }
            },
            "eventsToSaveRule": "ALL",
            "eventsToSendRule": "ALL"
          }
        },
        "auditTrail": [
          "Sun Jun 11 20:49:09 BST 2023 garygeeke updated configuration for local server type name to Metadata Access Store.",
          "Sun Jun 11 20:52:09 BST 2023 garygeeke updated configuration for the local repository."
        ]
      }
    }
    ```
    
    The next command to configure the server is to enable the [Open Metadata Access Services (OMASs)](/services/omas).  These are specialized open metadata and governance services.
    
    It is possible to activate each OMAS individually, but the the sake of this exercise we are going to activate them all using this command (request **5.** in Postman).
    
    ```
    GET https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/access-services/no-topics
    ```
    
    The OMASs provide both REST APIs and notifications.  The `no-topics` part of the command turns off the notifications so we don't need to set up Apache Kafka for this exercise.
    
    The final command requests that an [Open Metadata Archive](/concepts/open-metadata-archive) is loaded to provide some sample metadata.  The name of the open metadata archive file (`content-packs/SimpleDataCatalog.json`) is sent in the request body.
    
    ```
    GET https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/open-metadata-archives/file
    ```
    
    When the configuration is next queried (this is request **2.** in Postman), the complete configuration document is shown.
    
    ```json
    {
      "class": "OMAGServerConfigResponse",
      "relatedHTTPCode": 200,
      "omagserverConfig": {
        "class": "OMAGServerConfig",
        "versionId": "V2.0",
        "localServerId": "b49ab686-7b3b-4429-97fd-8d964ef3a4ff",
        "localServerName": "myMetadataServer",
        "localServerType": "Metadata Access Store",
        "localServerURL": "https://localhost:9443",
        "localServerUserId": "OMAGServer",
        "maxPageSize": 1000,
        "accessServicesConfig": [
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 210,
            "accessServiceDevelopmentStatus": "TECHNICAL_PREVIEW",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.datamanager.admin.DataManagerAdmin",
            "accessServiceName": "Data Manager",
            "accessServiceFullName": "Data Manager OMAS",
            "accessServiceURLMarker": "data-manager",
            "accessServiceDescription": "Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.",
            "accessServiceWiki": "https://egeria-project.org/services/omas/data-manager/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 226,
            "accessServiceDevelopmentStatus": "TECHNICAL_PREVIEW",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.subjectarea.admin.SubjectAreaAdmin",
            "accessServiceName": "Subject Area",
            "accessServiceFullName": "Subject Area OMAS",
            "accessServiceURLMarker": "subject-area",
            "accessServiceDescription": "Document knowledge about a subject area",
            "accessServiceWiki": "https://egeria-project.org/services/omas/subject-area/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 218,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.glossaryview.server.admin.GlossaryViewAdmin",
            "accessServiceName": "Glossary View",
            "accessServiceFullName": "Glossary View OMAS",
            "accessServiceURLMarker": "glossary-view",
            "accessServiceDescription": "Support glossary terms visualization",
            "accessServiceWiki": "https://egeria-project.org/services/omas/glossary-view/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 213,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.designmodel.admin.DesignModelAdmin",
            "accessServiceName": "Design Model",
            "accessServiceFullName": "Design Model OMAS",
            "accessServiceURLMarker": "design-model",
            "accessServiceDescription": "Exchange design model content with tools and standard packages",
            "accessServiceWiki": "https://egeria-project.org/services/omas/design-model/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 223,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.securityofficer.server.admin.SecurityOfficerAdmin",
            "accessServiceName": "Security Officer",
            "accessServiceFullName": "Security Officer OMAS",
            "accessServiceURLMarker": "security-officer",
            "accessServiceDescription": "Set up rules and security tags to protect data",
            "accessServiceWiki": "https://egeria-project.org/services/omas/security-officer/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 204,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.assetmanager.admin.AssetManagerAdmin",
            "accessServiceName": "Asset Manager",
            "accessServiceFullName": "Asset Manager OMAS",
            "accessServiceURLMarker": "asset-manager",
            "accessServiceDescription": "Manage metadata from a third party asset manager",
            "accessServiceWiki": "https://egeria-project.org/services/omas/asset-manager/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 208,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.itinfrastructure.admin.ITInfrastructureAdmin",
            "accessServiceName": "IT Infrastructure",
            "accessServiceFullName": "IT Infrastructure OMAS",
            "accessServiceURLMarker": "it-infrastructure",
            "accessServiceDescription": "Manage information about the deployed IT infrastructure",
            "accessServiceWiki": "https://egeria-project.org/services/omas/it-infrastructure/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 212,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.datascience.admin.DataScienceAdmin",
            "accessServiceName": "Data Science",
            "accessServiceFullName": "Data Science OMAS",
            "accessServiceURLMarker": "data-science",
            "accessServiceDescription": "Create and manage data science definitions and models",
            "accessServiceWiki": "https://egeria-project.org/services/omas/data-science/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 207,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.communityprofile.admin.CommunityProfileAdmin",
            "accessServiceName": "Community Profile",
            "accessServiceFullName": "Community Profile OMAS",
            "accessServiceURLMarker": "community-profile",
            "accessServiceDescription": "Define personal profile and collaborate",
            "accessServiceWiki": "https://egeria-project.org/services/omas/community-profile/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 209,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.dataengine.server.admin.DataEngineAdmin",
            "accessServiceName": "Data Engine",
            "accessServiceFullName": "Data Engine OMAS",
            "accessServiceURLMarker": "data-engine",
            "accessServiceDescription": "Exchange process models and lineage with a data engine",
            "accessServiceWiki": "https://egeria-project.org/services/omas/data-engine/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 217,
            "accessServiceDevelopmentStatus": "TECHNICAL_PREVIEW",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.discoveryengine.admin.DiscoveryEngineAdmin",
            "accessServiceName": "Discovery Engine",
            "accessServiceFullName": "Discovery Engine OMAS",
            "accessServiceURLMarker": "discovery-engine",
            "accessServiceDescription": "Support for automated metadata discovery engines",
            "accessServiceWiki": "https://egeria-project.org/services/omas/discovery-engine/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 215,
            "accessServiceDevelopmentStatus": "TECHNICAL_PREVIEW",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.digitalarchitecture.admin.DigitalArchitectureAdmin",
            "accessServiceName": "Digital Architecture",
            "accessServiceFullName": "Digital Architecture OMAS",
            "accessServiceURLMarker": "digital-architecture",
            "accessServiceDescription": "Design of the digital services for an organization",
            "accessServiceWiki": "https://egeria-project.org/services/omas/digital-architecture/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 205,
            "accessServiceDevelopmentStatus": "STABLE",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.assetowner.admin.AssetOwnerAdmin",
            "accessServiceName": "Asset Owner",
            "accessServiceFullName": "Asset Owner OMAS",
            "accessServiceURLMarker": "asset-owner",
            "accessServiceDescription": "Manage an asset",
            "accessServiceWiki": "https://egeria-project.org/services/omas/asset-owner/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 225,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.stewardshipaction.admin.StewardshipActionAdmin",
            "accessServiceName": "Stewardship Action",
            "accessServiceFullName": "Stewardship Action OMAS",
            "accessServiceURLMarker": "stewardship-action",
            "accessServiceDescription": "Manage exceptions and actions from open governance",
            "accessServiceWiki": "https://egeria-project.org/services/omas/stewardship-action/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 220,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.governanceprogram.admin.GovernanceProgramAdmin",
            "accessServiceName": "Governance Program",
            "accessServiceFullName": "Governance Program OMAS",
            "accessServiceURLMarker": "governance-program",
            "accessServiceDescription": "Manage the governance program",
            "accessServiceWiki": "https://egeria-project.org/services/omas/governance-program/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 216,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.digitalservice.admin.DigitalServiceAdmin",
            "accessServiceName": "Digital Service",
            "accessServiceFullName": "Digital Service OMAS",
            "accessServiceURLMarker": "digital-service",
            "accessServiceDescription": "Manage a digital service through its lifecycle",
            "accessServiceWiki": "https://egeria-project.org/services/omas/digital-service/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 203,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.assetlineage.admin.AssetLineageAdmin",
            "accessServiceName": "Asset Lineage",
            "accessServiceFullName": "Asset Lineage OMAS",
            "accessServiceURLMarker": "asset-lineage",
            "accessServiceDescription": "Store asset lineage",
            "accessServiceWiki": "https://egeria-project.org/services/omas/asset-lineage/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 201,
            "accessServiceDevelopmentStatus": "STABLE",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.assetconsumer.admin.AssetConsumerAdmin",
            "accessServiceName": "Asset Consumer",
            "accessServiceFullName": "Asset Consumer OMAS",
            "accessServiceURLMarker": "asset-consumer",
            "accessServiceDescription": "Access assets through connectors",
            "accessServiceWiki": "https://egeria-project.org/services/omas/asset-consumer/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 200,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.assetcatalog.admin.AssetCatalogAdmin",
            "accessServiceName": "Asset Catalog",
            "accessServiceFullName": "Asset Catalog OMAS",
            "accessServiceURLMarker": "asset-catalog",
            "accessServiceDescription": "Search and understand your assets",
            "accessServiceWiki": "https://egeria-project.org/services/omas/asset-catalog/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 214,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.devops.admin.DevOpsAdmin",
            "accessServiceName": "DevOps",
            "accessServiceFullName": "DevOps OMAS",
            "accessServiceURLMarker": "devops",
            "accessServiceDescription": "Manage a DevOps pipeline",
            "accessServiceWiki": "https://egeria-project.org/services/omas/dev-ops/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 224,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.softwaredeveloper.admin.SoftwareDeveloperAdmin",
            "accessServiceName": "Software Developer",
            "accessServiceFullName": "Software Developer OMAS",
            "accessServiceURLMarker": "software-developer",
            "accessServiceDescription": "Interact with software development tools",
            "accessServiceWiki": "https://egeria-project.org/services/omas/software-developer/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 221,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.projectmanagement.admin.ProjectManagementAdmin",
            "accessServiceName": "Project Management",
            "accessServiceFullName": "Project Management OMAS",
            "accessServiceURLMarker": "project-management",
            "accessServiceDescription": "Manage governance related projects",
            "accessServiceWiki": "https://egeria-project.org/services/omas/project-management/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 219,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.governanceengine.admin.GovernanceEngineAdmin",
            "accessServiceName": "Governance Engine",
            "accessServiceFullName": "Governance Engine OMAS",
            "accessServiceURLMarker": "governance-engine",
            "accessServiceDescription": "Set up an operational governance engine",
            "accessServiceWiki": "https://egeria-project.org/services/omas/governance-engine/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 211,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.dataprivacy.admin.DataPrivacyAdmin",
            "accessServiceName": "Data Privacy",
            "accessServiceFullName": "Data Privacy OMAS",
            "accessServiceURLMarker": "data-privacy",
            "accessServiceDescription": "Manage governance of privacy",
            "accessServiceWiki": "https://egeria-project.org/services/omas/data-privacy/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          },
          {
            "class": "AccessServiceConfig",
            "accessServiceId": 222,
            "accessServiceDevelopmentStatus": "IN_DEVELOPMENT",
            "accessServiceAdminClass": "org.odpi.openmetadata.accessservices.securitymanager.admin.SecurityManagerAdmin",
            "accessServiceName": "Security Manager",
            "accessServiceFullName": "Security Manager OMAS",
            "accessServiceURLMarker": "security-manager",
            "accessServiceDescription": "Manages exchange of metadata with a security service",
            "accessServiceWiki": "https://egeria-project.org/services/omas/security-manager/overview/",
            "accessServiceOperationalStatus": "ENABLED"
          }
        ],
        "repositoryServicesConfig": {
          "class": "RepositoryServicesConfig",
          "auditLogConnections": [
            {
              "class": "Connection",
              "headerVersion": 0,
              "qualifiedName": "Console- default",
              "displayName": "Console",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "4afac741-3dcc-4c60-a4ca-a6dede994e3f",
                "qualifiedName": "Egeria:AuditLogDestinationConnector:Console",
                "displayName": "Console Audit Log Destination Connector",
                "description": "Connector supports logging of audit log messages to stdout.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.auditlogstore.console.ConsoleAuditLogStoreProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.auditlogstore.OMRSAuditLogStore"
                ],
                "recognizedConfigurationProperties": [
                  "supportedSeverities"
                ]
              },
              "configurationProperties": {
                "supportedSeverities": [
                  "<Unknown>",
                  "Information",
                  "Event",
                  "Decision",
                  "Action",
                  "Error",
                  "Exception",
                  "Security",
                  "Startup",
                  "Shutdown",
                  "Asset",
                  "Types",
                  "Cohort"
                ]
              }
            }
          ],
          "openMetadataArchiveConnections": [
            {
              "class": "Connection",
              "headerVersion": 0,
              "displayName": "Open Metadata Archive File content-packs/SimpleDataCatalog.json Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "f4b49aa8-4f8f-4e0d-a725-fef8fa6ae722",
                "qualifiedName": "Egeria:OpenMetadataArchiveStoreConnector:File",
                "displayName": "File-based Open Metadata Archive Store Connector",
                "description": "Connector supports storing of an open metadata archive as a single file stored using JSON format.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.archiveconnector.file.FileBasedOpenMetadataArchiveStoreProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore.OpenMetadataArchiveStore"
                ]
              },
              "endpoint": {
                "class": "Endpoint",
                "headerVersion": 0,
                "address": "content-packs/SimpleDataCatalog.json"
              }
            }
          ],
          "localRepositoryConfig": {
            "class": "LocalRepositoryConfig",
            "metadataCollectionId": "02694e83-a284-4f03-ac0c-34bfa2ce5c65",
            "localRepositoryMode": "OPEN_METADATA_NATIVE",
            "localRepositoryLocalConnection": {
              "class": "Connection",
              "headerVersion": 0,
              "displayName": "In Memory Local Repository Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "65cc9091-757f-4bcd-b937-426160be8bc2",
                "qualifiedName": "Egeria:OMRSRepositoryConnector:InMemory",
                "displayName": "In Memory OMRS Repository Connector",
                "description": "Native open metadata repository connector that maps open metadata calls to a set of in memory hash maps - demo use only.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector.OMRSMetadataCollectionManager"
                ]
              }
            },
            "localRepositoryRemoteConnection": {
              "class": "Connection",
              "headerVersion": 0,
              "displayName": "Local Repository Remote Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "guid": "75ea56d1-656c-43fb-bc0c-9d35c5553b9e",
                "qualifiedName": "Egeria:OMRSRepositoryConnector:CohortMemberClient:REST",
                "displayName": "REST Cohort Member Client Connector",
                "description": "Cohort member client connector that provides access to open metadata located in a remote repository via REST calls.",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector.OMRSMetadataCollectionManager"
                ]
              },
              "endpoint": {
                "class": "Endpoint",
                "headerVersion": 0,
                "address": "https://localhost:9443/servers/myMetadataServer"
              }
            },
            "eventsToSaveRule": "ALL",
            "eventsToSendRule": "ALL"
          },
          "enterpriseAccessConfig": {
            "class": "EnterpriseAccessConfig",
            "enterpriseMetadataCollectionName": "myMetadataServer Enterprise Metadata Collection",
            "enterpriseMetadataCollectionId": "78fbc21f-ffff-45ad-9466-310fc70337d0",
            "enterpriseOMRSTopicConnection": {
              "class": "VirtualConnection",
              "headerVersion": 0,
              "displayName": "Enterprise OMRS Topic Connection",
              "connectorType": {
                "class": "ConnectorType",
                "headerVersion": 0,
                "type": {
                  "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "typeName": "ConnectorType",
                  "typeVersion": 1,
                  "typeDescription": "A set of properties describing a type of connector."
                },
                "qualifiedName": "org.odpi.openmetadata.repositoryservices.connectors.omrstopic.OMRSTopicProvider",
                "displayName": "OMRS Topic Connector",
                "description": "Provides access to the OMRS Topic that is used to exchange events between members of a cohort, or to notify Open Metadata Access Services (OMASs) of changes to metadata in the enterprise.",
                "connectorProviderClassName": "org.odpi.openmetadata.repositoryservices.connectors.omrstopic.OMRSTopicProvider",
                "connectorFrameworkName": "Open Connector Framework (OCF)",
                "connectorInterfaceLanguage": "Java",
                "connectorInterfaces": [
                  "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                  "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                  "org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic.OpenMetadataTopicListener",
                  "org.odpi.openmetadata.frameworks.connectors.VirtualConnectorExtension",
                  "org.odpi.openmetadata.repositoryservices.connectors.omrstopic.OMRSTopic"
                ]
              },
              "embeddedConnections": [
                {
                  "class": "EmbeddedConnection",
                  "headerVersion": 0,
                  "position": 0,
                  "displayName": "Enterprise OMRS Events",
                  "embeddedConnection": {
                    "class": "Connection",
                    "headerVersion": 0,
                    "displayName": "Kafka Event Bus Connection",
                    "connectorType": {
                      "class": "ConnectorType",
                      "headerVersion": 0,
                      "type": {
                        "typeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                        "typeName": "ConnectorType",
                        "typeVersion": 1,
                        "typeDescription": "A set of properties describing a type of connector."
                      },
                      "guid": "ed8e682b-2fec-4403-b551-02f8c46322ef",
                      "qualifiedName": "Egeria:OpenMetadataTopicConnector:InMemory",
                      "displayName": "In Memory Open Metadata Topic Connector",
                      "description": "In Memory Open Metadata Topic Connector supports string based events over an in memory event bus.",
                      "connectorProviderClassName": "org.odpi.openmetadata.adapters.eventbus.topic.inmemory.InMemoryOpenMetadataTopicProvider",
                      "connectorFrameworkName": "Open Connector Framework (OCF)",
                      "connectorInterfaceLanguage": "Java",
                      "connectorInterfaces": [
                        "org.odpi.openmetadata.frameworks.connectors.SecureConnectorExtension",
                        "org.odpi.openmetadata.frameworks.auditlog.AuditLoggingComponent",
                        "java.lang.Runnable",
                        "org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic.OpenMetadataTopic"
                      ]
                    },
                    "endpoint": {
                      "class": "Endpoint",
                      "headerVersion": 0,
                      "address": "myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic"
                    },
                    "configurationProperties": {
                      "local.server.id": "b49ab686-7b3b-4429-97fd-8d964ef3a4ff"
                    }
                  }
                }
              ]
            },
            "enterpriseOMRSTopicProtocolVersion": "V1"
          }
        },
        "auditTrail": [
          "Sun Jun 11 20:49:09 BST 2023 garygeeke updated configuration for local server type name to Metadata Access Store.",
          "Sun Jun 11 20:52:09 BST 2023 garygeeke updated configuration for the local repository.",
          "Sun Jun 11 20:58:16 BST 2023 garygeeke updated configuration for access services.",
          "Sun Jun 11 20:58:16 BST 2023 garygeeke updated configuration for enterprise repository services (used by access services).",
          "Sun Jun 11 21:07:23 BST 2023 garygeeke updated list of open metadata archives loaded at server start up."
        ]
      }
    }
    ```
    
    You have probably noticed how quickly the configuration document grew into a complex structure. The commands you used made use of all of the configuration default values. There are other commands that enable you to customize the configuration document to
    adapt it to specific environment.  However, the defaults provide a good starting point.
    
    !!! education "Further reading"
        The contents of this tutorial cover a very simple OMAG server configuration. For guidance on configuring more complex OMAG servers see the [Administration Services User Guide](/guides/admin)
    
??? education "Activating an OMAG Server in the OMAG Server Platform"
    ### Activating OMAG servers in the OMAG server platform
    
    Once you have [created a configuration document for an OMAG server](task-creating-configuration-documents.md)
    it is started in the [OMAG Server Platform](/concepts/omag-server-platform) using the following command (this is request **7.** in Postman).
    
    ```
    POST https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platformservers/myMetadataServer/instance
    ```
    
    The response from the command lists the subsystems that have been activated in the OMAG server:
    
    ```json
    {
      "class": "SuccessMessageResponse",
      "relatedHTTPCode": 200,
      "successMessage": "Sun Jun 11 21:19:16 BST 2023 myMetadataServer is running the following services: [Open Metadata Repository Services (OMRS), Connected Asset Services, Open Metadata Store Services, Open Integration Service, Data Manager OMAS, Subject Area OMAS, Glossary View OMAS, Design Model OMAS, Security Officer OMAS, Asset Manager OMAS, IT Infrastructure OMAS, Data Science OMAS, Community Profile OMAS, Data Engine OMAS, Discovery Engine OMAS, Digital Architecture OMAS, Asset Owner OMAS, Stewardship Action OMAS, Governance Program OMAS, Digital Service OMAS, Asset Lineage OMAS, Asset Consumer OMAS, Asset Catalog OMAS, DevOps OMAS, Software Developer OMAS, Project Management OMAS, Governance Engine OMAS, Data Privacy OMAS, Security Manager OMAS]"
    }
    ```
    
    The window where your OMAG Server Platform is running will show the start-up
    audit log messages, something like this:
    
    ```text
     Project Egeria - Open Metadata and Governance
        ____   __  ___ ___    ______   _____                                 ____   _         _     ___
       / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
      / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
     / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
     \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/
    
     :: Powered by Spring Boot (v3.0.6) ::
    
    2023-06-11T20:48:53.256+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 17.0.6 with PID 4805 (/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz/platform/omag-server-platform-4.2-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz)
    2023-06-11T20:48:53.259+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to 1 default profile: "default"
    2023-06-11T20:48:56.607+01:00  INFO 4805 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
    2023-06-11T20:48:57.924+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Working directory is: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.2-SNAPSHOT-distribution.tar.gz
    2023-06-11T20:48:57.924+01:00  WARN 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Java trust store 'javax.net.ssl.trustStore' is null - this is needed by Tomcat - using 'server.ssl.trust-store'
    2023-06-11T20:49:00.519+01:00  INFO 4805 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 9443 (https) with context path ''
    2023-06-11T20:49:00.539+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Started OMAGServerPlatform in 7.942 seconds (process running for 8.699)
    Sun Jun 11 20:49:00 BST 2023 No OMAG servers listed in startup configuration
    Sun Jun 11 20:49:00 BST 2023 OMAG server platform ready for more configuration
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0064 The Open Metadata Repository Services (OMRS) has initialized the audit log for the Metadata Access Store called myMetadataServer
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMAG-ADMIN-0001 The myMetadataServer server is configured with a max page size of 1000
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0001 The Open Metadata Repository Services (OMRS) is initializing the subsystems to support a new server
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0002 Enterprise access through the Enterprise Repository Services is initializing
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0003 The local repository is initializing the metadata collection named myMetadataServer with an id of 02694e83-a284-4f03-ac0c-34bfa2ce5c65
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0029 The local repository outbound event manager is initializing
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0030 Registering the Local Repository to Local Enterprise event consumer with the local repository outbound event manager
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0044 The connector for the local repository is being started in mode Open Metadata Native using connector provider org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider and configuration properties null
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0045 The connector for the local repository has been initialized
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0046 The connector for the local repository is about to be started
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Startup OMRS-AUDIT-0047 The connector for the local repository has been started
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Information OMRS-AUDIT-0050 The Open Metadata Repository Services (OMRS) is about to process open metadata archive Open Metadata Types
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called object with a unique identifier of 1c4b21f4-0b67-41a7-a6ed-2af185eb9b3b and a version number of 1 from Egeria (4.2)
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called boolean with a unique identifier of 3863f010-611c-41fe-aaae-5d4d427f863b and a version number of 1 from Egeria (4.2)
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called byte with a unique identifier of 6b7d410a-2e8a-4d12-981a-a806449f9bdb and a version number of 1 from Egeria (4.2)
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called char with a unique identifier of b0abebe5-cf85-4065-86ad-f3c6360ed9c7 and a version number of 1 from Egeria (4.2)
    Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called short with a unique identifier of 8e95b966-ab60-46d4-a03f-40c5a1ba6c2a and a version number of 1 from Egeria (4.2)
     :        :         :          :        :       :        :         :          :        :    :        :         :          :        :
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Types OMRS-AUDIT-0303 The local server has updated an existing type called DigitalProduct with a unique identifier of 4aaaa7ca-6b4b-4c4b-997f-d5dfd42917b0 to version number of 3 using a patch from Egeria (4.1)
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Types OMRS-AUDIT-0303 The local server has updated an existing type called Process with a unique identifier of d8f33bd7-afa9-4a11-a8c7-07dcec83c050 to version number of 3 using a patch from Egeria (4.1)
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Information OMRS-AUDIT-0053 The Open Metadata Repository Services (OMRS) has processed 1025 types and 0 instances from open metadata archive Open Metadata Types
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OCF-FILE-OPEN-METADATA-ARCHIVE-STORE-CONNECTOR-0001 Opening file "content-packs/SimpleDataCatalog.json" for Open Metadata Archive Store
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Information OMRS-AUDIT-0050 The Open Metadata Repository Services (OMRS) is about to process open metadata archive SimpleDataCatalog
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Information OMRS-AUDIT-0053 The Open Metadata Repository Services (OMRS) has processed 0 types and 15 instances from open metadata archive SimpleDataCatalog
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Repository REST Services
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Repository REST Services has started
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0007 The Open Metadata Repository Services (OMRS) has initialized
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0031 The local repository outbound event manager is starting with 1 type definition event consumer(s) and 1 instance event consumer(s)
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0032 The local repository outbound event manager is sending out the 1025 type definition events that were generated and buffered during server initialization
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Connected Asset Services
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Connected Asset Services has started
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup CONNECTED-ASSET-SERVICES-0001 The Open Connector Framework (OCF) Metadata Management Service is initializing the connected asset services in a new server instance
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup CONNECTED-ASSET-SERVICES-0003 The Open Connector Framework (OCF) Metadata Management Service has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OPEN-METADATA-STORE-0001 The Open Metadata Store Services are initializing a new server instance
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OPEN-METADATA-STORE-0005 The Open Metadata Store Services has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OPEN-INTEGRATION-SERVICE-0001 The Open Integration Service is initializing a new server instance
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OPEN-INTEGRATION-SERVICE-0005 The Open Integration Service has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMAG-ADMIN-0010 The Open Metadata Access Services (OMASs) are starting
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Data Manager OMAS
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Data Manager OMAS has started
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMAS-DATA-MANAGER-0001 The Data Manager Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMAS-DATA-MANAGER-0004 The Data Manager Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Subject Area OMAS
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Subject Area OMAS has started
    Sun Jun 11 21:19:15 BST 2023 myMetadataServer Startup OMAS-SUBJECT_AREA-0001 The Subject Area Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SUBJECT_AREA-0003 The Subject Area Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Glossary View OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Glossary View OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GLOSSARY-VIEW-0001 The Glossary View Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GLOSSARY-VIEW-0002 The Glossary View Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Design Model OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Design Model OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DESIGN-MODEL-0001 The Design Model Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DESIGN-MODEL-0003 The Design Model Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Security Officer OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Security Officer OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SECURITY-OFFICER-0001 The Security Officer Open Metadata Access Service (OMAS) is initializing
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAG-ADMIN-0209 The Security Officer OMAS Open Metadata Access Service (OMAS) is registering a listener with the enterprise OMRS Topic for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SECURITY-OFFICER-0003 The Security Officer Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Asset Manager OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Asset Manager OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-MANAGER-0001 The Asset Manager Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-MANAGER-0005 The Asset Manager Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the IT Infrastructure OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the IT Infrastructure OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-IT-INFRASTRUCTURE-0001 The IT Infrastructure Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-IT-INFRASTRUCTURE-0003 The IT Infrastructure Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Data Science OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Data Science OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-SCIENCE-0001 The Data Science Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-SCIENCE-0003 The Data Science Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Community Profile OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Community Profile OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-COMMUNITY-PROFILE-0001 The Community Profile Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAG-ADMIN-0205 The Community Profile Open Metadata Access Service (OMAS) is not collecting karma points in this server
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAG-ADMIN-0207 The Community Profile Open Metadata Access Service (OMAS) is using the default threshold for reporting Karma Point Plateaus: 500
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-COMMUNITY-PROFILE-0004 The Community Profile Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Data Engine OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Data Engine OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-ENGINE-0001 The Data Engine Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-ENGINE-0002 The Data Engine Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Discovery Engine OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Discovery Engine OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DISCOVERY-ENGINE-0001 The Discovery Engine Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DISCOVERY-ENGINE-0003 The Discovery Engine Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Digital Architecture OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Digital Architecture OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DIGITAL-ARCHITECTURE-0001 The Digital Architecture Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DIGITAL-ARCHITECTURE-0003 The Digital Architecture Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Asset Owner OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Asset Owner OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-OWNER-0001 The Asset Owner Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-OWNER-0003 The Asset Owner Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Stewardship Action OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Stewardship Action OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-STEWARDSHIP-ACTION-0001 The Stewardship Action Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-STEWARDSHIP-ACTION-0003 The Stewardship Action Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Governance Program OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Governance Program OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GOVERNANCE-PROGRAM-0001 The Governance Program Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GOVERNANCE-PROGRAM-0002 The Governance Program Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Digital Service OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Digital Service OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DIGITAL-SERVICE-0001 The Digital Service Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DIGITAL-SERVICE-0003 The Digital Service Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Asset Lineage OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Asset Lineage OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-LINEAGE-0001 The Asset Lineage Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-LINEAGE-0002 The Asset Lineage Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Asset Consumer OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Asset Consumer OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-CONSUMER-0001 The Asset Consumer Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-CONSUMER-0003 The Asset Consumer Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Asset Catalog OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Asset Catalog OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-CATALOG-0002 The Asset Catalog Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-ASSET-CATALOG-0001 The Asset Catalog Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the DevOps OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the DevOps OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DEV-OPS-0001 The DevOps Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DEV-OPS-0003 The DevOps Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Software Developer OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Software Developer OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SOFTWARE-DEVELOPER-0001 The Software Developer Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SOFTWARE-DEVELOPER-0003 The Software Developer Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Project Management OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Project Management OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-PROJECT-MANAGEMENT-0001 The Project Management Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-PROJECT-MANAGEMENT-0003 The Project Management Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Governance Engine OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Governance Engine OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GOVERNANCE-ENGINE-0001 The Governance Engine Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-GOVERNANCE-ENGINE-0005 The Governance Engine Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Data Privacy OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Data Privacy OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-PRIVACY-0001 The Data Privacy Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-DATA-PRIVACY-0003 The Data Privacy Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0040 An enterprise OMRS connector has been created for the Security Manager OMAS
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0041 The enterprise OMRS connector for the Security Manager OMAS has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SECURITY-MANAGER-0001 The Security Manager Open Metadata Access Service (OMAS) is initializing a new server instance
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAS-SECURITY-MANAGER-0005 The Security Manager Open Metadata Access Service (OMAS) has initialized a new instance for server myMetadataServer
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAG-ADMIN-0012 25 out of 25 configured Open Metadata Access Services (OMASs) have started.
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0019 An OMRS Topic Connector has registered with an event bus connector for topic myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0020 An OMRS Topic Connector is ready to send and receive events on topic myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMRS-AUDIT-0015 The listener thread for an OMRS Topic Connector for topic myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic has started
    Sun Jun 11 21:19:16 BST 2023 myMetadataServer Startup OMAG-ADMIN-0004 The myMetadataServer server has successfully completed start up.  The following services are running: [Open Metadata Repository Services (OMRS), Connected Asset Services, Open Metadata Store Services, Open Integration Service, Data Manager OMAS, Subject Area OMAS, Glossary View OMAS, Design Model OMAS, Security Officer OMAS, Asset Manager OMAS, IT Infrastructure OMAS, Data Science OMAS, Community Profile OMAS, Data Engine OMAS, Discovery Engine OMAS, Digital Architecture OMAS, Asset Owner OMAS, Stewardship Action OMAS, Governance Program OMAS, Digital Service OMAS, Asset Lineage OMAS, Asset Consumer OMAS, Asset Catalog OMAS, DevOps OMAS, Software Developer OMAS, Project Management OMAS, Governance Engine OMAS, Data Privacy OMAS, Security Manager OMAS]
    ```
    
    The start-up messages show the [open metadata types](/types) being loaded, followed by the open metadata archive `content-packs/SimpleDataCatalog.json`.  Then the local repository is initialized and finally the OMASs are started.

??? education "Calling the Open Metadata and Governance APIs"
    ### Calling Open Metadata and Governance Services
    
    Now that the metadata server is started, it is possible to query the metadata.
    
    Egeria offers many different REST APIs to retrieve and maintain metadata.  In this exercise it is not possible to try them all out.  The aim is to show an example of how metadata is retrieved.  The command below finds [assets](/concepts/asset).  Assets represent resources such as data sets and servers used by the organization.
    
    ```text
    POST https://localhost:9443/servers/myMetadataServer/open-metadata/access-services/asset-owner/users/peterprofile/assets/by-search-string?startFrom=0&pageSize=10
    ```
    The request body contains the search parameters.
    ```json
    {
        "class" : "SearchStringRequestBody",
        "searchString" : ".*."
    }
    ```
    The results show there are two assets in the metadata repository - a database and a database schema.
    ```json
    {
      "class": "AssetElementsResponse",
      "relatedHTTPCode": 200,
      "startingFromElement": 0,
      "assets": [
        {
          "elementHeader": {
            "class": "ElementHeader",
            "headerVersion": 0,
            "status": "ACTIVE",
            "type": {
              "typeId": "eab811ec-556a-45f1-9091-bc7ac8face0f",
              "typeName": "DeployedDatabaseSchema",
              "superTypeNames": [
                "DataSet",
                "Asset",
                "Referenceable",
                "OpenMetadataRoot"
              ],
              "typeVersion": 1,
              "typeDescription": "A collection of database tables and views running in a database server."
            },
            "origin": {
              "sourceServer": "myMetadataServer",
              "originCategory": "DEREGISTERED_REPOSITORY",
              "homeMetadataCollectionId": "2216ab62-176a-46c0-b889-9aa081754b54",
              "homeMetadataCollectionName": "SimpleDataCatalog"
            },
            "versions": {
              "createdBy": "Egeria",
              "createTime": "2021-09-19T10:10:51.579+00:00",
              "version": 1
            },
            "guid": "4782e08b-043c-4017-9b2f-d63163f67fd8"
          },
          "assetProperties": {
            "class": "AssetProperties",
            "qualifiedName": "V37B8752.FH567.sys/BRANCH.RETAILSCHEMA",
            "typeName": "DeployedDatabaseSchema",
            "displayName": "RETAILSCHEMA",
            "name": "RETAILSCHEMA",
            "description": "Retail banking schema.",
            "ownerType": "OTHER"
          }
        },
        {
          "elementHeader": {
            "class": "ElementHeader",
            "headerVersion": 0,
            "status": "ACTIVE",
            "type": {
              "typeId": "0921c83f-b2db-4086-a52c-0d10e52ca078",
              "typeName": "Database",
              "superTypeNames": [
                "DataStore",
                "Asset",
                "Referenceable",
                "OpenMetadataRoot"
              ],
              "typeVersion": 2,
              "typeDescription": "A data store containing relational data."
            },
            "origin": {
              "sourceServer": "myMetadataServer",
              "originCategory": "DEREGISTERED_REPOSITORY",
              "homeMetadataCollectionId": "2216ab62-176a-46c0-b889-9aa081754b54",
              "homeMetadataCollectionName": "SimpleDataCatalog"
            },
            "versions": {
              "createdBy": "Egeria",
              "createTime": "2021-09-19T10:10:51.579+00:00",
              "version": 1
            },
            "guid": "076b4498-a099-4c6b-9243-73e816b28504"
          },
          "assetProperties": {
            "class": "AssetProperties",
            "qualifiedName": "V37B8752.FH567.sys/BRANCH",
            "typeName": "Database",
            "displayName": "BRANCH Database",
            "name": "BRANCH Database",
            "description": "Main branch system database.",
            "ownerType": "OTHER"
          }
        }
      ]
    }
    ```
    
    !!! education "Further APIs"
        * The [Open Metadata Access Services (OMASs)](/services/omas) show the range of APIs offered by Egeria.
        * [Finding Metadata](/guides/developer/finding-metadata/overview) explains how metadata retrieval requests work.

??? education "Shutting down a server"
    ### Shutting down OMAG servers in the OMAG server platform
    
    Once you have finished calling the open metadata and governance APIs you can stop your server in the [OMAG Server Platform](/concepts/omag-server-platform) using the following command (this is command **8.** in Postman).
    
    ```
    POST https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform/servers/myMetadataServer/instance
    ```
    
    The window where your OMAG server platform is running will show the shutdown messages
    
    ```text
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAG-ADMIN-0005 The myMetadataServer server has begun the shutdown process
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DATA-MANAGER-0005 The Data Manager Open Metadata Access Service (OMAS) is shutting down server instance myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-SUBJECT_AREA-0004 The Subject Area Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-GLOSSARY-VIEW-0003 The Glossary View Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DESIGN-MODEL-0004 The Design Model Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-SECURITY-OFFICER-0005 The Security Officer Open Metadata Access Service (OMAS) has completed shutdown of server instance myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-ASSET-MANAGER-0006 The Asset Manager Open Metadata Access Service (OMAS) is shutting down server instance myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-IT-INFRASTRUCTURE-0004 The IT Infrastructure Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DATA-SCIENCE-0004 The Data Science Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-COMMUNITY-PROFILE-0005 The Community Profile Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DATA-ENGINE-0003 The Data Engine Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DISCOVERY-ENGINE-0008 The Discovery Engine Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DIGITAL-ARCHITECTURE-0004 The Digital Architecture Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-ASSET-OWNER-0004 The Asset Owner Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-STEWARDSHIP-ACTION-0004 The Stewardship Action Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-GOVERNANCE-PROGRAM-0004 The Governance Program Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DIGITAL-SERVICE-0004 The Digital Service Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-ASSET-LINEAGE-0003 The Asset Lineage Open Metadata Access Service (OMAS) is shutting down server instance myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-ASSET-CONSUMER-0004 The Asset Consumer Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-ASSET-CATALOG-0004 The Asset Catalog Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DEV-OPS-0004 The DevOps Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-SOFTWARE-DEVELOPER-0004 The Software Developer Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-PROJECT-MANAGEMENT-0004 The Project Management Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-GOVERNANCE-ENGINE-0012 The Governance Engine Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-DATA-PRIVACY-0004 The Data Privacy Open Metadata Access Service (OMAS) is shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAS-SECURITY-MANAGER-0006 The Security Manager Open Metadata Access Service (OMAS) is shutting down server instance myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown CONNECTED-ASSET-SERVICES-0004 The Open Connector Framework (OCF) Metadata Management Service is shutting down its instance of the connected asset services for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OPEN-METADATA-STORE-0012 The Open Metadata Store Services are shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OPEN-INTEGRATION-SERVICE-0012 The Open Integration Service are shutting down its instance for server myMetadataServer
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMRS-AUDIT-0010 The Open Metadata Repository Services (OMRS) is disconnecting the open metadata repositories
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMRS-AUDIT-0021 The OMRS Topic Listener has disconnected the event bus connectors for topic myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMRS-AUDIT-0011 The Open Metadata Repository Services (OMRS) has disconnected from the open metadata repositories
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMAG-ADMIN-0006 The myMetadataServer server has completed shutdown
    Sun Jun 11 21:52:43 BST 2023 myMetadataServer Shutdown OMRS-AUDIT-0016 The listener thread for the OMRS Topic Connector for topic myMetadataServer.openmetadata.repositoryservices.enterprise.myMetadataServer.OMRSTopic has shutdown
    ```
    
    Even though the server has stopped, the platform is still running and it is possible to query the platform about the server.  The next command queries the status of the server (this is command **9.** in Postman).
    
    ```
    GET https://localhost:9443/open-metadata/platform-services/users/garygeeke/server-platform/servers/myMetadataServer/status
    ```
    
    You can see that it is not currently active and the times when it was active.
    
    ```json
    {
      "class": "ServerStatusResponse",
      "relatedHTTPCode": 200,
      "serverName": "myMetadataServer",
      "serverType": "Metadata Access Store",
      "serverEndTime": "2023-06-11T20:52:43.631+00:00",
      "serverHistory": [
        {
          "startTime": "2023-06-11T20:19:15.181+00:00",
          "endTime": "2023-06-11T20:52:43.631+00:00"
        }
      ],
      "active": false
    }
    ```
    
    You can experiment by starting and stopping your server and trying this status command both while it is running and after it is stopped to see the different statuses.
    
    !!! education "The platform operation services"
        Explore the [Platform Services](/services/platform-services/overview) to discover more commands to monitor and control the OMAG Server Platform.
    
??? education "Deleting a server's configuration"
    ### Deleting an OMAG server's configuration
    
    An [OMAG Server](/concepts/omag-server)'s configuration document can be deleted from the configuration store using the following command.
    
    ```
    DELETE https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/cocoMDS1/instance
    ```

??? education "Shutting down the platform"
    ### Stopping the OMAG server platform
    
    Once you have Stopped your OMAG server you can stop the [OMAG Server Platform](/concepts/omag-server-platform) using the following command (this is request **10.** in Postman).
    
    ```
    POST https://localhost:9443/open-metadata/admin-services/users/garygeeke/server-platform/instance
    ```
    
    There is no response from the request because the platform exits before it sends the response.
    

## Digging Deeper

* [Running the Egeria samples](/education/tutorials/running-samples-tutorial/overview)
to understand more about the different Egeria APIs.
* [Calling the OMAG Clients from Java](/education/tutorials/omag-client-tutorial/overview)
to understand how to call Egeria APIs from your code.
* [Running the Open Metadata Conformance Suite](/guides/cts/overview)
to understand how a technology/software product can demonstrate
its conformance to the Egeria standards.

--8<-- "snippets/abbr.md"