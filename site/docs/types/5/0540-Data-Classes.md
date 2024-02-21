<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0540 Data Classes

Data classes describe logical data types that can be used to classify data values in a consistent and standardized way.  They are particularly important in [metadata discovery](/features/discovery-and-stewardship/overview).

![UML](0540-Data-Classes.svg)

## DataClass

The *DataClass* entity provides the specification of a [logical data type](/concepts/data-class). This goes beyond the [*SchemaType*](/types/5/0501-Schema-Elements) used to store the data value and includes a specification of the values that are found in this logical type.  For example, a credit card number is typically stored as a string.  However, it has a well-defined pattern of four groups of four digits.  The data class allows the capture of the specification of a credit card number type that can be used by discovery engines to narrow down the expected data values within a [digital resource](/concepts/digital-resource).


## DataClassHierarchy

Data classes can be organized into a hierarchy using the *DataClassHierarchy* relationship where more general data classes, such as *date* are at the top and underneath it are more specialized classes such as *date of birth*.  This means that discovery and stewardship processes can use the data class to hone in on the most specific logical data type for a data field and consequently run the most appropriate data quality rules on the data field's values.  This hierarchy can also be used when generating software artifacts, such as *Open API Specifications*, *Database Definition Language (DDL)* scripts or *JSON schema*.  If ia field is assigned a data class that is not present in the target programming language, the generator can navigate up the data class hierarchy to the more general type that is supported in the target language.

## DataClassComposition

Data classes can be organized into a structural hierarchy using the *DataClassComposition* relationship.  For example, an address data class could be composed of a number of data classes that each describe a part of the address.  The properties in this relationship show how the fields are arranged.

## DataClassAssignment

Data classes can be assigned to elements (typically [*SchemaAttributes*](/types/5/0505-Schema-Attributes)) to show that the data stored in the data field represented by the element conforms to the type.  An [open discovery service](/concepts/open-discovery-service) can propose a list of data class assignments and these are stored in the [*DataClassAnnotation*](/type/6/0625-Data-Class-Discovery).  Subsequent stewardship - either automated or with human assistance - can confirm the correct assignment using the *DataClassAssignment* relationship.



## DataClassSnippet

The *DataClassSnippet* links a data class to an [ImplementationSnippet](/types/5/0504-Implementation-Snippets) that describes how to implement the type in a specific language.

--8<-- "snippets/abbr.md"

