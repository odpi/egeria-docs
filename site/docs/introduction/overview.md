---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria In Action

Although it is desirable to synchronize metadata between the tools and platforms used by an organization, there are typically many technologies, each using a different format, naming conventions and interfaces, that it would be a complex and expensive project to build point-to-point metadata exchange integrations between them.

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

The picture below represents an Egeria platform deployment.  The platform's official name is the [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform). Linked above it is [*pyegeria*](/concepts/pyegeria).  This is the Python-based toolkit for Egeria.  It has a python library that supports calls to the platform for use by Python programmers. It also has commands (for the command line and the ability to process CSV files and markdown documents containing metadata, and produce reports.  

![Single Egeria platform deployment](egeria-solution-components.svg)




--8<-- "snippets/abbr.md"
