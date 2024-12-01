<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connector catalog

Egeria has a growing collection of *connectors* to third party technologies. These connectors help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

A connector is a client to a third party technology. It supports a standard API that Egeria calls, and it then translates these calls into requests to the third party technology. Some connectors are also able to listen for notifications from the third party technology. When a notification is received, the connector converts its content into a call to Egeria to distribute the information to the open metadata ecosystem.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the [OMAG servers](/concepts/omag-server). The Connector Catalog list the connector implementations supplied by the Egeria community. There are three broad categories of connectors and the connector catalog is organized accordingly:

* Connectors that support the [exchange and maintenance of metadata](#metadata-exchange-and-maintenance-connectors) with third party technology. This includes the resource connectors, survey action connectors, integration connectors and adapter repository connectors.  These connectors are organized by the type of third part technology type work with.

* Connectors that support the [governance of open metadata](#open-metadata-governance-connectors). This includes the context event services and governance action services.  These connectors are organized by function.

* Connectors that support the integration of [Egeria’s runtimes](#runtime-connectors) into the IT infrastructure where it is running. This includes the native repository connectors, event bus connectors, cohort registry stores, configuration stores, audit log destination connectors, open metadata archive stores, REST client connectors and the cohort member remote repository connectors.  These connectors are organized by connector type.

## Metadata exchange and maintenance connectors

The connectors that support the exchange and maintenance of metadata help to accelerate the rollout of your open metadata ecosystem, since they can be used to automate the extraction and distribution of metadata to the third party technologies.

* [Secrets Store connectors](#secrets-stores)  manage the retrieval of secrets (passwords, certificates, ...) from secured locations at runtime.                          
* [File connectors](#files) work with different types of files.
* [JDBC Database connectors](#relational-databases) make use of the JDBC standards to work with different types of relational databases.
* [Apache Kafka connectors](#apache-kafka) work with the topics and/or events passing through the Apache Kafka event broker.
* [Apache Atlas connectors](#apache-atlas) work with an Apache Atlas server.
* [Strimzi connector](#strimzi) works with the cloud-based Apache Kafka deployment called Strimzi.
* [Open API Specification connectors](#open-api-specification) extract metadata about APIs through the Open API interfaces provided through the Swagger API.
* [Open Lineage Event connectors](#open-lineage-events) works with the open lineage event standard.

### Secrets Stores

[Secrets stores](/concepts/secrets-store-connector) externalize secrets such as passwords, tokens and certificates so they do not need to be stored in either the [configuration document](/concepts/configuration-document) or [open metadata repositories](/concepts/open-metadata-repository).

* The [Environment Variables Secret Store connector](/connectors/secrets/environment-variable-secrets-store-connector) retrieves secret values from environment variables.
* The [YAML File Secret Store connector](/connectors/secrets/yaml-secrets-store-connector) retrieves secret values from environment variables.

### Files

Files provide storage for many types of data.  They are organizes into folders (also known as directories on some operating systems).  Some connectors work with any type of file.  Other connectors are able to understand the content of specific types of file formats and so these connectors are organized by file type.

#### Any type of File 

* The [Basic File Resource Connector](/connectors/resource/basic-file-resource-connector)  provides support to read and write to a file using the Java File object.
* The [Move/Copy File Provisioning Governance Action Service](/connectors/governance-action/move-copy-file-provisioning-governance-action-service)  moves or copies files from one location to another and maintains the lineage of the action. 

#### File Folders (Directories)

* The [Basic Folder Resource Connector](/connectors/resource/basic-folder-resource-connector) is for accessing the files within a folder (directory).
* The [Data Files Monitor Integration Connector](/connectors/integration/data-files-monitor-integration-connector) maintains a `DataFile` asset for each file in the directory (or any subdirectory). When a new file is created, a new DataFile asset is created.  If a file is modified, the lastModified property of the corresponding DataFile asset is updated.  When a file is deleted, its corresponding DataFile asset is also deleted (or archived if it is still needed for lineage).
* The [Generic Folder Watchdog Governance Action Service](/connectors/governance-action/generic-folder-watchdog-governance-action-service) listens for changing `DataFile` assets linked to a specified `FileFolder` element and initiates governance actions when specific events occur. This may be for files directly linked to the folder or located in sub-folders.

#### Data Folders

* The [Data Folder Resource Connector](/connectors/resource/data-folder-resource-connector) is for accessing data that is stored as a number of files within a folder (directory).
* The [Data folder Monitor Integration Connector](/connectors/integration/data-folder-monitor-integration-connector) maintains a `DataFolder` asset for the directory.  The files and directories underneath it are assumed to be elements/records in the DataFolder asset and so each time there is a change to the files and directories under the monitored directory, it results in an update to the lastModified property of the corresponding DataFolder asset.

#### CSV Files

* The [CSV File Resource Connector](/connectors/resource/csv-file-resource-connector)  is able to retrieve data from a Comma Separated Values (CSV) file where the contents are stored in logical columns with a special character delimiter between the columns.

#### Open Metadata Archive Files

* The [File-based Open Metadata Archive Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-file-connector){ target=gh } stores an open metadata archive as a plain text JSON file.


### Relational Databases

* The [JDBC Resource Connector](/connectors/resource/jdbc-resource-connector) is for accessing a database via the JDBC DataSource interface.
* The [JDBC Integration Connector](/connectors/integration/jdbc-integration-connector) automatically maintains the open metadata instances on a database server via JDBC. This includes the database schemas, tables, columns, primary keys and foreign keys.                                                                                      

### Unity Catalog

---8<-- "snippets/systems/unity-catalog-intro.md"

The Unity Catalog connectors provide a suite of function that integrates a Unity Catalog server into the open metadata ecosystem.

* The [Unity Catalog Resource Connector](/connectors/unity-catalog/resource-connector) is a [digital resource connector](/concepts/digital-resource-connector) that acts as a Java client to the Unity Catalog Server REST API.  It is used by the other Unity Catalog connectors.
* The [Unity Catalog Server Synchronizer](/connectors/unity-catalog/sync-server-connector) is an [integration connector](/concepts/integration-connector) that exchanges details about the catalogs defined for a Unity Catalog Server.
* The [Unity Catalog Inside Catalog Synchronizer](/connectors/unity-catalog/sync-catalog-connector) is an [integration connector](/concepts/integration-connector) that exchanges details about the resources (schemas, tables, volumes and functions) defined within a Catalog found in a Unity Catalog Server.
* The [Unity Catalog Server Survey Service](/connectors/unity-catalog/server-survey-service) is a [Survey Action Service](/concepts/survey-action-service) that surveys the resources defined in a Unity Catalog Server.
* The [Unity Catalog Inside Catalog Survey Service](/connectors/unity-catalog/catalog-survey-service) is a [Survey Action Service](/concepts/survey-action-service) that surveys the resources defined in a Catalog inside a Unity Catalog Server.
* The [Unity Catalog Inside Schema Survey Service](/connectors/unity-catalog/schema-survey-service) is a [Survey Action Service](/concepts/survey-action-service) that surveys the resources defined in a Schema inside a Unity Catalog Server.

### Apache Kafka

* The [Kafka Open Metadata Topic Connector](/connectors/resource/kafka-open-metadata-topic-connector) implements a [resource connector](/concepts/digital-resource-connector) for a topic that exchanges Java Objects as JSON payloads across an [Apache Kafka](https://kafka.apache.org/) event bus.   It is configured in the Egeria [OMAG Servers](/concepts/omag-server) through the [Event Bus Configuration](/concepts/event-bus).  This the connector that is used by default in the Egeria runtimes to exchange events (notifications between the [OMAG Servers](/concepts/omag-server)).
* The [Kafka Monitor Topic integration connector](/connectors/integration/kafka-monitor-integration-connector) automatically maintains the open metadata instances for the topics hosted on an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka }.
* The [Kafka Audit Topic integration connector](/connectors/integration/kafka-topics-audit-integration-connector) validates that topics that are active in an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka } are also catalogued in open metadata.  Creates an audit log record for each topic that is not catalogued.
* The [Sample Lineage Integration Connector](/connectors/integration/sample-lineage-event-receiver-integration-connector)  is a sample connector to listen for lineage events (not in an [open lineage format](#open-lineage-events)) and catalog the associated assets, processes, schema and lineage.                                                                                                                                                              |

### Apache Atlas

---8<-- "snippets/systems/apache-atlas-intro.md"

The Apache Atlas connectors provide a suite of function that integrates an Apache Atlas server into the open metadata ecosystem.

* [Apache Atlas REST Connector](/connectors/apache-atlas/apache-atlas-rest-connector) is a [digital resource connector](/concepts/digital-resource-connector) that acts as a Java client to the Apache Atlas Server REST API.  It is used by the other Apache Atlas connectors.
* [Apache Atlas Survey Action Service](/connectors/apache-atlas/apache-atlas-survey-action-service) reviews the types and instances stored in an Apache Atlas Server and creates a [survey report](/concepts/survey-report).   This connector helps to provide insight into the content of the Apache Atlas server to determine if it contains valuable metadata that should be integrated into the open metadata ecosystem.  This connector can also be configured to create a graph schema for the server that describes is supported types and how they link together.
* [Apache Atlas Integration Connector](/connectors/apache-atlas/apache-atlas-catalog-integration-connector) automatically catalogues the content of an Apache Atlas Server into the open metadata ecosystem. It may also be configured to push selected open metadata into the Apache Atlas Server, such as glossary terms, tags and classifications.

### Strimzi

* [Strimzi Monitor topic integration connector](/connectors/integration/strimzi-monitor-integration-connector) automatically maintains the open metadata instances for the topics hosted in [Strimzi :material-dock-window:](https://strimzi.io){ target=strimzi }.                                                                                         

### Open API Specification

The [Open API Monitor integration connector](/connectors/integration/open-api-monitor-integration-connector) automatically maintains the open metadata instances for the APIs extracted from the Open API Specification extracted from an application. 

### Open Lineage Events

The open lineage connectors work with the [Open Lineage standard](/features/lineage-management/overview/#the-openlineage-standard)

* [Open Lineage Event Receiver integration connector](/connectors/integration/open-lineage-event-receiver-integration-connector) receives open lineage events from an event topic and publish them to lineage integration connectors with listeners registered in the same instance of the Lineage Integrator OMIS.                                                                                                              
* [Governance Action to Open Lineage integration connector](/connectors/integration/governance-action-open-lineage-integration-connector) listens for governance actions executing in the open metadata ecosystem, generate open lineage events for them and publish them to the integration connectors running in the same instance of Lineage Integrator OMIS that are listening for OpenLineage events.                                
* [API-based Open Lineage Log Store integration connector](/connectors/integration/api-based-open-lineage-log-store-integration-connector) calls an OpenLineage compliant API to store the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS.                                                                                                              
* [File-based Open Lineage Log Store integration connector](/connectors/integration/file-based-open-lineage-log-store-integration-connector) stores the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS. Each OpenLineage event is stored in its own file in JSON format.  These files are organized according to the namespace and job name in the event. 
* [Open Lineage Cataloguer integration connector](/connectors/integration/open-lineage-cataloguer-integration-connector)  registers an Open Lineage listener with the Lineage Integrator OMIS and to catalog any processes that are not already known to the open metadata ecosystem.

## Open Metadata Governance Connectors

* The [Generic Element Watchdog Governance Action Service](/connectors/governance-action/generic-element-watchdog-governance-action-service) listens for changing metadata elements and initiates governance action processes when certain events occur.
* The [Origin Seeker Governance Action Service](/connectors/governance-action/origin-seeker-remediation-governance-action-service)  walks backwards through the lineage relationships to discover the origin of the data asset.
* The [Zone Publisher Governance Action Service](/connectors/governance-action/zone-publisher-governance-action-service) updates the zone membership on the target action assets.

## Runtime connectors

*Runtime* connectors enable Egeria's [OMAG Server Platform](/concepts/omag-server-platform) and its hosted [OMAG Servers](/concepts/omag-server) to operate in many environments by providing plug-in points for the runtime services it needs to operate. Most of the runtime connectors relate to persistent storage, or connections to distributed services.  The connectors are organized by type to allow you to choose the options available from the Egeria community.

| Type                                                                                | Description                                                                                                                                                            |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Repository and Event Mapper connectors](#repository-and-event-mapper-connectors)   | Integrate metadata repositories into the open metadata ecosystem so that they can interact with one or more [open metadata repository cohorts](/services/omrs/cohort). |
| [Platform Metadata Security Connectors](#platform-metadata-security-connectors)     | manage authorization requests for the OMAG Server Platform's services.                                                                                                 |
| [Server Metadata Security Connectors](#server-metadata-security-connectors)         | manage authorization requests for the OMAG Server's services.                                                                                                          |
| [Configuration Document Store Connectors](#configuration-document-store-connectors) | manage the persistence and retrieval of [configuration documents](/concepts/configuration-document).                                                                   |
| [Cohort Registry Store Connectors](#cohort-registry-store-connectors)               | store the [open metadata repository cohort](/concepts/cohort-member) membership details in the [cohort registry store](/concepts/cohort-registry-store).               |
| [Open Metadata Archive Store Connectors](#open-metadata-archive-store-connectors)   | read and write [open metadata archives](/concepts/open-metadata-archive).                                                                                              |
| [Audit Log Destination Connectors](#audit-log-destination-connectors)               | support different destinations for audit log records.                                                                                                                  |
| [REST Client Connectors](#rest-client-connectors)                                   | issue REST API calls to Egeria's deployed platforms and third party technologies.                                                                                      |
| [Cohort Member Client Connector](#cohort-member-client-connectors)                  | supports repository service called to remote cohort members.                                                                                                           |
| [Open Metadata Topic Connectors](#open-metadata-topic-connectors)                   | send and receive events.                                                                                                                                               |


### Repository and Event Mapper Connectors

---8<-- "snippets/connectors/repository-connector-intro.md"

The table below lists the repository connectors supporting the native open metadata repositories.

| Native Repository Connector                                                         | Description                                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PostgreSQL OMRS Repository Connector](/connectors/repository/postgres/overview)    | provides a native repository for a metadata server using [PostgreSQL :material-dock-window:](https://www.postgresql.org/){ target=postgres } as the backend.                                                                                                                                   |
| [XTDB OMRS Repository Connector](/connectors/repository/xtdb)                       | provides a native repository for a metadata server that supports historical queries, using [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb } as the persistent store.                                                                                                             |
| [In-memory OMRS Repository Connector](/connectors/repository/in-memory/overview)    | provides a simple native repository implementation that "stores" metadata in HashMaps within the JVM; it is used for testing, or for environments where metadata maintained in other repositories needs to be cached locally for performance/scalability reasons.                              |
| [Read-only OMRS Repository Connector](/connectors/repository/read-only/overview)    | provides a native repository implementation that does not support the interfaces for create, update, delete; however, it does support the search interfaces and is able to cache metadata -- this means it can be loaded with open metadata archives to provide standard metadata definitions. |
| [JanusGraph OMRS Repository Connector](/connectors/repository/janus-graph/overview) | provides a native repository for a metadata server using [JanusGraph :material-dock-window:](https://janusgraph.org){ target=janus } as the backend.                                                                                                                                           |

The table below lists the repository connectors that act as an adapter for third party metadata repositories.

| Adapter Repository Connectors                                                                                                                                        | Description                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IBM Information Governance Catalog (IGC) OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=gh } | implements read-only connectivity to the metadata repository within the [IBM InfoSphere Information Server :material-dock-window:](https://www.ibm.com/analytics/information-server){ target=ibm } suite |
| [SAS Viya OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-sas-viya){ target=gh }                                               | implements metadata exchange to the metadata repository within the [SAS Viya Platform :material-dock-window:](https://support.sas.com/en/software/sas-viya.html){ target=sas }                           |
| [Sample Repository proxy (adapter) using polling to access files :material-github:](https://github.com/odpi/egeria-connector-repository-file-sample){ target=gh }    | implements metadata exchange to a file system using a polling pattern and an embedded OMRS repository.                                                                                                   |
| [HMS Repository proxy (adapter) using polling to access HMS Tables :material-github:](https://github.com/odpi/egeria-connector-hivemetastore){ target=gh }           | implements metadata exchange to a Hive metastore using a polling pattern and an embedded OMRS repository.                                                                                                |

??? education "Further information relating to Repository and Event Mapper connectors"

    - [Configuring a native repository connector](/guides/admin/servers/by-server-type/configuring-a-metadata-access-store/#configure-the-native-repository-connector) to understand how to set up a repository connector in a [Metadata Access Store](/concepts/metadata-access-store).
    - [Configuring an adapter repository connector](/guides/admin/servers/by-server-type/configuring-a-repository-proxy/#configure-the-connectors-to-the-third-party-metadata-repository) to understand how to set up a repository connector in a [Repository Proxy](/concepts/repository-proxy).
    - [Writing repository and event mapper connectors](/guides/developer/repository-connectors/overview) for more information on writing new repository and event mapper connectors.


### Platform Metadata Security Connectors

---8<-- "snippets/connectors/platform-metadata-security-connector-intro.md"

There is one implementation of the platform metadata security connector provided by Egeria.  It is a sample that encodes information from the Coco Pharmaceutical scenarios.

* **[Coco Pharmaceuticals Platform Metadata Security Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh }** 

??? education "Further information relating to Platform Metadata Security Connectors"

    - [Configuring a Platform Metadata Security Connector](/guides/admin/configuring-the-omag-server-platform/#platform-security) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Metadata Security](/features/metadata-security/overview) to understand the platform metadata security connector in the context of all of the security features.
    - [Writing a Platform Metadata Security Connector](/guides/developer/runtime-connectors/platform-metadata-security-connector).

### Server Metadata Security Connectors

---8<-- "snippets/connectors/server-metadata-security-connector-intro.md"

There is one implementation of the server metadata security connector provided by Egeria.  It is a sample that encodes information from the Coco Pharmaceuticals scenarios.

* **[Coco Pharmaceuticals Server Metadata Security Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh }** 

??? education "Further information relating to Server Metadata Security Connectors"

    - [Configuring a Server Metadata Security Connector](/guides/admin/configuring-the-omag-server-platform/#platform-security) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Metadata Security](/features/metadata-security/overview) to understand the server metadata security connector in the context of all of the security features.
    - [Writing a Server Metadata Security Connector](/guides/developer/runtime-connectors/server-metadata-security-connector).

### Configuration Document Store Connectors

---8<-- "snippets/connectors/configuration-document-store-connector-intro.md"

There are two implementations of the configuration document store connector provided by Egeria: one for an encrypted store (default) and the other for a plain text store.

* **[Encrypted File Configuration Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector){ target=gh }** stores each configuration document as an encrypted JSON file.

* **[File Configuration Store :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector){ target=gh }** stores each configuration document as a clear text JSON file.


??? education "Further information relating to Configuration Document Store Connectors"

    - [Configuring a Configuration Document Store Connector](/guides/admin/configuring-the-omag-server-platform/#configuration-store) in the [OMAG Server Platform](/concepts/omag-server-platform)
    - [Writing a Configuration Document Store Connector](/guides/developer/runtime-connectors/configuration-document-store-connector).


### Cohort Registry Store Connectors

---8<-- "snippets/connectors/cohort-registry-store-connector-intro.md"

Egeria provides a single implementation of a cohort registry store connector:

* [Cohort Registry File Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors/cohort-registry-file-store-connector){ target=gh }
  provides the means to store the cohort registry membership details as a JSON file.

??? education "Further information relating to Cohort Registry Store Connectors"

    - [Configuring a Cohort Registry Store Connector](/guides/admin/servers/by-section/repository-services-section/#registering-the-server-with-a-cohort) in the [Cohort Member](/concepts/cohort-member) server.
    - [Cohort Operations](/features/cohort-operations/overview) to understand the way the cohort is formed.
    - [Writing a Cohort Registry Store Connector](/guides/developer/runtime-connectors/cohort-registry-store-connector).

  
### Open Metadata Archive Store Connectors

---8<-- "snippets/connectors/open-metadata-archive-store-connector-intro.md"

Egeria provides two implementations of the open metadata archive store connector:

* [File-based Open Metadata Archive Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-file-connector){ target=gh }
  stores an open metadata archive as a plain text JSON file.
  
* [Directory-based Open Metadata Archive File Store Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-directory-connector){ target=gh }
  stores an open metadata archive in a directory structure where each type definition and metadata instance is stored in JSON format in its own file.  

??? education "Further information relating to Open Metadata Archive Store Connectors"

    - [Metadata Archiving](/features/metadata-archiving/overview) to understand the different mechanisms that use open metadata archives.
    - [Open Metadata Archives](/concepts/open-metadata-archive) to understand structure of an open metadata archive.
    - [Writing a Open Metadata Archive Store Connector](/guides/developer/runtime-connectors/open-metadata-archive-store-connector).
    - [Loading an Open Metadata Archive at server statup](/guides/admin/servers/by-section/repository-services-section/#configuring-the-open-metadata-archives-to-load-on-server-startup)
    - [Loading an Open Metadata Archive in a running server](/guides/operations/adding-archive-to-running-server)


### Audit Log Destination Connectors

---8<-- "snippets/connectors/audit-log-destination-connector-intro.md"


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

---8<-- "snippets/connectors/rest-client-connector-intro.md"

Egeria provides a single implementation for Spring.

* [Spring REST Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/spring-rest-client-connector){ target=gh }
  uses the Spring RESTClient to issue REST API calls.
  
This is embedded in Egeria's Java clients. See

- Egeria's [Platform API clients](/guides/developer/#working-with-the-platform-apis).
- Egeria's [OMAS clients](/guides/developer/#working-with-the-open-metadata-and-governance-apis).

### Cohort Member Client Connectors

---8<-- "snippets/connectors/cohort-member-client-connector-intro.md"

Egeria's [Open Metadata Repository Services (OMRS)](/services/omrs) provides a default REST API implementation and a corresponding client:

* [REST Cohort Client Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/omrs-rest-repository-connector){ target=gh }
  supports remote calls to the OMRS REST API.
  
The connection for this connector is configured in the `LocalRepositoryRemoteConnection` property of the
cohort member's [Local Repository Configuration](/user/guides/admin/servers/by-section/#configuring-the-local-repository-store).



--8<-- "snippets/abbr.md"
