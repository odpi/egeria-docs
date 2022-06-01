<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Schema

A *schema* describes the structure of the data associated with an [Asset](/concepts/asset).
The technology that supports the asset often limits the structural choices for data.
For example:

* A relational database organizes data into collections of tables and columns.
* Technologies such as JSON or XML, organizes data into nested structures.
* Graph databases organizes data in nodes and relationships.

These differences need to be represented in the [Open Metadata Types](/types).  However, at the same time,
data governance is concerned with the accuracy and appropriate use of individual data values.
This is very expensive if each data item was governed individually so the data governance practices aim to group
like data together, so they can be governed in a consistent way.  As such, the open metadata types
provide a root set of types that all the specific schema structures inherit from.

## Schema Elements

The schema root type is called [Schema Element](/types/5/0501-Schema-Elements)
which is then dividing into a **Schema Attribute** (think of this as a variable) and a **Schema Type**.
The schema type describes the structure of the data associated with the schema attribute.

In the early versions of Egeria, the schema attribute and the schema type were represented as
as two separate entities in the open metadata types with a **SchemaTypeForAttribute** relationship to connect them together.
This is shown in figure 1.

![Figure 1](/guides/developer/mapping-technology/old-schema-types.svg)
> **Figure 1:** Original model for SchemaAttribute and its SchemaType

However, it became obvious that since these two elements need to retrieved together, it is much more
more efficient if the schema type is represented as a classification for the SchemaAttribute since
classifications are typically stored, distributed and retrieved with their entity.
The new classification is called **TypeEmbeddedAttribute** and it contains all of the properties found in
the schema types plus a **typeName** property to identify the corresponding schema type.

Figure 2 shows the new types for representing a schema attribute and its type.

![Figure 2](/guides/developer/mapping-technology/generic-schema-attribute.svg)
> **Figure 2:** Collapsing SchemaAttribute and SchemaType into an entity with a classification

Schema type entities are still used:

* to connect [Assets](/types/5/0503-Asset-Schema) and [Ports](/types/5/0520-Process-Schemas) to their schemas
* to connect structural schema types such as [maps](/types/5/0511-Map-Schema-Elements)
  and [external schemas](/types/5/0507-External-Schema-Type) to other types that represent their contents.

Figure 3 shows the use of the schema type:

![Figure 3](/guides/developer/mapping-technology/generic-schema-type.svg)
> **Figure 3:** The SchemaType is still used as the top level element in a schema and for complex structures

## Specific Schema Types

The root SchemaType and SchemaAttribute are specialized to support different structures.
The diagrams show how the structure is represented for a SchemaAttribute on the left and
how it is represented as a SchemaType on the right.

### Primitives

Primitives are single values such a string, characters and numbers.
They are represented by the [PrimitiveSchemaType](/types/5/0501-Schema-Elements).

![Figure 4](/guides/developer/mapping-technology/primitive-schema.svg)
> **Figure 4:** The PrimitiveSchemaType

### Literals (Constants)

Literals are fixed values, also known as **constants**.
They are represented by the [LiteralSchemaType](/types/5/0501-Schema-Elements).

![Figure 5](/guides/developer/mapping-technology/literal-schema.svg)
> **Figure 5:** The LiteralSchemaType

### Enumerations

Enumerations (Enums) define a list of valid values.  The valid values are recorded in a
[ValidValuesSet](/types/5/0545-Reference-Data) linked to an
[EnumSchemaType](/types/5/0501-Schema-Elements).

![Figure 6](/guides/developer/mapping-technology/enum-schema.svg)
> **Figure 6:** The EnumSchemaType

### Linking to a standard schema type

External schema types link to a schema type that is reused in multiple assets - typically it is
part of a standard.  The use of an external schema type is represented by an
[ExternalSchemaType](/types/5/0507-External-Schema-Type).

![Figure 7](/guides/developer/mapping-technology/external-schema.svg)
> **Figure 7:** The ExternalSchemaType

### Maps

Maps show how one set of values link to another.  They are often used for look up tables.  The map is
represented by a
[MapSchemaType](/types/5/0511-Map-Schema-Elements) that then links to two other SchemaTypes,
one for the type of the starting value and the other for the type of value it is mapped to.

![Figure 8](/guides/developer/mapping-technology/map-schema.svg)
> **Figure 8:** The MapSchemaType

### Alternative types

In some schemas, it is possible that there are multiple choices for the type of an element.
This is supported by the [SchemaTypeChoice](/types/5/0501-Schema-Elements).
This links to the options for the SchemaType.

![Figure 9](/guides/developer/mapping-technology/schema-choice.svg)
> **Figure 9:** The SchemaTypeChoice

### Structures or Records

It is common for an attribute to consist of a collection of other values.  For example
an attribute called employee may consist of multiple values from employee number, name, address, department, ....
These types of attribute are represented by the [StructSchemaType](/types/5/0505-Schema-Attributes).

![Figure 10](/guides/developer/mapping-technology/struct-schema.svg)
> **Figure 10:** The StructSchemaType

The relationship between the schema attribute and its nested schema attributes is **NestedSchemaAttribute**.
The relationship between the StructSchemaType and its nested schema attributes is **AttributeForSchema**.

## Related Information

[Data classes](/concepts/data-class) provide the ability to define logical data types to complement the schema elements.

### Open Metadata Types

Open Metadata types for connecting schemas to other types of elements:

* **[0503 Asset Schema](/types/5/0503-Asset-Schema)** - for the relationship between an Asset and
  its top level SchemaType.
* **[0520 Process Schemas](/types/5/0520-Process-Schemas)** - showing how a schema type can be attached to a process port.

Open Metadata Types for different types of data structures:

* **[0501 Schema Elements](/types/5/0501-Schema-Elements)** - for SchemaElement, SchemaType,
  PrimitiveSchemaType, LiteralSchemaType, EnumSchemaType and SchemaTypeChoice.
* **[0505 Schema Attributes](/types/5/0505-Schema-Attributes)** - for SchemaAttribute, ComplexSchemaType,
  StructSchemaType.
* **[0507 External Schema Types](/types/5/0507-External-Schema-Type)** - for ExternalSchemaType.
* **[0511 Map Schema Element](/types/5/0511-Map-Schema-Elements)** - for MapSchemaType.
* **[0512 Derived Schema Elements](/types/5/0512-Derived-Schema-Elements)** for DerivedSchemaTypeQueryTarget

Specializations of the main types of schema structures for particular types of technology.
They enable retrieval of technology-specific schema elements.
For example, a query for relational columns with a particular characteristic.

* **[0530 Tabular Schema](/types/5/0530-Tabular-Schemas)** - for TabularSchemaType and TabularColumn.
* **[0531 Document Schemas](/types/5/0531-Document-Schemas)** - for DocumentSchemaType and DocumentSchemaAttribute.
* **[0532 Object Schemas](/types/5/0532-Object-Schemas)** - for ObjectSchemaType and ObjectAttribute.
* **[0533 Graph Schema](/types/5/0533-Graph-Schemas)** - for types associated with graph stores.
* **[0534 Relational Schema](/types/5/0534-Relational-Schemas)** for types associated with relational data
* **[0535 Event Schema](/types/5/0535-Event-Schemas)** - for EventTypeList, EventType and EventSchemaAttribute.
* **[0536 API Schemas](/types/5/0536-API-Schemas)** - for types associated with APIs.

### Open Metadata and Governance APIs
APIs that support the definition of schemas:

* [Asset Owner OMAS](/services/omas/asset-owner/overview)
* [Asset Manager OMAS](/services/omas/asset-manager/overview)
* [Data Manager OMAS](/services/omas/data-manager/overview)
* [Governance Engine OMAS](/services/omas/governance-engine/overview)
* [Database Integrator OMIS](/services/omis/database-integrator/overview)
* [Files Integrator OMIS](/services/omis/files-integrator/overview)
* [API Integrator OMIS](/services/omis/api-integrator/overview)
* [Topic Integrator OMIS](/services/omis/topic-integrator/overview)
* [Governance Action OMES](/services/omes/governance-action/overview)

Other types of information associated with an Asset:

* [The contents of an asset catalog](/patterns/metadata-manager/overview)

--8<-- "snippets/abbr.md"
