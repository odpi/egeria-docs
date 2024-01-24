---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# GAF Metadata Management

GAF metadata management provides the context services defined by the [Governance Action Framework (GAF)](/frameworks/gaf/overview) along with services that support the [Open Metadata Access Services (OMASs)](/services/omas):

* Open Metadata Store is a generic metadata interface.  It enables the searching for and retrieval of open metadata type definitions, plus the searching for, update and retrieval of all types of open metadata elements: entities, relationships and classifications.
* Open Governance Service supports the setting up of governance actions such as [governance action processes](/concepts/governance-action-process) and [governance action types](/concepts/governance-action-type), and the initiation of [engine actions](/concepts/engine-action) either directly or via a governance action process or governance action type.

It provides base clients for each of these services that are specialized by each OMAS to limit metadata access to its supported zones.

--8<-- "snippets/abbr.md"
