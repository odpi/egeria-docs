---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->



# Governance Engine Definition

A *governance engine definition* describes the [services](/concepts/governance-service) that can be invoked in a [governance engine](/concepts/governance-engine).  It consists of a list of [governance request types](/concepts/governance-request-type) that define the logical names of each of the functions of the governance engine.  Each governance request type is mapped to at least one [governance service](/concepts/governance-service) implementation along with request parameters to configure the behaviour of the service in a [governance engine definition](/concepts/governance-engine).

![Governance Engine Definition Structure](/guides/developer/open-metadata-archives/governance-engine-definition.svg)
> **Figure 1:** Logical structure of a governance engine definition showing how the governance request types map to the governance service definitions

There are three types of governance engine ([archive engine](/concepts/archive-engine), [open discovery engine](/concepts/open-discovery-engine), [governance action engine](/concepts/governance-action-engine)) and they each support a specialist type of governance service ([archive service](/guides/developer/archive-services/overview), [open discovery service](/guides/developer/open-discovery-services/overview) and [governance action service](/guides/developer/governance-action-services/overview) respectively).  Therefore the governance engine definitions include definitions of governance services that are consistent with the type of governance engine.

![Archive Engine Definition Structure](/guides/developer/open-metadata-archives/archive-engine-definition.svg)
> Logical structure of an archive engine definition showing how the governance request types map to the archive service definitions

![Governance Action Engine Definition Structure](/guides/developer/open-metadata-archives/governance-action-engine-definition.svg)
> Logical structure of a governance action engine definition showing how the governance request types map to the governance action service definitions

![Open Discovery Engine Definition Structure](/guides/developer/open-metadata-archives/open-discovery-engine-definition.svg)
> Logical structure of an open discovery engine definition showing how the governance request types map to the open discovery service definitions.  Some of these services are *Open Discovery Pipelines* that control the choreography of a number of nested open discovery services


??? education "Further information"

    The Open Metadata Types model [0461 Governance Action Engines](/types/4/0461-Governance-Engines) shows the types for a governance engine definition.
    
    Governance engine definitions are typically defined in a [governance engine pack](/concepts/governance-engine-pack) or through the [Governance Engine OMAS](/services/omas/governace-engine/overview) API.

    Governance engines are run by the [Open Metadata Engine Services (OMES)](/services/omes) in an [Engine Host](/concepts/engine-host) OMAG Server.  The [Engine Host Services](/services/engine-host-services) called the [Governance Engine OMAS](/services/omas/governance-engine/overview)
  


--8<-- "snippets/abbr.md"