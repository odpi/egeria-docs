<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

A connector provider is the factory for a particular type of [Connector](/concepts/connector).  It is typically called from the [Connector Broker](/concepts/connector-broker), although it may also be called directly.  It has two types of methods:

- Return the [ConnectorType](/concepts/connector-type) object that is added to a [Connection](/concepts/connection) object used to hold the properties needed to create an instance of the connector.  The connector type describes the capabilities of the connector.

- Return a new instance of the connector based on the properties in a supplied [Connection](/concepts/connection) object.  The Connection object that has all of the properties
needed to create and configure the instance of the connector.  This includes the class name of the connector provider.


--8<-- "snippets/abbr.md"
