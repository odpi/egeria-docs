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

## Visualizing Information Supply Chains

When an information supply chain is retrieved with its implementation (`addImplementation=true`), Egeria returns a set of [mermaid](/user-interfaces/mermaid/overview) graphs along with its properties.  A single graph of a large information supply chain is often too big for mermaid to display, so the description is split into five graphs: one for the information supply chain's purpose, its design and the progress of its implementation, and one for each [layer of lineage](/features/lineage-management/overview/#the-layers-of-lineage) that implements it.  A graph is only returned if it has something in it.

| Property                        | What it shows                                                                                                                                                                                                                                         |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *iscImplementationMermaidGraph* | The **Context**, **Design** and **Status** of the information supply chain, in three areas drawn one above the other.  The elements within each area are laid out from left to right.                                                                  |
| *iscDataMeshMermaidGraph*       | The [digital products](/concepts/digital-product) at either end of the information supply chain's implementation, and the [*DigitalProductDependency*](/types/7/0710-Digital-Products) relationships between them that make up the [data mesh](/concepts/data-mesh). |
| *iscSystemFabricMermaidGraph*   | The IT infrastructure (such as hosts) and the [software capabilities](/concepts/software-capability) (such as database managers) at either end of the implementation - the systems that the data and processes run on.                                  |
| *iscDataFabricMermaidGraph*     | The data assets, processes and actions linked by data lineage (*DataFlow*, *ProcessCall*, *LineageMapping*, *UltimateSource* and *UltimateDestination*), *ControlFlow* and *ActionRequester* relationships.  This is the [data fabric](/concepts/data-fabric) - how the data actually moves. |
| *iscDataMappingMermaidGraph*    | The elements linked by *DataMapping* relationships, such as the columns of tables, and the anchors of those elements.                                                                                                                                 |

### The areas of the implementation graph

| Area        | What it shows                                                                                                                                                                                                                                                                                                                                       |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Context** | The information supply chain itself, along with its parent and its nested [segments](#information-supply-chain-segments) (linked by dotted lines) and the information supply chains that it receives from or supplies to through *InformationSupplyChainLink* relationships (linked by solid lines).                                                 |
| **Design**  | The [solution components](/concepts/solution-component) that are members of the information supply chain, and the *SolutionLinkingWire* relationships between them that carry the information supply chain's qualified name in their *iscQualifiedNames* attribute.  Wires that belong only to other information supply chains are left out.  |
| **Status**  | The same solution components and wires as the *Design* area, but coloured to show how far the implementation of each component has progressed - see below.                                                                                                                                                                                          |

### Showing the progress of the implementation

The *Status* area colours each solution component by its *deploymentStatus*.  When the status is anything other than *Active*, it is also written into the component's label, so that the status can still be read when the graph is displayed without colour.

| Deployment status                          | How the solution component is drawn                                                    |
|:-------------------------------------------|:---------------------------------------------------------------------------------------|
| *Active*, or no status                     | The normal solution component style - the component is assumed to be deployed.         |
| *Proposed*, *Approved for deployment*      | Light yellow.                                                                          |
| *Under development*, *Development complete* | Pale orange (papaya whip).                                                            |
| *StandBy*                                  | Silver.                                                                                |
| *Disabled*                                 | Dark grey.                                                                             |
| *Rejected*                                 | Rosy brown.                                                                            |
| *Failed*                                   | Orange-red.                                                                            |
| *Other*                                    | The normal style, with the *userDefinedDeploymentStatus* written into the label.       |

A component with the [*Promise*](/concepts/promise) classification has not been delivered at all, so it is drawn in the *Promise* style whatever its deployment status.  Likewise, a component with the [*Memento*](/concepts/memento) classification has been retired, and is drawn in the *Memento* style.  These styles are also used for promised and retired elements in the other graphs, so that planned and retired resources stand out from the ones that are in use.  Promised and retired elements are only returned when the information supply chain is retrieved with `forLineage=true` - in Egeria Explorer and the Lineage Explorer, this is the *Show Promise / Memento* option.

### The layer graphs

The four layer graphs are built from the information supply chain's *implementation*: the relationships that carry its qualified name in their *iscQualifiedName* attribute (see [Lineage Implementation](#lineage-implementation) below).  In each one, the elements of the layer are drawn inside a subgraph named after the layer, and each relationship between them is drawn as a line labelled with its label or role and its type.

Elements from outside the layer are drawn outside the subgraph, with their links into it:

* The solution components linked to the layer's elements, typically through *ImplementedBy* relationships, which are drawn as thin lines.  This shows which part of the design each element implements.
* In the data fabric, the digital products linked to its elements - for example, by the lineage mapping from the data set that a digital product packages.
* The anchors of the layer's elements, linked to them by a line labelled *Anchor for*.  In the data mapping graph this is every anchor, such as the asset that a column belongs to.  In the other graphs it is the solution components, and in the data mesh the digital products too.  An anchor is only drawn if it is itself part of the information supply chain - a member of it, or at the end of one of its relationships.

An element that is only linked by a relationship that none of the layers uses does not appear in any of the graphs.

### Sample information supply chain

The [Core Content Pack](/content-packs/core-content-pack/overview) includes an information supply chain called *SAMPLE Information Supply Chain - Deployment Status Demonstration* that exists only to show each of these graphs.  Everything in it is named *SAMPLE* so that it is not mistaken for real content, and it may be deleted.  It contains:

* A chain of solution components, one for each deployment status plus one with the *Promise* classification, for the implementation graph.
* A provider digital product that packages the target data set, a consumer product that depends on it, and an extract product that also depends on it, for the data mesh.  The consumer product is anchored to the *Proposed* solution component, and the extract product is anchored to the consumer product.
* A host and a database manager that runs on it, for the system fabric.  The database manager is anchored to the *Development Complete* solution component.
* A source data file, a load process and a target data set, for the data fabric.  The load process passes control to a validate process (*ControlFlow*) and requests a review action (*ActionRequester*), which is anchored to the *Under Development* solution component.
* A column in the source data file that is copied to a column in the target data set (*DataMapping*), for the data mapping graph.  Each column is anchored to its data asset.
* *ImplementedBy* relationships from the *Active* solution component to the load process, from *Approved For Deployment* to the provider product, and from *Standby* to the host.

The sample also shows the [Darwin Product Dependency Manager](/features/lineage-management/overview/#rolling-up-the-lineage) at work.  The unlabelled data flow from the source file to the target data set in the data fabric graph is not part of the sample: Darwin derives it from the data mapping between the two columns, and tags it with the sample's qualified name.  Darwin also records an exception against the dependency between the consumer and provider products, because the lineage beneath them does not prove it - this is expected.

The graphs below are the sample information supply chain as Egeria draws them.  They were retrieved with `forLineage=true`, so the promised component at the start of the chain is included.

#### Implementation graph

```mermaid
---
title: Information Supply Chain - SAMPLE Information Supply Chain - Deployment Status Demonstration [f9d90bd0-9364-4015-a1b9-9bfff6d9a3e7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

subgraph 1 [Context]
direction LR
2@{ shape: flip-tri, label: "*Information Supply Chain*
**SAMPLE Information Supply Chain - Deployment Status Demonstration**"}
end
subgraph 3 [Design]
direction LR
4@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Failed**"}
5@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Other**"}
6@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Active**"}
7@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Proposed**"}
8@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Standby**"}
9@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Promise**"}
10@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Disabled**"}
11@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Under Development**"}
12@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Approved For Deployment**"}
13@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Development Complete**"}
14@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Rejected**"}
4-. "sample flow [Solution Linking Wire]" .->5
10-. "sample flow [Solution Linking Wire]" .->4
8-. "sample flow [Solution Linking Wire]" .->6
6-. "sample flow [Solution Linking Wire]" .->10
9-. "sample flow [Solution Linking Wire]" .->7
7-. "sample flow [Solution Linking Wire]" .->11
14-. "sample flow [Solution Linking Wire]" .->8
11-. "sample flow [Solution Linking Wire]" .->13
12-. "sample flow [Solution Linking Wire]" .->14
13-. "sample flow [Solution Linking Wire]" .->12
end
subgraph 15 [Status]
direction LR
16@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Failed**
Deployment Status: Failed"}
17@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Other**
Deployment Status: Awaiting vendor"}
18@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Active**"}
19@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Proposed**
Deployment Status: Proposed"}
20@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Standby**
Deployment Status: StandBy"}
21@{ shape: datastore, label: "*Solution Component*
**SAMPLE Solution Component - Promise**
Deployment Status: Proposed"}
22@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Disabled**
Deployment Status: Disabled"}
23@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Under Development**
Deployment Status: Under development"}
24@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Approved For Deployment**
Deployment Status: Approved for deployment"}
25@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Development Complete**
Deployment Status: Development complete"}
26@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Rejected**
Deployment Status: Rejected"}
16-. "sample flow [Solution Linking Wire]" .->17
22-. "sample flow [Solution Linking Wire]" .->16
20-. "sample flow [Solution Linking Wire]" .->18
18-. "sample flow [Solution Linking Wire]" .->22
21-. "sample flow [Solution Linking Wire]" .->19
19-. "sample flow [Solution Linking Wire]" .->23
26-. "sample flow [Solution Linking Wire]" .->20
23-. "sample flow [Solution Linking Wire]" .->25
24-. "sample flow [Solution Linking Wire]" .->26
25-. "sample flow [Solution Linking Wire]" .->24
end
1~~~3
3~~~15
style 22 color:#000000, fill:#A9A9A9, stroke:#000000
style 23 color:#000000, fill:#FFEFD5, stroke:#004563
style 24 color:#000000, fill:#ffffe0, stroke:#004563
style 25 color:#000000, fill:#FFEFD5, stroke:#004563
style 26 color:#000000, fill:#bc8f8f, stroke:#000000
style 10 color:#000000, fill:#DDA0DD, stroke:#000000
style 11 color:#000000, fill:#DDA0DD, stroke:#000000
style 12 color:#000000, fill:#DDA0DD, stroke:#000000
style 13 color:#000000, fill:#DDA0DD, stroke:#000000
style 14 color:#000000, fill:#DDA0DD, stroke:#000000
style 15 color:#000000, fill:#b0c4de, stroke:#000000
style 16 color:#FFFFFF, fill:#ff4500, stroke:#000000
style 17 color:#000000, fill:#DDA0DD, stroke:#000000
style 18 color:#000000, fill:#DDA0DD, stroke:#000000
style 19 color:#000000, fill:#ffffe0, stroke:#004563
style 1 color:#FFFFFF, fill:#FFFFFF, stroke:#FFFFFF
style 2 color:#FFFFFF, fill:#004563, stroke:#e0ab18
style 3 color:#000000, fill:#b0c4de, stroke:#000000
style 4 color:#000000, fill:#DDA0DD, stroke:#000000
style 5 color:#000000, fill:#DDA0DD, stroke:#000000
style 6 color:#000000, fill:#DDA0DD, stroke:#000000
style 7 color:#000000, fill:#DDA0DD, stroke:#000000
style 8 color:#000000, fill:#DDA0DD, stroke:#000000
style 9 color:#000000, fill:#DDA0DD, stroke:#000000
style 20 color:#000000, fill:#C0C0C0, stroke:#000000
style 21 color:#004563, fill:#F8F8FF, stroke:#F0FFFF
```

#### Data mesh graph

```mermaid
---
title: Information Supply Chain Data Mesh - SAMPLE Information Supply Chain - Deployment Status Demonstration [f9d90bd0-9364-4015-a1b9-9bfff6d9a3e7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Approved For Deployment**"}
2@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Proposed**"}
subgraph 3 [Data Mesh]
direction BT
4@{ shape: rect, label: "*Digital Product*
**SAMPLE-DigitalProduct:Extract**"}
5@{ shape: rect, label: "*Digital Product*
**SAMPLE-DigitalProduct:Provider**"}
6@{ shape: rect, label: "*Digital Product*
**SAMPLE-DigitalProduct:Consumer**"}
end
4==>|"sample extracts from [Digital Product Dependency]"|5
6==>|"sample depends on [Digital Product Dependency]"|5
1-->|"sample product [Implemented By]"|5
6-->|"Anchor for"|4
2-->|"Anchor for"|6
style 1 color:#000000, fill:#DDA0DD, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#000000, fill:#5f9ea0, stroke:#3079ab
style 4 color:#000000, fill:#838cc7, stroke:#3079ab
style 5 color:#000000, fill:#838cc7, stroke:#3079ab
style 6 color:#000000, fill:#838cc7, stroke:#3079ab
```

#### System fabric graph

```mermaid
---
title: Information Supply Chain System Fabric - SAMPLE Information Supply Chain - Deployment Status Demonstration [f9d90bd0-9364-4015-a1b9-9bfff6d9a3e7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Standby**"}
2@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Development Complete**"}
subgraph 3 [System Fabric]
4@{ shape: rect, label: "*Host*
**SAMPLE-Host:Server**"}
5@{ shape: rounded, label: "*Database Manager*
**SAMPLE-DatabaseManager:Database-Manager**"}
end
5==>|"sample runs on [Lineage Mapping]"|4
1-->|"sample platform [Implemented By]"|4
2-->|"Anchor for"|5
style 1 color:#000000, fill:#DDA0DD, stroke:#000000
style 2 color:#000000, fill:#DDA0DD, stroke:#000000
style 3 color:#004563, fill:#b7c0c7, stroke:#004563
style 4 color:#FFFFFF, fill:#A9A9A9, stroke:#FFFF00
style 5 color:#000000, fill:#e0ab18, stroke:#004563
```

#### Data fabric graph

```mermaid
---
title: Information Supply Chain Data Fabric - SAMPLE Information Supply Chain - Deployment Status Demonstration [f9d90bd0-9364-4015-a1b9-9bfff6d9a3e7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Active**"}
2@{ shape: rect, label: "*Digital Product*
**SAMPLE-DigitalProduct:Provider**"}
3@{ shape: rect, label: "*Solution Component*
**SAMPLE Solution Component - Under Development**"}
subgraph 4 [Data Fabric]
5@{ shape: tag-doc, label: "*Data File*
**SAMPLE-DataFile:Source**"}
6@{ shape: cyl, label: "*Data Set*
**SAMPLE-DataSet:Target**"}
7@{ shape: subproc, label: "*Process*
**SAMPLE-Process:Load**"}
8@{ shape: subproc, label: "*Action*
**SAMPLE-Action:Review-Load**"}
9@{ shape: subproc, label: "*Process*
**SAMPLE-Process:Validate**"}
end
5==>|"Data Flow"|6
7==>|"sample load [Data Flow]"|6
5==>|"sample extract [Data Flow]"|7
7==>|"sample requests review [Action Requester]"|8
7==>|"sample then validate [Control Flow]"|9
1-->|"sample loader [Implemented By]"|7
6==>|"sample packaged as [Lineage Mapping]"|2
3-->|"Anchor for"|8
style 1 color:#000000, fill:#DDA0DD, stroke:#000000
style 2 color:#000000, fill:#838cc7, stroke:#3079ab
style 3 color:#000000, fill:#DDA0DD, stroke:#000000
style 4 color:#004563, fill:#b7c0c7, stroke:#004563
style 5 color:#000000, fill:#BDB76B, stroke:#004563
style 6 color:#000000, fill:#BDB76B, stroke:#004563
style 7 color:#000000, fill:#BDB76B, stroke:#004563
style 8 color:#000000, fill:#BDB76B, stroke:#004563
style 9 color:#000000, fill:#BDB76B, stroke:#004563
```

#### Data mapping graph

```mermaid
---
title: Information Supply Chain Data Mapping - SAMPLE Information Supply Chain - Deployment Status Demonstration [f9d90bd0-9364-4015-a1b9-9bfff6d9a3e7]
---
flowchart TD
%%{init: {"flowchart": {"htmlLabels": false}} }%%

1@{ shape: tag-doc, label: "*Data File*
**SAMPLE-DataFile:Source**"}
2@{ shape: cyl, label: "*Data Set*
**SAMPLE-DataSet:Target**"}
subgraph 3 [Data Mapping]
4@{ shape: rect, label: "*Schema Attribute*
**SAMPLE-SchemaAttribute:Source-Customer-Id**"}
5@{ shape: rect, label: "*Schema Attribute*
**SAMPLE-SchemaAttribute:Target-Customer-Id**"}
end
4==>|"sample copy [Data Mapping]"|5
1-->|"Anchor for"|4
2-->|"Anchor for"|5
style 1 color:#000000, fill:#BDB76B, stroke:#004563
style 2 color:#000000, fill:#BDB76B, stroke:#004563
style 3 color:#004563, fill:#b7c0c7, stroke:#004563
style 4 color:#ffffe0, fill:#800080, stroke:#CCFFFF
style 5 color:#ffffe0, fill:#800080, stroke:#CCFFFF
```

## Modelling Information Supply Chains

An information supply chain is represented by an [*InformationSupplyChain*](/types/7/0720-Information-Supply-Chains) entity.  This is a type of [collection](/types/0/0021-Collections).  So, its nested segments, and any parent information supply chain are organised into a hierarchy using the [*CollectionMembership*](/types/0/0021-Collections) relationship.  The handoff of control/data flow between information supply chains is captured using the [*InformationSupplyChainLink*](/types/7/0720-Information-Supply-Chains) relationship.  This relationship can also be used to link the business elements (typically [business capability](/concepts/business-capability) or [actor](/concepts/actor)) that initiates or consumes the data/control flow.

### Information Supply Chain Design

The high-level components illustrating the flow of data/control are captured by [Solution Components](/concepts/solution-component).  Providing a design is optional, but recommented since it creates a pictorial view of the flow for people that find the detail overwhelming and/or do not have access to the technical assets that are involved.  

A solution component may represent an implementation that has multiple information supply chains flowing through it.  The linkage between  the *InformationSupplyChain* and a relevant solution component uses a [CollectionMembership](/types/0/0021-Collections) relationship.  The flows between these solution component in the information supply chain's design are [SolutionLinkingWire](/types/7/0735-Solution-Ports-and-Wires) relationships that have the qualified name of the information supply chain stored in their *iscQualifiedNames* attribute.

An information supply chain segment is also represented by an *InformationSupplyChain* entity. It is also linked to its parent using the *CollectionMembership* relationship.

### Lineage Implementation

The unique identifiers/names of the information supply chain segments, or information supply chain itself, are encoded in the *iscQualifiedName* attribute of the lineage relationships captured in the lower levels of lineage detail.

The *iscQualifiedName* attribute is defined on [*LineageRelationship*](/types/0/0010-Base-Model/#lineagerelationship-relationship), so the relationships that can be tagged with an information supply chain are its subtypes:

* The [data passing](/types/7/0750-Data-Passing) relationships: DataFlow, ControlFlow and ProcessCall.
* The [lineage mapping](/types/7/0770-Lineage-Mapping) relationships: LineageMapping and DataMapping.
* The [ultimate edges](/types/7/0755-Ultimate-Source-Destination) relationships: UltimateSource and UltimateDestination.
* The [DigitalProductDependency](/types/7/0710-Digital-Products) relationship, which records that one digital product consumes data from another.  These relationships form the [data mesh](/concepts/data-mesh) and are shown in the data mesh graph when the information supply chain's implementation is displayed.  The remaining lineage relationships describe the [data fabric](/concepts/data-fabric), the systems it runs on and the mappings between data elements, and are shown in the graphs for those layers.
* The [ActionRequester](/types/0/0013-Actions) relationship, which links an action to the element that requested it.

Retrieving an information supply chain with its implementation matches on the *iscQualifiedName* alone, with no restriction on the relationship type, so any relationship type with an *iscQualifiedName* attribute can form part of an implementation.  Three relationship types that are not a *LineageRelationship* define the attribute for themselves, because each of them reveals where something's content comes from:

* [DataSetContent](/types/2/0210-Data-Stores) - the resources a data set draws on.
* [DerivedSchemaTypeQueryTarget](/types/5/0512-Derived-Schema-Elements) - the sources of a calculated data field.
* [ImplementedBy](/types/7/0737-Solution-Implementation) - the elements that implement a [solution component](/concepts/solution-component).  Tagging these with the information supply chain links its design to its implementation, and they are drawn as thin lines from the solution components into each layer graph.

The coarser-grained of these relationships do not have to be captured by hand.  The [Darwin Product Dependency Manager](/features/lineage-management/overview/#rolling-up-the-lineage) derives the data flows between data assets and processes, the data flows, process calls and control flows between software servers, and the dependencies between digital products from the finer-grained lineage beneath them, and carries the *iscQualifiedName* up from the finer-grained relationship onto the coarser one at each step, so that the whole of an information supply chain's implementation stays tagged with its name.  It spreads the supply chain downwards too: a relationship that names no *iscQualifiedName*, on a path whose supply chain is known - from another relationship on the path, or from the relationship the path proves in the layer above - is given that supply chain, or, where it lies on the paths of several, is recorded once for each.


???+ info "Further information"
    * [Lineage Management](/features/lineage-management/overview)

--8<-- "snippets/abbr.md"
