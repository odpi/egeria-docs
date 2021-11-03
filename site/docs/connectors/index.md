<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connector catalog

Egeria has a growing collection of *connectors* to third party technologies. These connectors help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

A connector is a client to a third party technology. It supports a standard API that Egeria calls and it then translates these calls into requests to the third party technology. Some connectors are also able to listen for notifications from the third party technology. When a notification is received, the connector converts its content into a call to Egeria to distribute the information to the open metadata ecosystem.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the OMAG servers. The Connector Catalog list the connector implementations supplied by the Egeria community. There are three broad categories of connectors and the connector catalog is organized accordingly:

* Connectors that support the [exchange and maintenance of metadata](#metadata-exchange-and-maintenance-connectors). This includes the integration connectors, repository connectors, discovery services and governance action services.

* Connectors that support [Egeria’s runtime](#runtime-connectors). This includes the event bus connectors, cohort registry stores, configuration stores, audit log destination connectors, open metadata archive stores, REST client connectors and the cohort member remote repository connectors

* Connectors that provide access to [digital resources and their metadata](#digital-resource-connectors) that is stored in the open metadata ecosystem.

## Metadata exchange and maintenance connectors

The connectors that support the exchange and maintenance of metadata help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

| Type | Description |
|---|---|
| [Integration connectors](#integration-connectors) | manage the metadata exchange to a third party technology through an [integration service](/egeria-docs/services/omis). |
| [Repository and Event Mapper connectors](#repository-and-event-mapper-connectors) | integrate metadata repositories through one or more [open metadata repository cohorts](/egeria-docs/services/omrs/cohort). |
| [Open Discovery Services](#open-discovery-services) | analyze the content of resources in the digital landscape and create annotations that are attached to the resource's [asset](/egeria-docs/concepts/asset) metadata element in the open metadata repositories in the form of an open discovery report |
| [Governance Action Services](#governance-action-services) | perform monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities as required. |

## Integration Connectors

The integration connectors support the exchange of metadata with third party technologies.  This exchange
may be inbound, outbound, synchronous, polling or event-driven.

![Figure 1](/egeria-docs/connectors/integration/integration-connectors.svg)
> **Figure 1:** Integration Connectors

Details of how integration connectors work is described in [the developer guide](/egeria-docs/guides/developer/integration-connectors/overview).

#### Files

The `files` integration connectors run in the [Files Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/files-integrator/overview) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).

| Connector | Description |
|---|---|
| [Data files monitor](/egeria-docs/connectors/integration/data-files-monitor-integration-connector) | maintains a `DataFile` asset for each file in the directory (or any subdirectory). When a new file is created, a new DataFile asset is created.  If a file is modified, the lastModified property of the corresponding DataFile asset is updated.  When a file is deleted, its corresponding DataFile asset is also deleted (or archived if it is still needed for lineage). |
| [Data folder monitor](/egeria-docs/connectors/integration/data-folder-monitor-integration-connector) | maintains a `DataFolder` asset for the directory.  The files and directories underneath it are assumed to be elements/records in the DataFolder asset and so each time there is a change to the files and directories under the monitored directory, it results in an update to the lastModified property of the corresponding DataFolder asset. |

#### Databases

The database integration connectors run in the [Database Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/database-integrator/overview) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).

| Connector | Description |
|---|---|
| [PostgreSQL database connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/egeria-connector-postgres){ target=gh } | automatically maintains the open metadata instances for the databases hosted on a [PostgreSQL server :material-dock-window:](https://www.postgresql.org){ target=psql } This includes the database schemas, tables, columns, primary keys and foreign keys.|


#### Topics

The topic integration connectors run in the [Topic Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/topic-integrator/overview) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).

| Connector | Description |
|---|---|
| [Kafka Monitor topic integration connector](/egeria-docs/connectors/integration/kafka-monitor-integration-connector) | automatically maintains the open metadata instances for the topics hosted on an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka }.|


#### APIs

The API integration connectors run in the [API Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/api-integrator/overview) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).

| Connector | Description |
|---|---|
| [Open API Monitor integration connector](/egeria-docs/connectors/integration/open-api-monitor-integration-connector) | automatically maintains the open metadata instances for the APIs extracted from the Open API Specification extracted from an application.|

#### Security Enforcement Engines

The security integration connectors run in the [Security Integrator Open Metadata Integration Service (OMIS)](/egeria-docs/services/omis/security-integrator) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).

#### Lineage

The lineage integration connectors run in the [Lineage Integrator OMIS](/egeria-docs/services/omis/lineage-integrator/overview) hosted in the [integration daemon](/egeria-docs/concepts/integration-daemon).  They support [Lineage Management](/egeria-docs/features/lineage-management/overview).


| Connector | Description |
|---|---|
| [Open Lineage Event Receiver integration connector](/egeria-docs/connectors/integration/open-lineage-event-receiver-integration-connector) | Connector to receive open lineage events from an evvent topic and publish them to lineage integration connectors with listeners registered in the same instance of the Lineage Integrator OMIS.|
| [Governance Action to Open Lineage integration connector](/egeria-docs/connectors/integration/governance-action-open-lineage-integration-connector) | Connector to listen for governance actions executing in the open metadata ecosystem, generate open lineage events for them and publish them to the integration connectors running in the same instance of Lineage Integrator OMIS that are listening for OpenLineage events. |
| [API-based Open Lineage Log Store integration connector](/egeria-docs/connectors/integration/api-based-open-lineage-log-store-integration-connector) | Connector that calls an OpenLineage compliant API to store the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS.|
| [File-based Open Lineage Log Store integration connector](/egeria-docs/connectors/integration/file-based-open-lineage-log-store-integration-connector) | Connector that stores the open lineage events that are passed to it through the OpenLineage listener that is registered with the Lineage Integrator OMIS. Each OpenLineage event is stored in its own file in JSON format.  These files are organized according to the namespace and job name in the event. |
| [Open Lineage Cataloguer integration connector](/egeria-docs/connectors/integration/open-lineage-cataloguer-integration-connector) | Connector to register an OpenLineage listener with the Lineage Integrator OMIS and to catalog any processes that are not already known to the open metadata ecosystem. |


## Repository and Event Mapper Connectors

The repository connectors provide the ability to integrate a third party metadata repository
into an [open metadata repository cohort](/egeria-docs/concepts/cohort-member).

Figure 2 shows the repository connector providing a native open metadata repository
that uses a particular type of store within an Egeria [Metadata Access Server](/egeria-docs/concepts/metadata-access-server).

![Figure 2](/egeria-docs/connectors/repository/native-repository-connector.png)
> **Figure 2:** Repository connector supporting a native open metadata repository


| Connector | Description |
|---|---|
| [JanusGraph OMRS Repository Connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/graph-repository-connector){ target=gh } | provides a native repository for a metadata server using [JanusGraph :material-dock-window:](https://janusgraph.org){ target=janus } as the backend. |
| [XTDB OMRS Repository Connector](/egeria-docs/connectors/repository/xtdb) | provides a native repository for a metadata server that supports historical queries, using [XTDB :material-dock-window:](https://xtdb.com){ target=xtdb } as the backend. |
| [In-memory OMRS Repository Connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector){ target=gh } | provides a simple native repository implementation that "stores" metadata in HashMaps within the JVM; it is used for testing, or for environments where metadata maintained in other repositories needs to be cached locally for performance/scalability reasons.  |
| [Read-only OMRS Repository Connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/inmemory-repository-connector){ target=gh } | provides a native repository implementation that does not support the interfaces for create, update, delete; however, it does support the search interfaces and is able to cache metadata -- this means it can be loaded with open metadata archives to provide standard metadata definitions. |

Figure 3 shows the repository connector providing a native open metadata repository
that uses a particular type of store within an Egeria [Metadata Access Server](/egeria-docs/concepts/metadata-a-access-server).

![Figure 3](/egeria-docs/connectors/repository/adapter-repository-connector.svg)
> **Figure 3:** Repository connector and optional event mapper supporting an adapter to a third party metadata catalog

| Connector | Description |
|---|---|
| [Apache Atlas OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=gh } | implements read-only connectivity to the [Apache Atlas :material-dock-window:](https://atlas.apache.org){ target=atlas } metadata repository |
| [IBM Information Governance Catalog (IGC) OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=gh } | implements read-only connectivity to the metadata repository within the [IBM InfoSphere Information Server :material-dock-window:](https://www.ibm.com/analytics/information-server){ target=ibm } suite |
| [SAS Viya OMRS Repository Connector :material-github:](https://github.com/odpi/egeria-connector-sas-viya){ target=gh } | implements metadata exchange to the metadata repository within the [SAS Viya Platform :material-dock-window:](https://support.sas.com/en/software/sas-viya.html){ target=sas } |

The [repository connectors](/egeria-docs/connectors/repository-connector) implement the [`OMRSMetadataCollection` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } interface to allow metadata to be communicated and exchanged according to Egeria's protocols and [type definitions](/egeria-docs/types).


## Open Discovery Services

[Open discovery services](/egeria-docs/frameworks/odf/#discovery-service) are connectors that analyze the content of resources in the digital landscape and create annotations that are attached to the resource's Asset metadata element in the open metadata repositories in the form of an open discovery report.

![Figure 4](/egeria-docs/connectors/discovery/discovery-service.svg)
> **Figure 4:** Discovery Services

The definition of the connector interfaces for discovery services is defined in the [open-discovery-services :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/frameworks/open-discovery-framework/src/main/java/org/odpi/openmetadata/frameworks/discovery){ target=gh } module.

| Connector | Description |
|---|---|
| [CSV Discovery Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } | extracts the column names from the first line of the file, counts up the number of records in the file and extracts its last modified time. |
| [Sequential Discovery Pipeline :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } | runs nested discovery services in a sequence ([more information on discovery pipelines](/egeria-docs/frameworks/odf/#discovery-pipeline)). |

## Governance Action Services

[Governance action services](/egeria-docs/frameworks/gaf/#governance-action-service) are connectors that perform monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request.

![Figure 5](/egeria-docs/connectors/governance-action/governance-action-service.svg)
> **Figure 5:** Governance Action Services

They run in the [Governance Action Open Metadata Engine Service (OMES)](/egeria-docs/services/omes/governance-action) hosted by the [Engine Host OMAG Server](/egeria-docs/concepts/engine-host).

| Connector | Description |
|---|---|
| [Generic Element Watchdog Governance Action Service](generic-element-watchdog-governance-action-service.md) | listens for changing metadata elements and initiates governance action processes when certain events occur. |
| [Generic Folder Watchdog Governance Action Service](generic-folder-watchdog-governance-action-service.md) | listens for changing assets linked to a `DataFolder` element and initiates governance actions when specific events occur. This may be for files directly linked to the folder or located in sub-folders.|
| [Move/Copy File Provisioning Governance Action Service](move-copy-file-provisioning-governance-action-service.md) | moves or copies files from one location to another and maintains the lineage of the action. |
| [Origin Seeker Remediation Governance Action Service](origin-seeker-remediation-governance-action-service.md) | walks backwards through the lineage mappings to discover the origin of the data |

The definition of the connector interfaces for governance action services is defined in the [governance-action-framework :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/frameworks/governance-action-framework) module.


## Runtime connectors

*Runtime* connectors support Egeria's runtime:
Connectors enable Egeria to operate in many environments by providing plug-in points for the runtime services
it needs to operate.  Most of these connectors relate to persistent storage, or connections to distributed services.

## Configuration Document Store Connectors

The configuration store connectors contain the connector implementations that manage
the [Configuration Documents](../../../open-metadata-implementation/admin-services/docs/concepts/configuration-document.md)
for [OMAG Servers](../../../open-metadata-implementation/admin-services/docs/concepts/omag-server.md).

![Figure 7](/egeria-docs/connectors/runtime/configuration-document-store-connector.svg)
> **Figure 7:** Configuration Document Store Connector

There is one configuration document store connector defined for each
[OMAG Server Platform](../../../open-metadata-implementation/admin-services/docs/concepts/omag-server-platform.md).

There are two implementations of the configuration document store connector provided by Egeria: one for an encrypted store (default) and the other for a plain text store.

* **[Encrypted File Configuration Store Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-encrypted-file-store-connector)** stores each
configuration document as an encrypted JSON file.

* **[File Configuration Store](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors/configuration-file-store-connector)** stores each
configuration document as a clear text JSON file.

The definition of the connector interface for these connectors is
defined in the [admin-services-api](../../../open-metadata-implementation/admin-services/admin-services-api) module in the
[org.odpi.openmetadata.adminservices.store](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/admin-services/admin-services-api/src/main/java/org/odpi/openmetadata/adminservices/store) Java package.

Configuring a configuration store connector in the
OMAG Server Platform is described in the [Administration Guide](../../../open-metadata-implementation/admin-services/docs/user/configuring-the-configuration-document-store.md).
If no connector is configured, the OMAG Server Platform uses the Encrypted File Configuration Store Connector.


## Cohort Registry Store Connectors

The cohort registry store connectors store the
[open metadata repository cohort](../../../open-metadata-implementation/repository-services/docs/open-metadata-repository-cohort.md)
membership details used and maintained by the [cohort registry](../../../open-metadata-implementation/repository-services/docs/component-descriptions/cohort-registry.md).
The cohort protocols are peer-to-peer and hence there is a cohort registry
(with a [cohort registry store](../../../open-metadata-implementation/repository-services/docs/component-descriptions/connectors/cohort-registry-store-connector.md))
for each [member of a cohort](../../../open-metadata-implementation/admin-services/docs/concepts/cohort-member.md).

![Figure 8](/egeria-docs/connectors/runtime/cohort-registry-store-connector.svg)
> **Figure 8:** Open Metadata Topic Connectors

Egeria provides a single implementation of a
cohort registry store connector:

* [Cohort Registry File Store Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors/cohort-registry-file-store-connector)
  provides the means to store the cohort registry membership details as a JSON file.
  
The definition of the connector interface for these connectors is
defined in the [repository-services-api](.https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis) module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.cohortregistrystore](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/cohortregistrystore) Java package.

  
## Open Metadata Archive Store Connectors

The open metadata archive store connectors can
read and write [open metadata archives](/egeria-docs/concepts/open-metadata-archive).
Open metadata archives store open metadata types and instances for sharing,
or for back up.
These archives can be
[loaded into an OMAG Server at start up](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-store#configuring-the-startup-archives) or
[added to a running OMAG Server](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-store#adding-archive-to-running-server).

![Figure 9](/egeria-docs/connectors/runtime/open-metadata-archive-store-connector.svg)
> **Figure 9:** Open Metadata Archive Store Connector


Egeria provides a single implementation of the open metadata archive store connector:

* [Open Metadata Archive File Store Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors/open-metadata-archive-file-connector)
  stores an open metadata archive as a plain text JSON file.

The definition of the connector interface for these connectors is
defined in the [repository-services-api](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis) module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore) Java package.


## Audit Log Destination Connectors

The audit log destination connectors support different destinations for audit log records.
Multiple of these connectors can be [active in an OMAG Server](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-point/#configure-the-audit-log)
at any one time and they can each be configured to only process particular types of audit log records.


![Figure 10](/egeria-docs/connectors/runtime/audit-log-destination-connector.svg)
> **Figure 10:** Audit Log Destination Connector

Below are the connector implementations provided by Egeria

* [Console Audit Log Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-console-connector)
  writes selected parts of each audit log record to stdout.

* [slf4j Audit Log Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-slf4j-connector)
  writes full log records to the slf4j ecosystem.

* [File Audit Log Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-file-connector)
  creates log records as JSON files in a shared directory.

* [Event Topic Audit Log Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors/audit-log-event-topic-connector)
  sends each log record as an event on the supplied event topic.

The definition of the connector interface for these connectors is
defined in the [repository-services-api](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis) module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.auditlogstore](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/auditlogstore) Java package.

There is more information on the use of audit logging in the [Diagnostic Guide](/egeria-docs/guides/diagnostic).

## REST Client Connectors

Egeria makes extensive use of [REST API calls](/egeria-docs/concepts/basic-concepts) for synchronous (request-response) communication with
its own deployed runtimes and third party technologies.  The client connectors are used to issue
the REST API calls.  Egeria provides a single implementation for Spring.

* [Spring REST Client Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/spring-rest-client-connector)
  uses the Spring RESTClient to issue REST API calls.
  
This is embedded in Egeria's [clients](/egeria-docs/guides/developer/using-egeria-clients).

![Figure 11](/egeria-docs/connectors/runtime/rest-client-connector.svg)
> **Figure 11:** REST Client Connector

The definition of the connector interface for these connectors is
defined in the [rest-client-connector-api](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/rest-client-connectors-api) module in the
[org.odpi.openmetadata.adapters.connectors.restclients](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/rest-client-connectors/rest-client-connector-api/src/main/java/org/odpi/openmetadata/adapters/connectors/restclients) Java package.


## Cohort Member Client Connector

Members of an [Open Metadata Repository Cohort](/egeria-docs/concepts/cohort-member)
provide the other cohort members with a
Connection to a connector that supports the OMRSRepositoryConnector interface during the cohort registration process.
This connector translates calls to retrieve and maintain metadata in the member's repository into
remote calls to the real repository.


![Figure 12](/egeria-docs/connectors/runtime/cohort-member-client-connector.svg)
> **Figure 12:** Cohort Member Client Connector used for federating queries across the cohort

Egeria's [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) provides a default REST API
implementation and a corresponding client:

* [REST Cohort Client Connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/omrs-rest-repository-connector)
  supports remote calls to the OMRS REST API.
  
The connection for this connector is configured in the `LocalRepositoryRemoteConnection` property of the
cohort member's [Local Repository Configuration](../../../open-metadata-implementation/admin-services/docs/user/configuring-the-local-repository.md).

The definition of the connector interface for these connectors is
defined in the [repository-services-api](https://github.com/odpi/egeria/tree/master//open-metadata-implementation/repository-services/repository-services-apis) module
in the
[org.odpi.openmetadata.repositoryservices.connectors.stores.metadatacollectionstore.repositoryconnector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/repositoryconnector) Java package.
It is the same interface as the [repository connectors](#Repository and Event Mapper Connectors) that are used to provide the local repository to a metadata server
so that the Open Metadata Repository Services (OMRS)
issue calls to the same interface irrespective of whether the call is to the local repository or a remote cohort member.


## Digital resource connectors

*Digital resource* connectors provide access to digital resources and their metadata that is stored in the open metadata ecosystem.  These connectors are for use by external applications and tools to connect with resources and services in the digital landscape.  These connectors also supply the Asset metadata from Egeria that describes these resources.

Instances of these connectors are created through the 
[Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer/overview) or
[Asset Owner OMAS](/egeria-docs/services/omas/asset-owner/overview) interfaces.
They use the Connection linked to the corresponding Asset in the open metadata ecosystem.
Connection objects are associated with assets in the
metadata catalog using the Asset Owner OMAS,
[Data Manager OMAS](/egeria-docs/services/omas/data-manager/overview) and
[Asset Manager OMAS](/egeria-docs/services/omas/asset-manager/overview).


## Files

* The [Avro file connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/avro-file-connector) 
  provides access to an Avro file that has been catalogued using open metadata.
  
* The [basic file connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector) 
  provides support to read and write to a file using the Java File object.  

* The [CSV file connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/csv-file-connector) 
  is able to retrieve data from a Comma Separated Values (CSV) file where the contents are stored in logical columns
  with a special character delimiter between the columns.
  
* The [data folder connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/data-folder-connector)
  is for accessing data that is
  stored as a number of files within a folder (directory).
  
## Databases

*More coming ...*


## Open Metadata Topic Connectors

The Open Metadata Topic Connectors are used by Egeria to read and write 
[events](/egeria-docs/concepts/basic-concepts/#event) to a
[topic](/egeria-docs/concepts/basic-concepts/#topic) managed by an
[event broker](/egeria-docs/concepts/basic-concepts/#event-broker).
These events contain notifications relating to changes in metadata and the topic provides
an asynchronous event exchange service hosted in the event broker.

![Figure 6](/egeria-docs/connectors/resource/open-metadata-topic-connector.svg)
> **Figure 6:** Open Metadata Topic Connectors

The Open Metadata Topic Connectors connect servers into an [open metadata repository cohort](/egeria-docs/concepts/cohort-member)
and exchange notifications through the [Open Metadata Access Services (OMAS)'s](/egeria-docs/services/omas)
topics called the
[InTopic](/egeria-docs/concepts/in-topic) and
[OutTopic](/egeria-docs/concepts/out-topic).

Egeria provides a single implementation of an open metadata connector for Apache Kafka that it uses by default.

* The [Kafka Open Metadata Topic Connector](/egeria-docs/connectors/resource-connectors/kafka-open-metadata-topic-connector) implements 
an [Apache Kafka](https://kafka.apache.org/) connector for a topic that exchanges
Java Objects as JSON payloads.

The definition of the connector interface for these connectors is defined in the `repository-services-apis` module in the [org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic) Java package.

It is configured in the Egeria [OMAG Servers](/egeria-docs/concepts/omag-server) through the [Event Bus Configuration](/egeria-docs/concepts/event-bus).



--8<-- "snippets/abbr.md"
