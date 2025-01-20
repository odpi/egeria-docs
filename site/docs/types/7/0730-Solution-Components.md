<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0730 Solution Components

Solution components proves an architectural summary of the logical components that make up the IT landscape.  These components are linked together via [Solution Ports and Wires](/types/7/0735-Solution-Ports-and-Wires)

![UML](0730-Solution-Components.svg)

## SolutionComponent entity

A *SolutionComponent* is an architecture description of a digital implementation that provides a well-defined function.  They can be modelled as *UML components* and provide a way to organize the digital landscape into course-grained functional components. Solution components communicate via [ports and wires](/types/7/0735-Solution-Ports-and-Wires).

## SolutionComposition relationship

The *SolutionComposition* relationship allows solution components to be decomposed into smaller solution components.

## SolutionActorRole entity

A *SolutionActorRole* is a type of [ActorRole](/types/1/0118-Actor-Roles) that is principally interacting with a solution.

## SolutionComponentActor relationship

The *SolutionComponentActor* records the [Actors](/types/1/0110-Actors) that are interacting with the solution components.  Typically, these are *SolutionActorRole* entities.

--8<-- "snippets/abbr.md"