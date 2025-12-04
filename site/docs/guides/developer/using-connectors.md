<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


[*Connectors*](/concepts/connector) can be created through the [Connection Maker](/services/omvs/asset-maker/overview)


![An asset with a connection](asset-connection.png)



### Connecting to assets with different levels of security

It is possible that an asset can have multiple connections, each with different levels of security access encoded. Egeria is able to determine which one to use by calling the `validateUserForAssetConnectionList()` method of the [Server Security Metadata Connector](/guides/developer/runtime-connectors/server-metadata-security-connector).

![Multiple connections for an asset](multiple-asset-connections.svg)

### Other links to the connection

Open metadata is a connected network (graph) of information. The connector type and endpoint that a connection object links to are typically shared with many connections. This creates some interesting insight.

For example, there is typically one connector type for each connector implementation. By retrieving the relationships from the connector type to the connections, it is possible to see the extent to which the connector is used.

#### Connector types

![Uses of a connector implementation](uses-of-a-connector-implementation.svg)

The connector types for Egeria's data store connectors are available in an open metadata archive called `DataStoreConnectorTypes.json` that can be loaded into the server. This approach can be used for all of your connector implementations to create the connector type objects in our metadata repository. See the [open-connector-archives :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-connector-archives){ target=gh } for more detail.


!!! education "Further information"
    The [connector catalog](/connectors) lists the connectors provided by the Egeria community.


