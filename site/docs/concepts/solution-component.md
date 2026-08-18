<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Solution Component

*Solution components* provide an architectural summary of the logical components that make up the IT landscape.  Each one is an architecture description of a digital implementation that performs a well-defined function - the equivalent of a UML component.

Solution components sit at a deliberately coarse grain.  They are held in the open metadata repository to give business context to the [assets](/concepts/asset) they describe: a solution component says *this is the part of the landscape that does X*, without committing to which server, which database or which release currently implements it.

## Assembling a solution

* Solution components are gathered into a [solution blueprint](/concepts/solution-blueprint), which shows how they work together to deliver a business solution.
* The *SolutionComposition* relationship decomposes a component into smaller components, so a blueprint can be read at whatever level of detail the discussion needs.
* [Solution ports and wires](/types/7/0735-Solution-Ports-and-Wires) show how the components communicate with each other.
* A *SolutionActorRole* is an [actor role](/concepts/actor-role) that interacts with a solution.  The *SolutionComponentActor* relationship records which roles interact with which components - which is how a blueprint shows the people alongside the technology.

## From architecture to implementation

Two relationships provide traceability from the design down to what was actually built:

* *ImplementedBy* records how a solution component - or a design model element - is refined into an implementation artifact.
* *ImplementationResource* identifies the components that are useful when building that implementation.

Both ends are referenceables, so an organization can capture as much or as little of the chain as is useful to it.

???+ info "Additional information"
    * The *SolutionComponent* and *SolutionActorRole* types are described in [Model 0730 Solution Components](/types/7/0730-Solution-Components); the traceability relationships are in [Model 0737 Solution Implementation](/types/7/0737-Solution-Implementation).
    * The [Solution Architect API](/services/omvs/solution-architect/overview) provides the operations for defining solution blueprints and their components.

--8<-- "snippets/abbr.md"
