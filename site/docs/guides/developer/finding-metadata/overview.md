<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Finding and retrieving metadata

This section describes how to retrieve metadata from the open metadata ecosystem.  The metadata is stored in all the open metadata repositories connected to the server you are calling via one or more [Open Metadata Repository Cohorts](/features/cohort-operation/overview).  Creating, updating and deleting metadata is covered in [Maintaining Metadata](/guides/developer/maintaining-metadata/overview).

## Mechanisms to retrieve metadata

Search methods can be thought of as having 2 phases:

* Retrieve a set of candidate elements from the repositories.
* Apply additional filtering to further limit the values returned to the caller.

### Repository mechanisms

Egeria's [native metadata repositories](/concepts/repository-connector) (the PostgreSQL repository connector and the in-memory repository connector) support 2 kinds of retrieval, illustrated in the diagram below.  Conceptually, there is a graph store and an index store.

![Mechanisms for retrieving metadata](retrieving-metadata-mechanisms.svg)
> An Egeria native repository supports both navigational (graph) and value-based (index) retrieval.

The **graph store** supports requests to retrieve metadata that involves navigating from a starting point to related instances.  For example, a request to retrieve all the glossary terms for a [glossary](/types/3/0310-Glossary) involves locating the glossary entity and navigating via the [CollectionMembership relationship](/types/0/0021-Collections) to the glossary terms.

```mermaid
flowchart LR
    G["Glossary"] -- CollectionMembership --> T1["GlossaryTerm"]
    G -- CollectionMembership --> T2["GlossaryTerm"]
    G -- CollectionMembership --> T3["GlossaryTerm"]
```

The **index store** contains lists of values with links to the instance they came from.  It is used to locate instances that have particular values.  For example, a request to retrieve all glossary terms with a particular name would use the index store.  The terms returned could come from any glossary.

How these mechanisms are implemented depends on the repository.  For example, the PostgreSQL repository connector stores each entity, relationship and classification in its own table, with their property values in separate `entity_property_value`, `relationship_property_value` and `classification_property_value` tables.  Navigational requests follow the `end1`/`end2` links in the relationship table, and value searches are mapped onto SQL queries over the property value tables.

### Filtering

Filtering takes the list of instances returned by the repositories and removes the instances that do not match the filtering criteria.

The more work that can be pushed to the repositories, the faster the retrieval is probably going to be.
However, filtering can not always be avoided when the request combines both navigation and matching on values.

For example, consider a search request that asks for all glossary terms of a certain name, but only from a particular glossary.  This request is both a value search and a navigational search.

The choice of whether the navigational search or the value search is pushed down to the repositories, leaving the other to be managed with filtering is down to performance.  It is expensive to retrieve elements from the repositories.  We therefore want the repository search to return the minimum number of results, leaving the filtering to discard a small number of instances.

For example, in the case of locating particularly named glossary terms within a specific glossary, we could either:

1. Retrieve all the glossary terms for the glossary from the repositories using a navigational query and then inspect each one returned to filter out the ones with the wrong name.
2. Retrieve all the glossary terms from the repositories that have a matching name using a value search and then filter out the ones from the wrong glossaries.

In most systems, the number of glossary terms in a glossary are likely to be much greater than the number of glossary terms with the matching name.  Therefore, in this example, Egeria will use option 2.

Egeria's ordering choice is not going to be optimal for all situations.  The aim is to pick the best order for most situations.  This is also an area with opportunities to improve Egeria's performance.

### Types of filtering

The example above combined a value search with a navigational one.  There are other types of options on search requests that are always filters because they describe situations that are not directly supported by the repositories.

* The *effectiveTime* option requests that results only include elements that have their effectivity dates set up so that they are effective at that time.  You may notice this option on create, update and delete requests too.  This is because they involve at least one query to locate, say the instance that the new instance is to be connected to.
* The *forLineage* option requests that the results include instances that have been archived using the [*Memento*](/concepts/memento) classification, and instances that are not yet delivered and carry the [*Promise*](/concepts/promise) classification.  Normally these instances are not returned.  They are only used in lineage to show resources involved in a lineage flow that no longer exist, or do not exist yet.
* The *forDuplicateProcessing* option turns off Egeria's deduplication processing to allow the caller to modify how the duplicates are linked together.  Normally, duplicates are selected and merged by Egeria during its filtering stage.

### Paging

It is possible that the caller wants to retrieve a lot of metadata, too much in fact to be retrieved in one request.  Therefore, Egeria's retrieval requests include paging.  This is expressed using 2 parameters:

* A starting point in the list of results to return.  This is `startFrom` on the view services and in the Open Metadata Framework's `PagingOptions`, and `fromEntityElement`/`fromRelationshipElement` on the repository services.
* The maximum number of results to return, called `pageSize`.

Every server limits the maximum number of elements that can be returned, so if the caller requests too much, or a page size of 0, the server's maximum is used.

The caller then codes a loop that retrieves the results, incrementing the starting point by the page size each time until a null result is returned.

It is possible that the caller may be returned an empty list on some iterations.  This means all the values returned by the repository have been filtered out and the caller should increment the starting point and continue to retrieve new results.

![Paging with filtering](retrieving-metadata-paging.svg)

In order for this loop to work, the caller needs to know the real paging size used.  Therefore, the page size value used by callers should be established as a value lower than that set by the servers.   The purpose of the server's maximum page size is to prevent rogue requests from impacting the server.


## Choosing the API to use

Egeria APIs each have their own data models which affects the structure of information returned on a retrieval call.

For example, the repository services (OMRS) return entity and relationship instances.  The view services (OMVSs) return *metadata elements* that describe assets, glossary terms, connections, ... along with their related elements.

Often the results returned by an OMVS includes information from multiple OMRS instances.  These are filled in via additional navigational retrieval requests once the initial retrieval from the repository services has returned a selection of OMRS instances.

The most perfect, rich result set from an OMVS for your needs, may involve many requests to the repositories. If an OMVS query seems to be taking a lot of time, it might just be that it is doing a lot of work. However, if too much information is being returned, it may be that the API call is not the best choice for your needs, or the options need to be adjusted to prune the results.  The get/query/search options (the `GetOptions` class and its subclasses in the [Open Metadata Framework](/frameworks/omf/overview)) include:

* `graphQueryDepth` - the maximum number of relationships away from the starting element that the request traverses to fill in related elements.  The default is 5.  If you are only processing the main element and do not care about its relationships, set `graphQueryDepth=0`.
* `relationshipsPageSize` - the maximum number of relationships of each kind returned with an element.  Zero means up to the server's maximum page size.
* `includeOnlyRelationships` and `skipRelationships` - lists of relationship type names that restrict which relationships are returned.
* `maxMermaidNodeCount` - the maximum number of nodes in any [mermaid](https://mermaid.js.org/) graph returned with the element.

## Metadata elements

The view services return *metadata elements* on their APIs.  In its simplest form, a metadata element maps to a single OMRS instance (typically an entity) and includes an *element header* and its *properties*.

* The element header comes from the header of the OMRS instance. This information is managed by the OMRS.
* The properties are managed by the caller.  They are used when creating/updating the OMRS instance and are different for each type of instance.  The types of the properties for a particular type of instance are defined in the [Open Metadata Types](/types).

The illustration below shows the typical structure of a metadata element that is populated from an OMRS entity instance.

Notice the element header includes the entity's classifications.

![Metadata Element Structure](retrieving-metadata-metadata-element.svg)

Most view service operations return an `OpenMetadataRootElement` (package `org.odpi.openmetadata.frameworks.openmetadata.metadataelements`) for each element.  It has the element header (`elementHeader`), a properties bean (`properties`) whose class matches the element's type - for example `SoftwareServerProperties` for a *SoftwareServer* - and, depending on the request, lists of related elements and [mermaid](https://mermaid.js.org/) graphs (such as `mermaidGraph`) that visualize the element and its relationships.

```mermaid
classDiagram
    class MetadataElement {
        <<interface>>
    }
    class AttributedMetadataElement {
        ElementHeader elementHeader
        List~RelatedMetadataElementSummary~ externalReferences
        List~RelatedMetadataElementSummary~ memberOfCollections
        RelatedMetadataElementSummary connectorType
        RelatedMetadataElementSummary endpoint
        List~RelatedMetadataElementSummary~ certifications
        ...
    }
    class OpenMetadataRootElement {
        OpenMetadataRootProperties properties
        Map specification
        String mermaidGraph
        ...
    }
    MetadataElement <|.. AttributedMetadataElement
    AttributedMetadataElement <|-- OpenMetadataRootElement
```

### Element header

The structure of the element header is defined by the `ElementHeader` class in the Open Metadata Framework (OMF).  It extends `ElementControlHeader`, which it shares with classifications and relationships.  It includes:

* Element status (`status`) - the status of the element is its lifecycle state.  Most elements are in either ACTIVE or DELETED status.  Some types of entities have an [extended lifecycle](/concepts/instance-status).
* Element type (`type`) - the type defines what the entity represents, and (from its type definition) which properties can be stored in the entity.  It includes the type's name, its super types and its description.
* Element origin (`origin`) - the origin defines the element's [provenance](/features/metadata-provenance/overview).
* Element versions (`versions`) - the versions identify which version and who is responsible for making the changes to bring it to its current version.
* The unique identifier (`guid`) of the element.
* The element's classifications.  The commonly used classifications have their own field, named after the classification - for example `anchor` (*Anchors*), `zoneMembership`, `confidentiality`, `ownership`, `memento`, `template` and `usageActivity`.  Classifications that can appear more than once have a list, such as `collectionKinds` and `executionPoints`, and any other classifications are in `otherClassifications`.

```mermaid
classDiagram
    class ElementControlHeader {
        long headerVersion
        ElementStatus status
        ElementType type
        ElementOrigin origin
        ElementVersions versions
    }
    class ElementHeader {
        String guid
        ElementClassification anchor
        ElementClassification zoneMembership
        ElementClassification ownership
        ElementClassification memento
        ElementClassification usageActivity
        List~ElementClassification~ collectionKinds
        List~ElementClassification~ otherClassifications
        ...
    }
    ElementControlHeader <|-- ElementHeader
```

This is an abbreviated element returned from the [Runtime Manager](/services/omvs/runtime-manager/overview) for the `qs-metadata-store` server.  Notice the *Anchors* classification is returned in the `anchor` field of the element header.

```json
{
  "class": "OpenMetadataRootElement",
  "elementHeader": {
    "class": "ElementHeader",
    "status": "ACTIVE",
    "type": {
      "typeName": "SoftwareServer",
      "superTypeNames": ["ITInfrastructure", "Infrastructure", "Asset", "Referenceable", "OpenMetadataRoot"],
      "typeCategory": "ENTITY_DEF"
    },
    "origin": {
      "sourceServer": "qs-metadata-store",
      "originCategory": "LOCAL_COHORT",
      "homeMetadataCollectionName": "qs-metadata-store"
    },
    "versions": {
      "createdBy": "omagspcatnpa",
      "createTime": "2026-10-25T10:25:42.604+00:00",
      "version": 9
    },
    "guid": "81aee2d5-151f-4f61-b8ad-b22785cd6ffd",
    "anchor": {
      "class": "ElementClassification",
      "classificationName": "Anchors",
      "classificationOrigin": "ASSIGNED",
      "classificationProperties": {
        "class": "AnchorsProperties",
        "anchorTypeName": "SoftwareServer",
        "anchorDomainName": "Asset"
      }
    }
  },
  "properties": {
    "class": "SoftwareServerProperties",
    "typeName": "SoftwareServer",
    "qualifiedName": "Metadata Access Store::https://localhost:9443::qs-metadata-store",
    "displayName": "qs-metadata-store from Coco Pharmaceuticals on https://localhost:9443",
    "deployedImplementationType": "Metadata Access Store",
    "deploymentStatus": "ACTIVE"
  }
}
```

### Element classification

Classifications are structured as follows.  Notice they include the same header control information as the OMRS instances.

![ElementClassification](retrieving-metadata-element-classification.svg)

### Composite metadata elements

Metadata elements can include information from multiple OMRS instances.  The `AttributedMetadataElement` class, which `OpenMetadataRootElement` extends, has a field for each kind of relationship that the element may have, named for the role the related element plays.  Each field holds a `RelatedMetadataElementSummary` (or a list of them) for the relationships that were retrieved.

For example, a valid [connection](/concepts/connection) is always linked to a connector type.  It may have a link to an endpoint and may be linked to other embedded connections.  When a connection is retrieved through the [Connection Maker](/services/omvs/connection-maker/overview) API, these linked objects are returned in the `connectorType`, `endpoint` and `embeddedConnections` fields of the connection's metadata element.

#### Element stub

An element stub (class `ElementStub`) identifies an element without returning its properties.  It is the element header plus the element's `uniqueName`.  It is created from the part of a relationship that describes the entity at one of the ends of the relationship.  In OMRS, this is called an *entity proxy*.

An element stub is used when the relationship needed to be retrieved to satisfy another part of the request, and the caller may wish to retrieve the linked entity in a subsequent call.  This is more efficient using the unique identifier (guid) of the entity.  So since the information has already been retrieved, and may be useful later, it is included.

### Supplementary properties

Some elements, such as assets catalogued from a third party technology, are read-only for the people that use them.  A steward or owner can still maintain additional descriptive properties about such an element by linking it to a glossary term using the [SupplementaryProperties](/types/3/0395-Supplementary-Properties) relationship.

![SupplementaryProperties relationship linking an asset to a glossary term](retrieving-metadata-supplementary-properties.svg)

When the element is retrieved, the linked glossary term is returned in the `supplementaryProperties` field of its metadata element.

### Relationship metadata elements

Some metadata elements represent a relationship.  For example, a certification for an element, such as an asset, is stored in a [Certification](/types/4/0482-Certifications) relationship linked to the type of certification.

![Certification relationship with CertificationType entity](retrieving-metadata-certification-relationship.svg)

When the certified element is retrieved, each certification is returned in the `certifications` field of its metadata element.  Both the certification relationship and the certification type entity are represented: the entry is a related element (described below) whose `relationshipHeader` and `relationshipProperties` come from the *Certification* relationship, and whose `relatedElement` is the *CertificationType*.

#### Related element

Some retrieval methods that navigate relationships may link to entities of multiple types - for example when the members of a [Collection](/types/0/0021-Collections) are returned, they may be any type of referenceable entity.

If the relationship properties are needed, as well as the related entity, then a *related element* (class `RelatedMetadataElementSummary`) is used.  This is also the class used for the related elements in a [composite metadata element](#composite-metadata-elements).

```mermaid
classDiagram
    class RelatedMetadataElementSummary {
        ElementHeader relationshipHeader
        RelationshipBeanProperties relationshipProperties
        Date effectiveFromTime
        Date effectiveToTime
        MetadataElementSummary relatedElement
        boolean relatedElementAtEnd1
    }
    class MetadataElementSummary {
        ElementHeader elementHeader
        OpenMetadataRootProperties properties
    }
    RelatedMetadataElementSummary --> MetadataElementSummary : relatedElement
```

`relatedElementAtEnd1` tells you which end of the relationship the related element is at.

## Retrieval requests

The open metadata repositories support the following retrieval requests (the method names are from the repository services' `OMRSMetadataCollection` interface):

* Value-based queries:

    * Get an instance (entity or relationship) by its unique identifier (guid) - `getEntityDetail`, `getEntitySummary`, `getRelationship`.
    * Get all the entities of a particular type that have specific properties set to specific values - `findEntitiesByProperty`.
    * Get all the relationships of a particular type that have specific properties set to specific values - `findRelationshipsByProperty`.
    * Get all the entities of a particular type that have a specific classification with specific properties set to specific values - `findEntitiesByClassification`.
    * Get all the entities of a particular type that have any property set to a specific value - `findEntitiesByPropertyValue`.
    * Get all the relationships of a particular type that have any property set to a specific value - `findRelationshipsByPropertyValue`.
    * Get all the entities (or relationships) of a particular type that match a combination of property and classification conditions - `findEntities`, `findRelationships`.  `countEntities` returns the number of entities that would match.

* Navigational queries:
    * Get all the relationships connected to an entity - `getRelationshipsForEntity`.

* Historical queries:
    * Get the versions of an instance over a period of time - `getEntityDetailHistory`, `getRelationshipHistory`, `getClassificationHistory`.

The OMVS APIs are then built up from these basic building block queries.



--8<-- "snippets/abbr.md"
