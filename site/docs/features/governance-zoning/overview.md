<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Governance Zoning

A *Governance Zone* defines a list of elements, such as [assets](/concepts/asset)  or [digital products](/concepts/digital-product) that are grouped together for a specific purpose. It may represent elements that are consumed or managed in a particular way; or should only be visible to particular groups of users, or processed by particular types of engine. There may also be zones used to indicate that the element is in a particular state.  

![Figure 1](/features/governance-zoning/types-of-zones.svg)
> **Figure 1:** Examples of types of zones

For example, Coco Pharmaceuticals use a quarantine zone for data that has arrived from an external partner. It is not visible to the researchers until it has been cataloged and verified.  Then it is added to the zones that others can see.

![Figure 2](/features/governance-zoning/visiblity-rules-for-governance-zones.svg)
> **Figure 2:** Visibility rules associated with governance zones

Zones are typically independent of one another, but they can be nested if desired.  

## Defining governance zones

Governance zones are defined as part of the governance program.  They are stored in open metadata as
[`GovernanceZone`](/types/4/0424-Governance-Zones) entities.  They can be linked to [governance definitions](/features/governance-program/overview) that may directly or indirectly identify the visibility rules that apply to the zone.

![Figure 3](/features/governance-zoning/defining-visibility-rules.svg)
> **Figure 3:** Visibility rules associated with governance zones

The visibility rules associated with the zones are typically executed [via the server security connector](/concepts/server-metadata-security-connector) that can both dynamically assign/augment the zones for an element before its security is checked and then use the setting of the element's zones to determine if the requested action by the requested user is allowed.  The security connector may also delegate this decision to [an external security manager](/features/synchronizing-access-security/overview) where the zone information is typically transforming into security tags or settings in access control lists (ACLs).

## Use cases

Governance zones help to support the following types of use cases:

* Data sovereignty - by defining zones that represent the origin of data and using visibility rules that match consumer to origin.
* Adjustments for legal jurisdiction - by defining zones for each jurisdiction and attaching appropriate rules to each.
* Asset visibility and access control - by defining zones that group elements into 
* Data access control - using the zones assigned to the element [when setting up security tags](/features/synchronized-access-control/overview/#consolidate).
* Maintenance and backup processing - by defining zones that represent different archiving or maintenance requirements.  The engines that perform the automated maintenance work through the list of elements in the relevant zones.
* Understanding dependencies between different parts of the organizations to support the information supply chains - by defining zones for different parts of the organization and visualizing 
* Metering and billing - by defining zones that represent the cost structure of assets and using the zone membership of assets being used to determine the charge.



## Membership of a zone

An element can belong to all, one or many zones.  By default, it belongs to all zones. The [ZoneMembership classification](/types/4/0424-Governance-Zones/) is used to restrict its visibility by specifying the list of zones that it belongs to in the `zoneMembership` property.  If zoneMembership is null or empty, the element belongs to all zones, as if the element has no ZoneMembership classification.  Otherwise, it belongs only to the zones that are listed.  It is added to or removed from a zone by updating the ZoneMembership classification.

For example, as new data sets are onboarded, the setting of the templates or governance action services can ensure that the assets that represent these data sets are assigned to the right set of zones as they are added to the catalog.  The zones can then be maintained as needed throughout the lifetime of the assets.  If the assets become part of a digital product, their zone membership may be updated to match the zones for the overall digital product.  

![Figure 4](/features/governance-zoning/asset-in-many-zones.svg)
> **Figure :** Examples of types of zones

When designing the governance zones for your organization, it is necessary to take care that the visibility rules associated with an element's zones are complementary rather than conflicting.

Here is an example:

![Figure 5](/features/governance-zoning/multi-zone-membership.svg)
> **Figure 5:** Thinking through the meaning of belonging to multiple zones

## Default zone settings

A [Metadata Access Store](/concepts/metadata-access-store) can be configured with a list of zones to be assigned to new elements of a particular type.  If the type for a new element is not featured in the default zones configuration then no zones are assigned to the element.

The default zones can be used to limit the number of users that can retrieve an element when it is first created.  Once it is completely set up and approved, the ones can be updated to widen its visibility. One way to do this is using the publish zones.

## Publish zone settings

A [Metadata Access Store](/concepts/metadata-access-store) can also be configured with a list of zones to be assigned to elements of particular types when they are published.  Publishing means calling the `publish` method on the open metadata interface.

There is also a `withdraw` method.  This sets the governance zones of an element back to the default zones setting for its type.  For example, if a number of changes need to be made to an element and while this is happening, the element should not be visible to general users, calling withdraw will set ip back to its initial zone settings.  Once the updates are complete, the element can be published again to broaden its visibility.

Changing an element's visibility can be achieved by updating the elements zone membership through [Classification Manager](/services/omvs/classification-manager).  The `publish` and `withdraw` methods externalize the list of zones that need to be set into ZoneMembership rather than having these values hard coded in various connectors and external programs.

## Filtering query results using governanceZoneFilter

The [Open Metadata View Services (OMVSs)](/services/omvs) have a **governanceZoneFilter** option on query requests that allow the caller to further restrict the elements returned based on their governance zone membership.  

> Note: This filtering is done after the security connector has filtered out elements that are not visible to the calling user.



--8<-- "snippets/abbr.md"