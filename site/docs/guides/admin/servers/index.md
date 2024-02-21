<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring an OMAG Server

An [OMAG Server](/concepts/omag-server) is a configured set of services and connectors that support the integration of a particular type of technology.  This configuration is located in a [configuration document](/concepts/configuration-document) that is stored in the [configuration document store](/concepts/configuration-document-store-connector).

The configuration document is divided into sections.  Each section described the configuration of a particular [OMAG Subsystem](/concepts/omag-subsystem).
The configuration document for a specific OMAG Server determines which OMAG subsystems (and hence the types of services) should be activated in the OMAG Server.

There are [different types of OMAG Server](/concepts/omag-server#types-of-omag-server) each with a specific purpose.  They then may call to one another once they are running.  The server types define the combination of subsystems that need to be active to perform a particular role in the open metadata ecosystem. This means, the configuration document for each type of server, will have different sections filled out.   

![Configuration Document Sections](configuration-document-structure-simplified.svg)

Many of the configuration values are [connections](/concepts/connection) to allow the server to create the [connectors](/concepts/connectors) to the [digital resources](/concepts/digital-resource) it needs.

These connectors enable Egeria to run in different deployment environments and to connect to different third party technologies.

![Connector types supported by the OMAG Servers](omag-server-connector-types.svg)

## Retrieving the configuration document

It is possible to retrieve whole configuration document for a server either as a single structure, or by section.  This first command retrieves the whole configuration document.

--8<-- "snippets/admin/calls/get-stored-configuration.md"

This next command retrieves the basic server properties.

--8<-- "snippets/admin/calls/get-basic-server-properties.md"


!!! get "GET - retrieve the origin of the server"
    It is also possible to query the origin of the server supporting the open metadata services.
    For the Egeria OMAG Server Platform, the response is `Egeria OMAG Server Platform (version {{releaseName}})`.

    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/servers/{{serverName}}/server-platform-origin
    ```


--8<-- "snippets/abbr.md"
