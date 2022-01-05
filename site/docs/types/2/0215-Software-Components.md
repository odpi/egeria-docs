---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0215 Software Components

**DeployedSoftwareComponent** describes a code asset that is deployed to implement a 
[software capability](/egeria-docs/types/0/0042-Software-Server-Capabilities).
Each software component has a well defined interface describe by an [APISchema](/egeria-docs/types/5/0536-API-Schemas) that is
linked to the DeployedSoftwareComponent by the [AssetSchemaType](/egeria-docs/types/5/0503-Asset-Schema) relationship.

**DeployedConnector** represents specialist software component called a
**connector** that provides pluggable access to third party
technologies.  These connectors implement the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview)
interfaces.

**EmbeddedProcess** describes a processing element nested within a DeployedSoftwareComponent.
The **TransientEmbeddedProcess** describes an EmbeddedProcess that runs only for a short period of time.

These variations are used to provide more information for lineage graphs.

**ProcessHierarchy** defines a parent-child relationship between processes, which can be used to define
more abstract processes that are comprised of lower-level processes; helping to support navigating
the process hierarchy.

![UML](0215-Software-Components.svg)



## More information

#### Related Open Metadata Type Definitions

* [Definition of Process](/egeria-docs/types/0/0010-Base-Model)
* [Linking of processes into lineage graphs](/egeria-docs/types/7)
* [Ports to show specific input and output flows for a process](/egeria-docs/types/2/0217-Ports)
* [PortSchema relationships to describe the structure of data supported by a Port](/egeria-docs/types/5/0520-Process-Schemas)


#### Use of these open metadata types

* [Egeria Developer Guide](/egeria-docs/guides/developer) for more information on connectors and how to implement them.
* [Lineage](/egeria-docs/features/lineage-management/overview) describes the different types of lineage and how the open metadata types link
together to form lineage graphs.

--8<-- "snippets/abbr.md"