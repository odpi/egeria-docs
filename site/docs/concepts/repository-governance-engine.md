---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019, 2020. -->

# Repository Governance Engine

The repository governance engine describes a set of related [repository governance services](/guides/developer/repository-governance-services/overview) that perform governance on open metadata repositories such as dynamically manage [open metadata archives](/concepts/open-metadata-archives) based on changes in the open metadata.

A repository governance engine is hosted in the [Repository Governance Open Metadata Engine Service (OMES)](/services/omes/repository-governance/overview) running on one or more [Engine Host OMAG Servers](/concepts/engine-host).

When a repository governance engine is called, it is passed a governance request type and request parameters. This is mapped to a call to a repository governance service through the [repository governance engine definition](/concepts/governance-engine-definition).

![Repository Governance Engine Definition Structure](/guides/developer/open-metadata-archives/repository-governance-engine-definition.svg)
> Logical structure of a repository governance engine definition showing how the governance request types map to the repository governance service definitions

??? education "Further information"

    The Open Metadata Types used to define the repository governance engines are located in model **[0461 Governance Engines](/types/4/0461-Governance-Engines)**.




--8<-- "snippets/abbr.md"
