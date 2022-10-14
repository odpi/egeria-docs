<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0534 Relational Schemas

Model 0534 describes the parts of a relational schema. These are used in relational databases represented by the [Database](/types/2/0224-databases) or [DeployedDatabaseSchema](/types/2/0224-databases) entity. There are multiple tables and views defined within the relational schema.   The columns are within both the tables and views.

![UML](0534-Relational-Schemas.svg)

## RelationalDBSchemaType

The starting entity for a relational schema (known as the [*RootSchemaType*](/types/5/0530-Tabular-Schemas)) is the *RelationalDBSchemaType*.  It is linked to one or more *RelationalTable* entities using the [*AttributeForSchema*](/types/5/0505-Schema-Attributes) relationship.

## RelationalTable

The *RelationalTable* entity represents a table in a relational schema.  *RelationalTable* inherits from [*SchemaAttribute*](/types/5/0505-Schema-Attributes).  The schema type to use with a *RelationalTable* is *RelationalTableType*.

## RelationalTableType

*RelationalTableType* is the schema type for a *RelationalTable* entity.  It inherits from [*ComplexSchemaType*](/types/5/Schema-Attributes) to show that it is made up of multiple elements - in this case, the elements are *RelationalColumn* entities.

??? info "Choices on representing the schema type for a relational table"
    The type information for each table is typically embedded in the *RelationalTable* through the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes) classification. The *typeName* attribute of this classification is set to *RelationalTableType*.

     Older implementations of the open metadata types may use a separate [*SchemaType*](/types/5/0501-Schema-Elements) entity linked to the *RelationalTable* via the [*SchemaAttributeType*](/types/5/0505-Schema-Attributes) relationship.

??? info "Choices on linking a relational table to a relational column"
    If the *RelationalTable* entity has the *TypeEmbeddedAttribute* classification, it is connected to its *RelationalColumn* entities using the [*NestedSchemaAttribute*](/types/5/0505-Schema-Attributes) relationship.

    Otherwise the associated *RelationalTableType* entity is linked to the *RelationalColumn* via the *AttributeForSchema* relationship.

??? info "Representing relational views"
    A relational view is a relational query that returns a table as its results.  It may retrieve data from multiple tables and these tables may be stored in multiple database.

    A relational view is represented as a *RelationalTable* entity with the [*CalculatedValue*](0512-Derived-Schema-Elements) classification attached.  The query string used to create the view is stored in the *formula* attribute.

## RelationalColumn

A *RelationalColumn* entity represents a column in a relational table.  It inherits from [*SchemaAttribute*](/types/5/0505-Schema-Attributes)

??? info "Choices on representing the schema type for a relational column"
    The type information for each column is typically embedded in the *RelationalColumn* through the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes) classification.  The *typeName* attribute in the classification is set to the name of the SchemaType that represents the type of data stored in the column.

    Older implementations of the open metadata types may use a separate [*SchemaType*](/types/5/0501-Schema-Elements) entity linked to the *RelationalColumn* via the [*SchemaAttributeType*](/types/5/0505-Schema-Attributes) relationship.

??? info "Representing a derived relational column"
    Some columns in a relational table are calculated from other data.  For example a relational table may include both a `date of birth` and an `age` column for a person.  Only date of birth is stored and the `age` is calculated from the date of birth and the current date each time the table is retrieved.

    Columns that are calculated on retrieval are called derived relational columns.  Such a derived relational column is represented by a *RelationalColumn* entity with an attached [*CalculatedValue*](/types/5/0512-Derived-Schema-Elements) classification.

## PrimaryKey

The *PrimaryKey* classification can be attached to a *RelationalColumn* to indicate that the value stored for this column in each row of the table is a unique identifier for the row.

## ForeignKey

The *ForeignKey* relationship links a relational column in one relational table to a relational column in another relational table.

It indicates that the values stored in the first relational column are values from the second relational column.  Typically, the second relational column is a *PrimaryKey*.

Foreign keys are used to represent relationships between relational tables.

??? deprecated "Deprecated types"
     - The supertype of *RelationalTableType* has be changed to *ComplexSchemaType* rather than *TabularColumnType* since [TabularColumnType](/types/5/0530-Tabular-Schemas) is now deprecated.
     - *DerivedRelationalColumn* has been replaced by [CalculatedValue](/types/5/0512-Derived-Schema-Elements)and [DerivedSchemaTypeQueryTarget](/types/5/0512-Derived-Schema-Elements).
     - *RelationalView* has been replaced by [CalculatedValue](/types/5/0512-Derived-Schema-Elements).

--8<-- "snippets/abbr.md"