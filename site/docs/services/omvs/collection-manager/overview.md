<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Collection Manager OMVS

The Collection Manager Open Metadata View Services (OMVS) is a REST API designed to back user interfaces (UIs) that support the maintenance and browsing of hierarchies of [collections](/concepts/collection) and their members.

Collections are used to organize elements.  Elements (including other collections) are linked to a collection to show that they are a member of the collection.  An element can be a member of none, one or multiple collections.

There are different types of collections that are identified by their classifications and *collectionType* property.  These are some examples:

* **Root Collection** - A root collection is the root node of a hierarchy of collections.  Its members are typically other collections.
* **Folder** - a folder is a collection that is part of a collection hierarchy structure.  It may have members that are collections and/or other types of elements.
* **Digital Product** - A [digital product](/concepts/digital-product) is a collection of [assets](/concepts/asset) that have been especially crafted to support a specific use case (or related use cases).  The assets may represent different versions of the product or customized versions of the same data for different purposed, or supporting different non-functional requirements.

The Collection Manager OMVS supports:

* The creation and maintenance of the properties associated with a collection.  New collections can be created using another collection as a template.
* The management of the members of a collection.
* The attachment of a collection as a resource of an entity such as a project, community or user's profile.
* The ability to create a collection using another collection as a template.
* The ability to search collections, with or without particular classifications and properties and navigate through a collection's membership.

## Managing collection entities

When working with collections, there are 4 concepts that you need to keep in mind:

* Which elements, if any, is the collection linking to.  These elements are called the parent elements.
* Is the collection its own [anchor](/featires/anchor-management/overview) or is it anchored to another element.
* What values should be assigned to it attributes.
* Which classifications should be added to the collection to indicate its purpose and usage.

### createCollection (no parent relationship)

This first example of a create request is for a collection that is its own anchor and is to be created without a parent.  The placeholder property `{{classificationName}}` is set to a [valid classification name](/types/0/0021-Collections/#collection-classifications) for the collection.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections?classificationName={{classificationName}}
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "isOwnAnchor" : true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "Must provide a unique name here",
    "name" : "Add display name here",
    "description" : "Add description of the collection here",
    "collectionType": "Add appropriate valid value for type"
  }
}
```
### createCollection (with parent)



```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "anchorGUID" : "anchor GUID, if set then isOwnAnchor=false",
  "isOwnAnchor" : false,
  "parentGUID" : "parent GUID, if set, set all parameters beginning 'parent'",
  "parentRelationshipTypeName" : "open metadata type name",
  "parentAtEnd1": true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "Must provide a unique name here",
    "name" : "Add display name here",
    "description" : "Add description of the collection here",
    "collectionType": "Add appropriate valid value for type"
  }
}
```
### createRootCollection
Create a new collection with the RootCollection classification.  Used to identify the top of a collection hierarchy.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/root-collection
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "anchorGUID" : "anchor GUID, if set then isOwnAnchor=false",
  "isOwnAnchor" : false,
  "parentGUID" : "parent GUID, if set, set all parameters beginning 'parent'",
  "parentRelationshipTypeName" : "open metadata type name",
  "parentAtEnd1": true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "Must provide a unique name here",
    "name" : "Add display name here",
    "description" : "Add description of the collection here",
    "collectionType": "Add appropriate valid value for type"
  }
}
```

### createDataSpecCollection
Create a new collection with the DataSpec classification.  Used to identify a collection of data fields and schema types.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/data-spec-collection
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "anchorGUID" : "anchor GUID, if set then isOwnAnchor=false",
  "isOwnAnchor" : false,
  "parentGUID" : "parent GUID, if set, set all parameters beginning 'parent'",
  "parentRelationshipTypeName" : "open metadata type name",
  "parentAtEnd1": true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "Must provide a unique name here",
    "name" : "Add display name here",
    "description" : "Add description of the collection here",
    "collectionType": "Add appropriate valid value for type"
  }
}
```
### createFolderCollection
Create a new collection with the Folder classification.  This is used to identify the organizing collections in a collection hierarchy.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/folder
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "NewCollectionRequestBody",
  "anchorGUID" : "anchor GUID, if set then isOwnAnchor=false",
  "isOwnAnchor" : false,
  "parentGUID" : "parent GUID, if set, set all parameters beginning 'parent'",
  "parentRelationshipTypeName" : "open metadata type name",
  "parentAtEnd1": true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "Must provide a unique name here",
    "name" : "Add display name here",
    "description" : "Add description of the collection here",
    "collectionType": "Add appropriate valid value for type",
    "collectionOrdering" : "OTHER",
    "orderPropertyName" : "Add property name if 'collectionOrdering' is OTHER"
  }
}
```
### createCollectionFromTemplate
Create a new metadata element to represent a collection using an existing metadata element as a template.
The template defines additional classifications and relationships that should be added to the new collection.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/from-template
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class": "TemplateRequestBody",
  "anchorGUID": "anchor GUID, if set then isOwnAnchor=false",
  "isOwnAnchor": false,
  "parentGUID": "parent GUID, if set, set all parameters beginning 'parent'",
  "parentRelationshipTypeName": "open metadata type name",
  "parentAtEnd1": true,
  "templateGUID": "template GUID",
  "replacementProperties": {
    "class": "ElementProperties",
    "propertyValueMap" : {
      "propertyName" : {
        "class": "PrimitiveTypePropertyValue",
        "typeName": "string",
        "primitiveTypeCategory" : "OM_PRIMITIVE_TYPE_STRING",
        "primitiveValue" : "value of property"
      }
    }
  },
  "placeholderPropertyValues" : {
    "placeholderProperty1Name" : "property1Value",
    "placeholderProperty2Name" : "property2Value"
  }
}

```

### updateCollection
Update the properties of a collection.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/update?replaceAllProperties=false
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "CollectionProperties",
  "qualifiedName": "Must provide a unique name here",
  "name" : "Add display name here",
  "description" : "Add description of the collection here",
  "collectionType": "Add appropriate valid value for type"
}
```


### deleteCollection

Delete a collection.  It is detected from all parent elements.  If members are anchored to the collection
then they are also deleted.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/delete
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "NullRequestBody"
}
```

## Managing digital products

### createDigitalProduct

Create a new collection that represents a digital product.
Note: the three dates: introductionDate, nextVersionDate and withdrawDate must be valid dates if specified,
otherwise you will get a 400 error response.
The valid values for productStatus are: DRAFT, PREPARED, PROPOSED, APPROVED, REJECTED, APPROVED_CONCEPT,
UNDER_DEVELOPMENT, DEVELOPMENT_COMPLETE, APPROVED_FOR_DEPLOYMENT, ACTIVE, DISABLED, DEPRECATED,
OTHER.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/digital-products
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "NewDigitalProductRequestBody",
  "isOwnAnchor" : true,
  "parentGUID" : "xxx",
  "parentRelationshipTypeName" : "CollectionMembership",
  "parentAtEnd1": true,
  "collectionProperties": {
    "class" : "CollectionProperties",
    "qualifiedName": "DigitalProduct:Add product name here",
    "name" : "=Product contents",
    "description" : "Add description of the contents of the product",
    "collectionType": "Digital Product"
  },
  "digitalProductProperties" : {
    "class" : "DigitalProductProperties",
    "productStatus" : "DRAFT",
    "productName" : "Add product name here",
    "productType" : "Periodic Delta",
    "description" : "Add description of product and its expected usage here",
    "maturity" : "Add valid value here",
    "serviceLife" : "Add the estimated lifetime of the product",
    "introductionDate" : "date",
    "nextVersionDate": "date",
    "withdrawDate": "date",
    "currentVersion": "V0.1",
    "additionalProperties": {
      "property1Name" : "property1Value",
      "property2Name" : "property2Value"
    }
  }
}

```

### updateDigitalProduct

Update the properties of the DigitalProduct classification attached to a collection.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/digital-products/{{digitalProductGUID}}/update?replaceAllProperties=false
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "DigitalProductProperties",
  "productStatus" : "ACTIVE",
  "productName" : "Add product name here",
  "productType" : "Periodic Delta",
  "description" : "Add description of product and its expected usage here",
  "introductionDate" : "date",
  "maturity" : "Add valid value here",
  "serviceLife" : "Add the estimated lifetime of the product",
  "currentVersion": "V1.0",
  "nextVersionDate": "date",
  "withdrawDate": "date",
  "additionalProperties": {
    "property1Name" : "property1Value",
    "property2Name" : "property2Value"
  }
}

```
## Managing collection members

[Referenceable](/concepts/referenceable) elements can be added as members to a collection using the [CollectionMembership](/types/0/0021-Collections) relationship.  These membership relationships can be maintained manually by people, or by automated services (typically [governance services](/concepts/governance-service)).  The attributes of the *CollectionMembership* relationship are optional, but important where the reasons for the membership, and the confidence of whether it is valid, need to be actively managed.  The properties are:

* The *membershipRationale* attribute describes why the member is part of the collection.
* The *expression* attribute indicates the expression used to decide on the membership. This is typically set up by automated processes to identify the rule they used to determine the membership.
* The *confidence* attribute indicates how confident that the membership is correct.
* The *createdBy* attribute is the identifier of the process or person that created (curated) the relationship. This is useful for identifying the instance of a process that created the membership relationship or the curator if they are different from the steward.
* The *source* attribute describes the source of information that identified this membership.
* The *steward* attribute identifies the person that is accountable for the correctness of this membership relationship.
* The *stewardTypeName* attribute identifies the type of element (such as UserIdentity, Person, PersonRole) that is responsible for the correctness of this relationship.
* The *stewardPropertyName* attribute identifies the property (such as guid or qualifiedName) used to identify the steward.
* The *notes* attribute enables the steward to add additional information about this relationship.
* The *status* attribute indicates the status of the member in the collection. It is a [MembershipStatus](/types/0/0021-Collections) value.
* The *userDefinedStatus* provides a status value when status=OTHER.

The Collection Manager OMVS has operations to add and remove members from the collection and also update the membership properties.


### addToCollection

Add an element to a collection.  The request body is optional. The variable `elementGUID` is the unique identifier of the element that is to be a member of the collection.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/members/{{elementGUID}}/attach
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "CollectionMembershipProperties",
  "membershipRationale": "xxx",
  "createdBy": "user id here",
  "expression": "expression that described why the element is a part of this collection",
  "confidence": 100,
  "status": "PROPOSED",
  "userDefinedStatus": "Add valid value here",
  "steward": "identifier of steward that validated this member",
  "stewardTypeName": "type name of element identifying the steward",
  "stewardPropertyName": "property name if the steward's identifier",
  "source": "source of the member",
  "notes": "Add notes here"
}
```
### updateCollectionMembership

Update an element's membership to a collection.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/members/{{elementGUID}}/update?replaceAllProperties=false
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "CollectionMembershipProperties",
  "membershipRationale": "xxx",
  "createdBy": "user id here",
  "expression": "expression that described why the element is a part of this collection",
  "confidence": 100,
  "status": "PROPOSED",
  "userDefinedStatus": "Add valid value here",
  "steward": "identifier of steward that validated this member",
  "stewardTypeName": "type name of element identifying the steward",
  "stewardPropertyName": "property name if the steward's identifier",
  "source": "source of the member",
  "notes": "Add notes here"
}
```
### removeFromCollection

Remove an element from a collection.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/members/{{elementGUID}}/detach
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "NullRequestBody"
}
```

### getCollectionMembers

Return a list of elements that are a member of a collection.
```
GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}/members?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
```

## Attaching a collection as a resource

The [*ResourceList*](/types/0/0019-More-Information) relationship links a [referenceable](/concepts/referenceable) element to an element that represent a useful resource.  The relationship has four properties:

* *resourceUse* - how should the resource be used.
* *resourceUseDescription* - a description of the resource use.
* *resourceUseProperties* - additional properties needed when using the resource.
* *watchResource* - a boolean flag indicating whether changes to the resource should be reported to the linked from element.  To have an effect, a [governance service](/concepts/governance-service) needs to be running to honour the request.

Collection Manager OMVS has an operation to attach a collection as a resource, detach it, and search for collections linked to an element as a resource.


### attachCollection

Connect an existing collection to an element using the ResourceList relationship.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/metadata-elements/{{parentGUID}}/collections/{{collectionGUID}}/attach?makeAnchor=false
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "ResourceListProperties",
  "resourceUse" : "Add valid value here",
  "resourceUseDescription" : "Add description here",
  "watchResource" : false,
  "resourceUseProperties": {
    "property1Name" : "property1Value",
    "property2Name" : "property2Value"
  }
}
```


### detachCollection 
Detach an existing collection from an element.  If the collection is anchored to the element, it is deleted.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/metadata-elements/{{parentGUID}}/collections/{{collectionGUID}}/detach
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "NullRequestBody"
}

```

## Retrieving collections

### getClassifiedCollections
Returns the list of collections with a particular classification.  These classifications
are typically "RootCollection", "Folder" or "DigitalProduct".
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/by-classifications?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
Content-Type: application/json

{
"filter" : ""
}
```
### findCollections
Returns the list of collections matching the search string.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/by-search-string?startFrom=0&pageSize=0&startsWith=false&endsWith=false&ignoreCase=true
Authorization: Bearer {{token}}
Content-Type: application/json

{
"filter" : "Data Product Development Journey"
}
```
### getCollectionsByName

Returns the list of collections with a particular name.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/by-name?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
Content-Type: application/json

{
"filter" : "DataJourneyProject:Data Acquisition Journey:{{projectName}}:ActivityFolder:Potential Data Sources"
}
```
### getCollectionsByType

Returns the list of collections with a particular collectionType.  This is an optional text field in the collection element.
```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/by-collection-type?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
Content-Type: application/json

{
"filter" : ""
}
```

### getCollection

Return the properties of a specific collection.
```
GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/collections/{{collectionGUID}}
Authorization: Bearer {{token}}
```

### getLinkedCollections

Returns the list of collections that are linked off of the supplied element.

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/collection-manager/metadata-elements/{{parentGUID}}/collections?startFrom=0&pageSize=0
Authorization: Bearer {{token}}
Content-Type: application/json

{
}
```

---8<-- "snippets/abbr.md"






