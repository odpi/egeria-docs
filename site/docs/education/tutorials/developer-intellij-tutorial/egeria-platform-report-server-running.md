<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Platform report for: https://localhost:9443

## Platform deployment
* **Egeria version**: Egeria OMAG Server Platform (version 5.0)
* **Configuration document store connector**: *null*
* **Platform security connector**: *null*
## Registered services
* **Data Manager OMAS**: Capture changes to the data stores and data set managed by a data manager such as a database server, content manager or file system.
* **Design Model OMAS**: Exchange design model content with tools and standard packages
* **Asset Manager OMAS**: Manage metadata from a third party asset manager
* **IT Infrastructure OMAS**: Manage information about the deployed IT infrastructure
* **Data Science OMAS**: Create and manage data science definitions and models
* **Community Profile OMAS**: Define personal profile and collaborate
* **Digital Architecture OMAS**: Design of the digital services for an organization
* **Asset Owner OMAS**: Manage an asset
* **Stewardship Action OMAS**: Manage exceptions and actions from open governance
* **Governance Program OMAS**: Manage the governance program
* **Digital Service OMAS**: Manage a digital service through its lifecycle
* **Asset Lineage OMAS**: Store asset lineage
* **Asset Consumer OMAS**: Access assets through connectors
* **DevOps OMAS**: Manage a DevOps pipeline
* **Software Developer OMAS**: Interact with software development tools
* **Project Management OMAS**: Manage governance related projects
* **Governance Server OMAS**: Set up an operational governance engine
* **Data Privacy OMAS**: Manage governance of privacy
* **Security Manager OMAS**: Manages exchange of metadata with a security service
* **Governance Action OMES**: Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.
* **Repository Governance OMES**: Dynamically governance open metadata repositories in the connected cohorts.
* **Survey Action OMES**: Analyses the content of an asset's real world counterpart, generates annotations in an open discovery report that is attached to the asset in the open metadata repositories.
* **Infrastructure Integrator OMIS**: Exchange information relating to IT infrastructure such as hosts, platforms, servers, server capabilities and services.
* **Files Integrator OMIS**: Extract metadata about files stored in a file system or file manager.
* **Topic Integrator OMIS**: Exchange metadata with third party event-based brokers.
* **Security Integrator OMIS**: Distribute security properties to security enforcement points.
* **API Integrator OMIS**: Exchange metadata with third party API Gateways.
* **Lineage Integrator OMIS**: Manage capture of lineage from a third party tool.
* **Database Integrator OMIS**: Extract metadata such as schema, tables and columns from database managers.
* **Catalog Integrator OMIS**: Exchange metadata with third party data catalogs.
* **Display Integrator OMIS**: Exchange metadata with applications that display data to users.
* **Analytics Integrator OMIS**: Exchange metadata with third party analytics tools.
* **Organization Integrator OMIS**: Load information about the teams and people in an organization and return collaboration activity.
* **Glossary Manager OMVS**: Create glossary terms and organize them into categories as part of a controlled workflow process. It supports the editing glossary and multiple states.
* **My Profile OMVS**: Manage information about the logged on user as well as their preferences.
* **Glossary Browser OMVS**: View glossary terms and categories within a glossary.
## Platform servers
### Server: test-metadata-store
* **Type**: Metadata Access Store
* **Description**: Metadata Access Store called test-metadata-store running on platform https://localhost:9443
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
* **Location**: https://localhost:9443/servers/test-metadata-store
#### Runtime Status
* **Last Start Time**: Wed Sep 13 19:28:42 BST 2023
* **Server Active Status**: Running
#### Services
##### Service: Asset Manager OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]
##### Service: Open Governance Framework Services
* **Service Status**: Starting
##### Service: Open Metadata Repository Services (OMRS)
* **Service Status**: Running
##### Service: Connected Asset Services
* **Service Status**: Starting
##### Service: Community Profile OMAS
* **Service Status**: Running
###### Service Options
* **KarmaPointPlateau**: 10
* **SupportedZones**: [data-lake, personal-files]
* **DefaultZones**: [personal-files]
##### Service: Data Manager OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]
##### Service: Digital Architecture OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]
##### Service: Asset Consumer OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [data-lake, personal-files]
* **DefaultZones**: [personal-files]
##### Service: Governance Program OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]
##### Service: IT Infrastructure OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]
##### Service: Open Integration Service
* **Service Status**: Starting
##### Service: Asset Owner OMAS
* **Service Status**: Running
###### Service Options
* **SupportedZones**: [quarantine, trash-can, data-lake]
* **PublishZones**: [data-lake, personal-files]
* **DefaultZones**: [quarantine]

--8<-- "snippets/abbr.md"