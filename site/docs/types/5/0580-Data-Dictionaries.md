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

## DataField entity

A [referenceable](/type/0/0010-Base-Model) that describes a data field.

* *displayName* - Name of the data field.
* *namespace* - Optional namespace to help build a qualified name for the data field.
* *aliases* - Alternative name to use for the data field - useful when matching against a schema.
* *namePatterns* - List of patterns to use to match a name against a schema attribute - useful when matching against a schema.
* *description* - Description of the data field.
* *isDeprecated* - Is this data field deprecated?
* *versionIdentifier* - Managed version identifier.
* *defaultValue* - Default value to use if the actual data value is null.
* *isNullable* - Can the data field store null?
* *dataType* - What is the data type of this field
* *minimumLength* - What is the minimum length of this field - typically used with string fields.
* *length* -  What is the length (in bytes) table up by this field.
* *precision* - How many digits after the decimal point.
* *orderedValues* - Are the values sorted
* *sortOrder* - DataItemSortOrder value identifying the sort direction used on the data field values.
* *namePatterns* - Regular expressions that characterize the name of the data field.

## ObjectIdentifier classification

The *ObjectIdentifier* classification indicates that a data item is typically used as a unique identifier.  It is typically attached to a data field.

## DataDictionary classification

Identifies that a [collection](/type/0/0021-Collections) is a [data dictionary](/concepts/data-dictionary).  This is an organized collection of defined data fields that can be used as a knowledge base of preferred data definitions for data professionals.

## DataSpec classification

Identifies that this is a [collection](/type/0/0021-Collections) is a [data specification](/concepts/data-specification) that describes the data requirements for a project or initiative.  Its members are typically [data structures](/concepts/data-structure).

## DataStructure entity

A [referenceable](/type/0/0010-Base-Model) that provides list of data fields that describe the structure of a data source within a data specification.

* *displayName* - Name of the data structure.
* *namespace* - Optional namespace to help build a qualified name for the data structure.
* *description* - Description of the data field.
* *versionIdentifier* - Managed version identifier.

It is used to specify/validate the values in an asset's [schema](/concepts/schema), which in turn describes the structure of data in the [digital resource](/concepts/digital-resource).


## MemberDataField relationship

Represents an association between a data structure and one of its data fields.

## DataStructureDefinition relationship

Represents an association between a data structure that describes a data source and a certification type that indicates that certified elements conform to the data structure and associated definitions (such as glossary term and data class).

--8<-- "snippets/abbr.md"