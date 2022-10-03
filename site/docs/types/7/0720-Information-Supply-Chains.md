---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0720 Information Supply Chains

An *InformationSupplyChain* identifies the flow of a particular type of data across a digital landscape.  It is an architectural construct that can provide the focus for data governance activities that ensure data is delivered where it is needed in a timely and efficient manner.

The information supply chain is typically broken down into segments represented by *InformationSupplyChainSegment* entities that each define a particular exchange of data.  The segments are linked to their information supply chain via the *InformationSupplyChainComposition* relationship.

![UML](0720-Information-Supply-Chains.svg)

The flow of data that the information supply chain represents is described using [solution components](/types/7/0730-Solution-Components) that are linked via [ports and wires](/types/7/0735-Solution-Ports-and-Wires).  the *SolutionLinkingWire* contains the unique identifiers of the information supply chain segments that it implements.  Typically, each identified segment is for a different information supply chain that happen to share a part of the data flow.

If additional processing is required to move the data between solution components *along the wire*, for example via an ETL process, this is shown by an *ImplementedBy* relationship between the information supply chain segment and the [Process](/types/0/0010-Base-Model) that represents the implementation.  Alternatively, the component that provides the data movement can be show explicitly as a solution component in the [solution blueprint](/types/7/0740-Solution-Blueprints).


--8<-- "snippets/abbr.md"