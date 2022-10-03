<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Defining valid values for your open metadata

The [open metadata types](/types) include properties that are string values.  These string values give you freedom and flexibility to add the values you want.  However, arbitrary strings can make automation hard and you may want to set up some more formal definitions of the values that should be used.

Consider the *ProjectCharter* entity type shown below.  In addition to the *qualifiedName* and *additionalProperties* properties inherited from *Referenceable*, this type adds in three new properties:

* *mission*
* *projectType*
* *purposes*

![ProjectCharter type](/types/4/0442-Project-Charter.svg)

The *mission* property is likely to be free-form text laying out the reasons and aspirations behind the project.  However, the *projectType* and the *purposes* may be used by automated processes - or may trigger people to perform certain tasks.  Having free-form text may lead to errors and misunderstandings.  Therefore, Egeria supports the ability to set up lists of valid values for particular properties in open metadata.

Part of the planning process is to consider which properties should have restricted values and which can be free-form text since setting these up early avoids reworking the metadata values later.


## Specialized valid metadata values

Some properties have special types for maintaining valid value lists.

* The governance *domainIdentifiers* can be set up in the [Governance Domain Descriptions](/guides/planning/governance-program/overview/#governance-domains).
* The [governance zones](/concepts/governance-zone) are set up using the [Governance Zone](/services/omas/governance-program/overview/#governance-classification,-tagging-and-linking) entity.
* The *statusIdentifiers* used in many governance-related entities, relationships and classifications can be defined using the [GovernanceStatusLevel](/services/omas/governance-program/overview/#governance-status-identifers) entity.

## Creating your own valid value sets for open metadata

For other metadata properties it is possible to set up *valid metadata sets*.  These list the values that are expected in a particular property and provide validation checks.

The support for this capability is through the [OpenMetadataClient](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceprogram/client/OpenMetadataStoreClient.html) available on most [Open Metadata Access Services (OMASs)](/services/omas)

--8<-- "snippets/abbr.md"
