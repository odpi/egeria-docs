<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Modelling IT Infrastructure

The IT Infrastructure types are used for capturing metadata from deployment artifacts, or to generate deployment artifacts from open metadata. The other major use of IT Infrastructure modelling is to [manually catalog the key pieces of IT Infrastructure used by an organization](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview). The creation of this metadata may be used to kick off the automated cataloging of the capabilities and assets associated with the infrastructure.


![Infrastructure Stack](infrastructure-stack.svg)


## Basic Concepts

At the base is the notion of a **Host**.  This could be:

- *BareMetalComputer* - traditional computer hardware or
- *VirtualMachine* - a virtualized machine (such as VMWare or VirtualBox) that uses a hypervisor to virtualize machine hardware or
- *VirtualContainer* - a software system using a container library to virtualize the operating system it uses or
- *HostCluster* - a cluster of Hosts that are operating as a single operational environment (such as a Hadoop cluster or kubernetes cluster).

Hosts are composable and reusable.  For example, figure 1 shows a Virtual Container that is deployed to two Bare Metal Computers.  The relationship between them is called *DeployedOn*.

![Figure 1](virtual-container-host.svg)
> **Figure 1:** A virtual container deployed to two bare metal computers

Figure 2 shows an example of Host Cluster, such as a Hadoop Cluster, that manages multiple Hosts (Bare Metal Computers in this example).  The relationship between the Host Cluster and each subordinate Host is *HostClusterMember*.  The host cluster may not have all of its members active.  The membership denotes the pool of resources that the cluster has to work with.

![Figure 2](hadoop-host-cluster.svg)
> **Figure 2:** A cluster of bare metal computers operating as single host

### Storage

A host may have its own storage - or it may be shared.  One or more hosts can be linked to a *StorageVolume* via the *AttachedStorage* relationship.

![Storage](storage.svg)
> **Figure 3:** Showing how storage is allocated to the hosts


A host typically runs an operating system and may have various hardware characteristics of interest (such as byte ordering). Collectively this information is called the *OperatingPlatform*. 

The Operating Platform can be linked to many hosts through the *OperatingPlatformUse* relationship.  This is shown in figure 4. It documents that these hosts are running the software identified by the operating platform. This is particularly useful if you are using standard software stack builds that are deployed to multiple hosts since it is easy to see which hosts are at which levels of the software and to manage the rollout of upgrades to the stack.

![Figure 4](operating-platform-deployment.svg)
> **Figure 4:** A collection of hosts using the same operating platform

The *SoftwarePackageManifest* shown in figure 5 details the software stack for the operating platform.  It is represented as a *Collection* linked to the operating platform using the *OperatingPlatformManifest* relationship.

![Figure 5](operating-platform-definition.svg)
> **Figure 5:** The software stack definition for an operating platform

Linked to a host via the *DeployedOn* relationship are the *SoftwareServerPlatform*s.  They describe the operating system processes running on the Host that use software described in the Operating Platform. This is shown in figure 6.

![Figure 6](software-server-platform.svg)
> **Figure 6:** The software server platforms running on the host

The functions of the software server platform are described using *SoftwareCapabilities*.  They typically host/manage assets such as *DataSets*, *DataStores* and *Processes* that are linked to the software capability using the **CapabilityAssetUse** relationship.

Some technologies are written as a single stack.
Figure 7 shows the structure of the metadata elements
for a technology - such as Apache Kafka or a Database Server - that is a single stack.

![Figure 7](single-stack-platform.svg)
> **Figure 7:** The metadata elements to represent a single stack technology

Figure 8 shows the representation of the stack
of a platform that allows multiple virtual servers to be configured.
The servers are represented by *SoftwareServers*.  Software capabilities can be attached to the software servers as well as the software server platforms.

![Figure 8](configurable-software-server-platform.svg)
> **Figure 8:** The metadata elements to represent a configurable software server platform

Egeria's [OMAG Server Platform](/concepts/omag-server-platform) is an example of this type of technology. This is illustrated in figure 9.  The software servers are [OMAG Servers](/concepts/omag-server) and the registered services are software capabilities of type *SoftwareService*.  The kind of OMAG Server - for example *Metadata Access Store*, *Integration Daemon*, *Engine Host* or *View Server* - is recorded in the *deployedImplementationType* property of the *SoftwareServer* element.

![Figure 9](omag-server-platform-stack.svg)
> **Figure 9:** The OMAG server platform

The assets managed by the OMAG server's software server capabilities are *DeployedConnectors*.  The APIs are linked to the OMAG Server Platform.  Specific API operations can be linked to the software services using the *ProcessCall* relationship.

### IT Infrastructure Assets

Hosts, software server platforms and software servers are all types of *ITInfrastructure* assets.  The *OperatingPlatformUse* relationship does in fact link the operating platform with any type of IT infrastructure assets.  This means that software used by specific parts of the IT landscape can nailed down.

The *DeployedOn* relationship is between an IT infrastructure asset and an asset that represented its real world counterpart's deployment destination.  This means that the deployment "stack" can be represented with as many levels as needed to describe the environment.  At the base of the stack, it is possible to link an asset of type *Infrastructure* (rather than *ITInfrastructure*) to show the physical deployment of the software.

### Server purposes

The role that a software server is performing is captured in the *deployedImplementationType* property of its *SoftwareServer* element, using one of the [deployed implementation types](/concepts/deployed-implementation-type) defined in Egeria's reference data.  General purpose values include:

* *Database Server* - hosting a database management system (DBMS).
* *Integration Server* - hosting data movement processes, with *Apache Airflow Server* as a more specific value.
* *Metadata Server* - manages and stores a collection of metadata, with *Marquez Server* and *Apache Superset* as more specific values.

Egeria's own server types use the values *OMAG Server*, *Metadata Access Server*, *Metadata Access Store*, *Integration Daemon*, *Engine Host* and *View Server*, and the platform that hosts them is an *OMAG Server Platform*.  Integration connectors for other technologies define their own values - for example *PostgreSQL Server*.

### Software Capabilities

There are many types of software capability.  The list below shows the subtypes of *SoftwareCapability* defined in the open metadata types.

* *APIManager* - A capability that manages callable APIs.
    * *RESTAPIManager* - A capability that supports REST APIs in a server.
* *Application* - A server capability supporting a specific business function.
* *AuthorizationManager* - A capability that supports the authorization of requests.
* *CohortMember* - A capability enabling a server to access an open metadata repository cohort.
* *DataManager* - A capability that manages collections of stored data.
    * *DatabaseManager* - A capability that manages data organized as relational schemas.
    * *DataAccessManager* - A capability that manages data organized as structured schemas by linking them to the data stores that hold the data.
* *Engine* - A programmable engine for running automated processes.
    * *WorkflowEngine* - An engine capable of running a mixture of human and automated tasks as part of a workflow process.
    * *ReportingEngine* - An engine capable of creating reports by combining information from multiple data sets.
    * *AnalyticsEngine* - An engine capable of running analytics models using data from one or more data sets.
    * *DataMovementEngine* - An engine capable of copying data from one data store to another.
    * *DataVirtualizationEngine* - An engine capable of creating new data sets by dynamically combining data from one or more data stores or data sets.
    * *GovernanceEngine* - A collection of related governance services of the same type.
        * *GovernanceActionEngine* - A collection of related governance services supporting the Open Governance Framework (OGF).
        * *SurveyActionEngine* - A collection of related governance services supporting the Open Survey Framework (OSF).
        * *WatchdogActionEngine* - A collection of related governance services supporting the Open Watchdog Framework (OWF).
        * *ExplorerActionEngine* - A governance engine supported by tools such as the Resource Explorer.
        * *RepositoryGovernanceEngine* - A governance engine for open metadata repositories.
* *EventBroker* - A capability that supports event-based services, typically around topics.
* *EventManager* - A capability that sends and/or receives events as part of its software function.
* *IntegrationGroup* - A collection of integration connectors to run together.
* *InventoryCatalog* - A capability that manages collections of descriptions about people, places, digital assets, things, ...
* *NetworkGateway* - A connection point enabling network traffic to pass between two networks.
* *ResourceManager* - A manager of resources.
    * *FileSystem* - A store of files organized into a hierarchy of file folders.
    * *FileManager* - A manager of a collection of files and folders.
    * *ContentCollectionManager* - A manager of controlled documents and related media.
    * *ChangeManagementLibrary* - A managed collection of requirements, defects and proposed changes to a project.
    * *SoftwareLibrary* - A collection of software modules.
    * *SourceControlLibrary* - A software source code library that provides version control.
    * *MasterDataManager* - A system that manages the consolidation and reconciliation of master data.
    * *NotificationManager* - A capability that distributes events from a topic to its subscriber list.
    * *UserAccessDirectory* - A system that stores the access rights and groups for users.
    * *UserProfileManager* - A system that stores descriptions of individuals and their roles/interests in an organization.
* *SoftwareService* - A capability that provides externally callable functions to other services.
* *UserAuthenticationManager* - A capability that supports the identification/authentication of users.

### Types of endpoints

An *Endpoint* describes the address (URL, port etc) of a component that can be called across the network.  With so much infrastructure running as software today, it is common to see endpoints linked at all levels of the IT infrastructure metadata.

Figure 10 shows some examples.  The relationships used to link the endpoint indicate how it is used.

* *ConnectToEndpoint* links a connection to an endpoint.  The connection provides the information used to connect to the [resource](/concepts/resource) described by an asset.

* *ServerEndpoint* indicates that the real-world counterpart of an IT infrastructure asset is called for requests at this address. The REST API paths are examples of server endpoints. So is Egeria's [platform URL root](/concepts/platform-url-root).

* *VisibleEndpoint* indicates that the endpoint address is visible through the linked *Network*.  It is used in threat modelling.

![Figure 10](types-of-endpoints.svg)
> **Figure 10:** Types of endpoints


### Technology Examples

Using the basic concepts described above, here are some examples of metadata for different types of technologies.

Figure 11 shows the example of the software stack for Apache Kafka.

![Figure 11](kafka-software-stack.svg)
> **Figure 11:** The metadata elements to represent an Apache Kafka Server


Figure 12 shows the example of the software stack for a database.

![Figure 12](database-software-stack.svg)
> **Figure 12:** The metadata elements to represent a database


### Attachments and Classifications

In addition, the IT Infrastructure assets can be linked to governance metadata as follows:

* Locations - the IT Infrastructure assets can be linked to the locations defined in the [Location Arena](/services/omvs/location-arena/overview).
* Zones - the IT Infrastructure assets can be published and withdrawn to control their visibility while they are being maintained
* Ownership and origin - the *Ownership* and *DigitalResourceOrigin* classifications can be applied.
* External References - links to external online documentation can be added.
* Non-personal accounts (NPAs) - *ITProfiles* and *UserIdentities* can be set up to describe system users and assigned to the IT Infrastructure assets that are using them.

## Infrastructure managers (external sources)

When capturing metadata from deployment artifacts that are managed wholly by a specific technology or automated process, the metadata should be stored in a [metadata collection](/concepts/metadata-collection) that represents that technology.  For an [integration connector](/concepts/integration-connector), this is set with the *metadataCollectionQualifiedName* property of its *RegisteredIntegrationConnector* or *CatalogTarget* relationship, and the context then supplies the external source GUID and name on every request through the `MetadataSourceOptions` (`externalSourceGUID` and `externalSourceName`).  This marks the metadata elements as managed by an external source, which makes the metadata read-only to all but the process responsible for cataloguing the artifact.

Where Egeria is the primary catalog of the infrastructure metadata, or the deployment artifacts that the metadata is derived from are either manually created or maintained by multiple processes, the external source is left blank so the resulting metadata elements are editable by any authorized caller.

See [Metadata Provenance](/features/metadata-provenance/overview)
for more information about the use of external source identifiers.


--8<-- "snippets/abbr.md"
