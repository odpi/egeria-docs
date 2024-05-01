<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

### Activating OMAG servers in the OMAG Server Platform

Once you have created a configuration document for an OMAG server, it is started in the [OMAG Server Platform](/concepts/omag-server-platform) using the following command (this is request **7.** in Postman).

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

The window where your OMAG Server Platform is running will show the start-up audit log messages, something like this:

```text
 Project Egeria - Open Metadata and Governance
    ____   __  ___ ___    ______   _____                                 ____   _         _     ___
   / __ \ /  |/  //   |  / ____/  / ___/ ___   ____ _   __ ___   ____   / _  \ / / __    / /  / _ /__   ____ _  _
  / / / // /|_/ // /| | / / __    \__ \ / _ \ / __/| | / // _ \ / __/  / /_/ // //   |  / _\ / /_ /  | /  _// || |
 / /_/ // /  / // ___ |/ /_/ /   ___/ //  __// /   | |/ //  __// /    /  __ // // /  \ / /_ /  _// / // /  / / / /
 \____//_/  /_//_/  |_|\____/   /____/ \___//_/    |___/ \___//_/    /_/    /_/ \__/\//___//_/   \__//_/  /_/ /_/

 :: Powered by Spring Boot (v3.0.6) ::

2023-06-11T20:48:53.256+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Starting OMAGServerPlatform using Java 17.0.6 with PID 4805 (/Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz/platform/omag-server-platform-4.3-SNAPSHOT.jar started by mandy-chessell in /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz)
2023-06-11T20:48:53.259+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : No active profile set, falling back to 1 default profile: "default"
2023-06-11T20:48:56.607+01:00  INFO 4805 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 9443 (https)
2023-06-11T20:48:57.924+01:00  INFO 4805 --- [           main] o.o.o.s.springboot.OMAGServerPlatform    : Working directory is: /Users/mandy-chessell/CloudStation/Drive/Code/ODPi/egeria-code/egeria/open-metadata-distribution/open-metadata-assemblies/build/unpacked/egeria-4.3-distribution.tar.gz
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
Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called object with a unique identifier of 1c4b21f4-0b67-41a7-a6ed-2af185eb9b3b and a version number of 1 from Egeria (4.3)
Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called boolean with a unique identifier of 3863f010-611c-41fe-aaae-5d4d427f863b and a version number of 1 from Egeria (4.3)
Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called byte with a unique identifier of 6b7d410a-2e8a-4d12-981a-a806449f9bdb and a version number of 1 from Egeria (4.3)
Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called char with a unique identifier of b0abebe5-cf85-4065-86ad-f3c6360ed9c7 and a version number of 1 from Egeria (4.3)
Sun Jun 11 21:19:14 BST 2023 myMetadataServer Types OMRS-AUDIT-0301 The local server has added a new type called short with a unique identifier of 8e95b966-ab60-46d4-a03f-40c5a1ba6c2a and a version number of 1 from Egeria (4.3)
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

The start-up messages show the [open metadata types](/types) being loaded, followed by the open metadata archive `content-packs/SimpleCatalog.json`.  Then the local repository is initialized and finally the OMASs are started.



