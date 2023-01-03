<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

The purpose of the connector provider is to provide information on how to configure, and initialize a particular connector implementation.  It is both an information component describing the properties of the connector during set up, and also the factory class used to create an instance of the connector at runtime.

### The ConnectorProvider interface

All connector providers implement the [`ConnectorProvider`](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/connectors/ConnectorProvider.html) interface.  This interface includes the `getConnectorType()` method that returns the [`ConnectorType`](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/connectors/properties/beans/ConnectorType.html) that is added to a [Connection object](/concepts/connection) used to create an instance of the connector.

![Connection object structure](/concepts/connection.svg)
> The connection object contains properties needed by the connection object to operate.  It includes a connector type object that is used when constructing the connector and an endpoint object that defines where the corresponding [digital resource](/concepts/digital-resource) is located.

The connector type describes the capabilities of the connector such as:

- the java class of this connector provider. A connector provider is the factory for its [Connector](/concepts/connector).  It is typically called from the [Connector Broker](/concepts/connector-broker).  The connector broker uses the `connectorProviderClassName` in the connector type to create an instance of the connector provider.

- the `configurationProperties` that can be added to the connector's connection object to adapt its behavior.  The administrator who is configuring the connector used the `recognizedConfigurationProperties` from the connector type to determine the properties

The `ConnectorProvider` interface also defines the `getConnector()` method called to construct an instance of the connector at runtime using the connection object.

### Audit Logging

If the connector provider implements the [`AuditLoggingComponent`](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/auditlog/AuditLoggingComponent.html) interface, it is passed an [audit log object](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/auditlog/AuditLog.html) used to create child audit log objects that are passed to each connector instance when it is created.

The connector provider is also able to return the [`ComponentDescription`](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/auditlog/ComponentDescription.html) object used in each child audit log.

### ConnectorProviderBase class

Egeria provides a base class for the connector provider called [`ConnectorProviderBase`](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/connectors/ConnectorProviderBase.html) that implements the factory classes for a connector.  It also stores all the properties needed by the information methods such as `getConnectorType()`.  Most connector provider implementations use this base class and only need to pass appropriate values to initialize the properties for the information methods.

--8<-- "snippets/abbr.md"
