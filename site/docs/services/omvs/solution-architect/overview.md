<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Solution Architect API

The Solution Architect API provides a REST API to support user interfaces (UIs)
relating to the definition and display of solution blueprints and their supporting solution components,
information supply chains and design patterns.

## Key Features

During the planning phase of a project, architects typically use drawing tools to sketch out the new
components that are to be developed and how they relate to existing components.

* **Solution blueprints** are the open metadata equivalent of the sketch and they show the solution
  components and actors involved and how they collaborate. The advantage of creating a solution blueprint
  over a sketch diagram is that it is easy to visualize different levels of detail and, as the project rolls out,
  the implementation of the components can be linked into the blueprint, providing traceability from project
  intent to actual operation.
* **Information supply chains** allow the modelling of key data flows needed by your organization.
  These can then be linked to metadata about the systems and pipelines that implement them, providing a
  means to summarize statistics from lineage about the operation of the data flows.
* **Solution components** represent the individual parts of a solution.
* **Design patterns** provide reusable solutions to commonly occurring problems in solution design.

The Solution Architect API supports the definition and display of these elements and their relationships.

## Further information

* [Solution Blueprint Concept](/concepts/solution-blueprint)
* [Information Supply Chain Concept](/concepts/information-supply-chain)
* [Design Pattern Concept](/concepts/design-pattern)

Sample requests for the REST API can be found in [Egeria-api-solution-architect.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/solution-architect/Egeria-api-solution-architect.http).
[Egeria-jacquard-solution-blueprints.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/solution-architect/Egeria-jacquard-solution-blueprints.http) shows how to retrieve the solution blueprints that describe the behaviour of the connectors supporting the Open Metadata Digital Product Catalog function.

## API Overview

The Solution Architect services support the definition and display of [solution blueprints](/concepts/solution-blueprint) and their supporting solution components along with the relevant [information supply chains](/concepts/information-supply-chain).

During the planning phase of a project, architects typically use drawing tools to sketch out the new components that are to be developed and how they relate to existing components.  *Solution blueprints* are the open metadata equivalent of the sketch, and they show the solution components and actors involved and how they collaborate.  The advantage of creating a solution blueprint over a sketch diagram is that it is easy to visualize different levels of detail and, as the project rolls out, the implementation of the components can be linked into the blueprint, providing traceability from project intent to actual operation.  

In a similar way, *information supply chains* allow the modelling of key data flows needed by your organization.   These can then be linked to metadata about the systems and pipelines that implement them, providing a means to summarize statistics from lineage about the operation of the data flows.  


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






