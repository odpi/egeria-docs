<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Governance Zoning

A *Governance Zone* defines a list of assets that are grouped together for a specific purpose. It may represent assets that are consumed or managed in a particular way; or should only be visible to particular groups of users, or processed by particular types of engine. There may also be zones used to indicate that the asset is in a particular state.  

![Figure 1](types-of-zones.svg)
> **Figure 1:** Examples of types of zones

For example, Coco Pharmaceuticals use a quarantine zone for data that has arrived from an external partner. It is not visible to the researchers until it has been cataloged and verified.  Then it is added to the zones that others can see.

![Figure 2](visiblity-rules-for-governance-zones.svg)
> **Figure 2:** Visibility rules associated with governance zones

Zones are typically independent of one another, but they can be nested if desired.  They help to support the following types of use cases:

* Data sovereignty
* Adjustments for legal jurisdiction
* Asset visibility and access control
* Data access control
* Maintenance and backup processing
* Understanding dependencies
* Metering and billing

An asset can belong to all, one or many zones.  The list of zones that an asset belongs to is configured in
the `zoneMembership` property of its [`AssetZoneMembership` classification](/types/4/0424-Governance-Zones/).  If it is blank, it means the asset logically belongs to all zones.  Otherwise it belongs only to the zones that are listed.  It is added to or removed from a zone by updating the AssetZoneMembership classification.

![Figure 3](asset-in-many-zones.svg)
> **Figure 3:** Examples of types of zones

When designing the governance zones for your organization, it is necessary to take care that the visibility rules associated with an asset's zones are complementary rather than conflicting.

![Figure 4](multi-zone-membership.svg)
> **Figure 4:** Thinking through the meaning of belonging to multiple zones


All Open Metadata Access Services (OMASs) that retrieve assets, such as [Asset Catalog](/services/omas/asset-catalog/overview), [Asset Consumer](/services/omas/asset-consumer/overview) and [Asset Owner](/services/omas/asset-owner/overview), use the **supportedZones** option that is configured for the service in the in their server's configuration document.  This property defines the zones of assets that can be returned by this instance of the access service.

In addition, access services that create assets, use the **defaultZones** option to define
the list of zones set up in any new asset they create.

Finally access services that are synchronizing assets between different third party
technologies, such as the [Data Manager OMAS](/services/omas/data-manager/overview), will also use the
**publishZones** option to publish an asset to consumer zones once they are completely defined in the
catalog.

![Figure 5](governance-zone-access-setting-examples.svg)
> **Figure 5:** Visibility setting in the Open Metadata Access Services (OMASs)

The meaning, purpose and governance requirements for assets within a specific zone are maintained through the [Governance Program OMAS](/services/omas/governance-program/overview).

It is also possible to associate [security access control with a governance zone](/festures/metadata-security/overview).



--8<-- "snippets/abbr.md"