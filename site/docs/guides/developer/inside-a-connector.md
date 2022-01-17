<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->



[Connectors](/egeria-docs/concepts/connector) are plug-in Java clients that either perform an additional service, or, more typically, enable Egeria to integrate with a third party technology.

The concept of a connector comes from the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview). The OCF provides a common framework for components that enable one technology to call another, arbitrary technology through a common interface. The implementation of the connector is dynamically loaded based on the connector's configuration.

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

### Lifecycle of the connector

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


--8<-- "snippets/abbr.md"
