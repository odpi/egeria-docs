<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connection

The **connection** provides the set of properties needed to create and initialize an instance
of a [connector](connector.md), and is part of the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf).

A connection contains properties about the specific use of the connector, such as
user Id and password, or parameters that control the scope or resources that should be
made available to the connector.

It links to an optional:

- [Connector type](connector-type.md) - this is an object that describes the type of the connector that needs to be
  created in order to access the Asset.
- [Endpoint](endpoint.md) - this is the object that describes the server endpoint where the asset is accessed from.

Connector types and endpoints can be reused in multiple connections.

![Connection structure](connection.png)

Connections are typically managed in a metadata repository, but they can also be manually populated.

## Connection implementations

The OCF offers two implementations of the connection:

- [`Connection` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/beans/Connection.java){ target=gh } -
  is a bean implementation of the connection used in REST API requests and events. It allows properties
  to be set up and retrieved.
- [`ConnectionProperties` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/ConnectionProperties.java){ target=gh } -
  is a read-only wrapper for the connection properties that is used in client interfaces that do not allow the
  properties to be updated.

## Connection properties

The properties for a connection are defined in [model 0201](/egeria-docs/types/2) and include:

| Property | Description |
|---|---|
| `guid` | GUID for the connection. |
| `url` | URL of the connection definition in the metadata repository. |
| `qualifiedName` | The official (unique) name for the connection. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. (Sourced from the `qualifiedName` attribute in `Referenceable` - [model 0010](/egeria-docs/types/0/0010-base-model))
| `displayName` | A consumable name for the connection. Often a shortened form of the qualifiedName for use on user interfaces and messages. The displayName should be only be used for audit logs and error messages if the qualifiedName is not set. |
| `type` | Information about the TypeDef for the connection. |
| `description` | A full description of the connection covering details of the assets it connects to along with usage and version information. |
| `additionalProperties` | Any additional properties associated with the connection. |
| `configurationProperties` | Properties for configuring the connector. |
| `securedProperties` | Protected properties for secure log on by connector to back end server. These are protected properties that can only be retrieved by privileged connector code. |
| `userId` | Name or URI of connecting user. |
| `encryptedPassword` | Password for the userId - needs decrypting by connector before use. |
| `clearPassword` | Password for userId - ready to use. |
| [`connectorType`](connector-type.md) | Properties that describe the connector type for the connector. |
| [`endpoint`](endpoint.md) | Properties that describe the server endpoint where the connector will retrieve the assets. |

## Using Connections from open metadata repositories

Each connection stored in a metadata repository has a unique identifier.
An application can request a connector instance through selected Egeria OMAS interfaces, such
as the [Asset Consumer OMAS](/egeria-docs/services/omas/asset-consumer), with just the unique identifier or name
of a connection.  

The OMAS retrieves the connection object from the open metadata repositories and passes it to the [connector broker](connector-broker.md)
factory object. The connector broker (and underlying [connector provider](connector-provider.md)) uses the information from the connection object
to create an instance of the connector.

The advantage of retrieving the connection information from a metadata repository is that the connection properties
do not need to be hard-coded in the consuming applications and the metadata associated with the linked asset
can be retrieved via the connector's [connected asset properties](connected-asset-properties.md) interface.

Connections can be created in the open metadata repositories through the following interfaces:

- [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner)
- [Asset Manager OMAS](/egeria-docs/services/omas/asset-manager)
- [Data Manager OMAS](/egeria-docs/services/omas/data-manager)
- [Database Integrator OMIS](/egeria-docs/services/omis/database-integrator)
- [Files Integrator OMIS](/egeria-docs/services/omis/files-integrator)
- [Governance Action OMES](/egeria-docs/services/omes/governance-action)
 
## Configuring connections

The [administration guide](/egeria-docs/guides/admin) describes how to configure Egeria's
OMAG Server Platforms and servers. Both the platform and the servers use connectors for access to the
external resources to support their basic operation and to coordinate metadata and governance with
third party technologies. This means that the configuration includes connection definitions for these connectors.

All of these interfaces have Java clients that enable you to set up the connection using the OCF connection bean.
However, if you want to use the REST API directly, then you need to specify the connection in JSON.

!!! example "Example connection definition in JSON"
    Egeria's JSON structures map one-to-ene with the properties in the equivalent Java beans and also include
    a `class` property that gives the name of the class that it maps to. So a simple connection object
    would look something like this in JSON:

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
