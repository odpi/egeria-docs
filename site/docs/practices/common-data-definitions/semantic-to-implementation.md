<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


??? info "The glossary"

    The glossary is at the heart of the materials for a [subject area](/concepts/subject-area). Figure 1 shows that the glossary contains glossary terms.  Each glossary term describes a concept used by the business. It is also possible to link two glossary terms together with a relationship. The relationship may describe a semantic relationship or a structural one.

    ![Figure 1](/practices/common-data-definitions/semantic-to-implementation-glossaries.svg)
    > Figure 1: Glossaries for describing concepts and the relationships between them

    Semantic relationships include:

    * *RelatedTerm* is a relationship used to say that the linked glossary term may also be of interest. It is like a "see also" link in a dictionary.
    * *Synonym* is a relationship between glossary terms that have the same, or a very similar meaning.
    * *Antonym* is a relationship between glossary terms that have the opposite (or near opposite) meaning.
    * *PreferredTerm* is a relationship that indicates that one term should be used in place of the other term linked by the relationship.
    * *ReplacementTerm* is a relationship that indicates that one term must be used instead of the other. This is stronger version of the PreferredTerm.
    * *Translation* is a relationship that defines that the linked terms represent the same meaning but each are written in a different language. Hence, one is a translation of the other. The language of each term is defined in the Glossary that owns the term.
    * *IsA* is a relationship that defines that the one term is a more generic term than the other term. For example, this relationship would be used to say that "Cat" IsA "Animal".

    Structural relationships in the glossary are relationships that show how terms are typically used together. 

    * *UsedInContext* links a term to another term that describes a context. This helps to distinguish between terms that have the same name but different meanings depending on the context.
    * *HasA* is a term relationship between a term representing a SpineObject (see glossary term classifications below) and a term representing a SpineAttribute.
    * *IsATypeOf* is a term relationship between two SpineObjects saying that one is the subtype (specialisation) of the other.
    * *TypedBy* is a term relationship between a SpineAttribute and a SpineObject to say that the SpineAttribute is implemented using a type represented by the SpineObject

    !!! education "Further information"
        * See [Area 3](/types/3) in the *Open Metadata Types* to understand how these concepts are represented on open metadata.

??? info "Data classes"

    A *data class* provides the specification of a data type that is important to the subject area.  *Date*, *Social Security Number* and *Credit Card Number* are examples of data classes.

    The data class specification defines how to identify data fields of its type by inspecting the data values stored in them.  The specification is independent of a particular technology, which is why they are often described as *logical data types*.  The specification may include preferred implementation types for different technologies using *Implementation Snippets*.

    Data classes are used during *metadata discovery* (see below) to identify the types of data in the discovered data fields.  This is an important step in understanding the meaning and business value of the data fields.  They can also be used in quality rules to validate that data values mat the perscribed data class.

    Data classes can be linked together in part-of and is-a hierarchies to create a logical type system for a subject area. A glossary term can be linked to a data class via an *ImplementedBy* relationship to identify the preferred data class to use when implementing a data field with meaning described in the glossary term.  A data class can be linked to glossary term that describes the meaning of the data class via a *SemanticAssignment* relationship.

    ![Figure 2](/practices/common-data-definitions/semantic-to-implementation-data-classes.svg)
    > Figure 2: Data classes for describing the logical data types and implementation options

    !!! education "Further information"
        * See [Model 0540](/types/5/0540-Data-Classes) in the *Open Metadata Types* to understand how data classes are represented on open metadata.
        * See [Model 0737](/types/7/0737-Solution-Implementation) in the *Open Metadata Types* to understand the *ImplementedBy* relationship.
        * See [Model 0370](/types/3/0340-Semantic-Assignment) in the *Open Metadata Types* to understand the *SemanticAssignment* relationship.
        * See [Model 0504](/type/5/0504-Implementation-Snippets) in the *Open Metadata Types* to understand *ImplementationSnippets*.


??? info "Consuming the glossary in design models"

    Design models (such as Concept models, E-R Models, UML models) and ontologies capture similar concepts to those described in the glossary.  It helps if their definitions are consistent.  When a new glossary is being built, existing models and ontologies can be used to seed the glossary.   The models/ontologies themselves can be loaded in open metadata and the model elements linked to their corresponding glossary terms.  Then new versions of the data models/ontologies can be generated from open metadata.

    ![Figure 3](/practices/common-data-definitions/semantic-to-implementation-models.svg)
    > Figure 3: Linking to models

    Any linked data classes provide details of language types to use when generating compliant artifacts from the models.

    !!! education "Further information"
        * See [Model 0571](/types/5/0571-Concept-Models) in the *Open Metadata Types* to understand how concept models are represented on open metadata.
        * See [Model 0565](/types/5/0565-Design-Model-Elements) in the *Open Metadata Types* to understand how design models are represented on open metadata.

??? info "Schemas"

    Schemas document the structure of data, whether it is stored or moving through APIs, events and data feeds. A schema begins with a *schema type*. This may be a single primitive field, a set of values, an array of values, a map between two sets of values or a nested structure. The nested structure is the most common. In this case the schema type has a list of schema attributes that describe the fields in the structure.  Each of these attributes has its own schema type located in its *TypeEmbeddedAttribute* classification.

    Figure 4 shows a simple structure schema.

    ![Figure 4](/practices/common-data-definitions/semantic-to-implementation-schemas.svg)
    > Figure 4: Schemas for documenting the structure of data

    !!! education "Further information"
        * See [Schemas](/concepts/schema) to understand how different types of schema are represented.
        * See [Model 0501](/types/5/0501-Schema-Elements) in the *Open Metadata Types* to see the formal definition of these types.
        * See [Model 0505](/types/5/0505-Schema-Attributes) in the *Open Metadata Types* to understand schema attributes and the *TypeEmbeddedAttribute* classification.

??? info "Schemas and assets"

    An [asset](/concepts/asset) describes a valuable [resource](/concepts/resource) (typically digital).  Such resources include databases, data files, documents, APIs, data feeds, and applications. A digital resource can be dependent on other digital resource to fulfill their implementation.  This relationship is also captured in open metadata with relationships such as [DataContentForDataSet](/types/2/0210-Data-Stores).  These relationships help to highlight inconsistencies in the assets' linkage to the subject area's materials, which may be due to errors in either the metadata or the implementation/deployment/use of the associated digital resources.

    ![Figure 5](/practices/common-data-definitions/semantic-to-implementation-assets-and-schemas-dependencies.svg)
    > Figure 5: Dependencies between digital resources are reflected in open metadata by relationships between assets

    Since schema types describe the structure of data, they can be attached to assets using the *AssetSchemaType* relationship to indicate that this asset's data is organized as described by the schema.  Schemas are important because they show how individual data values are organized.  Governance is often concerned with the meaning, correctness and use of individual data values since they are used to influence the decisions made within the organization.  Therefore, even though the content of a schema bulks up the size and complexity of the metadata, it is necessary to capture this detail.

    ![Figure 6](/practices/common-data-definitions/semantic-to-implementation-assets-and-schemas.svg)
    > Figure 6: Schemas describe the structure of the data store in a digital resource (described by the asset in the catalog)

    A schema is typically attached to only one asset since it is classified and linked to other elements assuming that the asset/schema combinations describes the particular collection of data stored in the associated digital resource.  However, there is still a role for the subject area materials to provide preferred schema structures for software developers, data engineers and data scientists to use when they create implementations of new digital resources.

    When a new asset is created, the schema definition in the subject area can be used as a template to define the schema for the asset (see figure 7). Then:

    * The digital resource can be generated from the asset/schema, or
    * *Metadata discovery* (see below) can be used to validate that the schema defined in the digital resource matches the schema associated with the asset.

    ![Figure 7](/practices/common-data-definitions/semantic-to-implementation-assets-and-schemas-templates.svg)
    > Figure 7: Using a schema from a subject are as a template for a new asset

    There is also an opportunity to share schemas between assets using an *ExternalSchemaType*.  This option has the advantage that there only one copy of the schema.  However, it is only used when all classifications and relationships attached to the shared part of the schema apply to all data in the associated digital resources.

    ![Figure 8](/practices/common-data-definitions/semantic-to-implementation-assets-and-schemas-external.svg)
    > Figure 8: Using an external schema type to share a common schema 

    !!! education "Further information"
        * See [Model 0503](/types/5/0503-Asset-Schema) in the *Open Metadata Types* to understand the *AssetSchemaType* relationship.
        * See [Model 0501](/types/5/0501-Schema-Elements) in the *Open Metadata Types* to understand how schemas are represented on open metadata.
        * See [Model 0505](/types/5/0505-Schema-Attributes) in the *Open Metadata Types* to understand how schema attributes are represented on open metadata.


??? info "Reference value assignments"

    The common deinfitions for a subject area may include sets of values used to label metadata elements to show that they are in a particular state or have a specific characteristic that is important in the subject area.  For example, a subject area about people may include the notion of an *Adult* and a *Child* (or *Minor*).  The age of majority is different in each country and so a simple label assigned to a [Person](/types/1/0112-People) profile that indicates that a person is an adult would allow the knowledge of how to determine if someone is an adult to be contained around the maintenance of the person profiles, while the reference data value is used in multiple places.

    These labels are called *reference data values* and are managed in [Valid Value Sets](/types/5/0545-Reference-Data).  The association between a reference data value and a metadata element is [ReferenceValueAssignment](/types/5/0545-Reference-Data).

    ![Figure 9](/practices/common-data-definitions/semantic-to-implementation-reference-value-assignment.svg)
    > Figure 9: Labelling using reference data values

    !!! education "Further information"
        * [Reference Data Management](/features/reference-data-management/overview) describes different uses of valid value sets.

??? info "Schema assignments"

    Figure 10 show three types of assignments between the metadata associated with a digital resource ([technical metadata](/patterns/metadata-manager/overview/#technical-metadata)) and the subject area materials:

    * [SemanticAssignment](/types/3/0370-Semantic-Assignment) - Semantic assignments indicate that the data stored in the associated data field has the meaning described in the glossary term.
    * [ValidValuesAssignment](/types/5/0545-Reference-Data) - Valid value sets define a list of valid values.  They can be used to the values that are allowed to be stored in a particular data field if it can be described as a discrete set.  
    * [DataClassAssignment](/types/5/0540-Data-Classes) - A data class assignment means that the data in the data field conforms to the type described in the data class.

    When these relationships are used in combination, there should be consistency between the assignments to the data field and those to the associated glossary term.

    ![Figure 10](/practices/common-data-definitions/semantic-to-implementation-schema-assignment.svg)
    > Figure 10: Using assignment relationships to create a rich description of the data stored in a schema attribute (data field)

??? info "Governance action classifications"

    [Governance action classifications](/types/4/0422-Governance-Action-Classifications) can be attached to most types of metadata elements.  They can also be assigned to glossary terms to indicate that the classification applies to all data values associated with the glossary term.  The governance action classifications have attributes that identify a particular *level* that applies to the attached element. The definition for each [level](/types/4/0421-Governance-Classification-Levels) can be linked to appropriate Governance Definitions that define how digital resources classified at that level should be governed.  Governance Classification Levels are linked to Governance Definitions using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.

    ![Figure 11](/practices/common-data-definitions/semantic-to-implementation-governance-classification.svg)
    > Figure 11: Classifying glossary terms to identify the governance definitions that apply to all data values associated with the glossary term 

    !!! education "Further information"
        * [Setting up your Governance Program](guides/planning/governance-program/overview/) describes how different types of governance metadata are used.


??? info "Connectors and connections"

    The digital resources associated with the assets in the catalog are accessed through connectors.  A Connector is a client library that applications use to access the data/function held by the digital resource.  Typically, there is a specialized connector for each type of Asset/technology.  

    Sometimes there are multiple connectors to access a specific type of asset, each offering a different interface for  the application to use.

    Instances of connectors are created using the *[Connector Broker](/concepts/connector-broker)*.  The connector broker creates the connector instance using the information stored in a *[Connection](/concepts/connection)*.  These can be created by the application or retrieved from the open metadata stores.

    A connection is stored in the open metadata stores and linked to the appropriate asset for the digital resource.

    ![Figure 12](/practices/common-data-definitions/semantic-to-implementation-connectors.svg)
    > Figure 12: Connection information needed to access the data held by an asset

    !!! education "Further information"
        * See the [connector catalog](/connectors) to understand how connectors are used in Egeria.
        * See [Model 0201](/types/2/0201/Connectors-and-Connections) in the *Open Metadata Types* to understand how connections are represented.

??? info "Metadata discovery"

    An [open discovery service](/concepts/open-discovery-service) is a process that runs a pipeline of analytics to describe the data content of a resource. It uses statistical analysis, reference data and other techniques to determine the data class and range of values stored, potentially what the data means and its level of quality. The result of the analysis is stored in metadata objects called [annotations](/concepts/discovery-analysis-report/#discovery-annotations).

    Part of the discovery process is called *Schema Extraction*.  This is where the discovery service inspects the schema in the digital resource and builds a matching structure of *[DataField]/types/6/0615-Schema-Extraction/)* elements in open metadata.  As it goes on to analyse the content of a particular data field in the resource, it can add its results to an annotation that is attached to the DataField element.  It can also maintain a link between the DataField element and its corresponding SchemaAttribute element if the schema has already been attached.  Through ths process it is possible to detect any anomalies between the documented schema and what is actually implemented.

    Part of the analysis of a single data field may be to identify its *data class* (or a list of possible data classes if the analysis is not conclusive).  THe data class in turn may identify a list of possible glossary terms that could apply to the data field.

    For example, there may be a data class called address.  A discovery service may detect that an address is stored in a digital resource.  The data class may be linked to glossary terms for *Home Address*, *Work Location*, *Delivery Address*, ...  The discovery service may not be able to determine which glossary term is appropriate in order to establish the [SemanticAssignment](/types/3/0370-Semantic-Assignment) relationship, but providing a steward with a short list is a considerable saving.

    ![Figure 13](/practices/common-data-definitions/semantic-to-implementation-discovery.svg)
    > Figure 13: Output from a metadata discovery service

    !!! education "Further information"
        * See [Discovery and Stewardship](/features/discovery-and-stewardship/overview) to understand how metadata discovery works.
        * See [Area 6](/types/6) in the *Open Metadata Types* to understand how discovery metadata is represented.

??? summary "Bringing it all together"

    Figure 13 summarizes how the subject area materials create a rich picture around the resources used by your organization.  As they link to the technical metadata, they complement and reinforce the understanding of your data. In a real-world deployment, the aim is to automate as much of this linkage as possible. This is made considerably easier if the implementation landscape is reasonable consistent.  However, where the stored data values do not match the expected types defined in the schema, the metadata model reveals the inconsistencies and often requires human intervention to ensure the links are correct.

    ![Figure 14](/practices/common-data-definitions/semantic-to-implementation-big-picture.svg)
    > Figure 14: Linking the metadata together



--8<-- "snippets/abbr.md"
