---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# 0740 Solution Blueprints

A *SolutionBlueprint* describes the architecture of a digital service in terms of [solution components](/types/7/0730-Solution-Components).

## DigitalServiceDesign

There can be multiple solution blueprints for a digital service that each describe a version of its implementation.
The *DigitalServiceDesign* relationship identifies which [digital service](/types/7/0710-Digital-Service) the blueprint describes.

## SolutionBlueprintComposition

The *SolutionBlueprintComposition* relationship identifies the list of solution components that implement the digital service.  The definition of the solution components shows [how they are linked together](/types/7/0735-Solution-Ports-and-Wires) and so SolutionBlueprintComposition simply documents the role each solution component plays in supporting the digital service.

![UML](0740-Solution-Blueprints.svg)


--8<-- "snippets/abbr.md"