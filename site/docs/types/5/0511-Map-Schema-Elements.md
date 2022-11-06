<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0511 Map Schema Elements

Maps hold the relationship between pairs of values.  Often they show how one value (the domain) can be mapped to another value (the range).
The relationships start from [SchemaElement](/type/5/0501-Schema-Elements) rather than MapSchemaType since the schema type may be located in the [TypeEmbeddedAttribute classification](/types/5/0505-Schema-Attributes).

![UML](0511-Map-Schema-Elements.svg)

## MapSchemaType

The *MapSchemaType* describes the types of the values being mapped.

## MapFromElementType

The *MapFromElementType* relationship describes the domain type.

## MapToElementType

The *MapToElementType* relationship describes the range type.



--8<-- "snippets/abbr.md"