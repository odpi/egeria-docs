<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0042 Software Capabilities

![UML](0042-Software-Capabilities.svg)

## SoftwareCapability

[*IT Infrastructure*](/types/0/0030-Hosts-and-Platforms) contains many capabilities.  Each capability can be catalogued using the *SoftwareCapability* entity and linked to the hosting *ITInfrastructure* entity using the *SupportedSoftwareCapability* relationship. 

Different organizations and tools can choose the granularity in which the capabilities are catalogued in order to provide [appropriate context](/0/0045-Servers-and-Assets) to [assets](/types/0/0010-Base-Model) that are managed by the capabilities and the decisions made around them.

These are the subtypes of software capabilities defined in the open metadata types:

- *SoftwareServerCapability* - A capability that typically resides in a [*SoftwareServer*](/types/0/0040-Software-Servers).
- [*AccessControlManager*](/types/0/0050-Applications-and-Processes/#accesscontrolmanager) - A capability that manages access to specific resources.
- [*APIManager*](/types/0/0050-Applications-and-Processes/#apimanager) - A capability that manages callable APIs that typically delegate onto Software Services.
- [*Application*](/types/0/0050-Applications-and-Processes/#application) - A capability supporting a specific business function.
- [*Catalog*](/types/0/0050-Applications-and-Processes/#catalog) - A capability that manages collections of descriptions about people, places, digital assets, things, ...
- [*DataManager*](/types/0/0050-Applications-and-Processes/#datamanager) - A capability that manages collections of data.
    - [*DatabaseManager*](/types/0/0050-Applications-and-Processes/#databasemanager) - A capability that manages data organized as relational schemas.  Also known as a Database Management System (DBMS).
- [*Engine*](/types/0/0055-Data-Processing-Engines/#engine) - A programmable engine for running automated processes.
    - [*WorkflowEngine*](/types/0/0055-Data-Processing-Engines/#workflowengine) - An engine capable of running a mixture of human and automated tasks as part of a workflow process.
    - [*ReportingEngine*](/types/0/0055-Data-Processing-Engines/#reportingengine) - An engine capable of creating reports by combining information from multiple data sets.
    - [*AnalyticsEngine*](/types/0/0055-Data-Processing-Engines/#analyticsengine) - An engine capable of running analytics models using data from one or more data sets.
    - [*DataMovementEngine*](/types/0/0055-Data-Processing-Engines/#datamovementengine) - An engine capable of copying data from one data store to another.
    - [*DataVirtualizationEngine*](/types/0/0055-Data-Processing-Engines/#datavirtualizationengine) - An engine capable of creating new data sets by dynamically combining data from one or more data stores or data sets.
- [*EventBroker*](/types/0/0050-Applications-and-Processes/#eventbroker) - A capability that supports event-based services, typically around topics.
- [*SoftwareService*](/types/0/0057-Software-Services/#softwareservice) - A capability that provides externally callable functions to other services.
    - [*ApplicationService*](/types/0/0057-Software-Services/#applicationservice) - A software service that supports a reusable business function.
    - [*MetadataIntegrationService*](/types/0/0057-Software-Services/#metadataintegrationservice) - A software service that exchanges metadata between servers.
    - [*MetadataAccessService*](/types/0/0057-Software-Services/#metadataaccessservice) - A software service that provides access to stored metadata.
    - [*EngineHostingService*](/types/0/0057-Software-Services/#enginehostingservice) - A software service that provides services that delegate to a hosted engine.
    - [*UserViewService*](/types/0/0057-Software-Services/#userviewservice) - A software service that provides user interfaces access to digital resources.
- [*NetworkGateway*](/types/0/0070-Networks-and-Gateways/#networkgateway) - A connection point enabling network traffic to pass between two networks.
- [*EnterpriseAccessLayer*](/types/0/0057-Software-Services/#enterpriseaccesslayer) - Repository services for the Open Metadata Access Services (OMAS) supporting federated queries and aggregated events from the connected cohorts.
- [*CohortMember*](/types/0/0057-Software-Services/#cohortmember) - A capability enabling a server to access an open metadata repository cohort.
- [*GovernanceEngine*](/types/4/0461-Governance-Engines/#governanceengine) - A collection of related governance services of the same type.
    - [*GovernanceActionEngine*](/types/4/0461-Governance-Engines/#governanceactionengine) - A collection of related governance services supporting the Governance Action Framework (GAF).
    - [*OpenDiscoveryEngine*](/types/6/0601-Open-Discovery-Engine/#opendiscoveryengine) - A collection of related governance services supporting the Open Discovery Framework (ODF).
   - [*ArchiveEngine*](/types/4/0461-Governance-Engines/#archiveengine) - A collection of related governance services supporting maintenance of [Open Metadata Archives](/concepts/open-metadata-archive).

In addition, it is possible to augment software capabilities with the following classifications:

- [*CloudService*](/types/0/0090-Cloud-Platforms-and-Services/#cloudservice) - A capability enabled for a tenant on a cloud platform.
- [*ContentCollectionManager*](/types/0/0056-Resource-Managers/#contentcollectionmanager) - A manager of controlled documents and related media.
- [*FileSystem*](/types/0/0056-Resource-Managers/#filesystem) - A capability that supports a store of files organized into a hierarchy of file folders for general use.
- [*FileManager*](/types/0/0056-Resource-Managers/#filemanager) - A manager of a collection of files and folders.
- [*NotificationManager*](/types/0/0056-Resource-Managers/#notificationmanager) - A software capability that is distributing events from a topic to its subscriber list.

## SupportedSoftwareCapability

Defines the relationship between a *SoftwareCapability* and the *ITInfrastructure* asset that hosts it.

## ProcessingState

Defines a classification for a *SoftwareCapability*. The *ProcessingState* can be used to describe additional runtime processing information used by various SoftwareCapabilities.


??? deprecated "Deprecated types"
    - *SoftwareServerSupportedCapability* is deprecated in favor of *SupportedSoftwareCapability*.
    
--8<-- "snippets/abbr.md"
