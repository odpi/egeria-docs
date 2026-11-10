---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Modelling Databases


Figure 1 shows the types of metadata that describe databases.

![Figure 1](relational-database-model.svg)
> **Figure 1:** Database metadata

The structure of a database schema consists of a number of database tables and database views.
The difference is that the database table has its values stored in the database whereas the
database view is a set of values that are derived from accessing other
database tables using a query.

The structure of both the database tables and database views are described by database columns.

Database columns have a type that represents a single value.  This can be stored, or derived using a query.
If the column holds the unique identifier for a row within the table, it can be decorated with the
[PrimaryKey](/types/5/0534-Relational-Schemas) classification.
If a column contains values that are the primary key of another table then the two columns can be linked using the
[ForeignKey](/types/5/0534-Relational-Schemas) relationship.

Figure 2 shows the open metadata types used to represent this metadata.

![Figure 2](relational-database-open-metadata-types.svg)
> **Figure 2:** Database open metadata types for databases

A database schema is represented using the
[DeployedDatabaseSchema](/types/2/0224-Databases) entity,
the database table is represented using the 
[RelationalTable](/types/5/0534-Relational-Schemas) entity
and the database column is represented using the 
[RelationalColumn](/types/5/0534-Relational-Schemas) entity.
A database view is a 
[RelationalTable](/types/5/0534-Relational-Schemas) entity
with the [Calculated Value](/types/5/0512-Derived-Schema-Elements)
classification attached.

If the DatabaseManager is catalogued, link each Database to it using the
[CapabilityAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
A DeployedDatabaseSchema is linked to its Database using the
[DataSetContent](/types/2/0210-Data-Stores) relationship.
(The database schema is a DataSet over the database which is a type of DataStore).

Between the DeployedDatabaseSchema entity and its RelationalTable entities sit the
[Schema](/types/5/0503-Asset-Schema) relationship,
[RelationalDBSchemaType](/types/5/0534-Relational-Schemas) entity and
[AttributeForSchema](/types/5/0505-Schema-Attributes) relationship.
An integration connector creates these elements through the clients of its
[integration context](/guides/developer/integration-connectors/integration-context).  Egeria's database server connectors (for example, the PostgreSQL, Oracle, Microsoft SQL Server and Db2 server connectors)
create the database-level elements by [cataloguing from templates](/features/templated-cataloguing/overview) supplied on their catalog targets.

The SchemaType for a RelationalTable is [RelationalTableType](/types/5/0534-Relational-Schemas).
The schema attributes for RelationalTable and RelationalColumn also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).


---8<-- "snippets/abbr.md"