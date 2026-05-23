<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Connection Maker API

The Connection Maker API is a REST API that enables the caller to maintain and query connections, connector types and endpoints.

### Key Features

* **Connection Management**: Support for creating, retrieving, updating, and deleting connections.
* **Connector Type Management**: Defining and maintaining connector types, including support for templates.
* **Endpoint Management**: Managing endpoints and their association with network addresses.
* **Relationship Management**:
    * Linking connections to connector types and endpoints.
    * Managing embedded connections within other connections.
    * Linking assets to connections to define how to access the asset.
    * Linking endpoints to IT assets to represent where they are deployed.
* **Discovery and Search**: Finding connections, connector types, and endpoints by name, network address, or through search strings.

### Further information

* [Connection Concept](/concepts/connection/)
* [Connector Type Concept](/concepts/connector-type/)
* [Endpoint Concept](/concepts/endpoint/)

----
Sample REST API requests can be found in [Egeria-api-connection-maker.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/connection-maker/Egeria-api-connection-maker.http).
The [Egeria-list-connectors](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/connection-maker/Egeria-list-connectors.http) files shows how to retrieve the list of connectors that are available in an Egeria [platform](/concepts/omag-server-platform).


---8<-- "snippets/abbr.md"






