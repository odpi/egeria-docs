---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0530 Tabular Schemas

Model 0530 shows the the structure of a single table. This could be a file that is organized into columns such as a [CSV file](/types/2/0220-Files-and-Folders).

Note that for such a simple structure, the type information for each column can be directly embedded on the **TabularColumn** through the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes.md) classification.

![UML](0530-Tabular-Schemas.svg)


## Further Information

* [Files Integrator OMIS](/services/omis/files-integrator/overview)
* [Data Manager OMAS](/services/omas/data-manager/overview)



??? deprecated "Deprecated types"
    The **TabularColumnType** entity has been deprecated because it restricts tabular columns to primitive types and some technologies will be able to support more types.


--8<-- "snippets/abbr.md"