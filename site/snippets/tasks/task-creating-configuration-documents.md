<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

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

The **localServerId** property is a unique identifier given to the server and is used internally to improve the performance of its interaction with external components such as Apache Kafka.

The **localServerName** is the name of the OMAG server supplied on the command.

The **localServerType**, **localServerURL**, **localServerUserId** and **maxPageSize** are set to their default values and can be changed.

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

It is possible to activate each OMAS individually, but for the sake of this exercise we are going to activate them all using this command (request **5.** in Postman).

```
GET https://localhost:9443/open-metadata/admin-services/users/garygeeke/servers/myMetadataServer/access-services/no-topics
```

The OMASs provide both REST APIs and notifications.  The `no-topics` part of the command turns off the notifications, so we don't need to set up Apache Kafka for this exercise.

The final command requests that an [Open Metadata Archive](/concepts/open-metadata-archive) is loaded to provide some sample metadata.  The name of the open metadata archive file (`content-packs/SimpleCatalog.json`) is sent in the request body.

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
          "displayName": "Open Metadata Archive File content-packs/SimpleCatalog.json Connection",
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
            "address": "content-packs/SimpleCatalog.json"
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

You have probably noticed how quickly the configuration document grew into a complex structure. The commands you used made use of all the configuration default values. There are other commands that enable you to customize the configuration document to
adapt it to specific environment.  However, the defaults provide a good starting point.

!!! education "Further reading"
    The contents of this tutorial cover a very simple OMAG server configuration. For guidance on configuring more complex OMAG servers see the [Administration Services User Guide](/guides/admin).


--8<-- "snippets/abbr.md"


