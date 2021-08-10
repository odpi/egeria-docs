<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Key concepts

To further explain some of the key concepts of Egeria, let us delve deeper into an
example:

![Egeria solution composition](egeria-solution-components.png)

The inner ring, titled **Integrated Metadata**, illustrates the exchange of metadata
between metadata servers. The servers are connected together through an _Open Metadata
Repository Cohort_ or just _cohort_ for short.

## Cohorts

A cohort[^1] can support the exchange of many metadata servers: both internal
to Egeria and third party. A cohort is a group of OMAG servers that are
exchanging metadata using a peer-to-peer replication protocol and federated
queries.

The cohort is self-configuring. At the core it is between one and four shared topics. Each
member publishes a registration request on the appropriate topic when they want to join.
This is picked up by the existing members who add this new server to their registry of
members and re-send their registration through the same topic to allow the new member to
build up its own registry.

!!! attention "There is no central cohort controller"
    Note that there is no central cohort control or coordination logic: the registration and
    so on are all handled in a peer-to-peer manner with each participant communicating with
    all other participants.

When an OMAG server permanently leaves the cohort, it sends an unregistration request.
This enables the other members to remove the parting member from their registries.

### Federation

The purpose of the registry in each member is to configure its federated query capability
supported by the [enterprise repository services](todo.md).
The registration information includes the URL root and server name of the member. The
federation capability in each OMAG server allows it to issue metadata create, update,
delete and search requests to each and every member of the cohort. This is the primary
mechanism for accessing metadata.

### Replication

In addition, any change to metadata made by a member is replicated to the other members
of the cohort through the relevant cohort topic. This gives the other members an opportunity
to maintain cached copies of the metadata for performance / availability reasons.

!!! tip "Refresh requests"
    A member may also request that metadata is "refreshed" across the cohort. The
    originator of the requested metadata then sends the latest version of this metadata
    to the rest of the cohort through the cohort topic. This mechanism is useful to seed
    the cache in a new member of the cohort and is invoked as a result of a federated
    query issued from the new member. (A federated query occurs automatically whenever
    an [access service](../services/omas.md) makes a request for metadata.)

### Exchange protocol

The exchange of metadata uses the [Open Metadata Repository Services (OMRS)](../services/omrs.md)
interfaces, which gives fine-grained metadata notifications and updates[^2]. The server's
[metadata security connector](todo.md) provides fine-grained control on which metadata is sent,
received and/or stored by the server. This level of control is necessary for metadata
repositories that are managing specific collections of valuable objects such as [Assets](todo.md).

### Members

![Cohort member types](cohort-member-types.png)

A third party metadata server can embed the Egeria libraries in its
own runtime or, more commonly, use a special OMAG server called the
**Repository Proxy** to host connectors that map between the events and APIs of the
third party metadata server and the Open Metadata events and APIs.
The repository proxy manages all of the interaction with the other
members of the cohort.

The cohort protocols are peer-to-peer and the membership is dynamic.
When a third party metadata server connects to the cohort, either directly
or through its repository proxy, it automatically begins receiving
metadata from all of the other members. When it shares metadata,
it is shared with all the other members. Each member is free to choose what
to share and what to process from the other members of the cohort.

Other types of OMAG Servers that can be members of the cohort:

- The **Conformance Test Server** is used to verify that a member of the
  cohort is operating correctly.  It is typically only used in
  test environments because it sends out a lot of test metadata on the cohort
  and validates the responses from the cohort member it is testing.
- The **Metadata Server** provides a metadata repository
  that supports any type of open metadata.  It is a valuable
  member of the cohort because it is a metadata gap-filler.  By that we mean
  that is can store relationships between metadata
  from different third party repositories along with additional types of metadata
  not supported by any of the third party metadata repositories.
  It may optionally have the access services enabled so it can also
  act as a metadata access point.
- The **Metadata Access Point** supports Egeria's [Open Metadata Access
  Services (OMAS's)](../services/omas), or access services, for short. These access services
  provide specialized APIs and events for different types of technologies.

## Integrating metadata into solutions

The metadata access point is the bridge to the governance servers (the middle ring in
the initial illustration).

![Egeria solution composition](egeria-solution-components.png)

The addition of the governance servers provides active metadata
exchange and governance of any type of third party technology,
not just metadata servers.  We call this **Integrated Governance**.

For the most part, Egeria is a background technology.
However, once metadata is being exchanged and linked, new
**Governance Solutions** may emerge that bring value directly to individuals
working in an organization. Therefore we have added servers to
support browser-based user interfaces:

- The **View Server** provides REST APIs specifically for user interfaces. They are
  consumed by the Egeria UIs but can also be used by other UIs and tools.
- The **Presentation Server** ???

## Metadata instances

We refer to a specific metadata object, for example the business vocabulary term `Customer`, as a metadata
**instance**.

### Kinds of instances

#### Entities

An **entity** is capable of describing a metadata object on its own: for example, a business vocabulary term,
database, field in a schema, and so on. If you think about metadata as a graph, these are the nodes (vertices)
in the graph. They typically describe concepts, people, places and things.

??? question "How are entities modeled in Egeria?"
    Egeria models all entities using a general object -- [`EntitySummary`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntitySummary.java){ target=model }
    -- from which more detailed representations (like [`EntityDetail`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntityDetail.java){ target=model })
    are derived. Note that there is a property called `type` within this object (inherited from [`InstanceAuditHeader`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceAuditHeader.java){ target=model })
    that defines the specific _type_ of metadata the entity represents, rather than having a different
    type-specific object for every different type of entity.

#### Relationships

A **relationship** describes a (typically) directional association between two entities: for example, the
semantic meaning of a relational database column by relating a business vocabulary term with the relational
database column. In a graph sense, these are the links (edges) that show how entities are related.

??? question "How are relationships modeled in Egeria?"
    Egeria models all relationships using a general object -- [`Relationship`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/Relationship.java){ target=model }
    -- which links together exactly two entities (using [`EntityProxy`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/EntityProxy.java){ target=model },
    itself an extension of EntitySummary).
    
    These `EntityProxy`s act as a sort of "stub" to which the relationship can point, without needing to be
    aware of the entire set of details of each entity involved in the relationship, and are therefore an
    important piece of ensuring that relationships are treated as "first-class" objects in their own right.

    As with entities, there is a property called `type` within this `Relationship` object (also inherited from
    [`InstanceAuditHeader`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceAuditHeader.java){ target=model })
    that defines the specific _type_ of metadata the relationship represents, rather than having a different
    type-specific object for every different type of relationship.

#### Classifications

While not strictly speaking a kind of metadata instance, a **classification** provides a means to extend an
entity with additional facets of information: for example, describing the level of confidentiality with which
a particular relational database column should be treated. Classifications describe additional attributes of
an entity and can be used to identify entities that are similar in a specific aspect.

??? question "How are classifications modeled in Egeria?"
    Egeria models all classifications using a general object -- [`Classification`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/Classification.java){ target=model }
    -- any instance of which is possessed by exactly one entity (within the `EntitySummary`'s  `classifications` property).

    As with the other kinds of instances, note that there is a property called `type` within this `Classification`
    object (also inherited from [`InstanceAuditHeader`](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/properties/instances/InstanceAuditHeader.java){ target=model })
    that defines the specific _type_ of metadata the classification represents, rather than having a different
    type-specific object for every different type of classification.

    Furthermore, note that classifications in Egeria exist only as part of an entity: unlike `EntitySummary`
    and `Relationship`, they _do not_ extend `InstanceHeader` and therefore are not assigned a GUID through
    which they could be independently retrieved or updated. Classifications are only retrievable or updatable
    _through_ the entity by which they are possessed.

### Metadata types

Every metadata instance is linked to an open metadata type definition (`TypeDef`)
that describes what it represents and the properties that further describe and differentiate it from other
instances of that same type.

There are three categories of TypeDefs:

- **EntityDef**: the definition of a type of entity
- **RelationshipDef**: the definition of a type of relationship
- **ClassificationDef**: the definition of a type of classification

TypeDefs can inherit from other TypeDefs from the same category: open metadata supports single inheritance.

Each property defined in a TypeDef is defined in part by an `AttributeTypeDef` describing the type of the
property itself.

There are three categories of AttributeTypeDefs:

- **EnumDef**: the definition of an enumerated list of valid values.
- **CollectionDef**: the definition of a collection - such as an array of strings, or a map from string to object.
- **PrimitiveDef**: a primitive - such as a string, integer or date.

??? example "An example: GlossaryTerm, RelationalColumn and SemanticAssignment"
    For example, `GlossaryTerm` is a type of entity that is can be used to describe a specific term of business
    vocabulary. As a type of entity, `GlossaryTerm` is defined using an `EntityDef`. It has a number of properties
    like a `displayName`, itself defined as a `PrimitiveDef` of type string. And `GlossaryTerm` as a type
    extends a base type called `Referenceable` which defines common characteristics that many entities possess
    such as a `qualifiedName` (another `PrimitiveDef` of type string).

    `RelationalColumn` is another example of an entity, in this case one that can be used to describe
    relational database columns. Once again it is defined using an `EntityDef`, has a number of properties,
    and also extends the base type called `Referenceable` and therefore also gains common properties like
    the `qualifiedName`.

    Finally, let's consider a different type: `SemanticAssignment` is a type of relationship that can be
    used to describe the meaning of something. Because it is a type of relationship, it is defined using a
    `RelationshipDef`. As a relationship, the RelationshipDef defines the entities that it can inter-relate:
    in this example a `GlossaryTerm` and any other `Referenceable` (for example, a `RelationalColumn`).

??? question "Where are the types modeled?"
    As described in the models for the various kinds of instances, this TypeDef information is inherent
    in the `type` property of `InstanceAuditHeader`, from which all entities, relationships, and
    classification instances inherit.

    The TypeDefs themselves are described in detail under the [Types](../../types/types/) tab, and the
    canonical definitions ultimately [live in the code itself](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-archives/open-metadata-types/src/main/java/org/odpi/openmetadata/opentypes){ target=code }.

### Homed metadata

The metadata repository where a metadata instance is created is called its **home repository**.
Metadata in its home repository is _mutable_: it can be updated and deleted.

!!! tip "Each instance of metadata can be independently homed"
    Note that each instance of metadata -- whether an entity, relationship or classification -- can be
    homed independently from any other instance of metadata. For example: if we have a business vocabulary
    term `Address` that is related to a relational database column `ADDR` and given a `Confidentiality`
    classification, each of these could be homed in a different repository. That is, `Address` (entity) could
    be homed in repository A, `ADDR` (another entity) in repository B, the relationship
    between them in repository C, and the `Confidentiality` classification in repository D.

    As such, not only can a query for metadata be federated, but indeed even the holistic representation of a
    given piece of metadata (its instance and directly-related instances) is federated across the cohort.

The [Open Metadata Repository Services (OMRS)](../services/omrs) is responsible for sharing this metadata
with other metadata repositories who are members of the same cohort.

### Reference copies

The shared copies are called **reference copies** and are read-only (_immutable_). Update requests to a
reference copy are automatically redirected to the home repository by the OMRS, without the caller being
aware.

!!! tip "Distinguishing homed metadata from reference copies"
    Every metadata repository in a cohort has a unique identifier called the _local metadata collection id_.
    This identifier is set up in the server configuration and shared when this server connects to a cohort.

    When metadata is shared by OMRS, each instance is tagged with the metadata collection id of its home
    repository. OMRS is able to route update requests to the right server by comparing the metadata
    collection id in the metadata instance with the cohort registration information passed between members
    of the cohort when they connect.

### Unique identifiers (GUIDs)

Every open metadata instance has a unique identifier called the GUID.

!!! attention "GUIDs must be unique"
    This identifier needs to be globally unique -- so even if two metadata repositories
    simultaneously created a metadata instance about the same thing, the GUIDs of these
    two instances should be different.

    For example, in Egeria new GUIDs are created using the `UUID.randomUUID().toString()`
    method to produce something like: `87b06ffe-9db2-4ef5-ba6e-8127480cf30d`

    Egeria does not mandate the use this or any other particular algorithm for generating GUIDs,
    only that the principle of uniqueness is adhered to.

There should be, at most, a _tiny_ chance[^3] that two servers will generate the same GUID. Egeria
expects this to be exceedingly rare, but not impossible, and therefore if it does happen it is
detected by the [repository services](../services/omrs/) and at a minimum messages are output on
the detecting server's audit log. The repository services also have APIs for re-identifying (changing
the GUID) for a metadata instance to automate the resolution of such conflicts. We can expect that such
an operation could be resource-intensive; however, this is balanced against the exceeding rareness
with which it should need to be used.

## Conformance

Adhering to these concepts and the principles by which they behave is the subject of _conformance_. Egeria
provides an automated testing suite to validate that a given repository or third party integration behaves
according to these expectations, the successful completion of which is a necessary input to a tool being
granted the use of an Egeria conformance mark.

!!! attention "A common tripping point for conformance"
    The routing behavior described for homed metadata instances can only be enforced when the requests go
    through OMRS itself. For third party tools that provide their own services / user interface through which
    updates can be made, a common tripping point becomes the fact that these services / user interfaces
    need to adhere to the same protocol principles outlined above -- specifically, ensuring reference copies
    are also immutable through these product-native interfaces -- in order to conform to the Egeria protocol.

    For cases where the tool is unable to do so, we are actively investigating other mitigation measures like
    providing a [Smart Repository Proxy](https://github.com/odpi/egeria/issues/5402){ target=issue }
    to ensure that any changes to metadata that violate the protocol remain isolated in that third party
    technology and are not inadvertently propagated elsewhere in the cohort.

[^1]: You may want to see the [cohort interactions walkthrough](todo.md) for more details on how cohort participants interact.
[^2]: You may want to see the [OMRS metamodel](todo.md) for more details on the granularity of metadata exchange.
[^3]: The rarity will depend on the specific algorithm used, but as an example the algorithm used within Egeria
      generates type 4 UUIDs, for which the [probability of a collision is so small that it can almost be ignored](https://en.wikipedia.org/wiki/Universally_unique_identifier#Collisions){ target=wiki }.
      But as it is not _impossible_, Egeria does still provide the mechanisms to detect and resolve such conflicts.

--8<-- "snippets/abbr.md"
