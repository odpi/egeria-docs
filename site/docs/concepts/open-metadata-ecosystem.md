---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# The open metadata ecosystem

The *open metadata ecosystem* is the collection of deployed technology that is connected and exchanging metadata in the open metadata formats defined by Egeria.  This ecosystem includes the Egeria technology such as the [OMAG Server Platform](/concepts/omag_server_platform) plus other technologies that have adopted the standards and frameworks defined by Egeria.

The picture below is an illustration of an open metadata ecosystem.  The green clouds represent the different data centres and processing locations used by the organization.  They may be cloud services or on premises.

At each processing location there typically at least one [OMAG Server Platform (blue boxes)](/concepts/omag_server_platform) deployed that hosts [OMAG Servers](/concepts/omag_server) (orange circles) that provide the synchronization services tailored to specific types of tools (grey boxes).  The OMAG Servers themselves host [connectors](/concepts/connector) that each interface with a particular third party technology.   Egeria's [frameworks](/frameworks) define the interfaces of the connectors and how they plug into the OMAG Servers.

![Distributed operation](/introduction/egeria-distributed-operation.svg)


!!! education "Further information"

    - [Overview of Egeria](/introduction/overview)
    - [Open Metadata Frameworks](/frameworks)
    - [Open metadata types](/types)

--8<-- "snippets/abbr.md"