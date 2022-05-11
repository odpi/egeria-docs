---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->



# Governance Engine Definition

A *governance engine definition* describes the [governance services](/concepts/governance-service) that can be invoked in a [governance engine](/concepts/governance-engine).  It consists of a list of [governance request types](/concepts/governance-request-type) that define the logical names of each of the functions of the governance engine.  Each governance request type is mapped to one [governance service](/concepts/governance-service) implementation along with request parameters to configure the behaviour of the service in a [governance engine definition](/concepts/governance-engine). A governance service may support many request types, and execute different behaviors based on the request parameters and its configuration properties.

![Governance Engine Definition Structure](/guides/developer/open-metadata-archives/governance-engine-definition.svg)
> **Figure 1:** Logical structure of a governance engine definition showing how the governance request types map to the governance service definitions

There are three types of governance engine and they each support a specialist type of governance service.  Therefore the governance engine definitions include definitions of governance services that are consistent with the type of governance engine.

| Type of Governance Engine | Type of Governance Service | Description |
|---|---|---|
| [Governance action engine](/concepts/governance-action-engine) |  [Governance action service](/guides/developer/governance-action-services/overview)| Monitor and manage the content of open metadata across the open metadata landscape. |
| [Open discovery engine](/concepts/open-discovery-engine)| [Open discovery service](/guides/developer/open-discovery-services/overview) | Analyze the content of [resources](/concepts/resource) in the digital landscape and create annotations that are attached to the resource's [asset](/concepts/asset) metadata element in the open metadata repositories in the form of a [discovery analysis report](/concepts/discovery-analysis-report). |
| [Repository governance engine](/concepts/repository-governance-engine) | [Repository governance service](/guides/developer/repository-governance-services/overview) | Provide additional management of the open metadata repositories that are members of the connected [cohorts](/concepts/cohort-members). |

Each governance engine definition describes a single engine and its specialized services as illustrated below.

![Repository Governance Engine Definition Structure](/guides/developer/open-metadata-archives/repository-governance-engine-definition.svg)
> Logical structure of a repository governance engine definition showing how the governance request types map to the repository governance service definitions

![Governance Action Engine Definition Structure](/guides/developer/open-metadata-archives/governance-action-engine-definition.svg)
> Logical structure of a governance action engine definition showing how the governance request types map to the governance action service definitions

![Open Discovery Engine Definition Structure](/guides/developer/open-metadata-archives/open-discovery-engine-definition.svg)
> Logical structure of an open discovery engine definition showing how the governance request types map to the open discovery service definitions.  Some of these services are *Open Discovery Pipelines* that control the choreography of a number of nested open discovery services


!!! education "Further information"

    * Governance engine definitions are typically defined in a [governance engine pack](/guides/developer/open-metadata-archives/creating-governance-engine-packs) or through the [Governance Engine OMAS](/services/omas/governance-engine/overview) API.
    
    * The Open Metadata Types model [0461 Governance Action Engines](/types/4/0461-Governance-Engines) shows the types for a governance engine definition.
    
    * Governance engines are run by the [Open Metadata Engine Services (OMES)](/services/omes) in an [Engine Host](/concepts/engine-host) OMAG Server.  The [Engine Host Services](/services/engine-host-services) called the [Governance Engine OMAS](/services/omas/governance-engine/overview)
  

--8<-- "snippets/abbr.md"