<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Activating OMAG servers in the OMAG server platform

Once you have finished [calling the open metadata and governance APIs](/education/tutorials/omag-server-tutorial/task-calling-omag-apis)
you can stop your server in the
[OMAG Server Platform](/concepts/omag-server-platform)
using the following command (this is command **8.** in Postman).

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

## Next steps

Now the OMAG Server has stopped, you can [shut down your OMAG Server Platform](/education/tutorials/omag-server-tutorial/task-stopping-omag-server-platform).

--8<-- "snippets/abbr.md"


