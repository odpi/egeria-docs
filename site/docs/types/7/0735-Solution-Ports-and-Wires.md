<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0735 Solution Ports and Wires

[Solution components](/types/7/0730-Solution-Components) need well-defined interfaces.  These may be APIs or other types of request and information exchange mechanisms such as eventing.

![UML](0735-Solution-Ports-and-Wires.svg)

## SolutionPort entity

The interfaces for a solution component are defined using a *SolutionPort* entity.  Each port represents the interface for a particular type of consumer.  The port may offer multiple technology mechanisms (APIs, events, ...) to the consumer.  However, if these mechanisms are used for different purposes, they are better represented as different ports.

## SolutionComponentPort relationship

The *SolutionComponentPort* relationship links a solution component to one of its ports.

## SolutionLinkingWire relationship

The *SolutionLinkingWire* shows the linkage between solution components via their ports to other elements in the architecture.  The *iscQualifiedNames* property allows linkage to the [information supply chains](/types/7/0720-Information-Supply-Chains) that identify critical data flows for the organization.  The *label* and *description* attributes help to explain how/why the lineage flow progresses.

## SolutionPortDelegation relationship

Solution components can be decomposed into smaller solution components.  The *SolutionPortDelegation* relationship shows which ports in the parent solution components map to the ports of the solution components it is decomposed into.


## Example

The diagram below shows a set of linked solution components and their linkage to the assets that implement them.

![Mapping to Detailed Lineage](area-7-lineage-example-detail.svg)

??? info "Further information"
    * The implementation of this information supply chain is build out in the *Automated Curation* [Open Metadata Lab](/education/open-metadata-labs/overview).
    * More detail on the modelling of the information supply chain implemented by these solution components can be found in [0720 Information Supply Chains](/types/7/0720-Information-Supply-Chains).

--8<-- "snippets/abbr.md"