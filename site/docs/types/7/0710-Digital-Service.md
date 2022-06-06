---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0710 Digital Service

The *DigitalService* entity provides a root element for a digital capability that is significant to the owning organization.  This type of capability is referred to as a [Digital Service](/practices/digital-services/overview) in open metadata.  It may be implemented by many [digital resources](/concepts/resource) such as APIs, data sets, and software components.

![UML](0710-Digital-Service.svg)

The *DigitalServiceDependency* allows an organization to show the dependencies between digital services.  The nature of the dependency is supplied in the *description* property.

The architecture of a digital service is described in a [solution blueprint](/types/7/0740-Solution-Blueprints) made up of [solution components](/types/7/0730-Solution-Components).

--8<-- "snippets/abbr.md"