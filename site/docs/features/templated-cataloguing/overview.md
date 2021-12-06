---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Templated cataloging

When a new resource is catalogued, the catalog entry of a similar
resource can be supplied and it is used as a template to set up the new resource.

Templated cataloguing is useful for situations where new resources are regularly catalogued that are of the same kind.

## An example

[Peter Profile](https://opengovernance.odpi.org/coco-pharmaceuticals/personas/peter-profile.html) is responsible for cataloguing the weekly measurements supplied by the various hospitals as part of a clinical trial.  These measurements are supplied with certain terms and conditions (also known as a license) that Coco Pharmaceuticals must not only adhere to, but prove that they are doing so.  For that reason, when the measurements are catalogued, the [asset](/egeria-docs/concepts/asset) for the measurements data set is linked to the license as well as other elements that help to ensure that the measurements data sets are appropriately used and governed.

Figure 1 shows Peter making calls to Egeria to catalog the first set of measurements received for the clinical trial.  This includes an asset to represent the data set that is linked to the license along with a connection to allow the data scientist to connect to the data set and access the data and the schema showing the structure of the data in the data set.  The data fields identified in the schema each link to the glossary term that describes the meaning of the data stored in the field. There are also two classifications on the asset:

- *AssetZoneMembership* - The [governance zones](/egeria-docs/concepts/governance-zone) that the asset is a member of.  This controls who can access the asset and its related metadata elements such as the connection and the schema.
- *Ownership* - The owner of the data set.  This is the person who is accountable for ensuring that Coco Pharmaceuticals adheres to the license.

![Figure 1](cataloging-assets-week-1.svg)
> **Figure 1:** In week 1, Peter manually creates the asset and links it to the governance elements needed to ensure the data set is used and protected as laid out in the license.

The catalog entry for the Week 1 measurements can then be used as a template for cataloguing the subsequent weeks' measurements as shown in figure 2.

![Figure 2](cataloging-assets-week-2.svg)
> **Figure 2:** For subsequent weeks, the week 1 entry is used as a template for cataloguing subsequent weeks.  The result is an asset for each data set with a connector, a schema along with the ownership and zone membership classifications.  All of the assets are linked to the license and the data fields in each schema are linked to the correct glossary terms.

Egeria uses the [anchor](/egeria-docs/features/anchor-management/overview) classification to determine which entities are duplicated from the template and which entities are just linked to.  In figure 2, the connection and schema are anchored to the asset whilst the glossary terms and license are not.

## SourcedFrom relationship and Template classification

An entity that is being used as a template can be given the [`Template`](/egeria-docs/types/0/0011-Managing-Referenceables) classification to make it easier to find and understand what it is used for.

When an entity is used as a template, it is linked to the resulting new entity with the [`SourcedFrom`](/egeria-docs/types/0/0011-Managing-Referenceables) relationship.  This makes it easier to identity the entities that need changing if the template needs to be corrected or enhanced.

## Support for templated cataloguing

The [Asset Owner OMAS](/egeria-docs/services/omas/asset-owner),
[IT Infrastructure OMAS](/egeria-docs/services/omas/it-infrastructure) and [Digital Architecture OMAS](/egeria-docs/services/omas/digital-architecture) provides the ability to set up and use templates to catalog new assets.

## Adding automation

It is also possible to use templates in the connectors running during [Integrated cataloguing](/egeria-docs/feaatures/integrated-cataloguing).

--8<-- "snippets/abbr.md"