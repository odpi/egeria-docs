---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0501 Schema Elements

[Schema](/concepts/schema) are used to represent the structure of data.  They show the fields (also known as attributes or properties)
of the data along with its type.

**SchemaElement** describes the base definition for representing
schema elements in metadata.   The **SchemaType** describes the
top-level name of a schema and also the types of any fields nested in it.

![UML](0501-Schema-Elements.svg)

For complex data structures, [SchemaAttributes](/types/5/0505-Schema-Attributes) describe individual fields.

--8<-- "snippets/abbr.md"