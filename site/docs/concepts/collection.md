<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Collections

A collection is a reusable list of metadata elements.  [Assets](/concepts/asset) and other [referenceable](/concepts/referenceable) metadata elements can be linked to a collection. The collection itself can then be added to another collection, or linked to, say a [community](/concepts/community) or a [personal profile](/concepts/personal-profile).

Collections have classifications to indicate how they are being used. Below are some examples of collections deployed in different scenarios.  The type definitions for collections are found in [model 0021](/types/0/0021-Collections).

## Asset catalog hierarchy

Some asset catalogs organize their catalogued resources in a hierarchical folder structure, where each folder represents a particular theme. This allows people to browse the entries in a systematic way.  Since the folder structure organizes similar assets together, it is easier to compare entries and pick the best one for the use case.

Collections can be used to provide the folder structure.  The top of the hierarchy is typically classified with the *RootCollection* classification.  The nested collections linked underneath it are classified with the *Folder* classification.  The relationships linking the hierarchy and the assets together are of type *CollectionMembership*.

![Asset Folder Structure](collections-asset-catalog.svg)

## Product catalog organization

[Digital products](/concepts/digital-product) offer data sets and services that have been developed for a particular purpose.  They are typically versioned, and may offer the data/function in multiple formats.  

Collections are used in two ways for digital products.  Each digital product is represented using a collection with the [*DigitalProduct*](/types/7/0710-Digital-Service) classification attached.  The digital products are often organized in a folder hierarchy, like the asset catalog.

![Product catalog](collections-product-catalog.svg)

## Home collections

Home collections are used to organize elements for a particular person, team, project or community.  They are linked to the element representing the people they are supporting using the [ResourceList](/types/0/0019-More-Information) relationship.  An example of a home collection could be a favourites list.

![Home collections](collections-home-collections.svg)

## Work Item List

[ToDos](/concepts/to-do) describe actions for people to perform.  They are attached to one or more chosen [*actors*](/types/1/0110-Actors).  Collections with the *WorkItemList* can be used to organize these *ToDos* to help prioritize the work.

![Work Item List](collections-work-item-list.svg)

## Results Sets

Collections can be used by automated services, typically [governance services](/concepts/governance-service), to gather the results of their processing together.  Such a collection would have the *ResultsSet* classification attached to it.

For example, the results set collection shown below is from a governance service that is identifying assets that should be archived (for example, by reviewing their [Retention](/types/4/0422-Governed-Data-Classifications) classification).

![Service Results Sets](collections-results-set-1.svg)

This next example is from a governance service that is periodically processing a saved query, building up the results set over time as new metadata is created.

![Search Results Sets](collections-results-set-2.svg)

## Recent Access

User interfaces can keep track of the metadata elements that a particular user is working with, so they can quickly access them.  Such a collection would be chained off of the individual's *Person* element using the *ResourceList* relationship.  The collection would have the *RecentAccess* classification attached.

![Recent Access](collections-recent-access.svg)

???+ education "Further Information on Collections"
    The [Collection Manager OMVS](/services/omvs/collection-manager/overview) provides a specialist API for managing collections.

--8<-- "snippets/abbr.md"