---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Governance Zone

A *governance zone* defines a list of elements that are grouped together for a specific purpose.  The governance zone is then used to scope metadata visibility for activities that are a part of supporting that purpose.

A zone may represent elements that are consumed or managed in a particular way; or should only be visible to particular groups of users, or processed by particular types of engine. There may also be zones used to indicate that the element is in a particular state.

For example, Coco Pharmaceuticals use a quarantine zone for data that has arrived from an external partner. It is not visible to the researchers until it has been cataloged and verified. Then it is added to the zones that others can see.

Zones are typically independent of one another, but they can be nested if desired.

An element can belong to all, one or many zones. The list of zones that an element belongs to is configured in the `zoneMembership` property of an attached [ZoneMembership](/types/4/0424-Governance-Zones) classification. If it is blank, or the classification is not present, it means the element logically belongs to all zones. Otherwise, it belongs only to the zones that are listed. Add or remove it from a zone by updating the element's `zoneMembership` property.

All [Open Metadata View Services (OMVS)](/concepts/omvs) that retrieve elements, support the `governanceZoneFilter` option to limit the elements retrieved by governance zone. The [metadata security connectors](/features/metadata-security/overview) can also use the zone membership to restrict the elements returned on a query or specified in a maintenance request.  The metadata security connectors can also determine the default zones for a newly created element, and supply the list of zones when an element is published.

The meaning, purpose and governance requirements for elements within a specific zone are maintained through linked [Governance definitions](/concepts/governance-definition).

!!! education "Further information"
    See [Governance Zoning](/features/governance-zoning/overview) for further information on using governance zones.


--8<-- "snippets/abbr.md"
