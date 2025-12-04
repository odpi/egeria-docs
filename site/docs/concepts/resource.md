---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019. -->

# Resource

The term *resource* is used throughout the Egeria documentation to refer to something - either physical or digital - that is of value to the operation of the organization, or to the services it provides.

Examples of resources include:

- Data sources such as databases, files and data feeds.
- IT infrastructure and applications that automate many aspects of an organization's operation.
- APIs that provide access to the services offered by the organization.
- Analytical models and processes.
- Addresses and other locations.
- Physical objects such as buildings that can have a digitized representation with a unique identity (for example, serial number).
- People allocated to a project.

[Digital Resources](/concepts/digital-resource) and physical resources (such as computers, buildings etc) are described in open metadata as [Assets](/concepts/asset).  People and teams are captured using [Actors and Person Roles](/features/people-roles-organizations/overview)

In addition, the organization may capture many types of descriptions and definitions that describe their operations in open metadata, such as, for example, a [glossary term](/practices/common-data-definitions/anatomy-of-a-glossary/#inside-a-glossary-term) or a [governance definition](/services/omvs/governance-officer/overview). These elements can be [linked to the asset](/patterns/metadata-manager/overview) to provide more information on the resource's content, significance and proper use to the people working with the resource as well as guiding automated processes that are managing and governing it.

!!! education "ResourceList relationship"
    The [ResourceList](/types/0/0019-More-Information) relationship allows the list of resources allocated to a particular activity to be linked to the open metadata element that represents the activity.

--8<-- "snippets/abbr.md"
