<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connection

The **Connection** provides the set of properties needed to create and initialize an instance
of a [connector](/concepts/connector).

## Inside a Connection

A Connection contains properties about the specific use of the connector, such as
user id and password, or parameters that control the scope or resources that should be
made available to the connector.
It links to an optional **Endpoint** and/or **ConnectorType** object.  

* **ConnectorType** - this is an object that describes the type of the connector that needs to be created in order to
access the Asset.
* **Endpoint** - this is the object that describes the server endpoint where the asset is accessed from.

Figure 1 shows the structure of a connection. Connector types and endpoints can be reused in multiple connections.

![Figure 1](/concepts/connection.svg)
> **Figure 1:** Connection structure

Connections are typically managed in a metadata repository, but they can also be manually populated.

## Virtual connections

A virtual connection is a connection that provides a hierarchy of connection objects.  It is used to create [virtual connectors](connector.md).  When a virtual connection is used to create a connector, the connector broker looks to see if the resulting connector implements the `VirtualConnectorExtension` interface.  If the connector does implement this interface, the connector broker creates connectors for each of the connections nested in the virtual connection. The resulting connectors are then passed to the virtual connector through the `initializeEmbeddedConnectors` method.

Figure 2 shows an example of a virtual connection with two nested connections (see `EmbeddedConnections`).  One of these connections is also a virtual connection and will be processed in the same way as its parent.

![Figure 2](/concepts/virtual-connection.svg)
> **Figure 2:** Example virtual connection structure

The [open metadata topic connector](/concepts/open-metadata-topic-connector) is an example of a connector that is designed to be nested inside a virtual connector.

## Connection implementations

The OCF offers two implementations of the Connection.

```
org.odpi.openmetadata.frameworks.connectors.properties.beans.Connection
```

Connection is a bean implementation of the connection used in REST API requests and events.  It allows properties for be set up and retrieved.

```
org.odpi.openmetadata.frameworks.connectors.properties.ConnectionProperties
```

ConnectionProperties is a read-only wrapper for the Connection properties that is used in client interfaces that do not allow the properties to be updated.

## Connection properties

The properties for a connection are defined in model 0201.  They include the following identifiers:

 * **guid** - Globally unique identifier for the connection.
 * **url** - URL of the connection definition in the metadata repository.
 * **qualifiedName** - The official (unique) name for the connection.  This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages.  The qualifiedName is defined in the 0010 model as part of Referenceable.
 * **displayName** - A consumable name for the connection.   Often a shortened form of the qualifiedName for use on user interfaces and messages.  The displayName should be only be used for audit logs and error messages if the qualifiedName is not set.

Other properties for the connection include:

* **type** - information about the TypeDef for Connection
* **description** - A full description of the connection covering details of the assets it connects to along with usage and version information.
* **additionalProperties** - Any additional properties associated with the connection.
* **configurationProperties** - properties for configuring the connector.
* **securedProperties** - Protected properties for secure log on by connector to back end server.  These are protected properties that can only be retrieved by privileged connector code.
* **userId** - name or URI or connecting user.
* **encryptedPassword** - password for the userId - needs decrypting by connector before use.
* **clearPassword** - password for userId - ready to use.
* **[connectorType](/concepts/connector-type)** - Properties that describe the connector type for the connector.
* **[endpoint](/concepts/endpoint)** - Properties that describe the server endpoint where the connector will retrieve the assets.


## Using Connections from open metadata repositories

Each connection stored in a metadata repository has a unique identifier. An application can request a connector instance through selected Egeria OMAS interfaces, such as the [Asset Consumer OMAS](/services/omas/asset-consumer/overview), with just the unique identifier or name of a connection.  

The OMAS retrieves the connection object from the open metadata repositories and passes it to the [Connector Broker](/concepts/connector-broker) factory object.  The Connector Broker (and underlying [Connector Provider](/concepts/connector-provider)) uses the information from the Connection object to create an instance of the connector.

The advantage of retrieving the connection information from a metadata repository is that the connection properties do not need to be hard-coded in the consuming applications and the metadata associated with the linked Asset can be retrieved via the connectors [Connected Asset Properties](../../../saved/frameworks/connected-asset-properties.md) interface.

Connections can be created in the open metadata repositories through the following interfaces:

* [Asset Owner OMAS](/services/omas/asset-owner/overview)
* [Asset Manager OMAS](/services/omas/asset-manager/overview)
* [Data Manager OMAS](/services/omas/data-manager/overview)
* [Database Integrator OMIS](/services/omis/database-integrator/overview)
* [Files Integrator OMIS](/services/omis/files-integrator/overview)
* [Governance Action OMES](/services/omes/governance-action/overview)
 

## Configuring Egeria Connections

The [Administration Guide](/guides/admin) describes how to configure Egeria's OMAG Server Platforms and Servers.  Both the platform and the servers used connectors for access to the external resources to support their basic operation and to coordinate metadata and governance with third party technologies.  This means that the configuration includes Connection definitions for these connectors.

All of these interfaces have Java clients that enable you to set up the connection using the OCF Connection bean. However, if you want to use the REST API directly, then you need to specify the connection in JSON.

Egeria's JSON structures map one-to-ene with the properties in the equivalent Java beans and also include a `class` property that includes the name of the class that it maps to.  So a simple Connection object would look something like this in JSON:

```json
{
  "connection" : 
  {
    "class" : "Connection",
    "connectorType" : 
    {
      "class" : "ConnectorType",
      "connectorProviderClassName" : "...fully qualified class name..."
    },
    "endpoint" : 
    {
      "class" : "Endpoint",
      "address" : "... network address of resource ..."
    }
  }
}
```
--8<-- "snippets/abbr.md"

