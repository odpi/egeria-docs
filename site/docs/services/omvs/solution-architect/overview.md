---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Solution Architect

The Solution Architect services support the definition and display of [solution blueprints](/concepts/solution-blueprint) and their supporting solution components along with the relevant [information supply chains](/concepts/information-supply-chain).

During the planning phase of a project, architects typically use drawing tools to sketch out the new components that are to be developed and how they relate to existing components.  *Solution blueprints* are the open metadata equivalent of the sketch, and they show the solution components and actors involved and how they collaborate.  The advantage of creating a solution blueprint over a sketch diagram is that it is easy to visualize different levels of detail and, as the project rolls out, the implementation of the components can be linked into the blueprint, providing traceability from project intent to actual operation.  

In a similar way, *information supply chains* allow the modelling of key data flows needed by your organization.   These can then be linked to metadata about the systems and pipelines that implement them, providing a means to summarize statistics from lineage about the operation of the data flows.  




## API operation list

* createInformationSupplyChain
* createInformationSupplyChainFromTemplate
* updateInformationSupplyChain
* createInformationSupplyChainSegment
* updateInformationSupplyChainSegment
* linkSegments
* detachSegments
* deleteInformationSupplyChainSegment
* deleteInformationSupplyChain
* getInformationSupplyChainsByName
* findInformationSupplyChains
* getInformationSupplyChainByGUID

---8<-- "snippets/abbr.md"






