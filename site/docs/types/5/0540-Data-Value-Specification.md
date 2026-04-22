<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0540 Data Value Specification

The [*DataValueSpecification*](/concepts/data-value-specification) describes a specification of the values that are associated with a data field.

![UML](0540-Data-Value-Specification.svg)

## DataValueSpecification entity

In addition to inheriting from [AuthoredReferenceable](/types/0/0010-Base-Model), the attributes for a data value specification are:

* *namespacePath* - Namespace that the data class is organized under.
* *matchPropertyNames* - List of property names that are filled out in this data class.  This helps automation to locate the type of data values that this data class supports/represents.
* *matchThreshold* - The percentage of data values in the data resource that need to match to be assigned to this data class.
* *specification* - A specification of the matching data values.  This can be machine or human-readable.  This attribute allows a rules language to be used to describe the data class's values.  So it may be the rule explicitly stated, or the name of a rule.
* *specificationDetails* - Adds additional values to the specification - for example, they may be substitution values to insert in to the specification string.
* *dataType* - Name of the data type used to encode this type of data - for example, string, int, char, ...
* *units* - Units of measure for the data values.
* *absoluteUncertainty* - Absolute uncertainty of the data values.
* *relativeUncertainty* - Relative uncertainty of the data values.

## DataValueHierarchy relationship

Data value specification can be organized into a hierarchy using the *DataValueHierarchy* relationship where more general data value specifications, such as the *date* data data class are at the top and underneath it are more specialized data value specifications such as *date of birth*.  This means that discovery and stewardship processes can use the data class to hone in on the most specific logical data type for a data field and consequently run the most appropriate data quality rules on the data field's values.  This hierarchy can also be used when generating software artifacts, such as *Open API Specifications*, *Database Definition Language (DDL)* scripts or *JSON schema*.  If a field is assigned a data class that is not present in the target programming language, the generator can navigate up the data class hierarchy to the more general type that is supported in the target language.


## DataValueDefinition relationship

Data classes can be used to augment the definition of a [DataStructure](/types/5/0580-Data-Dictionaries) or [DataField](/types/5/0580-Data-Dictionaries) to make it easy to automated processes to identify the data class to use for an analysis.

## DataValueAssignment relationship

Data value specifications can be assigned to elements to show that the data associated with the element conforms to the specification.  A [survey action service](/concepts/survey-action-service) can propose a list of data value assignments and these are stored in the [*DataClassAnnotation*](/type/6/0625-Data-Class-Discovery) or [*DataGrainAnnotation*](/type/6/0626-Data-Grain-Discovery).  Subsequent stewardship - either automated or with human assistance - can confirm the correct assignment using the *DataValueAssignment* relationship.

## DataValueAssignmentStatus enumeration

The *DataValueAssignmentStatus* enumeration is used to describe the status of the assignment of a data value specification, such as a [data class](/concepts/data-class), or a [data grain](/concepts/data-grain), to an element.

* DISCOVERED - The data value specification has been discovered and assigned to the element.
* PROPOSED - The data value specification has been proposed for assignment to the element.
* IMPORTED - The data value specification has been imported from another system.
* VALIDATED - The data value specification has been confirmed as assigned to the element.
* DEPRECATED - The data value specification has been deprecated and should not be used.
* OBSOLETE - The data value specification has been superseded by another specification.
* OTHER - The data value specification has a status that is not defined in this enumeration.

--8<-- "snippets/abbr.md"

