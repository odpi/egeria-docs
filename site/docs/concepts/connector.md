---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connector

A connector is a client library for accessing a [resource](/concepts/resource) and, optionally, its associated [asset](/concepts/asset) metadata.

The concept of a connector comes from the [Open Connector Framework (OCF)](/frameworks/ocf/overview). The OCF provides a common framework for components (ie connectors) that enable one technology to call another, arbitrary technology through a common interface. The implementation of the connector is dynamically loaded based on the connector's configuration.

Through the OCF, we can:

1. Plug-in different technologies to Egeria.
2. Plug-in support for open metadata into the client libraries used by applications to access data resources and services.

![How OCF connectors are used in Egeria](/connectors/compare-use-of-connectors.svg)

Many subsystems in Egeria's [OMAG Server Platform](/concepts/omag-server-platform) and [servers](/concepts/omag-server) support the first approach. They define a specialized interface for the type of connector they support.

1. One or more connector implementations supporting that interface are then written either by the Egeria community or other organizations.
2. When an Egeria [OMAG Server](/concepts/omag-server) is configured, details of which connector implementation to use is specified in the server's [configuration document](/concepts/configuration-document) using the [connection](/concepts/connection) structure.
3. At start up, the OMAG Server passes the connector configuration to the OCF to instantiate the required connector instance.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the OMAG Servers.

The second approach is used by organizations that want to make use of metadata directly in applications and tools - or to externalize the security and driver properties needed to call the data source or service. In this case the OCF connector typically has the same interface as the data source's client library (unless you can do better :smile:). This minimizes the learning curve for application developers. The configuration for the connector is stored in an open metadata server and the application uses the [Asset Consumer OMAS](/services/omas/asset-consumer) client to [request a new instance of the connector](/guides/developer/#using-connectors). The application uses the returned connector instance to access the data source or server along with the metadata stored about it.

The connector provides two main APIs:

- An standard API called `getConnectedAssetProperties` for retrieving metadata.  This API is defined by the OCF.
- An API for working with the resource itself.  This interface is specialized for the type of resource and the use it is being put to.

## Specialist connectors that plug into the OMAG Server Platform

Various Egeria services provide specific interfaces for connectors to support their operation.  For example, the [Open Metadata Integration Services (OMIS)](/services/omis) define the interfaces for [integration-connectors](/concepts/integration-connector) used to [exchange metadata between Egeria and third party technologies](/patterns/metadata-exchange/overview). 

The table below lists the different types of connectors supported by Egeria's services. Connectors that are implemented by the Egeria community or trusted third parties are listed in the [connector catalog](/connectors).  You may [write your own connectors](/guides/developer/#building-connectors) to integrate additional types of technology or extend the capabilities of Egeria - and if you think your connector is more generally useful, you could consider [contributing it to the Egeria project](/guides/community).



| Type of Connector             | Description | Documentation | Connector Catalog link |
| :-----------------------------| :---------- | :------------ | :---------------------- |
| Integration Connector         | Implements metadata exchange with third party tools. | [Building Integration Connectors](/guides/developer/integration-connectors/overview) | [Integration Connector Catalog](/connectors/#integration-connectors) |
| Open Discovery Service        | Implements automated metadata discovery.| [Building Open Discovery Services](/guides/developer/open-discovery-services/overview) | [Open Discovery Service Catalog](/connectors/#open-discovery-services) |
| Governance Action Service     | Implements automated governance. | [Building Governance Action Services](/guides/developer/governance-action-services/overview) | [Governance Action Services Catalog](/connectors/#governance-action-services) |
| Archive Service               | Maintains open metadata archives based in the content of the open metadata repositories. | [Building Archive Services](/guides/developer/archive-services/overview) | [Archive Service Catalog](/connectors/#archive-services) |
| Configuration Document Store  | Persists the [configuration document](/concepts/configuration-document/#storage) for an OMAG Server. | [Building Configuration Document Store Connectors](/guides/developer/runtime-connectors/configuration-document-store-connector) | [Configuration Document Store Catalog](/connectors/#configuration-document-store-connectors) |
| Platform Security Connector   | Manages [service authorization](/features/metadata-security) for the OMAG Server Platform. | [Building Platform Metadata Security Connectors](/guides/developer/runtime-connectors/) | [Platform Metadata Security Connector Catalog](/connectors/#platform-metadata-security-connectors) |
| Server Security Connector     | Manages [service and metadata instance authorization](/features/metadata-security) for an OMAG Server. | [Building Server Metadata Security Connectors](/guides/developer/runtime-connectors/server-metadata-security-connector) | [Server Metadata Security Connector Catalog](/connectors/#server-metadata-security-connectors) |
| Open Metadata Archive Store   | Reads an open metadata archive from a particular type of store. | [OMRS Open Metadata Archive Store Connector](/concepts/open-metadata-archive-store-connector) | [open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh } |
| Audit Log Store               | Audit logging destination | [OMRS Audit Log Store Connector](/concepts/audit-log-store-connector) | [audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } |
| Cohort Registry Store         | Local store of membership of an [open metadata repository cohort](/concepts/cohort-member). | [Building Cohort Registry Store Connectors](/guides/developer/runtime-connectors/cohort-registry-store-connector) | [cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh } |
| Open Metadata Topic Connector | Sends and received events on a topic hosted by an external [event bus](/concepts/event-bus) such as Apache Kafka. | [Building Open Metadata Topic Connectors](/concepts/open-metadata-topic-connector) | [open-metadata- topic-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors){ target=gh } |
| Metadata Collection (repository) Store | Interfaces with a metadata repository API for retrieving and storing metadata. | [OMRS Repository Connectors](/concepts/repository-connector)| [open-metadata-collection-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } |
| Metadata Collection (repository) Event Mapper | Maps events from a third party metadata repository to open metadata events. | [OMRS Event Mappers](/concepts/event-mapper-connector) | none |



## Virtual connectors

OCF connectors are not limited to representing Assets as they are physically implemented. An OCF connector can represent a simplified logical (virtual) asset, such as a data set, that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources.  It is called a *virtual connector* and us created using a [*virtual connection*](/concepts/connection/#virtual-connections).

!!! education "Further information"

    The [connector catalog](/connectors) describes the connectors that are pre-built for the Egeria ecosystem.

    The [Egeria Developer Guide](/guides/developer/#building-connectors) describes how to write your own connectors.

--8<-- "snippets/abbr.md"




