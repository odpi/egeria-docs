<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Administration guide

The Egeria technology principally runs on the [Open Metadata and Governance (OMAG) Server Platform](/egeria-docs/concepts/omag-server-platform).
This platform hosts one or more [OMAG servers](/egeria-docs/concepts/omag-server),
each supporting a variety of open metadata and governance capabilities.

![OMAG Server Platforms running in different cloud platforms or data centers, each hosting OMAG Servers that are providing specialist integration capability for different tools](/egeria-docs/introduction/egeria-distributed-operation.svg)

In the illustration above, the OMAG Server Platforms are the blue, rounded boxes
and the orange circles are the OMAG Servers. The green clouds represent different cloud
platforms or data centers.

This guide explains how to configure the OMAG Server Platform
and the different types of OMAG Servers that run on it.

!!! tip "TL;DR"
    If you are keen to get started right away then these are the links
    to the configuration instructions.

    - [Configuring the OMAG Server Platform](configuring-the-omag-server-platform.md)
    - [Configuring an OMAG Server to run on an OMAG Server Platform](configuring-an-omag-server.md)
    - [Configuring the Presentation Server (for UIs)](configuring-the-presentation-server.md)

    and once you have your OMAG Servers configured:

    - [Operating an OMAG Server](operating-omag-server.md)

## OMAG subsystems

An [OMAG server](/egeria-docs/concepts/omag-server) is a set of configured [OMAG subsystems](/egeria-docs/concepts/omag-subsystem)
supported by the [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform).
Each subsystem supports a particular type of technology, so it can exchange metadata with the
open metadata ecosystem. Some technologies are sources of metadata, others just consume metadata
and then there are technologies that have a two-way exchange of metadata with the open metadata ecosystem.

The OMAG subsystems that are to be enabled in a specific instance of an OMAG server
are defined in a [configuration document](/egeria-docs/concepts/configuration-document).
When the configuration document is loaded into the OMAG Server Platform, the OMAG server that it describes
is started, and the subsystems defined in the configuration document are activated for that server.

## OMAG servers

In an open metadata landscape, there may be multiple
instances of [OMAG servers](/egeria-docs/concepts/omag-server) running in an [OMAG Server Platform](/egeria-docs/concepts/omag-server-platform),
each performing a different role.
Each of these server instances would have their own configuration document allowing them
to have different subsystems active.

## Configuring an OMAG server

The configuration document for a specific OMAG server is identified by the server's name.
This is passed on the URL of every admin services API request along with the user
id of the administrator. By default, the configuration is stored in a file called:

```
omag.server.{serverName}.config
```

The administration services that set up this file all begin with a URL like this:

```
.../open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/...
```

The `serverName` specified on these calls determines which configuration
document is used, and hence which OMAG server's configuration it is working with.

The OMAG Server Platform typically starts up without any OMAG servers active.
Once it is running, it can be used to set up the configuration documents
that describe the open metadata subsystems needed for each OMAG server instance.

Once the configuration document is in place, the OMAG server
can be activated and deactivated multiple times, across multiple
restarts of the OMAG Server Platform.

??? education "Further information"
    - [Configuring the OMAG Server Platform](configuring-the-omag-server-platform.md)
    - [Configuring an OMAG Server](configuring-an-omag-server.md)
    - [Operating the OMAG Server](operating-omag-server.md)
    - [Migrating OMAG Server Configuration Documents](migrating-configuration-documents.md)

## Examples of configuration calls

The admin-services modules has three [Postman :material-github:](https://github.com/odpi/egeria/blob/master/developer-resources/tools/Postman.md){ target=gh }
collections to illustrate many of the configuration and operation calls:

- [Egeria-admin-services-platform-configuration.postman_environment.json :material-github:](https://raw.githubusercontent.com/odpi/egeria/master/open-metadata-implementation/admin-services/Egeria-admin-services-platform-configuration.postman_collection.json){ target=gh } -
  setting up and configuring the OMAG Server Platform.
- [Egeria-admin-services-server-configuration.postman_environment.json :material-github:](https://raw.githubusercontent.com/odpi/egeria/master/open-metadata-implementation/admin-services/Egeria-admin-services-server-configuration.postman_collection.json){ target=gh } -
  setting up and configuring the variety of OMAG Servers.
- [Egeria-admin-services-operational.postman_environment.json :material-github:](https://raw.githubusercontent.com/odpi/egeria/master/open-metadata-implementation/admin-services/Egeria-admin-services-operational.postman_collection.json){ target=gh } -
  operating the OMAG Servers.

--8<-- "snippets/abbr.md"
