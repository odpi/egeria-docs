<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata and Governance (OMAG) Server

An *OMAG server* is a software server that runs inside the [OMAG Server Platform](omag-server-platform.md). It is therefore sometimes referred to as a "logical" server rather than a physical server that runs in its own process. It supports the integration of one or more technologies by hosting connectors that interact with that technology, or providing specialist [APIs](/egeria-docs/basic-concepts/#application-programming-interface-apis) or [event topics](/egeria-docs/basic-concepts/#topic) (both in and out).

Because of the wide variety of technologies deployed in organizations today, each with very different capabilities and needs, the integration and exchange of metadata needs to be organized. This organization is managed through the Egeria frameworks and services supported by the OMAG Servers. There are different types of OMAG Server, each supporting specific technologies. The OMAG Server ensures this type of technology is integrated appropriately for its needs.

The capabilities that are activated in an OMAG Server are defined in its [configuration document](configuration-document.md). When the server is started, the operational services of the OMAG Server Platform reads the configuration document and activates the OMAG Server with the requested services.

## Platform URL root

An OMAG server's *platform URL root* is the network address of the [OMAG Server Platform](omag-server-platform.md) where the OMAG Server is going to run. This is often the host name of the computer or container where the platform runs plus the port number allocated to the OMAG Server Platform.

Its value is needed when creating clients or configuring services that will call the OMAG Server because it provides the root of the URL used to call the server's open metadata and governance REST calls, which have the following format in their URLs:

```text
{{platformURLRoot}}/servers/{{serverName}}/<operation-name-and-parameters>
```

The platform URL root is the content of the URL prior to `/servers/`. The default value an OMAG Server Platform is `https://localhost:9443`.

## Server name

Most APIs in Egeria require both a [platform URL root](#platform-url-root) and a server name. The server name is the name of an OMAG Server where the desired service is running.

## Types of OMAG Server

The types of OMAG Server are shown in Figure 1. The hierarchy groups similar types of server together.

![Figure 1](types-of-omag-servers.png)
> **Figure 1:** Types of OMAG server

??? question "Detailed explanation of diagram"
    The way to understand the diagram is that the arrows should be read as **IS A**.  For example, the *repository proxy **IS A** cohort member* and the *cohort member **IS A** OMAG Server*. This means that everything documented about a particular type of server is also true for all server types that point to it through the **IS A** arrow, all the way down the hierarchy.

    Object-oriented software engineers would know of this type of relationship as behavior inheritance.

- [Cohort member](cohort-member) - able to exchange metadata through an open metadata repository cohort
    - [Metadata server](metadata-server) - supports a metadata repository that can natively store open metadata types as well as specialized metadata APIs for different types of tools (these APIs are called [access services](/egeria-docs/services/omas)).
    - [Metadata access point](metadata-access-point) - supports the access services like the metadata server but does not have a repository. All metadata it serves up and stores belongs to the metadata repositories in other members of the cohort.
    - [Repository proxy](repository-proxy.md) - acts as an open metadata translator for a third party metadata repository. It supports open metadata API calls and translates them to the proprietary APIs of the repository. It also translates events from the proprietary repository into open metadata events that flow over the cohort.
    - [Conformance test server](conformance-test-server) - validates that a member of the cohort is conforming with the open metadata protocols. This server is typically only seen in development and test cohorts rather than production.
- [View server](view-server) - manages specialist services for user interfaces.
- [Governance server](governance-server) - supports the use of metadata in the broader IT landscape.
    - [Engine host](engine-host) - provides a runtime for a specific type of [governance engine](/egeria-docs/services/omes).
    - [Integration daemon](integration-daemon) - manages the synchronization with third party technology that can not call the access services directly.
    - [Data engine proxy](data-engine-proxy) - supports the capture of metadata from a data engine. This includes details of the processing of data that it is doing which is valuable when piecing together lineage.
    - [Open lineage server](open-lineage-server) - Manages the collation of lineage information am maintains it in a format for reporting. This includes the state of the lineage at different points in time.

## Inter-connectivity

The different types of OMAG Servers connect together as illustrated in Figure 2. There is an inner ring of cohort members communicating via the cohort. Each cohort member is sharing the metadata they receive with the governance servers and view servers that connect to it. The governance servers connect out to external tools, engines and platforms.

![Figure 2](omag-server-ecosystem.svg)
> **Figure 2:** The inter-connectivity between OMAG servers

## Inside the OMAG server

The **OMAG server platform** provides the server environment for running open metadata
and governance services.  It hosts one or more **[OMAG servers](omag-server.md)**.  Each server is configured to support specific
open metadata and governance services.  Thus each server performance a specific role in an deployment landscape.

The OMAG server platform is included in the [ODPi Egeria Distribution TAR file](../../../open-metadata-distribution/open-metadata-assemblies)
which can be installed on your machine by following the [Installing ODPi Egeria Tutorial](../../../open-metadata-resources/open-metadata-tutorials/building-egeria-tutorial/task-installing-egeria.md).

The OMAG server platform supports four broad groups of services:

* **Server Origin Service** - used to determine the type and level of the OMAG server platform.
* **Platform Services** - used to determine the servers and their services running on the platform.
* **Administration Services** - used to configure and manage the OMAG servers running inside the OMAG server platform.
* **Open Metadata and Governance Services** - used to work with metadata and govern the assets of an organization.

Figure 1 shows the OMAG server platform when it first starts up.

![Figure 1](omag-server-platform-start-up.svg)
> Figure 1: OMAG server platform at start up

The server origin service  is operational at this point.  It can be used by operational scripts to determine if the 
OMAG server platform is still running.

The administration services are active at this point, while the open metadata and governance services
will return an error if called since there are no [OMAG servers](../../../open-metadata-implementation/admin-services/docs/concepts/logical-omag-server.md) running.

The configuration services are used to create [configuration documents](../../../open-metadata-implementation/admin-services/docs/concepts/configuration-document.md).  Each configuration document
describes the open metadata and governance services that should be activated in a OMAG server.

Figure 2 shows the configuration services creating three configuration documents:
* one for the **cdoMetadataRepository** OMAG server
* one for the **stewardshipServer** OMAG Server
* one for the **dataLakeDiscoveryEngine** OMAG Server

![Figure 2](omag-server-platform-configure.svg)
> Figure 2: Creating configuration documents for OMAG Servers

The [Administration Guide](/egeria-docs/guides/admin/guide)
provides detailed instructions on creating configuration documents.

Once a configuration document for an OMAG server is used by
the operational services initialize the requested services in the OMAG server.
The OMAG server can be started in any OMAG server platform.
It does not have to be the same OMAG server platform that created the configuration document.

Figure 3 shows an OMAG server platform with the **cdoMetadataRepository** local OMAG server
running.

![Figure 3](omag-server-platform-initialize-logical-omag-server.svg)
> Figure 3: Starting a OMAG Server through the operational services

Once the OMAG server has initialized successfully, the open metadata and governance services
can route requests to it.

An OMAG server platform can run multiple OMAG servers at one time.  Figure 4 shows an OMAG server platform
running multiple servers.

![Figure 4](omag-server-platform-overview.svg)
> Figure 4: An OMAG server platform running multiple OMAG servers



!!! education "Further information"
    The configuration for an OMAG Server is defined in a [configuration document](configuration-document.md).
    This configuration document is stored by a [configuration document store connector](../configuration-document/#storage).

    - [Configuring an OMAG Server](/egeria-docs/guides/admin/servers)
    - [Start and stop an OMAG Server](/egeria-docs/guides/admin/operating-omag-server.md)

--8<-- "snippets/abbr.md"
