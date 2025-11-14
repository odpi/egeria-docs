<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0042 Software Capabilities

Software capabilities are the capabilities implemented in software and supported by [ITInfrastructure](/types/0/0030-Hosts-and-Platforms) such as hosts, software server platforms and software servers.  They are composed of, support and/or consume various [digital resources](/concepts/resources) represented as [Asset entities](/types/0/0010-Base-Model).  They are linked together using the [ServerAssetUse relationship](/types/0045-Servers-and-Assets). 

![UML](0042-Software-Capabilities.svg)

## SoftwareCapability entity

[*IT Infrastructure*](/types/0/0030-Hosts-and-Platforms) contains many capabilities.  Each capability can be catalogued using the *SoftwareCapability* entity and linked to the hosting *ITInfrastructure* entity using the *SupportedSoftwareCapability* relationship.

*SoftwareCapability* is a [*Referenceable*](/types/0/0010-Base-Model) that adds the following attributes:

* *patchLevel* - any patches applied to the version.
* *source* - supplier of the capability.
* *deployedImplementationType* - the class of technology that is used in its implementation. Values for the *deployedImplementationType* attribute can be managed for consistency in a [*deployed implementation type*](/concepts/deployed-implementation-type) valid value set.

Different organizations and tools can choose the granularity in which the capabilities are catalogued in order to provide [appropriate context](/0/0045-Servers-and-Assets) to [assets](/types/0/0010-Base-Model) that are managed by the capabilities and the decisions made around them.

## SoftwareServerCapability entity

The *SoftwareServerCapability* describes a capability that is implemented in a [software server](/types/0/0040-Software-Server).  

These are the subtypes of software server capabilities defined in the open metadata types:

- [*AuthorizationManager*](/types/0/0050-Applications-and-Processes) - A capability that manages access to specific resources.
- [*APIManager*](/types/0/0050-Applications-and-Processes) - A capability that manages callable APIs that typically delegate onto Software Services.
    - [*RESTAPIManager*](/types/0/0050-Applications-and-Processes) - A capability that manages callable REST APIs that typically delegate onto Software Services.
- [*Application*](/types/0/0050-Applications-and-Processes) - A capability supporting a specific business function.
- [*ChangeManagementLibrary*](/types/0/0056-Resource-Managers) - A software capability that is capturing reports that describe planned and unplanned changes to the IT systems, and managing them through their lifecycle.
- [*CohortMember*](/types/0/0057-Software-Services) - A capability enabling a server to access an open metadata repository cohort.
- [*ContentCollectionManager*](/types/0/0056-Resource-Managers) - A manager of controlled documents and related media.
- [*DataManager*](/types/0/0050-Applications-and-Processes) - A capability that manages collections of data.
    - [*DatabaseManager*](/types/0/0050-Applications-and-Processes) - A capability that manages data organized as relational schemas.  Also known as a Database Management System (DBMS).
    - [*DatabaseAccessManager*](/types/0/0050-Applications-and-Processes) - A capability that manages data organized as relational schemas.  Also known as a Database Management System (DBMS).
- [*Engine*](/types/0/0055-Data-Processing-Engines/) - A programmable engine for running automated processes.
    - [*WorkflowEngine*](/types/0/0055-Data-Processing-Engines) - An engine capable of running a mixture of human and automated tasks as part of a workflow process.
    - [*ReportingEngine*](/types/0/0055-Data-Processing-Engines) - An engine capable of creating reports by combining information from multiple data sets.
    - [*AnalyticsEngine*](/types/0/0055-Data-Processing-Engines) - An engine capable of running analytics models using data from one or more data sets.
    - [*DataMovementEngine*](/types/0/0055-Data-Processing-Engines) - An engine capable of copying data from one data store to another.
    - [*DataVirtualizationEngine*](/types/0/0055-Data-Processing-Engines) - An engine capable of creating new data sets by dynamically combining data from one or more data stores or data sets.
- [*EventBroker*](/types/0/0050-Applications-and-Processes) - A capability that supports routing of events to subscribers, typically around topics.
- [*EventManager*](/types/0/0050-Applications-and-Processes) - A capability that supports event-based services, based on incoming events.
- [*InventoryCatalog*](/types/0/0050-Applications-and-Processes) - A capability that manages collections of descriptions about people, places, digital assets, things, ...
- [*FileSystem*](/types/0/0056-Resource-Managers) - A capability that supports a store of files organized into a hierarchy of file folders for general use.
- [*FileManager*](/types/0/0056-Resource-Managers) - A manager of a collection of files and folders.
- [*GovernanceEngine*](/types/4/0461-Governance-Engines) - A collection of related governance services of the same type.
    - [*GovernanceActionEngine*](/types/4/0461-Governance-Engines) - A collection of related governance services supporting the [Open Governance Framework (OGF)](/frameworks/ogf/overview).
    - [*SurveyActionEngine*](/types/4/0461-Governance-Engines) - A collection of related governance services supporting the [Open Survey Framework (OSF)](/frameworks/osf/overview).
    - [*WatchdogActionEngine*](/types/4/0461-Governance-Engines) - A collection of related governance services supporting the [Open Watchdog Framework (OWF)](/frameworks/owf/overview).
    - [*RepositoryGovernanceEngine*](/types/4/0461-Governance-Engines) - A collection of related governance services supporting maintenance of [Open Metadata Archives](/concepts/open-metadata-archive).
- [*NetworkGateway*](/types/0/0070-Networks-and-Gateways) - A connection point enabling network traffic to pass between two networks.
- [*NotificationManager*](/types/0/0056-Resource-Managers) - A software capability that is distributing events from a topic to its subscriber list.
- [*MasterDataManager*](/types/0/0056-Resource-Managers) - A software capability that is managing the capture and reconciliation of master data entities from many sources.
- [*SoftwareLibrary*](/types/0/0056-Resource-Managers) - A software capability that is storing software modules for use in IT systems.
- [*SoftwareService*](/types/0/0057-Software-Services) - A capability that provides externally callable functions to other services.
- [*SourceControlLibrary*](/types/0/0056-Resource-Managers) - A software capability that is managing versions of source code files.
- [*UserAccessManager*](/types/0/0056-Resource-Managers) - A software capability that is controlling which resources can be accessed by a specific user.
- [*UserAuthenticationManager*](/types/0/0050-Applications-and-Processes) - A collection of related governance services supporting maintenance of [Open Metadata Archives](/concepts/open-metadata-archive).
- [*UserProfileManager*](/types/0/0056-Resource-Managers) - A software capability that is managing user profiles.

In addition, it is possible to augment software capabilities with the following classification:

- [*CloudService*](/types/0/0090-Cloud-Platforms-and-Services) - A capability enabled for a tenant on a cloud platform.

## SupportedSoftwareCapability relationship

Defines the relationship between a *SoftwareCapability* and the *ITInfrastructure* entity that hosts it.  This relationship, plus the attached *SoftwareCapability* entity, help to build out a picture of the capabilities of a particular deployed host, software server platform or software server.  Together they help to describe where and how various IT capabilities are delivered to the owning organization.  This model can form the basis of traceability from business function to IT Infrastructure, particularly when combined with [location information](/types/0/0025-Locations) and [links to the data assets and APIs](/types/0/0045-Servers-and-Assets). 

## ProcessingState classification

Defines a classification for a *SoftwareCapability*. The *ProcessingState* can be used to describe additional runtime processing information used by the component represented by the *SoftwareCapability* entity.

??? deprecated "Deprecated types"
    - *SoftwareServerSupportedCapability* is deprecated in favour of the *SupportedSoftwareCapability* relationship.
    
--8<-- "snippets/abbr.md"
