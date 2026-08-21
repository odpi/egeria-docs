<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Software Server Capability

A *software server capability* is a [software capability](/concepts/software-capability) that is implemented in a [software server](/types/0/0040-Software-Servers).

The distinction matters when cataloguing IT infrastructure.  A software capability may be supported by any kind of [IT infrastructure](/types/0/0030-Operating-Platforms) - a host, a software server platform or a software server.  A *software server capability* narrows this to the capabilities that a running server offers, which is where most of the capabilities that manage data and metadata are found.

Open metadata defines a large number of specializations, including:

* **Data managers** - a *DataManager* manages collections of data; a *DatabaseManager* (a DBMS) manages data organized as relational schemas; a *FileSystem* and a *FileManager* manage files and folders.
* **Application and API capabilities** - an *Application* supports a specific business function; an *APIManager* or *RESTAPIManager* manages callable APIs; a *SoftwareService* provides externally callable functions to other services.
* **Engines** - an *Engine* runs automated processes, with specializations for workflow, reporting, analytics, data movement and data virtualization.  A [governance engine](/concepts/governance-engine) is the specialization Egeria uses to group its own [governance services](/concepts/governance-service).
* **Event handling** - an *EventBroker* routes events to subscribers around topics; an *EventManager* supports event-based services; a *NotificationManager* distributes events from a topic to its subscriber list.
* **Catalogs and libraries** - an *InventoryCatalog* manages descriptions of people, places, digital assets and things; a *MasterDataManager* reconciles master data entities from many sources; a *SoftwareLibrary* stores software modules; a *ContentCollectionManager* manages controlled documents.
* **Egeria's own capabilities** - a *CohortMember* is the capability that enables a server to join an [open metadata repository cohort](/concepts/cohort-member).

A software server capability is linked to the infrastructure that hosts it using the *SupportedSoftwareCapability* relationship, and to the [assets](/concepts/asset) it manages using the *ServerAssetUse* relationship.  Where the capability is the true master of the metadata it manages, its identifier is used to [document the provenance](/features/metadata-provenance/overview) of that metadata.

???+ info "Additional information"
    * The *SoftwareCapability* type and the full list of its subtypes are described in [Model 0042 Software Capabilities](/types/0/0042-Software-Capabilities).
    * [Software capability](/concepts/software-capability) describes the broader concept, including the capabilities that act as masters of metadata.

--8<-- "snippets/abbr.md"
