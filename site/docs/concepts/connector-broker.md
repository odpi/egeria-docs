---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connector Broker

The *Connector Broker* is the factory class for all [open connectors](/concepts/connector).  Given a valid [Connection](/concepts/connection) object, the Connector Broker is able to create a new instance of a connector.  This means the caller does not need to know the implementation details of the connector - just its interface.

It is implemented in the following Java class:

```
org.odpi.openmetadata.frameworks.connectors.ConnectorBroker
```

and is used as follows:

```
import org.odpi.openmetadata.frameworks.connectors.Connector;
import org.odpi.openmetadata.frameworks.connectors.ConnectorBroker;

   :
   
ConnectorBroker   connectorBroker     = new ConnectorBroker();
Connector         connector           = connectorBroker.getConnector(connection);
```

When the connector instance is requested, the Connector Broker uses the ConnectorType properties from the supplied Connection to identify the appropriate [Connector Provider](connector-provider.md).  The Connector Broker delegates the connector instance request to the Connector Provider and returns the result to its caller.

## Use of the Connector Broker in Egeria

The Connector Broker is used in the handlers that provide connector instances to their consumers.  Examples include:

* [Runtime Manager OMVS](/services/omvs/runtime-manager/overview)
* [Survey Action OMES](/services/omes/survey-action/overview)


---8<-- "snippets/abbr.md"