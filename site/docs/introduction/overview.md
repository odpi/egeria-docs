<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria In Action

Although it is desirable to synchronize metadata between the tools, systems and platforms used by an organization, there are typically many technologies involved, each using a different format, naming conventions and interfaces. This makes it a complex and expensive project to build point-to-point metadata exchange integrations between them.

![Before Egeria](before-egeria.svg)

Using Egeria, you only need to link each tool to Egeria, and it is Egeria that manages the complexity of the metadata exchange.

![Egeria concepts](egeria-concept.svg)

Each tool is linked via an Egeria connector (orange circles), tailored for that specific type of tool. The connector is responsible for translating between Egeria's [Open Metadata Types](/types) and the proprietary formats, naming conventions and interfaces of the tool.

![Connecting to Egeria](connecting-to-egeria.svg)

Behind the scenes, Egeria manages the exchange of metadata between the tools using a variety of techniques to ensure this occurs in the most efficient and timely manner possible.  Internally, Egeria uses the open metadata types for its storage and exchange. It also has services that tools can call directly to work with the open metadata.

![Connecting to Egeria](egeria-exchange.svg)

Although Egeria is shown above as a centralized solution, it is, in fact, implemented as a distributed solution to meet the needs of a larger enterprise that typically have their tools and technologies distributed across multiple data centres and cloud providers (green clouds). Each of these locations may be managed by different groups and use different technologies.  This makes a centralized metadata solution impractical from both a funding and operational perspective.

Using Egeria, each location runs their own Egeria **platform** (blue boxes) that hosts the appropriate **connectors** (orange circles) tailored to specific types of tools (grey boxes).  

![Distributed operation](egeria-distributed-operation.svg)

In addition, there is a Python-based toolkit for interacting with the platform.

## Single platform deployment 

The picture below represents an Egeria platform deployment (blue box).  The platform's official name is the [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform). Linked above it is [*pyegeria*](/concepts/pyegeria).  This is the Python-based toolkit for Egeria.  It has a python library that supports calls to the platform for use by Python programmers. It also has commands (for the command line and the ability to process CSV files and markdown documents containing metadata, and produce reports.  

![Single Egeria platform deployment](egeria-solution-components.svg)

### Content Packs

Notice the content packs on the bottom right-hand side.  Egeria's [content packs](/content-packs) load new [open metadata types](/types) and metadata to support [specific solutions](/egeria-solutions).  The metadata consists of reference data (lists of linked valid values used to validate and map data/metadata that Egeria is processing), configuration for Egeria's governance servers and definitions that describe the solutions it supports.  When a content pack is loaded into Egeria, it is immediately consumed but the appropriate parts of the runtime to activate the solution.

### Integrating with Egeria

There are multiple ways that tools and other runtimes are integrated with Egeria, however they divide in two groups:

* The tool/runtime integrated with one of Egeria's APIs or frameworks
* A [connector](/concepts/connector) translates requests between Egeria and the tool/system/platform's interface.

These are some examples:

* The [integration connector](/concepts/integration-connector) is the most common type of connector to synchronize metadata between Egeria and a third party technology.
* A bespoke browser-based UI or Tool could call the [Open Metadata and Governance REST APIs](/services/omvs).
* High-quality metadata repository can be integrated using a [Adapter Repository Connector](https://egeria-project.org/concepts/repository-connector/).

In addition, Egeria has extensive support for the [Open Lineage](/features/lineage-management/overview) standard events.  These are received via the [Open Lineage Proxy](/concepts/open-lineage-topic).

### Egeria's servers

Egeria's platform is highly configurable.  It also supports multi-tenant operation (ie multiple teams/organizations could run their independent metadata solution in the same platform instance).  This is achieved by organizing the configured services into virtual servers called [Open Metadata and Governance (OMAG) servers](/concepts/omag-server).  There are different kinds of OMAG Servers that specialized to perform certain tasks:

* The [View Server](/concepts/view-server) provides the [REST APIs to maintaining/query open metadata](/services/omvs) and to initiate/control [governance actions](/concepts/governance-action).
* The [Metadata Access Server](/concepts/metadata-access-server) provides services for the open metadata repositories and metadata change events (sent on the [OutTopic](/concepts/out-topic)) for other servers.
* The [Integration Daemon](/concepts/integration-daemon) hosts [integration connectors](/concepts/integration-connector).
* The [Engine Host](/concepts/engine-host) hosts the execution of calls to [governance services](/concepts/governance-services) that perform [governance actions](/concepts/governance-action).
* The [Repository Proxy](/concepts/repository-proxy) hosts an [adapter repository connector](https://egeria-project.org/concepts/repository-connector/) that is integrating with a third party metadata repository.

A platform can run multiple OMAG servers of each kind.

![Inside the Egeria Platform](egeria-solution-components-exposed.svg)


### Coco Pharmaceuticals

[*Coco Pharmaceuticals*](/practices/coco-pharmaceuticals) is a collection of personas and use cases that were developed by the Egeria community to act as a backdrop to the development work around Egeria's software.  Although the personas and the situations they find themselves are all fictitious, they are based on real people working in real organizations with real challenges.  They also occur in many organizations irrespective of industry.  You may even recognize some of them yourself :).  There is also a [content pack](/content-packs/coco-content-pack/overview) that loads metadata to support the scenarios.

--8<-- "snippets/abbr.md"
