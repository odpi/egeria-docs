<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connector catalog

Egeria has a growing collection of *connectors* to third party technologies. These connectors help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

A connector is a client to a third party technology. It supports a standard API that Egeria calls, and it then translates these calls into requests to the third party technology. Some connectors are also able to listen for notifications from the third party technology. When a notification is received, the connector converts its content into a call to Egeria to distribute the information to the open metadata ecosystem.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the [OMAG servers](/concepts/omag-server). The Connector Catalog list the connector implementations supplied by the Egeria community. There are three broad categories of connectors and the connector catalog is organized accordingly:

* Connectors that support the [exchange and maintenance of metadata](#metadata-exchange-and-maintenance-connectors). This includes the integration connectors, repository connectors, discovery services and governance action services.

* Connectors that support [Egeria’s runtime](#runtime-connectors). This includes the event bus connectors, cohort registry stores, configuration stores, audit log destination connectors, open metadata archive stores, REST client connectors and the cohort member remote repository connectors

* Connectors that provide access to [digital resources and their metadata](#digital-resource-connectors) that is stored in the open metadata ecosystem.

## Metadata exchange and maintenance connectors

The connectors that support the exchange and maintenance of metadata help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

| Type of Connector                                                                 | Description                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Integration connectors](#integration-connectors)                                 | manage the metadata exchange to a third party technology through an [integration service](/services/omis).                                                                                                                                                                                                 |
| [Repository and Event Mapper connectors](#repository-and-event-mapper-connectors) | integrate metadata repositories into the open metadata ecosystem so that they can interact with one or more [open metadata repository cohorts](/services/omrs/cohort).                                                                                                                                     |
| [Open Discovery Services](#open-discovery-services)                               | analyze the content of [resources](/concepts/resource) in the digital landscape and create annotations that are attached to the resource's [asset](/concepts/asset) metadata element in the open metadata repositories in the form of an [discovery analysis report](/concepts/discovery-analysis-report). |
| [Governance Action Services](#governance-action-services)                         | perform monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities as required.                                                                                                                                                                    |
| [Governance Daemon Connectors](#governance-daemon-connectors)                     | contain specialist connectors for the governance servers that make active use of open metadata.                                                                                                                                                                                                            |

### Integration Connectors

---8<-- "docs/connectors/integration/integration-connector-intro.md"

#### Cataloguing Files

The *files* integration connectors run in the [Files Integrator Open Metadata Integration Service (OMIS)](/services/omis/files-integrator/overview) hosted in the [integration daemon](/concepts/integration-daemon).

| Files Integration Connectors | Description |
|---|---|
| [Data files monitor](/connectors/integration/data-files-monitor-integration-connector) | maintains a `DataFile` asset for each file in the directory (or any subdirectory). When a new file is created, a new DataFile asset is created.  If a file is modified, the lastModified property of the corresponding DataFile asset is updated.  When a file is deleted, its corresponding DataFile asset is also deleted (or archived if it is still needed for lineage). |
| [Data folder monitor](/connectors/integration/data-folder-monitor-integration-connector) | maintains a `DataFolder` asset for the directory.  The files and directories underneath it are assumed to be elements/records in the DataFolder asset and so each time there is a change to the files and directories under the monitored directory, it results in an update to the lastModified property of the corresponding DataFolder asset. |

#### Cataloguing Databases and their Schemas

The *database* integration connectors run in the [Database Integrator Open Metadata Integration Service (OMIS)](/services/omis/database-integrator/overview) hosted in the [integration daemon](/concepts/integration-daemon).

| Database Integration Connectors                                                                                                                        | Description                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PostgreSQL database connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/egeria-connector-postgres){ target=gh } | automatically maintains the open metadata instances for the databases hosted on a [PostgreSQL server :material-dock-window:](https://www.postgresql.org){ target=psql } This includes the database schemas, tables, columns, primary keys and foreign keys. |
| [JDBC integration connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/jdbc-integration-connector){ target=gh }   | automatically maintains the open metadata instances on a database server via JDBC. This includes the database schemas, tables, columns, primary keys and foreign keys.                                                                                      |

#### Cataloguing event topics and the structure of their events

The *topic* integration connectors run in the [Topic Integrator Open Metadata Integration Service (OMIS)](/services/omis/topic-integrator/overview) hosted in the [integration daemon](/concepts/integration-daemon).

| Topic Integration Connector | Description |
|---|---|
| [Kafka Monitor topic integration connector](/connectors/integration/kafka-monitor-integration-connector) | automatically maintains the open metadata instances for the topics hosted on an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka }.|
| [Kafka Audit topic integration connector](/connectors/integration/kafka-topics-audit-integration-connector) | Validates that topics that are active in an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka } are also catalogued in open metadata.  Creates an audit log record for each topic that is not catalogued. |

#### Cataloguing APIs

The *API* integration connectors run in the [API Integrator Open Metadata Integration Service (OMIS)](/services/omis/api-integrator/overview) hosted in the [integration daemon](/concepts/integration-daemon).

| API Integration Connectors | Description |
|---|---|
| [Open API Monitor integration connector](/connectors/integration/open-api-monitor-integration-connector) | automatically maintains the open metadata instances for the APIs extracted from the Open API Specification extracted from an application.|

#### Populating security enforcement engines

The security integration connectors run in the [Security Integrator Open Metadata Integration Service (OMIS)](/services/omis/security-integrator) hosted in the [integration daemon](/concepts/integration-daemon).

#### Capturing and publishing Lineage

The lineage integration connectors run in the [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) hosted in the [integration daemon](/concepts/integration-daemon).  They support [Lineage Management](/features/lineage-management/overview).


| Lineage Integration Connectors                                                                                                             | Description |
|--------------------------------------------------------------------------------------------------------------------------------------------|---|
| [Open Lineage Event Receiver integration connector](/connectors/integration/open-lineage-event-receiver-integration-connector)             | Connector to receive open lineage events from an event topic and publish them to lineage integration connectors with listeners registered in the same instance of the Lineage Integrator OMIS.|
| [Governance Action to Open Lineage integration connector](/connectors/integration/governance-action-open-lineage-integration-connector)    | Connector to listen for governance actions executing in the open metadata ecosystem, generate open lineage events for them and publish them to the integration connectors running in the same instance of Lineage Integrator OMIS that are listening for OpenLineage events. |
| [API-based Open Lineage Log Store integration connector](/connectors/integration/api-based-open-lineage-log-store-integration-connector)   | Connector that calls an OpenLineage compliant API to store the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS.|
| [File-based Open Lineage Log Store integration connector](/connectors/integration/file-based-open-lineage-log-store-integration-connector) | Connector that stores the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS. Each OpenLineage event is stored in its own file in JSON format.  These files are organized according to the namespace and job name in the event. |
| [Open Lineage Cataloguer integration connector](/connectors/integration/open-lineage-cataloguer-integration-connector)                     | Connector to register an OpenLineage listener with the Lineage Integrator OMIS and to catalog any processes that are not already known to the open metadata ecosystem. |
| [Sample Lineage integration connector](/connectors/integration/sample-lineage-event-receiver-integration-connector)                        | Connector to register an OpenLineage listener with the Lineage Integrator OMIS and to catalog any processes that are not already known to the open metadata ecosystem. |


??? education "Further information relating to integration connectors"
    
    - [Configuring an integration connector](/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services) to understand how to set up an integration connector.
    - [Writing an integration connector](/guides/developer/integration-connectors/overview) for more information on writing new integration connectors.


### Repository and Event Mapper Connectors

---8<-- "docs/connectors/repository/repository-connector-intro.md"

The table below lists the repository connectors supporting the native open metadata repositories.

| Native Repository Connector                                                         | Description |
|-------------------------------------------------------------------------------------|---|
| [JanusGraph OMRS Repository Connector](/connectors/repository/janus-graph/overview) | provides a native repository for a metadata server using [JanusGraph :material-dock-window:](https://janusgraph.org){ target=janus } as the backend. |
| [XTDB OMRS Repository Connector](/connectors/repository/xtdb)                       | provides a native repository for a metadata server that supports historical queries, using [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb } as the persistent store. |
| [In-memory OMRS Repository Connector](/connectors/repository/in-memory/overview)    | provides a simple native repository implementation that "stores" metadata in HashMaps within the JVM; it is used for testing, or for environments where metadata maintained in other repositories needs to be cached locally for performance/scalability reasons.  |
| [Read-only OMRS Repository Connector](/connectors/repository/read-only/overview)    | provides a native repository implementation that does not support the interfaces for create, update, delete; however, it does support the search interfaces and is able to cache metadata -- this means it can be loaded with open metadata archives to provide standard metadata definitions. |

The table below lists the repository connectors that act as an adapter for third party metadata repositories.

| Adapter Repository Connectors                                                                                                                                        | Description                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Apache Atlas OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=gh }                                   | implements read-only connectivity to the [Apache Atlas :material-dock-window:](https://atlas.apache.org){ target=atlas } metadata repository                                                             |
| [IBM Information Governance Catalog (IGC) OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=gh } | implements read-only connectivity to the metadata repository within the [IBM InfoSphere Information Server :material-dock-window:](https://www.ibm.com/analytics/information-server){ target=ibm } suite |
| [SAS Viya OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-sas-viya){ target=gh }                                               | implements metadata exchange to the metadata repository within the [SAS Viya Platform :material-dock-window:](https://support.sas.com/en/software/sas-viya.html){ target=sas }                           |
| [Sample Repository proxy (adapter) using polling to access files :material-github:](https://github.com/odpi/egeria-connector-repository-file-sample){ target=gh }    | implements metadata exchange to a file system using a polling pattern and an embedded OMRS repository.                                                                                                   |

??? education "Further information relating to Repository and Event Mapper connectors"
    
    - [Configuring a native repository connector](/guides/admin/servers/configuring-a-metadata-access-store/#configure-the-native-repository-connector) to understand how to set up a repository connector in a [Metadata Access Store](/concepts/metadata-access-store).
    - [Configuring an adapter repository connector](/guides/admin/servers/configuring-a-repository-proxy/#configure-the-connectors-to-the-third-party-metadata-repository) to understand how to set up a repository connector in a [Repository Proxy](/concepts/repository-proxy).
    - [Writing repository and event mapper connectors](/guides/developer/repository-connectors/overview) for more information on writing new repository and event mapper connectors.

### Open Discovery Services

---8<-- "docs/connectors/discovery/discovery-service-intro.md"

| Connector                                                                                                                                                                                                     | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| [Sequential Discovery Pipeline :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh }                 | runs nested discovery services in a sequence ([more information on discovery pipelines](/frameworks/odf/#discovery-pipeline)). |
| [CSV Discovery Service :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh }                         | extracts the column names from the first line of the file, counts up the number of records in the file and extracts its last modified time. |
| [Validate Drop Foot Weekly Measurements Discovery Service :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/governance-services-sample){ target=gh } | runs nested discovery services in a sequence ([more information on discovery pipelines](/frameworks/odf/#discovery-pipeline)). |
| [Validate Patient Records :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/governance-services-sample){ target=gh }                                | runs nested discovery services in a sequence ([more information on discovery pipelines](/frameworks/odf/#discovery-pipeline)). |

??? education "Further information relating to Open Discovery Services"
    
    - [Configuring an engine host](/guides/admin/servers/configuring-an-engine-host) to understand how to set up the [Engine Host](/concepts/engine-host) server where the open discovery services run.
    - [Setting up a governance engine content pack](/guides/developer/open-metadata-archive/creating-governance-engine-content-packs) to create an [open discovery engine](/concepts/open-discovery-engine) definition to load into a [Metadata Access Store](/concepts/metadata-access-store).
    - [Writing an open discovery service](/guides/developer/open-discovery-services/overview) for information on writing new open discovery services.

### Governance Action Services

---8<-- "docs/connectors/governance-action/governance-action-service-intro.md"

| Connector | Description |
|---|---|
| [Generic Element Watchdog Governance Action Service](/connectors/governance-action/generic-element-watchdog-governance-action-service) | listens for changing metadata elements and initiates governance action processes when certain events occur. |
| [Generic Folder Watchdog Governance Action Service](/connectors/governance-action/generic-folder-watchdog-governance-action-service) | listens for changing assets linked to a `DataFolder` element and initiates governance actions when specific events occur. This may be for files directly linked to the folder or located in sub-folders.|
| [Move/Copy File Provisioning Governance Action Service](/connectors/governance-action/move-copy-file-provisioning-governance-action-service) | moves or copies files from one location to another and maintains the lineage of the action. |
| [Origin Seeker Remediation Governance Action Service](/connectors/governance-action/origin-seeker-remediation-governance-action-service) | walks backwards through the lineage mappings to discover the origin of the data |

??? education "Further information relating to Governance Action Services"
    
    - [Configuring an engine host](/guides/admin/servers/configuring-an-engine-host) to understand how to set up the [Engine Host](/concepts/engine-host) server where the governance action services run.
    - [Setting up a governance engine content pack](/guides/developer/open-metadata-archive/creating-governance-engine-content-packs) to create a [governance action engine](/concepts/governance-action-engine) definition to load into a [Metadata Access Store](/concepts/metadata-access-store).
    - [Writing a governance action service](/guides/developer/governance-action-services/overview) for information on writing new governance action services.

### Governance Daemon Connectors

---8<-- "docs/connectors/governance-daemon/governance-daemon-intro.md"

| Connector | Description |
|---|---|
| [Open Lineage Janus Connector](/connectors/governance-daemon/open-lineage-janus-connector) | The Open Lineage connectors provide plugins to the [Open Lineage Server](/services/open-lineage-services) that allow the Open Lineage Services to connect with databases. |


### Repository Governance Services

---8<-- "docs/connectors/repository-governance/repository-governance-service-intro.md"

There are currently no repository governance services supplied by Egeria.

??? education "Further information relating to Repository Governance Services"

    - [Configuring an engine host](/guides/admin/servers/configuring-an-engine-host) to understand how to set up the [Engine Host](/concepts/engine-host) server where the repository governance services run.
    - [Setting up a governance engine content pack](/guides/developer/open-metadata-archive/creating-governance-engine-content-packs) to create a [repository governance engine](/concepts/repository-governance-engine) definition to load into a [Metadata Access Store](/concepts/metadata-access-store).
    - [Writing a repository governance service](/guides/developer/archive-services/overview) to understand how to write a repository governance service.


## Runtime connectors

*Runtime* connectors enable Egeria's [OMAG Server Platform](/egeria docs/concepts/omag-server-platform) and its hosted [OMAG Servers](/concepts/omag-server) to operate in many environments by providing plug-in points for the runtime services it needs to operate. Most of the runtime connectors relate to persistent storage, or connections to distributed services.

| Type | Description |
|---|---|
| [Platform Metadata Security Connectors](#platform-metadata-security-connectors) | manage authorization requests for the OMAG Server Platform's services. |
| [Server Metadata Security Connectors](#server-metadata-security-connectors) | manage authorization requests for the OMAG Server's services. |
| [Configuration Document Store Connectors](#configuration-document-store-connectors) | manage the persistence and retrieval of [configuration documents](/concepts/configuration-document). |
| [Cohort Registry Store Connectors](#cohort-registry-store-connectors) | store the [open metadata repository cohort](/concepts/cohort-member) membership details in the [cohort registry store](/concepts/cohort-registry-store). |
| [Open Metadata Archive Store Connectors](#open-metadata-archive-store-connectors) | read and write [open metadata archives](/concepts/open-metadata-archive). |
| [Audit Log Destination Connectors](#audit-log-destination-connectors) | support different destinations for audit log records. |
| [REST Client Connectors](#rest-client-connectors) | issue REST API calls to Egeria's deployed platforms and third party technologies. |
| [Cohort Member Client Connector](#cohort-member-client-connectors) | supports repository service called to remote cohort members. |
| [Open Metadata Topic Connectors](#open-metadata-topic-connectors) | send and receive events. |


### Platform Metadata Security Connectors

---8<-- "docs/connectors/runtime/platform-metadata-security-connector-intro.md"

There is one implementation of the platform metadata security connector provided by Egeria.  It is a sample that encodes information from the Coco Pharmaceutical scenarios.

* **[Coco Pharmaceuticals Platform Metadata Security Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh }** 

??? education "Further information relating to Platform Metadata Security Connectors"

    - [Configuring a Platform Metadata Security Connector](/guides/admin/configuring-the-omag-server-platform/#platform-security) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Metadata Security](/features/metadata-security/overview) to understand the platform metadata security connector in the context of all of the security features.
    - [Writing a Platform Metadata Security Connector](/guides/developer/runtime-connectors/platform-metadata-security-connector).


### Server Metadata Security Connectors

---8<-- "docs/connectors/runtime/server-metadata-security-connector-intro.md"

There is one implementation of the server metadata security connector provided by Egeria.  It is a sample that encodes information from the Coco Pharmaceuticals scenarios.

* **[Coco Pharmaceuticals Server Metadata Security Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh }** 

??? education "Further information relating to Server Metadata Security Connectors"

    - [Configuring a Server Metadata Security Connector](/guides/admin/configuring-the-omag-server-platform/#platform-security) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Metadata Security](/features/metadata-security/overview) to understand the server metadata security connector in the context of all of the security features.
    - [Writing a Server Metadata Security Connector](/guides/developer/runtime-connectors/server-metadata-security-connector).


### Configuration Document Store Connectors

---8<-- "docs/connectors/runtime/configuration-document-store-connector-intro.md"

There are two implementations of the configuration document store connector provided by Egeria: one for an encrypted store (default) and the other for a plain text store.

* **[Encrypted File Configuration Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector){ target=gh }** stores each configuration document as an encrypted JSON file.

* **[File Configuration Store :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector){ target=gh }** stores each configuration document as a clear text JSON file.


??? education "Further information relating to Configuration Document Store Connectors"

    - [Configuring a Configuration Document Store Connector](/guides/admin/configuring-the-omag-server-platform/#configuration-store) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Writing a Configuration Document Store Connector](/guides/developer/runtime-connectors/configuration-document-store-connector).


### Cohort Registry Store Connectors

---8<-- "docs/connectors/runtime/cohort-registry-store-connector-intro.md"

Egeria provides a single implementation of a cohort registry store connector:

* [Cohort Registry File Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors/cohort-registry-file-store-connector){ target=gh }
  provides the means to store the cohort registry membership details as a JSON file.

??? education "Further information relating to Cohort Registry Store Connectors"

    - [Configuring a Cohort Registry Store Connector](/guides/admin/servers/configuring-the-cohort-registry-store-connector) in the [Cohort Member](/concepts/cohort-member) server
    - [Cohort Operations](/features/metadata-security/overview) to understand the way the cohort is formed.
    - [Writing a Cohort Registry Store Connector](/guides/developer/runtime-connectors/cohort-registry-store-connector).

  
### Open Metadata Archive Store Connectors

---8<-- "docs/connectors/runtime/open-metadata-archive-store-connector-intro.md"

Egeria provides two implementations of the open metadata archive store connector:

* [File-based Open Metadata Archive Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-file-connector){ target=gh }
  stores an open metadata archive as a plain text JSON file.
  
* [Directory-based Open Metadata Archive File Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-directory-connector){ target=gh }
  stores an open metadata archive in a directory structure where each type definition and metadata instance is stored in JSON format in its own file.  

??? education "Further information relating to Open Metadata Archive Store Connectors"

    - [Metadata Archiving](/features/metadata-archiving/overview) to understand the different mechanisms that use open metadata archives.
    - [Open Metadata Archives](/concepts/open-metadata-archive) to understand structure of an open metadata archive.
    - [Writing a Open Metadata Archive Store Connector](/guides/developer/runtime-connectors/open-metadata-archive-store-connector).
    - [Loading an Open Metadata Archive at server statup](/guides/admin/servers/configuring-a-metadata-access-store/#configure-metadata-to-load-on-startup)
    - [Loading an Open Metadata Archive in a running server](/guides/operations/adding-archive-to-running-server)


### Audit Log Destination Connectors

---8<-- "docs/connectors/runtime/audit-log-destination-connector-intro.md"


Below are the connector implementations provided by Egeria

* [Console Audit Log Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-console-connector){ target=gh }
  writes selected parts of each audit log record to stdout.

* [slf4j Audit Log Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-slf4j-connector){ target=gh }
  writes full log records to the slf4j ecosystem.

* [File Audit Log Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-file-connector){ target=gh }
  creates log records as JSON files in a shared directory.

* [Event Topic Audit Log Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-event-topic-connector){ target=gh }
  sends each log record as an event on the supplied event topic.

??? education "Further information relating to Audit Log Destination Connectors"

    - [Configuring a Audit Log Destination Connector](/concepts/audit-log/#configure-the-audit-log) in the [Cohort Member](/concepts/cohort-member) server
    - [Audit Log Framework (ALF)](/frameworks/alf/overview) to understand the framework behind the audit log.
    - [Writing a Audit Log Destination Connector](/guides/developer/runtime-connectors/audit-log-destination-connector).

### REST Client Connectors

---8<-- "docs/connectors/runtime/rest-client-connector-intro.md"

Egeria provides a single implementation for Spring.

* [Spring REST Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/spring-rest-client-connector){ target=gh }
  uses the Spring RESTClient to issue REST API calls.
  
This is embedded in Egeria's Java clients. See

    - Egeria's [Platform API clients](/guides/developer/#working-with-the-platform-apis).
    - Egeria's [OMAS clients](/guides/developer/#working-with-the-open-metadata-and-governance-apis).



### Cohort Member Client Connectors

---8<-- "docs/connectors/runtime/cohort-member-client-connector-intro.md"

Egeria's [Open Metadata Repository Services (OMRS)](/services/omrs) provides a default REST API implementation and a corresponding client:

* [REST Cohort Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/omrs-rest-repository-connector){ target=gh }
  supports remote calls to the OMRS REST API.
  
The connection for this connector is configured in the `LocalRepositoryRemoteConnection` property of the
cohort member's [Local Repository Configuration](/user/guides/admin/servers/configuring-a-metadata-access-point/#configure-the-local-repository).

## Digital resource connectors

---8<-- "docs/connectors/resource/digital-resource-connector-intro.md"

### Files

* The [Avro file connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/avro-file-connector){ target=gh } provides access to an Avro file that has been catalogued using open metadata.
  
* The [basic file connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector){ target=gh }  provides support to read and write to a file using the Java File object.  

* The [CSV file connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/csv-file-connector){ target=gh }  is able to retrieve data from a Comma Separated Values (CSV) file where the contents are stored in logical columns with a special character delimiter between the columns.
  
* The [data folder connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/data-folder-connector){ target=gh } is for accessing data that is stored as a number of files within a folder (directory).
  
### Databases

* The [jdbc resource connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/jdbc-resource-connector){ target=gh } is for accessing a database server.

### Open Metadata Topic Connectors

---8<-- "docs/connectors/resource/open-metadata-topic-connector-intro.md"

Egeria provides a single implementation of an open metadata connector for Apache Kafka that it uses by default.

* The [Kafka Open Metadata Topic Connector](/connectors/resource-connectors/kafka-open-metadata-topic-connector) implements  an [Apache Kafka](https://kafka.apache.org/) connector for a topic that exchanges Java Objects as JSON payloads.


It is configured in the Egeria [OMAG Servers](/concepts/omag-server) through the [Event Bus Configuration](/concepts/event-bus).



--8<-- "snippets/abbr.md"
