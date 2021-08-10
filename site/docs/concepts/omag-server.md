<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata and Governance (OMAG) server

An **OMAG server** is a software server that
runs inside the [OMAG Server Platform](omag-server-platform.md).
It supports the integration of one or more technologies by hosting
connectors that interact with that technology, or providing specialist
[APIs](../../../../basic-concepts/#application-programming-interface-apis) or
[event topics](../../../../basic-concepts/#topic) (both in and out).

Because of the wide variety of technologies deployed in organizations today,
each with very different capabilities and needs,
the integration and exchange of metadata needs to be organized.
This organization is managed through the Egeria frameworks and services
supported by the OMAG servers.
There are different types of OMAG server,
each supporting specific technologies. The OMAG server ensures this
type of technology is integrated appropriately for its needs.

The capabilities that are activated in an OMAG server are defined in its
[configuration document](configuration-document.md). When the server is started,
the operational services of the OMAG Server Platform reads the configuration document and
activates the OMAG server with the requested services.

## Platform URL root

An OMAG server's **platform URL root** is the network address of the [OMAG Server
Platform](omag-server-platform.md) where the OMAG server is going to run.  
This is often the host name of the computer or container where the platform runs plus the
port number allocated to the OMAG Server Platform.

Its value is needed when creating clients or configuring services that will call the OMAG server
because it provides the root of the URL used to call the server's
open metadata and governance REST calls, which have the following format
in their URLs:

```text
{platformURLRoot}/servers/{serverName}/<operation-name-and-parameters>
```

The platform URL root is the content of the URL prior to `/servers/`.
The default value an OMAG Server Platform is `https://localhost:9443`.

## Server name

Most APIs in Egeria require both a [platform URL root](#platform-url-root)
and a server name. The server name is the name of an OMAG server where the desired
service is running.

## Types of OMAG server

![Types of OMAG servers](types-of-omag-servers.png)

??? question "Detailed explanation of diagram"
    The way to understand the diagram is that the arrows should be read as **IS A**.  For example,
    the **Repository Proxy IS A Cohort Member** and the **Cohort Member IS A OMAG Server**.
    This means that everything documented about a particular type of server is also true for
    all server types that point to it through the **IS A** arrow, all the way down the hierarchy.

    Object-oriented software engineers would know of this type of relationship as behavior inheritance.

- [Cohort member](../../../../services/omrs/cohort/#cohort-members) - able to exchange metadata through an open metadata repository cohort
    - [Metadata server](metadata-server.md) - supports a metadata repository that can natively store open metadata types
      as well as specialized metadata APIs for different types of tools (these APIs are called [access services](../../../../services/omas.md)).
    - [Metadata access point](metadata-access-point.md) - supports the access services like the metadata server but does not have a repository.
      All metadata it serves up and stores belongs to the metadata repositories in other members of the cohort.
    - [Repository proxy](repository-proxy.md) - acts as an open metadata translator for
      a proprietary metadata repository. It supports open metadata API calls and translates them to the
      proprietary APIs of the repository. It also translates events from the proprietary repository into
      open metadata events that flow over the cohort.
    - [Conformance test server](conformance-test-server.md) - validates that a member of the
      cohort is conforming with the open metadata protocols. This server is typically only seen in development
      and test cohorts rather than production.
- [View server](view-server.md) - manages specialist services for user interfaces.
- [Governance server](governance-server-types.md) - supports the use of metadata in the broader IT landscape.
    - [Engine host](engine-host.md) - provides a runtime for a specific type of [governance engine](../../../../services/engine.md).
    - [Integration daemon](integration-daemon.md) - manages the synchronization with third party technology that
      can not call the access services directly.
    - [Data engine proxy](data-engine-proxy.md) - supports the capture of metadata from a data engine. This includes
      details of the processing of data that it is doing which is valuable when piecing together lineage.
    - [Open lineage server](open-lineage-server.md) - Manages the collation of lineage information am maintains it in a format for reporting.
      This includes the state of the lineage at different points in time.

## Interconnectivity

The different types of OMAG Servers connect together as illustrated below. There is an inner
ring of cohort members communicating via the cohort. Each cohort member is sharing the metadata
they receive with the governance servers and view servers that connect to it.
The governance servers connect out to external tools, engines and platforms.

![Interconnectivity](omag-server-ecosystem.png)

!!! education "Further information"
    The configuration for an OMAG Server is defined in a
    [configuration document](configuration-document.md).
    This configuration document is stored by a
    [configuration document store connector](configuration-document-store-connector.md).

    - [Configuring an OMAG server](../configuring-an-omag-server.md)
    - [Start and stop an OMAG server](../operating-omag-server.md)

There is design information on the OMAG Server and its relationship to
the OMAG Server Platform [here](../../../../open-metadata-publication/website/omag-server).

--8<-- "snippets/abbr.md"
