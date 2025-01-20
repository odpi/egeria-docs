---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Information supply chain

Lineage is typically captured from the running technology at a very fine-level of detail.  This detail enables automated governance processes to validate that the data pipelines are running as they should be.  However, this level of detail is too much for most business users and regulators to comprehend.  Therefore, it is necessary to model the flow of data at a level of detail that is meaningful to these users and correlate the fine-grained detail to this business view.

An *InformationSupplyChain* is the highest level of abstraction for lineage.  It typically identifies the flow of a particular type of data across a digital landscape.  For example, there may be an information supply chain capturing risk data for a regulatory compliance report, and another one showing how the data necessary for carbon accounting is assembled.

It is an architectural construct that can provide the focus for data governance activities that ensure data is delivered where it is needed in a timely and efficient manner.

The information supply chain is typically broken down into segments represented by *InformationSupplyChainSegment* entities that each define a particular exchange of data.  For example, it may be the flow of data through a specific business unit or country.  The segments are linked to their information supply chain via the *InformationSupplyChainComposition* relationship.  Their relationship to one another, and its logical sources and destinations are captured using *InformationSupplyChainLink* relationships.

The unique identifiers/names of the information supply chain segments, or information supply chain itself, are encoded in the lineage relationships captured in the lower levels of lineage detail:

* The architectural view of the flow of data that the information supply chain represents is described using [solution components](/concepts/solution-somponent) that are linked via [ports and wires](/types/7/0735-Solution-Ports-and-Wires).  The [*SolutionLinkingWire*](/types/7/0735-Solution-Ports-and-Wires) contains the unique identifiers (GUIDs) of the information supply chain segments that it implements.  Typically, each identified segment is for a different information supply chain that happen to share a part of the data flow.

* The fine-grained view captured from the implementation and operation of the deployed technology is described using the [data passing](/types/7/0750-Data-Passing) and [lineage mapping](/types/7/0770-Lineage-Mapping)  relationships.

If additional processing is required to move the data between solution components *along the wire*, for example via an ETL process, this is shown by an *ImplementedBy* relationship between the information supply chain segment and the [Process](/types/0/0010-Base-Model) that represents the implementation.  Alternatively, the component that provides the data movement can be show explicitly as a solution component in the [solution blueprint](/types/7/0740-Solution-Blueprints).

--8<-- "snippets/abbr.md"
