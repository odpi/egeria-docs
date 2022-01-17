---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Engine Services (OMES)

The engine services are each able to host a specific type of governance engine. 

Broadly there are three types of governance engines:

- *[Open discovery engines](/egeria-docs/concepts/open-discovery-engine)* that run automatic metadata discovery requests to analyze the content of an [asset's](/egeria-docs/concepts/asset) real-world [resource](/egeria-docs/conceepts/resource) counterpart. They implement the engine interface defined in the [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview).

- *[Governance action engines](/egeria-docs/concepts/governance-action-engine)* that manage the processing supporting governance processing such as the resolution of issues reported in the open metadata ecosystem or the assets it supports.  They implement the engine interface defined in the [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf/overview).

- *[Archive engines](/egeria-docs/concepts/archvie-engine)* that maintain [Open Metadata Archives](/egeria-docs/concepts/open-meetadata-archive) based on the live content of the open metadata repositories.

These engines are supported by the [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis/overview), [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) and [Archive Manager OMES](/egeria-docs/services/omes/archive-manager/overview) respectively.

--8<-- "snippets/abbr.md"
