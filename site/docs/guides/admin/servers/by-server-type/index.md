<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring different types of OMAG Servers

The configuration document controls that startup of services as an [OMAG Server](/concepts/omag-server) starts up.  When you use the configuration commands from the [Administration Services](/services/admin-services/overview) you are building up the properties in the configuration document.

The configuration document is divided into sections.  Some sections contain properties that are needed by all [types of servers](/concepts/omag-server/#types-of-omag-server) and others are specialized for a particular type of server.  The guides that follow show which services are relevant for each type of server and how to configure them.

![Different types of Server](/concepts/types-of-omag-servers.svg)



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


## Local Server Name


## Local Server Type


## Audit Trail

