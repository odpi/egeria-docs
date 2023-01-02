---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Open Metadata Type Definitions (TypeDefs)

TypeDefs define the characteristics of a particular type of an [open metadata instance/element](/concepts/open-metadata-instances).
There are three categories of TypeDefs (`TypeDefCategory`):

- *EntityDef*: the definition of a type of [entity](/concepts/open-metadata-instances)
- *RelationshipDef*: the definition of a type of [relationship](/concepts/open-metadata-instances)
- *ClassificationDef*: the definition of a type of [classification](/concepts/open-metadata-instances)

TypeDefs can inherit from other TypeDefs from the same category.  Open metadata support single inheritance.

TypeDefs also define then names and types of properties for a metadata instance of that type.
Each property has a *TypeDefAttribute* definition that references an **AttributeTypeDef**
as its type.

The AttributeTypeDefs are the type definitions for properties.
There are three categories of AttributeTypeDefs.

- *EnumDef*: the definition of an enumerated list of valid values.
- *CollectionDef*: the definition of a collection - such as an array of strings, or a map from string to object.
- *PrimitiveDef*: a primitive - such as a string, integer or date.


--8<-- "snippets/abbr.md"