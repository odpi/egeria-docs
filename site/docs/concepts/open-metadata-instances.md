<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Instances

An *open metadata instance* describes a single element of metadata.  There are two types of metadata instances in open metadata:

- *Entities* - these are the principle nodes (vertices) in the metadata graph.  They typically describe concepts, people, places, things.

- *Relationships* - these are links (edges) in the metadata graph that show how the entities are related.

Entities can also be decorated with *classifications*.  These elements label entities with specific characteristics.

![Figure 1](open-metadata-instances.svg)
> **Figure 1:** The open metadata standard describes metadata as a graph.  The principle nodes of the graph are called entities.  Entities are linked together by relationships.  Entities can also be annotated with classifications.  Each classification element can only connect to a single entity.

Entities, relationships and classifications can store attributes.  They can be primitive values, enums, or collections such as arrays and maps.

![Figure 2](open-metadata-instances-with-attributes.svg)

The attributes supported in the entities, relationships and classifications are controlled by the [open metadata type definitions (TypeDefs)](/concepts/open-metadata-type-definitions).  TypeDefs describes what the element represents and the attributes that may be stored in it.

## Storing and distributing open metadata elements

Linked entities, relationships and classifications can be stored in different repositories in the cohort.  The graph is broken down into the structures shown in figure 2 to send as events, pass over APIs and to store in [open metadata archives](/concepts/open-metadata-archive).

An entity proxy is a subset of an entity that is used to represent the entity that either a classification or a relationship is connected to.

![Figure 3](open-metadata-instances-graph-fragments.svg)
> **Figure 3:** Pieces of the graph of open metadata instances need to be sent and stored independently.  Entities have no dependencies on other elements and can be sent/stored.  Relationships need to identify the two entities that they connect together.  Therefore, they include a subset of the entity, called the entity proxy, in their definition.  Classifications can either be stored with their entity or stored independently with an entity proxy representing the entity it belongs to.

Each instance has a *home* repository where updates occur.

Each instance can be copied to other repositories for efficiency.  These copies are read-only and called *reference copies*.

This model is designed to allow metadata from one repository to be augmented by another.  This is particularly important when third party technologies that do not support all the open metadata types, are connected to the open metadata ecosystem.  Relationships and classifications that involve the third party technology's metadata elements can be stored in other repositories, and returned together on open metadata queries as if they were stored together.

## Properties in an open metadata instance

Figure 3 shows the structure of an open metadata instance.

![Figure 4](open-metadata-instances-structure.svg)
> **Figure 4:** The structures used in open metadata instances.  To read the diagram, locate the box labelled with the type of metadata instance you are interested in.  This will have the properties that are specific to that instance.  Follow the arrowed lines up the diagram and add in the properties you find until you have reached *InstanceAuditHeader* which holds the properties that are always present in a metadata instance.

### InstanceAuditHeader

The [*InstanceAuditHeader*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceAuditHeader.html) defines the properties present in all metadata instances and classifications.  Its purpose is to define the source of the metadata and the users would are maintaining it.

* *type* - All instances begin with a *type* description that is described by *InstanceType*.
* *instanceProvenanceType* describes how the metadata was introduced into the open metadata ecosystem.  The values are described in [metadata provenance](/features/metadata-provenance/overview).
* *metadataCollectionId* - Identifies the *home* metadata collection for the element.  This is typically where the instance was first created.
* *metadataCollectionName* - An optional name for the metadata collection identified by *metadataCollectionId*.
* *replicatedBy* - The *metadataCollectionId* for the server that is responsible for replicating any changes to this instance to the rest of the cohort.  If this is null, the server managing the *home* metadata collection is responsible.
* *instanceLicense* is a free-text field for storing license information in it.  This allows metadata content to be licensed.
* *createdBy* is the userId of the person/system that created the metadata element.
* *updatedBy* is the userId of the last person/system to make a change to one of the instance's properties.
* *maintainedBy* is the list of userIds that have made changed to the instance's properties.
* *createTime* is the time that the metadata element was created.
* *updateTime* is the last time that the metadata element was updated.
* *version* is the version number.  This number is increased on each update.  Egeria adds 1 to the version number - other technologies may use an update timestamp.
* *currentStatus* is the status of the element.
* *statusOnDelete* is typically null.  It is set to the currentStatus value when the element is soft-deleted. It is used to restore currentStatus after a restore request that undoes the soft-delete.  
* *mappingProperties* - optional properties used by a repository connector to map open metadata elements to third party metadata.  It is used in the [Adapter Pattern](https://egeria-project.org/connectors/#repository-and-event-mapper-connectors).

### InstanceType

The [*InstanceType*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceType.html) identifies the [open metadata type definition (TypeDef)](/concepts/open-metadata-type-definitions) that this instance belongs to.

### InstanceHeader

The [*InstanceHeader*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceHeader.html) is the common header for entities and relationships.  It includes the unique identifier (GUID) for the metadata instance.

### EntitySummary

The [*EntitySummary*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntitySummary.html) adds the classifications to the entity.  It is the common properties for both an EntityProxy and an EntityDetail. 

### EntityDetail

The [*EntityDetail*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntityDetail.html) is the complete entity.

### EntityProxy

The [*EntityProxy*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntityProxy.html) provides the identifiers to identify an entity.

### Relationship

The [*Relationship*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/Relationship.html) links two entities together.  It identifies the entities using EntityProxies.  The relationship is directional, identifying a starting end (end 1) and a finishing end (end 2).  This direction is to clarify the meaning of each connected entity.  It can be navigated in either direction.

### Classification

The [*Classification*](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/Classification.html) is the structure for a classification introduced in the EntitySummary.

--8<-- "snippets/abbr.md"