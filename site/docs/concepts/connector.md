---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connector

A connector is a client library for accessing a [digital resource](/concepts/digital-resource) and, optionally, its associated [asset](/concepts/asset) metadata.

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



| Type of Connector                             | Description                                                                                                                                                                | Documentation                                                           | 
|:----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| Digital Resource Connector                    | Wraps the standard API of a technology into a connector so it can be called in a standard way by other connectors, Egeria's runtimes, and applications.                    | [Further Information](/concepts/digital-resource-connector)             | 
| Integration Connector                         | Implements metadata exchange with third party tools.                                                                                                                       | [Further Information](/concepts/integration-connector)                  |
| Survey Action Service                         | Implements automated metadata discovery.                                                                                                                                   | [Further Information](/concepts/survey-action-service)                  |
| Governance Action Service                     | Implements automated governance.                                                                                                                                           | [Further Information](/concepts/governance-action-service)              | 
| Event Action Service                          | Implements the maintenance of [context events](/conepts/context-event).                                                                                                    | [Further Information](/concepts/event-action-service)                   | 
| Repository Governance Service                 | Maintains information about the status and content of the open metadata repositories.                                                                                      | [Further Information](/concepts/repository-governance-service)          | 
| Configuration Document Store                  | Persists the [configuration document](/concepts/configuration-document/#storage) for an OMAG Server.                                                                       | [Further Information](/concepts/configuration-document-store-connector) |
| Platform Security Connector                   | Manages [service authorization](/features/metadata-security) for the OMAG Server Platform.                                                                                 | [Further Information](/concepts/platform-metadata-security-connectors/) |
| Server Security Connector                     | Manages [service and metadata instance authorization](/features/metadata-security) for an OMAG Server.                                                                     | [Further Information](/concepts/server-metadata-security-connector)     |
| Open Metadata Archive Store                   | Reads an open metadata archive from a particular type of store.                                                                                                            | [Further Information](/concepts/open-metadata-archive-store-connector)  |
| Audit Log Store                               | Audit logging destination                                                                                                                                                  | [Further Information](/concepts/audit-log-store-connector)              |
| Cohort Registry Store                         | Local store of membership of an [open metadata repository cohort](/concepts/cohort-member).                                                                                | [Further Information](/concepts/cohort-registry-store-connector)        |
| Open Metadata Topic Connector                 | Sends and received events on a topic hosted by an external [event bus](/concepts/event-bus) such as Apache Kafka.                                                          | [Further Information](/concepts/open-metadata-topic-connector)          |
| Metadata Collection (repository) Store        | Interfaces with a metadata repository API for retrieving and storing metadata.                                                                                             | [Further Information](/concepts/repository-connector)                   |
| Metadata Collection (repository) Event Mapper | Maps events from a third party metadata repository to open metadata events.                                                                                                | [Further Information](/concepts/event-mapper-connector)                 |



## Virtual connectors

OCF connectors are not limited to representing Assets as they are physically implemented. An OCF connector can represent a simplified logical (virtual) asset, such as a data set, that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources.  It is called a *virtual connector* and us created using a [*virtual connection*](/concepts/connection/#virtual-connections).

!!! education "Further information"

    The [connector catalog](/connectors) describes the connectors that are pre-built for the Egeria ecosystem.

    The [Egeria Developer Guide](/guides/developer/#building-connectors) describes how to write your own connectors.

--8<-- "snippets/abbr.md"




