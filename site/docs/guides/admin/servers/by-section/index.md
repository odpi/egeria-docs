<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuration Document Sections

The configuration document controls that startup of services as an [OMAG Server](/concepts/omag-server) starts up.  When you use the configuration commands from the [Administration Services](/services/admin-services/overview) you are building up the properties in the configuration document.

The configuration document is divided into sections.  Some sections contain properties that are needed by all [types of servers](/concepts/omag-server/#types-of-omag-server) and others are specialized for a particular type of server.  This guide takes you through each section of the configuration document and explains where it is relevant and how to configure it.

![Configuration Document Structure](configuration-document-structure.svg)

* The [*LocalServerId*](#local-server-id), [*LocalServerName*](#local-server-name), [*Local Server Type*](#local-server-type) and [*Audit Trail*](#audit-trail) properties are managed by Egeria and you do not need to configure them.
* The [*Event Bus Config*](event-bus-config-section.md) is used to provide standard information about the event bus (typically Apache Kafka) that is used in each section that configures a service that is sending notifications over the event bus.
* The [*Basic Server Properties*](basic-server-properties-section.md) provides the standard properties of a server such as its user identifier and password.
* The [*Server Security Connection*](server-security-connection-section.md) provides the information needed to enable fine-grained metadata authorization checks.
* The [*Repository Services*](repository-services-section.md) defines the type of audit logging and metadata repository supported by the server.  It also defines which [open metadata repository cohorts](/concepts/cohort-member) that the server belongs to.
* The [*Access Services*](access-services-section.md) define which metadata APIs are activated in a [metadata access server](/concepts/metadata-access-service).
* The [*Engine Host Services*](engine-host-services-section.md) define which governance engines are activated in an [engine host](/concepts/engine-host) server.
* The [*Integration Daemon Services*](integration-daemon-services-section.md) define which integration connectors run in an [integration daemon](/concepts/integration-daemon) server.
* The [*View Services*](view-services-section.md) define which REST APIs are enabled in a [view server](/concepts/view-server).
* The [*Lineage Warehouse Services*](lineage-warehouse-services-section.md) define the properties of the repository for a [lineage warehouse](/concepts/lineage-warehouse) server.
* The [*Data Engine Proxy Services*](data-engine-proxy-services-section.md) define the properties of a [data engine proxy server](/concepts/data-engine-proxy) server.


## Local Server Id

The localServerId is a unique identifier for the server, it is used when accessing resource that require their callers to supply a unique identifier.  For example, when an OMAG server is accessing an Apache Kafka topic, it needs to reliably identify itself with a callerId so that the Kafka server knows which events it has received and which it has not.  The localServerId is used for this purpose when accessing the [open metadata repository cohort topics](/concepts/cohort-events) for example.

## Local Server Name

The localServerName is a unique name for the server.  This is a name you choose, and the administration services maintains the name in the configuration document.

## Local Server Type

The local server type is a classification of the type of the server based on the sections of the configuration document that have been configured.  Leave it blank and Egeria will fill it in on server start up.  There is also an administration call to query the type of server using the following call:



## Audit Trail

--8<-- "snippets/abbr.md"
