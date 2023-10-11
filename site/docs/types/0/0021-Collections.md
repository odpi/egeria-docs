<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0021 Collections

*Collection*s provide a general mechanism for grouping entities together.  A collection may be maintained manually, or via an automated process (ie a "smart collection").  The membership of a collection is established via a [*CollectionMembership* relationship](#collectionmembership-relationship), which has attributes that allow the rationale and the confidence of the membership to be established. A [*Referenceable*](/types/0/0010-Base-Model) entity can be a member of none, one or many collections.  

Since a collection is a *Referenceable* entity, collections can be organized into hierarchies - like a directory structure on the filesystem.


![UML](0021-Collections.svg)

## Collection

The *Collection* entity provides the node that represents the collection as a whole.  It inherits from [*Referenceable*](/types/0/0010-Base-Model).

The attributes for a collection, beyond the standard attributes for *Referenceable* include:

* *name* - this is the display name for the collection
* *description* - this is the text that describes the characteristics of the members that are to be found in the collection.
* *collectionType* - describes the type of collection that is used to select its icon or display layout.  For example, it may be a "theme", or "domain", or something else.

## Collection classifications

The classifications associated with *Collection* allow it to be specialized for particular uses.  They help when searching for collections for specific uses.

* [*RootCollection*](#root-collection-classification) means the collection is the top-level node in a collection hierarchy.  The members of this collection are typically all collections.
* [*Folder*](#folder-classification) means the collection can be treated as if it where a folder of metadata elements.  This classification includes properties to control how the members are displayed.
* [*Set*](#set-classification) means the collection is a set of related entities and no entity is a member more than once.
* [*DigitalProduct*](/types/7/0710-Digital-Service) describes a collection of [assets](/concepts/asset) that represent a digital product.
* [*GovernanceStatusSet*](/types/4/0421-Governance-Classification-Levels) for a collection of governance statuses.
* [*GovernanceClassificationSet*](/types/4/0421-Governance-Classification-Levels) for a collection of governance classification for a particular governance classification.
* [*EventSet*](/types/5/0421-Governance-Classification-Levels) for a collection of related event schemas.

The example below shows part of a collection hierarchy representing a digital product catalog.  The collections are shown in green and the assets that provide the content for the digital product are shown in yellow.

The collection at the root of the collection hierarchy is called "Product Catalog Collection" and has the *RootCollection* classification attached.  Its membership consists of collections with the *Folder* classification.  The leaf node collections have the *DigitalProduct* classification attach and have the data assets as their members.

![Collection Hierarchy](collection-hierarchy-example.svg)

### RootCollection classification

The *RootCollection* classification indicates that the collection is used to provide the starting node for a hierarchy of collections.

### Folder classification

The *Folder* classification indicates that the collection is used to organize metadata elements.  The attributes are used to indicate to the caller how they should be displayed.

* *orderBy* indicates the preferred ordering sequence
* *orderPropertyName* indicates which property to use if the *orderBy* attribute is set to `OTHER`.

### OrderBy enumeration

* *Name* - Order by name property.
* *Owner* - Order by owner property.
* *DateAdded* - Order by date added to the metadata collection.
* *DateUpdated* - Order by date that the asset was updated.
* *DateCreated* - Order by date that the asset was created.
* *Other* - Order by another property.

### Set classification

The *Set* classification indicates that the collection is a set of elements where each element is only included in the collection once.

## CollectionMembership relationship

The *CollectionMembership* relationship is used to link a [*Referenceable*](/types/0/0010-Base-Model) entity to a *Collection* entity to indicate that it is a member of the collection.

The *Collection* entity inherits from [*Referenceable*](/types/0/0010-Base-Model) so a collection can be a member of other collections.  For example, it is possible to create a nested set of folders for [assets](/concepts/assets).

![Asset Folder Hierarchy](asset-folder-hierarchy.svg)

The attributes for the *CollectionMembership* relationship establish the level of trust to give to a member's right to be part of the collection:

* The *membershipRationale* attribute describes why the member is part of the collection.
* The *expression* attribute indicates the expression used to decide on the membership.  This is typically set up by automated processes to identify the rule they used to determine the membership.
* The *confidence* attribute indicates how confident that the membership is correct.
* The *createdBy* attribute is the identifier of the process or person that created (curated) the relationship.  This is useful for identifying the instance of a process that created the membership relationship or the curator if they are different from the steward.
* The *source* attribute describes the source of information that identified this membership.
* The *steward* attribute identifies the person that is accountable for the correctness of this membership relationship.
* The *stewardTypeName* attribute identifies the type of element (such as UserIdentity, Person, PersonRole) that is responsible for the correctness of this relationship.
* The *stewardPropertyName* attribute identifies the property (such as guid or qualifiedName) used to identify the steward.
* The *notes* attribute enables the steward to add additional information about this relationship.
* The *status* attribute indicates the status of the member in the collection.  It is a [MembershipStatus](#membershipstatus-enumeration) value.
* The *userDefinedStatus* provides a status value when *status=OTHER*.

## MembershipStatus enumeration

The values for the *MembershipStatus* enumeration are:

* *Unknown* - The membership origin is unknown. This is the default value.
* *Discovered* - The membership was discovered by an automated process.
* *Assigned* - The membership was proposed by an expert curator.  The curator uses their expertise to create the membership. They may or may not be the steward who is ultimately accountable for the correctness of the membership.
* *Imported* - The membership was imported from another metadata system.
* *Validated* - The membership created by an automated process has been validated and approved by an expert curator.  Again, the curator may or may not be the steward.
* *Deprecated* - The membership should no longer be used.
* *Obsolete* - The membership must no longer be used.
* *Other* - Another membership status that is set up in the *userDefinedStatus* attribute.

They can be used to support a simple stewardship workflow.  For example, consider a [governance action](/concepts/governance-action) that scans through the [assets](/concepts/asset) examining each one's [Retention](/types/4/0422-Governance-Action-Classifications) classification.  If the values in the classification indicate that the [resource](/concepts/resource) that it represents should be archived, it may link the asset into a collection.

![Candidate assets for archive](archive-candidate-collection.svg)

The status value could be *Discovered* in each *CollectionMembership* relationship.  Once the collection is complete, the governance action could trigger a [request to a steward](/types/1/0137-Actions) to verify the list.  The steward could update the *CollectionMembership* status to either:

* *Validated* - The resource should be archived.
* *Obsolete* - The resource should be retained.

Once the review is complete, another governance action would drive the archive process for all resources indicated by the *CollectionMembership* relationships with *Validated* status.

--8<-- "snippets/abbr.md"
