<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

The purpose of the connector provider is to provide information on how to configure, and initialize a particular connector.  It is the factory class used to construct an instance of the connector at runtime using a [connection object](/concepts/connection) constructed as follows:

![Connection object structure](/concepts/connection.svg)
> The connection object contains properties needed by the connection object to operate.  It includes a connector type object that is used when constructing the connector and an endpoint object that defines where the corresponding [digital resource](/concepts/digital-resource) is located.




However it also provides information to
It returns the [ConnectorType](/concepts/connector-type) object for the connector.  The connector type describes the capabilities of the connector such as:

  - the java class of this connector provider. A connector provider is the factory for its [Connector](/concepts/connector).  It is typically called from the [Connector Broker](/concepts/connector-broker).  The connector broker uses the `connectorProviderClassName` in the connector type to create an instance of the connector provider. 
  
  - the `configurationProperties` that can be added to the connector's connection object to adapt its behavior.  The administrator who is configuring the connector used the `recognizedConfigurationProperties` from the connector type to determine the properties 

The connector type is included 

If the connector provider implements 

Return a new instance of the connector based on the properties in a supplied [Connection](/concepts/connection) object.  The Connection object that has all of the properties needed to create and configure the instance of the connector.  This includes the connector type described above.


--8<-- "snippets/abbr.md"
