---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0710 Digital Service

The *DigitalService* entity provides a root element for a digital capability that is significant to the owning organization.  This type of capability is referred to as a [Digital Service](/practices/digital-services/overview) in open metadata.  It may be implemented by many [digital resources](/concepts/resource) such as APIs, data sets, and software components.

The *DigitalProduct* classification identifies an element that represents a digital product that is typically advertised in a marketplace. A data product is an example of a digital product.  A *DigitalService* can consist of multiple *DigitalProducts*.

![UML](0710-Digital-Service.svg)

The *DigitalServiceDependency* allows an organization to show the dependencies between digital services.  The nature of the dependency is supplied in the *description* property.

The architecture of a digital service is described in a [solution blueprint](/types/7/0740-Solution-Blueprints) made up of [solution components](/types/7/0730-Solution-Components).  The *SolutionComponents* have [SolutionPorts](/types/7/0735-Solution-Ports-and-Wires) that describe the inputs and outputs of the solution components and how they are linked together.  A *SolutionPort* can represent the digital products that are linked to the solution components that provide the implementation of the production/maintenance processes and delivery processes.

--8<-- "snippets/abbr.md"