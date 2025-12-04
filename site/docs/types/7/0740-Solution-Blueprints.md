
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# 0740 Solution Blueprints

A [solution blueprint](/concepts/solution-blueprint) is a collection of [solution components](/types/7/0730-Solution-Components) that describe the architecture of a digital service, or a new capability.

![UML](0740-Solution-Blueprints.svg)

## SolutionBlueprint entity

The *SolutionBlueprint* entity describes a single version of the digital service's architecture.  It inherits from [DesignModel](/types/5/0565-Design-Models) which is a type of [Collection](/types/0/0021-Collections).
The [*CollectionMembership*](/types/0/0021-Collections) relationship identifies the list of solution components that implement the digital service.  The definition of the solution components shows [how they are linked together](/types/7/0735-Solution-Ports-and-Wires) and so SolutionBlueprintComposition simply documents the role each solution component plays in supporting the digital service.

## SolutionDesign relationship

There can be multiple solution blueprints for an architecture.  For example:

* to describe a version of the architecture.
* to define an aspect of the architecture.
* to describe different levels of detail.

The *SolutionDesign* relationship identifies which [element](/types/0/0010-Base-Model) the blueprint describes.  Its attributes identify what aspect of the architecture is covered by the blueprint.




--8<-- "snippets/abbr.md"