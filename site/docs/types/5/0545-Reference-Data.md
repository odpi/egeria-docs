---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0545 Reference Data

Reference data provides authoritative definitions of valid values for data.  An individual valid value can be either a *ValidValueSet* or a *ValidValueDefinition*.  *ValidValueSet*s can have other valid values nested inside them using the *ValidValueMapping* relationship.  As such, valid values can be organized in a hierarchy.

A set of valid values can be used to describe the values that may be stored in a data field.  The *ValidValuesAssignment* relationship is used to link the valid value set to an element that represents the data field such as a [GlossaryTerm](/types/3/0330-Terms) or a [SchemaElement](/types/5/0501-Schema-Elements). The *strictRequirement* properties indicates whether the data field can only contain the values listed (strictRequirement=true) or the valid value set is just a suggestion.

A valid values set can also be implemented in an asset that can be used as a look-up table while data is being processed.

![UML](0545-Reference-Data.svg)


--8<-- "snippets/abbr.md"