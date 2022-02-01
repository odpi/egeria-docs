---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Engine Services (OMES)

The engine services are each able to host a specific type of [governance engine](/concepts/governance-engine). 

Broadly there are three types of governance engines:

- *[Open discovery engines](/concepts/open-discovery-engine)* that run automatic metadata discovery requests to analyze the content of an [asset's](/concepts/asset) real-world [resource](/conceepts/resource) counterpart. They implement the engine interface defined in the [Open Discovery Framework (ODF)](/frameworks/odf/overview).

- *[Governance action engines](/concepts/governance-action-engine)* that manage the processing supporting governance processing such as the resolution of issues reported in the open metadata ecosystem or the assets it supports.  They implement the engine interface defined in the [Governance Action Framework (GAF)](/frameworks/gaf/overview).

- *[Archive engines](/concepts/archvie-engine)* that maintain [Open Metadata Archives](/concepts/open-meetadata-archive) based on the live content of the open metadata repositories.

These engines are supported by the [Asset Analysis OMES](/services/omes/asset-analysis/overview), [Governance Action OMES](/services/omes/governance-action/overview) and [Archive Manager OMES](/services/omes/archive-manager/overview) respectively.

--8<-- "snippets/abbr.md"
