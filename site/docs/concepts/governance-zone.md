---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Governance Zone

A *governance zone* defines a list of assets that are grouped together for a specific purpose.

A zone may represent assets that are consumed or managed in a particular way; or should only be visible to particular groups of users, or processed by particular types of engine. There may also be zones used to indicate that the asset is in a particular state.

For example, Coco Pharmaceuticals use a quarantine zone for data that has arrived from an external partner. It is not visible to the researchers until it has been cataloged and verified. Then it is added to the zones that others can see.

Zones are typically independent of one another, but they can be nested if desired.

An asset can belong to all, one or many zones. The list of zones that an asset belongs to is configured in its `zoneMembership` property. If it is blank, it means the asset logically belongs to all zones. Otherwise, it belongs only to the zones that are listed. Add or remove it from a zone by updating the asset's `zoneMembership` property.

All [Open Metadata Access Services (OMAS)](/egeria-docs/concepts/omas) that retrieve assets, such as [Asset Catalog](/egeria-docs/services/omas/asset-catalog/overview), [Asset Consumer](/egeria-docs/services/omas/asset-consumer/overview) and [Asset Owner](/egeria-docs/services/omas/asset-owner/overview), use the `supportedZones` option that is configured for the service in their server's configuration document. This property defines the zones of assets that can be returned by this instance of the access service.

In addition, access services that create assets use the `defaultZones` option to define the list of zones set up in any new asset they create.

Finally, access services that are synchronizing assets between different third party technologies, such as the [Data Manager OMAS](/egeria-docs/services/omas/data-manager/overview), will also use the `publishZones` option to publish an asset to consumer zones once they are completely defined in the catalog.

The meaning, purpose and governance requirements for assets within a specific zone are maintained through the [Governance Program OMAS](/egeria-docs/services/omas/governance-program/overview).

It is also possible to associate [security access control with a governance zone](/egeria-docs/features/metadata-security/overview).

--8<-- "snippets/abbr.md"
