<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0505 Schema Attributes

[Schemas](/concepts/schema) typically have a hierarchical structure. Model 0505 provides for a structure of complex schema types that have their own internal structure. This structure is defined through one or more nested *schema attributes* each with their own type.

![UML](0505-Schema-Attributes.svg)

## TypeEmbeddedAttribute classification

The *TypeEmbeddedAttribute* classification is applied directly to the *SchemaAttribute* to provide its type information. For example, if a ComplexSchemaType has a simple string attribute this can be captured as a SchemaAttribute (giving the name of the attribute) with a TypeEmbeddedAttribute classification (whose `dataType` property indicates `string`).

TypeEmbeddedAttribute can represent any of the standard schema types. Where a schema type is described using multiple schema type objects,(such as [MapSchemaType](/types/5/0511-Map-Schema-Elements), [SchemaOptionChoice](/types/5/0501-Schema-Elements) and [ExternalSchemaType](/types/5/0507-External-Schema-Type)) the schema relationships for that type begin with *SchemaElement* and then map to more detailed SchemaTypes. This is so they can be connected to a SchemaAttribute or a SchemaType.

## NestedSchemaAttribute relationship

A *SchemaAttribute* can be nested within another *SchemaAttribute* using the *NestedSchemaAttribute* relationship. See [0534 Relational Schemas](/types/5/0534-Relational-Schemas) for an
example of this between RelationalTables and RelationalColumns.

## SchemaAttributeType relationship

The *SchemaAttributeType* relationship only should be used if the same schema type is used in multiple attributes within the same schema. 

(To use a standard, pre-defined type for a schema attribute's type, set an [ExternalSchemaType](/types/5/0507-External-Schema-Type) in the TypeEmbeddedAttribute and link to the standard, pre-defined type using the *LinkedExternalSchemaType* relationship.)

The combined properties of *SchemaAttribute* can be used to represent simple bounded types like sets and arrays:

- Array: `minCardinality = 0`, `maxCardinality = -1`, `allowsDuplicateValues = true`, `orderedValues = true`
- Set: `minCardinality = 0`, `maxCardinality = -1`, `allowsDuplicateValues = false`, `orderedValues = false`
- Bag: `minCardinality = 0`, `maxCardinality = -1`, `allowsDuplicateValues = true`, `orderedValues = false`


## DataItemSortOrder enum

*DataItemSortOrder* provides the valid values for the *sortOrder* property of SchemaAttribute.  It indicates whether the rows/instances of the data stored in this schema appear in any particular order or not.

| Enumeration | Value | Name           | Description                                                                     |
|-------------|-------|----------------|------------------------------------------------------------------------------------------------|
| UNKNOWN     | 0     | "<Unknown>"    | The sort order is not specified. |
| ASCENDING   | 1     | "Ascending"    | The attribute instances are organized so that the smallest/lowest value is first and the rest of the instances follow in ascending order. |
| DESCENDING  | 2     | "Descending"   | The attribute instances are organized so that the largest/highest value is first and the rest of the instances follow in descending order. |
| UNSORTED    | 3     | "Unsorted"     | The instances of the schema attribute may appear in any order. |                                                                            


--8<-- "snippets/abbr.md"