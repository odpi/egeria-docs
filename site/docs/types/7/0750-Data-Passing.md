---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0750 Data Passing

Describes relationships that show where data and control is passed between processes and assets.  These relationships show the structure of the data processing.  They can link [Assets](/egeria-docs/types/0/0010-Base-Model), or [Ports](/egeria-docs/types/2/0217-Ports) or [SchemaAttributes](/egeria-docs/types/5/0505-Schema-Attributes)
depending on the level of detail that is known.

These relationships are then overlaid by the [LineageMapping](/egeria-docs/types/7/0770-Lineage-Mapping) relationship to show which are significant for lineage.


![UML](0750-Data-Passing.svg)


??? deprecated "Deprecated types"
    - *ProcessInput*
    - *ProcessOutput*

--8<-- "snippets/abbr.md"