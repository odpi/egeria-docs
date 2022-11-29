<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0501 Schema Elements

[Schema](/concepts/schema) are used to represent the structure of data.  They show the fields (also known as attributes or properties) of the data along with its type.

![UML](0501-Schema-Elements.svg)

## SchemaElement

*SchemaElement* describes the common attributes that are present in any entity that is part of a schema definition.  Notice it inherits [*Referenceable*](/types/0/0010-Base-Model) which means that it can be tagged with [glossary terms](/types/3/0370-Semantic-Assignment), [valid values](/types/5/0545-Reference-Data) and [feedback](/types/1/0150-Feedback).

## SchemaType

The *SchemaType* describes the structure of data.  It has many subtypes, each covering a specialized structure.

* [LiteralSchemaType](#literalschematype) for a fixed single value.
* [SimpleSchemaType](#simpleschematype) for a single value.
* [ComplexSchemaType](/types/5/0505-Schema-Attributes) for complex data structures.
* [SchemaTypeChoice](#schematypechoice-and-schematypeoption) for places where there are more than one option for the structure of the data.

## LiteralSchemaType

The *LiteralSchemaType* is used to describe a data field that has a fixed value.  It is used where literal values are encoded in the schema. 

## SimpleSchemaType

The *SimpleSchemaType* describes a data field that has a single value.  It includes a string name for the specific name of the data type and an optional default value.   The value of *dataType* is not controlled by the open metadata types.  You can choose to use the technical type name used to encode the data field in the schema, or you can define a [Valid Value Set](/types/5/0545-Reference-Data) to define the list of valid values and use those values.

There are two main subtypes of *SimpleSchemaType*:

* *PrimitiveSchemaType* for representing primitive types such as strings and numbers.
* *EnumSchemaType* for representing a fixed list of values (often called an enumeration or enum).  Any schema type can have a list of valid values attached to it via the [*ValidValueAssignment*](/types/5/0545-Reference-Data) relationship to show the values that the data field may have.  This practice is particularly relevant for EnumSchemaType data fields.

## SchemaTypeChoice and SchemaTypeOption

Some schemas include choices in how data can be structured.  Each choice is described as a schema type.  The place where the choice occurs is represented using a *SchemaTypeChoice* entity, and it is linked to each choice using the *SchemaTypeOption* relationship.







--8<-- "snippets/abbr.md"