<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# OMAG Server Platform

The OMAG Server Platform provides a runtime process and platform for
Open Metadata and Governance (OMAG) Services.

The OMAG services are configured and activated in [OMAG servers](omag-server.md) using the
[administration services](../index.md).
The configuration operations of the admin services create
[configuration documents](configuration-document.md), one for each OMAG server.
Inside a configuration document is the definition of which OMAG services to activate in the server.
These include the [repository services](../../../services/omrs) (any type of server),
the [access services](../../../services/omas.md) (for metadata access points
and metadata servers), [governance services](../../../services/governance.md) (for governance servers) and
[view services](../../../services/view.md) (for view servers).

Once a configuration document is defined, the OMAG Server can be started and stopped multiple times by
the admin services server instance operations.

The OMAG Server Platform also supports some [platform services](../../../platform-services)
to query details of the servers running on the platform.

The OMAG Server Platform can also host multiple OMAG servers at any one time:

![OMAG server deployment choices](egeria-operations-server-choices-no-description.png)

The choices are as follows:

- **A** - Each OMAG server has its own dedicated OMAG Server Platform - useful when only one server is needed
  in a deployment environment, or there is a desire to keep each server isolated in its own stack.
- **B** - Multiple OMAG servers are hosted on the same OMAG Server Platform. The OMAG Server Platform routes
  inbound requests to the right server based on the server name specified in the request URL.
  The servers may all be of the same type (multi-tenant operation) or be a set of collaborating servers
  of different types consolidated onto the same platform.
- **C** - Multiple copies of same server instance running on different platforms to provide
  high availability and distribution of workload (horizontal scalability).

Each OMAG server is isolated within the server platform and so the OMAG server platform can be used to 
support [multi-tenant :material-dock-window:](https://en.wikipedia.org/wiki/Multitenancy){ target=wikipedia }
operation for a cloud service,
or host a variety of different OMAG servers needed at a particular location.

??? education "Further reading"
    - [Configuring the OMAG Server Platform](../user/configuring-the-omag-server-platform.md)
    - [Overview of the OMAG Server Platform](../../../../open-metadata-publication/website/omag-server)
    - [Installing the OMAG Server Platform Tutorial](../../../../open-metadata-resources/open-metadata-tutorials/building-egeria-tutorial/task-installing-egeria.md)
    - [Running the OMAG Server Platform Tutorial](../../../../open-metadata-resources/open-metadata-tutorials/omag-server-tutorial)

--8<-- "snippets/abbr.md"
