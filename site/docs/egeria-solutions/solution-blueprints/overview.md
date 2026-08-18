<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Blueprints to delivery

Every project produces a design.  It is usually drawn in a diagramming tool, presented to stakeholders, agreed - and then left behind, because the implementation moves on and nobody can afford to keep the picture up to date.  A year later the only accurate description of the solution is the code, and the only people who understand it are the ones who wrote it.

A [solution blueprint](/concepts/solution-blueprint) is that design held as metadata instead, so that it can be linked to the implementation as it is built and to the operational picture once it is running.

## What a blueprint describes

A blueprint collects the [solution components](/concepts/solution-component) that together deliver a business solution, along with the roles of the people involved and the flow of data between components.

It deliberately stays above the level of a UML or entity-relationship model.  It does not carry data types or cardinality; its purpose is to support a conversation - to tell the story of how the solution works to the people who need to agree on it.  An element such as a [project](/concepts/project) or a [governance definition](/concepts/governance-definition) can have several blueprints, each showing a different aspect or level of detail.

The pieces are:

| Element | Role in the design |
|---------|--------------------|
| [Solution component](/concepts/solution-component) | A part of the solution: a process, a data store, a service, a piece of infrastructure.  Components can nest, so a component in one blueprint may be a whole blueprint of its own. |
| Solution actor role | Who interacts with a component, and in what capacity - the consumer, the subscriber, the person who maintains it. |
| Solution ports and wires | The inputs and outputs of each component, and the links that show how data passes between them. |
| [Information supply chain](/concepts/information-supply-chain) | The end-to-end flow of data across components, described from the business point of view. |

The blueprint below describes what happens when someone subscribes to a digital product.  Notice how much of it is about *people*: the subscriber and the consumer appear alongside the pipeline and the delivery location, because a design that omits the roles does not explain how the solution actually operates.

--8<-- "snippets/blueprints/digital-products/creating-a-new-subscription-to-a-digital-product-solution-blueprint-mermaid-graph.md"

Each component can also be viewed in its own right, showing the blueprint it belongs to, the roles that act on it and the components it exchanges data with.  This is one component from Coco Pharmaceuticals' clinical trial solution:

--8<-- "snippets/blueprints/components/analyse-patient-data-mermaid-graph.md"

## From design to delivery

The blueprint becomes valuable - rather than decorative - when it is connected to what is actually being built.

As implementation proceeds, solution components are linked to the [digital resources](/concepts/digital-resource) that implement them using the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship.  A component might be implemented by a catalogued database, an integration connector, a governance action process, or a whole subsystem.  Because these links are added as the resources appear in the catalog, the design and the implementation stay attached to each other instead of drifting apart.

That linkage supports several things at once:

* **Progress against the agreed design.**  Which components have implementations yet, and which are still just intent, is visible to stakeholders without asking the project for a status report.
* **Traceability in both directions.**  From a component you can reach the resources that realize it; from a catalogued resource you can reach the design that explains why it exists and what it is supposed to do.
* **Impact.**  When a change is proposed to a data store, the blueprint shows which parts of the solution - and which roles - depend on it.

## From delivery to operation

Once the solution is running, the blueprint becomes the natural place to aggregate its operational picture.  The design is already the map of what the solution consists of, so it is the right structure on which to hang what is happening:

* [Lineage](/features/lineage-management/overview) captured from the running implementation shows the data actually flowing along the wires the design described.
* Measurements and [governance metrics](/types/4/0450-Governance-Rollout) can be attached to the components and to the blueprint as a whole, so the effectiveness of the solution is reported against the same structure that was agreed at the start.
* Exceptions and incidents raised by the implementation resolve back to the component - and therefore the role - responsible for it.

In the [new systems architecture](/practices/coco-pharmaceuticals/scenarios/defining-new-systems-architecture/overview) scenario, this is exactly the argument Erin Overview makes: the blueprint makes the architecture visible to a broader audience, lets stakeholders follow the progress of the implementation because it is linked to the solution components, and once operational becomes the aggregation point for statistics about data sharing across the organization - so the teams relying on the exchange can verify that it is working.

## Creating and viewing blueprints

* The [Solution Architect](/services/omvs/solution-architect/overview) API maintains blueprints, solution components, ports, wires and information supply chains, and their links to the implementation.
* [Dr.Egeria](/user-interfaces/dr-egeria/overview) lets a blueprint be authored as a Markdown document.  This is how Erin creates the *Data-Driven Systems Architecture* blueprint, and how Robbie Records documents his [data sharing hub](/practices/coco-pharmaceuticals/scenarios/patient-data-sharing-hub/overview) for stakeholders.
* [Egeria Explorer](/user-interfaces/egeria-explorer/overview) displays blueprints and components, with the [mermaid graphs](/user-interfaces/mermaid/overview) shown above generated automatically from the metadata - which means the picture is always current, because it is drawn from the thing it describes.

!!! info "Related information"

    * [Model 0740 Solution Blueprints](/types/7/0740-Solution-Blueprints), [0730 Solution Components](/types/7/0730-Solution-Components), [0735 Solution Ports and Wires](/types/7/0735-Solution-Ports-and-Wires) and [0737 Solution Implementation](/types/7/0737-Solution-Implementation).
    * [Information supply chains](/concepts/information-supply-chain) - the end-to-end data flows that blueprints describe.
    * [Building data specifications](/egeria-solutions/building-data-specifications/overview) - the data the solution needs, specified alongside the design.

--8<-- "snippets/abbr.md"
