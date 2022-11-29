
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0530 Tabular Schemas

The 053x models cover specialized types that represent the popular technologies.  These types inherit from common schema element types:

* [SchemaAttribute](/types/5/0505-Schema-Attributes) - this is the place where the data is stored.
* [SchemaType](/types/5/0501-Schema-Elements) - ths is the type of the data - typically defining what values can be stored and how they are structured/formatted.  For example, the schema type may be a primitive value ([PrimitiveSchemaType](/types/5/0501-Schema-Elements)) or a structure ([ComplexSchemaType](/types/5/0505-Schema-Attributes)).

![UML](0530-Tabular-Schemas.svg)

## RootSchemaType

*RootSchemaType* is an informational type in that it does not add new attributes to the type system.  Instead, it provides a marker to indicate that types that inherit from it are typically the root of a schema definition.  It is this element that connects to [assets](/types/0503-Asset-Schema) and [ports](/types/5/0520-Process-Schemas).

## TabularSchemaType

*TabularSchemaType* is an example of a *RootSchemaType* that describes the structure of an asset that is a single table of data.
For example, this could be a file that is organized into columns such as in a [CSV file](/types/2/0220-Files-and-Folders) or spreadsheet.

![single table of data](cost-codes-contents.png)

The image above shows the content of a CSV file called `CostCodes.csv`.  It is catalogued using a [*CSVFile*](/types/2/0220-Files-and-Folders) asset entity.  Linking from it using the [*AssetSchemaType*](/types/5/0503-Asset-Schema) relationship would be a *TabularSchemaType* entity describing the structure of the data in the file.

## TabularColumn

A *TabularColumn* entity is used to describe one of the columns in a tabular schema.  It is linked to the *TabularSchemaType* entity using the [*AttributeForSchema*](/types/5/0505-Schema-Attributes) relationship.   The type information for each column is directly embedded on the *TabularColumn* entity through the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes) classification.


## TabularFileColumn

A *TabularFileColumn* is a specialization of *TabularColumn* to enable a column in a file to have a distinctive subtype from a column in a database - represented by [RelationalColumn](/types/5/0534-Relational-Schemas).

![Schema for the CostCodes.csv file](csv-schema-example.svg)




!!! info "Further Information"

    * [Relational database columns](/types/5/0534-Relational-Schemas) are specializations of the tabular schema.
    * [Files Integrator OMIS](/services/omis/files-integrator/overview) calls [Data Manager OMAS](/services/omas/data-manager/overview) to catalog files and their schemas.



??? deprecated "Deprecated types"
    The **TabularColumnType** entity has been deprecated because it restricts tabular columns to primitive types and some technologies will be able to support more types.


--8<-- "snippets/abbr.md"