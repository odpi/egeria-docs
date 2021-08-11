---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connector broker

The **connector broker** is the factory class for all open connectors, and is part of the
[Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf).
Given a valid [connection](connection.md) object, the
connector broker is able to create a new instance of a [connector](connector.md).
This means the caller does not need to know the implementation
details of the connector - just its interface.

It is implemented in the [`ConnectorBroker` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorBroker.java){ target=gh }
class, and is used as follows:

```java
import org.odpi.openmetadata.frameworks.connectors.Connector;
import org.odpi.openmetadata.frameworks.connectors.ConnectorBroker;

   :
   
ConnectorBroker   connectorBroker     = new ConnectorBroker();
Connector         connector           = connectorBroker.getConnector(connection);
```

When the connector instance is requested, the connector broker uses the [ConnectorType](connector-type.md) properties
from the supplied [connection](connection.md) to identify the appropriate [connector provider](connector-provider.md).
The connector broker delegates the connector instance request to the connector provider and returns
the result to its caller.

The connector broker is used in the client code of the [Open Metadata Access Services (OMAS)](/egeria-docs/services/omas)
that provide connector instances to their consumers, for example:

- [Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer)
- [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner)

--8<-- "snippets/abbr.md"
