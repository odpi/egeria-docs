---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0503 Asset Schema

Model 0503 shows the relationship between an [Asset](/types/0/0010-Base-Model)
and a [SchemaType](/types/5/0501-Schema-Elements).

When an asset is linked to a schema type it means that the schema type describes
the structure of the Asset. 

The schema type can not be shared between different assets.
If you are cataloging multiple assets with the same data structure, you can use
a template which will copy the schema structure from the template asset to the new asset.
(See [Templated Cataloging](/features/templated-cataloging/overview) for more details.

![UML](0503-Asset-Schema.svg)


--8<-- "snippets/abbr.md"