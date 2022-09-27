<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Platform report for: https://localhost:9443

## Platform deployment
* **Egeria version**: Egeria OMAG Server Platform (version 3.12-SNAPSHOT)
* **Configuration document store connector**: *null*
* **Platform security connector**: *null*
## Registered services
* **Data Manager OMAS**: Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.
* **Subject Area OMAS**: Document knowledge about a subject area
* **Design Model OMAS**: Exchange design model content with tools and standard packages
* **Glossary View OMAS**: Support glossary terms visualization
* **Asset Manager OMAS**: Manage metadata from a third party asset manager
* **Security Officer OMAS**: Set up rules and security tags to protect data
* **IT Infrastructure OMAS**: Manage information about the deployed IT infrastructure
* **Data Science OMAS**: Create and manage data science definitions and models
* **Community Profile OMAS**: Define personal profile and collaborate
* **Discovery Engine OMAS**: Support for automated metadata discovery engines
* **Data Engine OMAS**: Exchange process models and lineage with a data engine
* **Digital Architecture OMAS**: Design of the digital services for an organization
* **Asset Owner OMAS**: Manage an asset
* **Stewardship Action OMAS**: Manage exceptions and actions from open governance
* **Governance Program OMAS**: Manage the governance program
* **Digital Service OMAS**: Manage a digital service's lifecycle
* **Asset Lineage OMAS**: Store asset lineage
* **Analytics Modeling OMAS**: Provides metadata information for Analytics Modeling.
* **Asset Consumer OMAS**: Access assets through connectors
* **Asset Catalog OMAS**: Search and understand your assets
* **DevOps OMAS**: Manage a DevOps pipeline
* **Software Developer OMAS**: Interact with software development tools
* **Project Management OMAS**: Manage governance related projects
* **Governance Engine OMAS**: Set up an operational governance engine
* **Data Privacy OMAS**: Manage governance of privacy
* **Security Manager OMAS**: Manages exchange of metadata with a security service
* **Repository Governance OMES**: Maintains open metadata archives based on the activity in the connected cohorts.
* **Governance Action OMES**: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
* **Asset Analysis OMES**: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
* **Files Integrator OMIS**: Extract metadata about files stored in a file system or file manager.
* **Topic Integrator OMIS**: Exchange metadata with third party event-based brokers.
* **API Integrator OMIS**: Exchange metadata with third party API Gateways.
* **Security Integrator OMIS**: Distribute security properties to security enforcement points.
* **Search Integrator OMIS**: Store metadata with a third party technology that is focused on search efficiency.
* **Database Integrator OMIS**: Extract metadata such as schema, tables and columns from database managers.
* **Lineage Integrator OMIS**: Manage capture of lineage from a third party tool.
* **Catalog Integrator OMIS**: Exchange metadata with third party data catalogs.
* **Analytics Integrator OMIS**: Exchange metadata with third party analytics tools.
* **Display Integrator OMIS**: Exchange metadata with applications that display data to users.
* **Organization Integrator OMIS**: Load information about the teams and people in an organization and return collaboration activity.
* **Glossary Author OMVS**: View Service for glossary authoring.
* **Dynamic Infrastructure and Operations OMVS**: Explore and operate an open metadata ecosystem.
* **Repository Explorer OMVS**: Explore open metadata instances.
* **Type Explorer OMVS**: Explore the open metadata types in a repository or cohort.
* **Server Author OMVS**: Author servers.
## Platform servers
### Server: mds1
* **Type**: Metadata Access Store
* **Description**: Metadata Access Store called mds1 running on platform https://localhost:9443
* **UserId**: cocoMDS1npa
#### Security Connector
* **Implementation**: org.odpi.openmetadata.metadatasecurity.samples.CocoPharmaServerSecurityProvider
* **Location**: *null*
#### Local Repository
* **Local Repository Mode**: Open Metadata Native
##### Local Repository Connector
* **Implementation**: org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider
* **Location**: *null*
##### Local Repository Remote Connector
* **Implementation**: org.odpi.openmetadata.adapters.repositoryservices.rest.repositoryconnector.OMRSRESTRepositoryConnectorProvider
* **Location**: https://localhost:9443/servers/mds1
#### Runtime Status
* **Last Start Time**: Mon Feb 14 11:31:24 GMT 2022
* **Server Active Status**: Running
##### History
* **Start Time**: Mon Feb 14 10:43:01 GMT 2022
* **End Time**: Mon Feb 14 11:31:09 GMT 2022
* **Start Time**: Mon Feb 14 11:31:09 GMT 2022
* **End Time**: Mon Feb 14 11:31:24 GMT 2022
#### Services
##### Service: Asset Manager OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: [quarantine]
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetmanager.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetmanager.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Open Metadata Repository Services (OMRS)
* **Service Status**: Running
##### Service: Connected Asset Services
* **Service Status**: Starting
##### Service: Community Profile OMAS
* **Service Status**: Running
###### Service Options
* **KarmaPointPlateau**: 10
* **SupportedZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: []
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.communityprofile.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.communityprofile.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Data Manager OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: [quarantine]
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.datamanager.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.datamanager.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Digital Architecture OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: [quarantine]
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.digitalarchitecture.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.digitalarchitecture.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Asset Consumer OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: []
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetconsumer.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetconsumer.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Governance Program OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: [quarantine]
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.governanceprogram.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.governanceprogram.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
##### Service: Asset Owner OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files, personal-files]
* **DefaultZones**: [quarantine]
###### Connectors
###### ==> InTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetowner.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}
###### ==> OutTopic
* **Implementation**: org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider
* **Location**: egeria.omag.server.mds1.omas.assetowner.inTopic
* **Configuration Properties**: {producer={bootstrap.servers=localhost:9092}, local.server.id=e6afd331-1853-42d0-a816-bb1eeb30c7b8, consumer={bootstrap.servers=localhost:9092, auto.commit.interval.ms=1}}

--8<-- "snippets/abbr.md"