<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Developer Guide

Egeria is designed to simplify the effort necessary to integrate different technologies so that they can actively share and consume metadata from each other.

It focuses on providing five types of integration interfaces.

- [Connectors](#what-is-a-connector) that translate between third party APIs and open metadata APIs. These connectors are hosted in the Egeria servers and support the active exchange of metadata with these technologies.
- [Connectors](/egeria-docs/guides/developer/using-connectors) for accessing popular type of data sources that also retrieve open metadata about the data source. This allows applications and tools to understand the structure, meaning, profile, quality and lineage of the data they are using.
- [Java clients](#using-the-clients) for applications to call the [Open Metadata Access Service (OMAS)](/egeria-docs/services/omas) interfaces, each of which are crafted for particular types of technology. These interfaces support both synchronous APIs, inbound event notifications and outbound asynchronous events.
- [REST APIs](#using-the-rest-apis) for the Egeria Services. These include the [access services](/egeria-docs/services/omas), admin services and [platform services](/egeria-docs/services/platform).
- Kafka topics with JSON payloads for asynchronous communication (both in and out) with the open metadata ecosystem.
  [Learn more ...](/egeria-docs/services/omas)

## Using the clients

The Egeria clients wrap calls to Egeria's [REST APIs](#using-the-rest-apis) and topics. The aim is to provide a language-specific interface that manages the marshalling and de-marshalling of the call parameters and responses to these services.

## Using the REST APIs

Egeria supports REST [APIs](/egeria-docs/basic-concepts/#application-programming-interface-api) for making synchronous (request-response) calls between [OMAG Servers](/egeria-docs/concepts/omag-server) and between clients and OMAG Servers.

!!! attention "REST APIs are intended for internal use"
    The REST APIs are usable directly for calling from non-Java platforms; however, they are designed for the internal use of Egeria and are not guaranteed to be backwards compatible.

The structure of the URL for an Egeria REST API varies lightly depending on whether it is a call to an [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform) service or an [OMAG Server](/egeria-docs/concepts/omag-server) service.

## What is a connector?

[Connectors](/egeria-docs/concepts/connector) are plug-in Java clients that either perform an additional service, or, more typically, enable Egeria to integrate with a third party technology.

The concept of a connector comes from the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview). The OCF provides a common framework for components that enable one technology to call another, arbitrary technology through a common interface. The implementation of the connector is dynamically loaded based on the connector's configuration.

Through the OCF, we can:

1. Plug-in different technologies to Egeria.
2. Plug-in support for open metadata into the client libraries used by applications to access data resources and services.

![How OCF connectors are used in Egeria](compare-use-of-connectors.svg)

Many subsystems in Egeria's [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform) and [servers](/egeria-docs/concepts/omag-server) support the first approach. They define a specialized interface for the type of connector they support.

1. One or more connector implementations supporting that interface are then written either by the Egeria community or other organizations.
2. When an Egeria [OMAG Server](/egeria-docs/concepts/omag-server) is configured, details of which connector implementation to use is specified in the server's [configuration document](/egeria-docs/concepts/configuration-document).
3. At start up, the OMAG Server passes the connector configuration to the OCF to instantiate the required connector instance.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the OMAG Servers.

The second approach is used by organizations that want to make use of metadata directly in applications and tools - or to externalize the security and driver properties needed to call the data source or service. In this case the OCF connector typically has the same interface as the data source's client library (unless you can do better :smile:). This minimizes the learning curve for application developers. The configuration for the connector is stored in an open metadata server and the application uses the [Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer) client to [request a new instance of the connector](/egeria-docs/services/omas/asset-consumer/scenarios/working-with-connectors.md). The application uses the returned connector instance to access the data source or server along with the metadata stored about it.

### Configuration

The configuration for a connector is managed in a [*connection*](/egeria-docs/concepts/connection) object.

A connection contains properties about the specific use of the connector, such as user Id and password, or parameters that control the scope or resources that should be made available to the connector. It links to an optional [*endpoint*](/egeria-docs/concepts/endpoint) and a mandatory [*connector type*](/egeria-docs/concepts/connector-type) object.

- `ConnectorType` describes the type of the connector, its supported configuration properties and its factory object (called the [connector's provider](/egeria-docs/concepts/connector-provider)). This information is used to create an instance of the connector at runtime.
- `Endpoint` describes the server endpoint where the third party data source or service is accessed from.

Connector types and endpoints can be reused in multiple connections.

![Structure of a connection object](/egeria-docs/concepts/connection.svg)

### Factories

Each connector implementation has a factory object called a [*connector provider*](/egeria-docs/concepts/connector-provider). The connector provider has two types of methods:

- Return a new instance of the connector based on the properties in a supplied `Connection` object. The `Connection` object has all the properties needed to create and configure the instance of the connector.
- Return additional information about the connector's behavior and usage to make it easier to consume. For example, the standard base class for a connector provider has a method to return the `ConnectorType` object for this connector implementation that can be added to a `Connection` object used to hold the properties needed to create an instance of the connector.

### Inside the connector

Each connector has its own unique implementation that is structured around a simple lifecycle that is defined by the OCF. The OCF provides the interface for a connector called [`Connector` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/Connector.java){ target=gh } that has three methods: `initialize`, `start` and `disconnect`.

This connector interface supports the basic lifecycle of a connector. There are three phases:

1. *Initialization* - During this phase, the connector is passed the context in which it is to operate. It should store this information.

    This phase is initiated by a call to the connector's `initialize()` method, which is called after the connector's constructor and provides the connector with a unique instance identifier (for logging) and its configuration stored in a [connection](/egeria-docs/concepts/connection). After `initialize()` returns, there may be other calls to pass context to the connector. For example, if the connector implements the [`AuditLoggingComponent` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/audit-log-framework/src/main/java/org/odpi/openmetadata/frameworks/auditlog/AuditLoggingComponent.java){ target=gh }, an [audit log](/egeria-docs/frameworks/alf/overview) is passed to the connector.

2. *Running* - The connector is completely initialized with its context, and it can start processing.

    This phase is initiated by a call to the connector's `start()` method. At this point it should create its client to any third party technology and begin processing. It may also start up threads if it needs to perform any background processing (such as listening for notifications). If the connector throws an exception during start, Egeria knows the connector has a configuration or operational issue and will report the error and move it to disconnected state.

3. *Disconnected* - The connector must stop processing and release all of its resources.

    This phase is initiated by a call to the connector's `disconnect()` method.

Depending on the type of connector you are writing, there may be additional initialization calls occurring between the `initialize()` and the `start()` method. The connector may also support additional methods for its normal operation that can be called between the `start()` and `disconnect()` calls.

The OCF also provides the base class for a connector called [`ConnectorBase` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorBase.java){ target=gh }. The `ConnectorBase` base class manages the lifecycle state of the connector. For example, the default implementation of `initialize()` in the `ConnectorBase` class stores the supplied unique instance identifier and connection values in protected variables called `connectorInstanceId` and `connectionProperties` respectively.

!!! tip "Call the base class's methods in any overrides"
    If you override any of the  `initialize()`, `start()` or `disconnect()` methods, be sure to call `super.xxx()` at the start of your implementation to call the appropriate super class method so that the state is properly maintained.

## Extending Egeria using connectors

Egeria has extended the basic concept of the OCF connector and created specialized connectors for different purposes. The following types of connectors are supported by the Egeria subsystems with links to the documentation and implementation examples.

| Type of Connector             | Description | Documentation | Implementation Examples |
| :-----------------------------| :---------- | :------------ | :---------------------- |
| Integration Connector         | Implements metadata exchange with third party tools. | [Building Integration Connectors](../../../open-metadata-implementation/governance-servers/integration-daemon-services/docs/integration-connector.md) | [integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors){ target=gh } |
| Open Discovery Service        | Implements automated metadata discovery.| [Open Discovery Services](/egeria-docs/frameworks/odf/#discovery-service) | [discovery-service-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/discovery-service-connectors){ target=gh } |
| Governance Action Service     | Implements automated governance. | [Governance Action Services](/egeria-docs/frameworks/gaf/#governance-action-service) | [governance-action-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-action-connectors){ target=gh } |
| Configuration Document Store  | Persists the configuration document for an OMAG Server. | [Configuration Document Store Connectors](/egeria-docs/concepts/configuration-document/#storage) | [configuration-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/configuration-store-connectors){ target=gh } |
| Platform Security Connector   | Manages service authorization for the OMAG Server Platform. | [Metadata Security Connectors](/egeria-docs/features/metadata-security) | [open-metadata-security-samples :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } |
| Server Security Connector     | Manages service and metadata instance authorization for an OMAG Server. | [Metadata Security Connectors](/egeria-docs/features/metadata-security) | [open-metadata-security-samples :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } |
| Metadata Collection (repository) Store | Interfaces with a metadata repository API for retrieving and storing metadata. | [OMRS Repository Connectors](/egeria-docs/concepts/repository-connector)| [open-metadata-collection-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } |
| Metadata Collection (repository) Event Mapper | Maps events from a third party metadata repository to open metadata events. | [OMRS Event Mappers](/egeria-docs/concepts/event-mapper-connector) | none |
| Open Metadata Archive Store   | Reads an open metadata archive from a particular type of store. | [OMRS Open Metadata Archive Store Connector](/egeria-docs/concepts/open-metadata-archive-store-connector) | [open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh } |
| Audit Log Store               | Audit logging destination | [OMRS Audit Log Store Connector](/egeria-docs/concepts/audit-log-store-connector) | [audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } |
| Cohort Registry Store         | Local store of membership of an open metadata repository cohort. | [OMRS Cohort Registry Store](/egeria-docs/concepts/cohort-registry-store-connector) | [cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh } |
| Open Metadata Topic Connector | Connects to a topic on an external event bus such as Apache Kafka. | [Open Metadata Topic Connectors](/egeria-docs/concepts/open-metadata-topic-connector) | [open-metadata- topic-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors){ target=gh } |

You can write your own connectors to integrate additional types of technology or extend the capabilities of Egeria - and if you think your connector is more generally useful, you could consider [contributing it to the Egeria project](/egeria-docs/guides/community).

--8<-- "snippets/abbr.md"
