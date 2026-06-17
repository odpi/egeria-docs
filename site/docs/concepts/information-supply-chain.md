<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Information supply chain

[Lineage](/concepts/lineage) is typically captured at a very fine-level of detail.  This detail enables automated governance processes to validate that the data pipelines are running as they should be.  However, this level of detail is often too much for most business users and regulators to comprehend.  It is necessary to model the flow of data at a level of detail that is meaningful to these users and correlate the fine-grained detail to this business view.

An *InformationSupplyChain* serves as a high-level depiction of data and control movement. It generally outlines how a particular kind of data travels through a digital environment. For instance, one information supply chain might track risk data for a regulatory compliance report, while another illustrates the assembly of data required for carbon accounting.

So the information supply chain is an architectural construct that can provide the focus for data governance or compliance activities that must demonstrate data being delivered where it is needed in a timely and efficient manner.  

However, the information supply chain is more than a mere diagram. It is associated with the real lineage producing components that are executing the data flow.  It provides a target for roll-ups of activity, errors and volumetrics extracted from the underlying lineage data.  The traceability back to the actual components and lineage logs supports validation, investigation and auditability of the information supply chain metrics.

## Information Supply Chain Segments

An information supply chain may be broken down into multiple, nested *segments*. Each segment may represent, for example, the portion of the information supply chain that is owned by a particular team, or the data flows that occur at different phases of the work.  This allows drill-down and more focused analysis by the owners of each segment.

## Information Supply Chain Examples

The skill in using information supply chains is to get the right level of abstraction to make its description and analysis meaningful to its intended audience.  As such they tend to be designed as part of an initiative or project, where the audience is understood.

In the [Coco Pharmaceuticals](/practices/coco-pharmaceuticals) scenarios we see multiple examples of information supply chains:

* In the [Investigating suspicious activity](/practices/coco-pharmaceuticals/scenarios/investigating-suspicious-activity/overview) scenario, Coco Pharmaceuticals use an information supply chain to model the flow of supplier information and orders through their systems to identify where bogus supplier information could be inserted without detection.
* In the [Sustainability initiative](/practices/coco-pharmaceuticals/scenarios/sustainability-initiative/overview) scenario, Coco Pharmaceuticals model an information supply chain during the development of their new sustainability data pipeline.
* In [Receiving patient data from a hospital](/practices/coco-pharmaceuticals/scenarios/receiving-patient-data-from-a-hospital/overview), we seem various Coco Pharmaceuticals persona using the information supply chains supporting their clinical trials to understand the process of a clinical trial and any issues that need action.
* In the initial set up of the data governance program, we see Coco Pharmaceuticals [identifying the key information supply chains](/practices/coco-pharmaceuticals/scenarios/defining-information-supply-chains/overview) that the program will need to support.

## Working with Information Supply Chains

Information supply chains can be viewed in [Egeria Explorer](/user-interfaces/egeria-explorer/overview) by clicking on the **Information Supply Chains** card.  The [Quickstart](/egeria-workspaces/quick-start/overview) environment includes multiple examples of information supply chains, both from Coco Pharmaceuticals and those that are part of the base Egeria implementation.

The [Lineage Explorer](/user-interfaces/lineage-explorer/overview) supports linking from a technical component in a lineage graph to its associated information supply chains in *Egeria Explorer*.

The [Solution Architect API](/services/omvs/solution-architect/overview) is where you can define, query and maintain your information supply chains.  This includes the standard OMVS REST API, python interface and Java client libraries for connectors.  They are also fully supported by [Dr.Egeria](/user-interfaces/dr-egeria/overview) in the *Solution Architect* family.

## Modelling Information Supply Chains

An information supply chain is represented by an [*InformationSupplyChain*](/types/7/0720-Information-Supply-Chains) entity.  This is a type of [collection](/types/0/0021-Collections).  So, its nested segments, and any parent information supply chain are organised into a hierarchy using the [*CollectionMembership*](/types/0/0021-Collections) relationship.  The handoff of control/data flow between information supply chains is captured using the [*InformationSupplyChainLink*](/types/7/0720-Information-Supply-Chains) relationship.  This relationship can also be used to link the business elements (typically [business capability](/concepts/business-capability) or [actor](/concepts/actor)) that initiates or consumes the data/control flow.

### Information Supply Chain Design

The high-level components illustrating the flow of data/control are captured by [Solution Components](/concepts/solution-component).  Providing a design is optional, but recommented since it creates a pictorial view of the flow for people that find the detail overwhelming and/or do not have access to the technical assets that are involved.  

A solution component may represent an implementation that has multiple information supply chains flowing through it.  The linkage between  the *InformationSupplyChain* and a relevant solution component uses a [CollectionMembership](/types/0/0021-Collections) relationship.  The flows between these solution component in the information supply chain's design are [SolutionLinkingWire](/types/7/0735-Solution-Ports-and-Wires) relationships that have the qualified name of the information supply chain stored in their *iscQualifiedNames* attribute.

An information supply chain segment is also represented by an *InformationSupplyChain* entity. It is also linked to its parent using the *CollectionMembership* relationship.

### Lineage Implementation

The unique identifiers/names of the information supply chain segments, or information supply chain itself, are encoded in the *iscQualifiedName* attribute of the lineage relationships captured in the lower levels of lineage detail.

The lineage relationships that support information supply chains include:

* The [data passing](/types/7/0750-Data-Passing) relationships: DataFlow, ControlFlow and ProcessCall.
* The [lineage mapping](/types/7/0770-Lineage-Mapping) relationships: LineageMapping and DataMapping.
* The [ultimate edges](/types/7/0755-Ultimate-Source-Destination) relationships: UltimateSource and UltimateDesination.
* The [DataSetContent](/types/2/0210-Data-Stores) relationship.
* The [DerivedSchemaTypeQueryTarget](/types/5/0512-Derived-Schema-Elements) relationship.
* The [ImplementedBy](/types/7/0737-Solution-Implementation) relationship.


???+ info "Further information"
    * [Lineage Management](/features/lineage-management/overview)

--8<-- "snippets/abbr.md"
