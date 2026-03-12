<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Server Metadata Security Connector

The *server metadata security connector* provides authorization support for requests to an [OMAG Server](/concepts/omag-server).  There is one server metadata security connector configured for each OMAG Server.

![Server Metadata Security Connector](/server-metadata-security-connector.svg)

This connector is called each time a request is made to the server.  It is called to:

* Validate the user has access to the server.
* Validate the user has access to the called operation.
* Select which zones to associate with the requests based on the user.
* If the request involves an asset, then does the user have access to the asset and which properties are they allowed to see.
* If the request is for a connection for an asset, then select which one linked to the asset should be returned to the user.
* Determine which events to sent to the cohort.
* Determine what actions can be made on the metadata repository.


## Egeria Server Security Connectors

Egeria has a default implementation of the server metadata security connector:

* [Open Metadata Access Security Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors/open-metadata-access-security-connector)

??? education "Further information relating to Metadata Security Connectors"

    * [Metadata security overview](/features/metadata-security/overview) provides the interface for the server metadata security connector and manages the calls to it.
    * [Writing a server metadata security connector](/guides/developer/runtime-connectors/server-metadata-security-connector)
    * [Configuring the server metadata security connector](/guides/admin/servers/by-section/server-security-connection-section) in a server.


--8<-- "snippets/abbr.md"
