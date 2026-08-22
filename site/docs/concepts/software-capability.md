<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Software Capabilities

Many software servers are connected to the open metadata ecosystem, each with wildly differing
capabilities.

A software capability documents a specific function that an IT infrastructure asset, such as a host, software server platform and software server, is able to perform.
The open metadata type for a software capability is [`SoftwareCapability`](/types/0/0042-Software-Capabilities).

## Metadata managing software capabilities

Some software capabilities create and manage metadata - in fact they are the true master of this
metadata. for example, a database manager (aka database management system or DBMS) is the true
master of metadata about database schemas.

When metadata managed by such software capabilities is shared with an
[open metadata repository cohort](/concepts/cohort-member),
the members of the cohort need to take note that they should not update this metadata.

The software capabilities that are recognized as managing metadata are:

* [Asset manager](#asset-manager)
* [Master data manager](#master-data-manager)
* [Engine](#engine)
* [Tool](#tool)

The identifiers of these software capabilities are used to 
[document the provenance](/features/metadata-provenance/overview)
of any metadata that comes from these technologies.
Metadata instances that are mastered by specific software capabilities are referred to
as **external instances**.

## Asset Manager

An **asset manager**
is typically a service that provides a catalog of [assets](/concepts/asset).  It is responsible
for maintaining details of the assets including their characteristics,
ownership, assessments and governance requirements.

Often an asset manager is specialized for particular types of assets.
For example, you may see a **data catalog** cataloging information about data sets and data stores
for a data lake.
A Configuration Management Database (CMDB) is an asset manager of infrastructure assets.

### Open metadata support for asset managers

An asset manager may integrate with the open metadata ecosystem using one of three methods:

 * as a
[cohort member](/concepts/cohort-member)
through the
[Open Metadata Repository Services (OMRS) connectors](/concepts/repository-connector)
or 

* through an [integration connector](/concepts/integration-connector) or

* Through direct calls to the [Asset Maker](/services/omvs/asset-maker/overview) API.

The [Metadata Server Exchange](/patterns/information-exchange/overview)
pattern provides more information on these options.

## Master data manager

A master data manager is a capability in a software server to manage an authoritative
collection of master data, typically about people, organizations, products and accounts.

Master data managers that hold information about the people and organizations using open metadata
integrate their data through the [People Organizer](/services/omvs/people-organizer/overview) API.

## Engine

An engine is a software capability that is programmable to automate specific
processes.  Typically these processes manipulate and store data.

Below are examples of engines:

* Workflow engine - for automating processes that coordinate the activity of people and systems.
* Data movement engine - for automating the movement of data from one store to another.
* Data virtualization engine - for automating the federation and transformation
of data in response to a real-time query.
* Reporting engine - for extracting data and formatting into specific reports.
* Analytics engine - for executing analytical processes.

The metadata used by an engine relates to the processing it is performing and the
data sources it is working with.

Most engines have associated tools to create the process definitions and manage the metadata,
leaving the engines themselves to run the automated processes and create lineage metadata.

# Tool

A tool is a user program used to create definitions that automate processes.
Typically the output of a tool runs on an [engine](#engine).

Tools are the master of metadata about the processes being automated and the
data they are manipulating.

Examples of tools include:

* Analytics tool - for creating analytics - for example, a python notebook.
* Process automation tools - for creating workflows for workflow engines.

## Open Metadata Types for software capabilities

Open metadata defines a large number of specializations, including:

* **Data managers** - a *DataManager* manages collections of data; a *DatabaseManager* (a DBMS) manages data organized as relational schemas; a *FileSystem* and a *FileManager* manage files and folders.
* **Application and API capabilities** - an *Application* supports a specific business function; an *APIManager* or *RESTAPIManager* manages callable APIs; a *SoftwareService* provides externally callable functions to other services.
* **Engines** - an *Engine* runs automated processes, with specializations for workflow, reporting, analytics, data movement and data virtualization.  A [governance engine](/concepts/governance-engine) is the specialization Egeria uses to group its own [governance services](/concepts/governance-service).
* **Event handling** - an *EventBroker* routes events to subscribers around topics; an *EventManager* supports event-based services; a *NotificationManager* distributes events from a topic to its subscriber list.
* **Catalogs and libraries** - an *InventoryCatalog* manages descriptions of people, places, digital assets and things; a *MasterDataManager* reconciles master data entities from many sources; a *SoftwareLibrary* stores software modules; a *ContentCollectionManager* manages controlled documents.
* **Egeria's own capabilities** - a *CohortMember* is the capability that enables a server to join an [open metadata repository cohort](/concepts/cohort-member).

A software capability is linked to the infrastructure that hosts it using the *SupportedSoftwareCapability* relationship, and to the [assets](/concepts/asset) it manages using the *CapabilityAssetUse* relationship.  Where the capability is the true master of the metadata it manages, its identifier is used to [document the provenance](/features/metadata-provenance/overview) of that metadata.

???+ info "Additional information"
    * The *SoftwareCapability* type and the full list of its subtypes are described in [Model 0042 Software Capabilities](/types/0/0042-Software-Capabilities).

## Historical Note

Earlier versions of Egeria included a specialization of software capability called *SoftwareServerCapability* that was used to describe the capabilities found in software servers specifically.
The thinking was that this was where the capabilities that managed data and metadata are found.  Unfortunately, the real infrastructure landscape is not so neat and tidy so the distinction was dropped.




--8<-- "snippets/abbr.md"
