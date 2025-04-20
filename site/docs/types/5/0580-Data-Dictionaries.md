---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0580 Data Dictionaries

At the start of a data project, it is often necessary to describe the types of data that is needed.  This is called a data specification.  
*DataField* entities are used to model specific data fields required by the data project.  As the project progresses, [data schemas](/tpyes/5/0505-Schema-Attributes) are defined to describe how data is organized in the different data assets used by the project.

The data dictionary maintains lists of pre-defined, reusable data fields.

![UML](0580-Data-Dictionaries.svg)

## ObjectIdentifier classification

Th *ObjectIdentifier* classification indicated that a data item is typically used as a unique identifier.

## DataDictionary classification

Identifies that a [collection](/type/0/0021-Collections) is an organized collection of defined data fields that can be used in a data specification to describe some desired data.

## DataSpec classification

Identifies that this is a [collection](/type/0/0021-Collections) that describes the data requirements for a project or initiative.

## DataStructure entity

A list of data fields that describe the structure of a data source.

## DataField entity

A description of a data field.

## MemberDataField relationship

Represents an association between a data structure and one of its data fields.

## DataStructureDefinition relationship

Represents an association between a data structure that describes a data source and a certification type that indicates that certified elements conform to the data structure and associated definitions (such as glossary term and data class).

--8<-- "snippets/abbr.md"