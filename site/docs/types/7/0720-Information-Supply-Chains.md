<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0720 Information Supply Chains


An [InformationSupplyChain](/concepts/information-supply-chain) is a high level view of lineage.

![UML](0720-Information-Supply-Chains.svg)

## InformationSupplyChain entity

An *InformationSupplyChain* entity is a [Collection](/types/0/0021-Collections) that identifies an information supply chain.  It contains the description of the purposes and scope of the information supply chain and the description of its importance to the business.

## InformationSupplyChainLink

The *InformationSupplyChainLink* relationship links an information supply chain's components, and descriptions of the data sources and destinations together into a graph.  This graph represents the highest level abstraction of the operation of the information supply chain. The *label* and *description* attributes help to explain how/why the information supply chain progresses.

## Example

The diagram below shows a simple example of an information supply chain that shows how weekly measurements from the Drop Foot clinical trial are brought into the data lake for processing.

At the top is the *InformationSupplyChain* entity.  It has two segments:

* From hospital to landing area
* From landing area to data lake

These segments represent the different parts of the flow.  The first segment, from the hospital to the landing area is not modelled in detail since it is out of the control of Coco Pharmaceuticals.  It is the responsibility of the hospital to get the files to their respective landing areas.

The second segment from the landing area to the data lake is the responsibility of Coco Pharmaceuticals.  They are required to process the incoming files immediately, so they have a continuous monitoring process to kick off the onboarding process.  The onboarding process moves the files to the correct location in the data lake and catalogs them appropriately in the open metadata ecosystem via calls to the cocoMDS1 metadata access server.

![Modelled Lineage Flow](area-7-lineage-example-summary.svg)


??? info "Further information"
    * Further detail on the modelling of the solution components can be found in [0735 Solution Ports and Wires](/types/7/0735-Solution-Ports-and-Wires).



--8<-- "snippets/abbr.md"