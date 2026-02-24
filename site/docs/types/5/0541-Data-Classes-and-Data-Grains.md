
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0541 Data Classes and Data Grains

[Data classes](/concepts/data-class) describe logical data types that can be used to classify data values in a consistent and standardized way.  They are particularly important in [data quality assessments](/features/data-quality/overview) and [metadata discovery](/features/discovery-and-stewardship/overview).

[Data Grains](/concepts/data-grain) define the granularity of data.
They were invented by [the Kimball Group](https://www.kimballgroup.com/2008/11/fact-tables/) to describe the granularity of data in a data warehouse fact table.  The concept fits well into a metadata landscape too.  For example, you may have multiple data sources that capture sales data for your organization.  One data source may contain daily figures, another contains  weekly figures, and another contains monthly figures.  They are all the same type of data if you consider there [subject area](/concepts/subject-area).  They may even have the same [schema](/concepts/schema) so they will be technically easy to combine.  However, their different granularity means they can not be combined without transformation, and only at the most course-grained level, if distortion is to be avoided.
Data Grains are also useful when defining the data requirements for a project.  They can be associated with a [data field](/concepts/data-field) definition or associated with a [data lens](/concepts/data-lens).

![UML](0541-Data-Classes-and-Data-Grains.svg)

## DataClass entity

The *DataClass* entity provides the specification of a [logical data type](/concepts/data-class). This goes beyond the [*SchemaType*](/types/5/0501-Schema-Elements) used to store the data value and includes a specification of the values that are found in this logical type.  For example, a credit card number is typically stored as a string.  The fact that it is a string is described in the schema type.  However, it also has a well-defined pattern of four groups of four digits.  The data class allows the capture of the specification of a credit card number type that can be used by discovery engines to narrow down the expected data values within a [digital resource's](/concepts/digital-resource) data fields.

The data class is describing a set of data values found in a data field of a digital resource.  For example, the data values stored in a particular column of a database table.  When an automated process uses the data class, it assesses each of the data values it finds against the definition of the data class and determines the percentage of values that match the specification.  The *matchThreshold* determines what percentage of values must match to consider the data to be of the type described in the data class.  This discovered percentage can also be used as a confidence level or quality score.

The *DataClass* entity inherits from [DataValueSpecification](/types/5/0540-Data-Value-Specification) and adds the following attributes:

* *allowsDuplicateValues* - Indicates whether the values in the data resource may repeat, or whether this is a list of unique identifiers/values.
* *isNullable* - Are null values allowed?
* *defaultValue* - Value that is used when an instance of the data field is created, or if it is null.
* *averageValue* - Expected average value of the data values.  This can help assess whether the data values are in the normal range.
* *valueList* - Defines a list of valid values for the data.  If the list of values are long, need special curation or are used more broadly, they can be described using a *ValidValuesSet* and linked to the data class using the *ValidValuesAssignment* relationship.  See [model 0545 - Reference Data](/types/5/0545-Reference-Data).
* *valueRangeFrom*  and *valueRangeTo* - Allow the definition of a range of valid values for the data field.
* *sampleValues* - List of sample values for the data field.  This helps people select an appropriate data class.
* *dataPatterns* - Regular expressions that characterize the values in the data field.

## DataClassComposition relationship

Data classes can be organized into a structural hierarchy using the *DataClassComposition* relationship.  For example, an address data class could be composed of a number of data classes that each describe a part of the address.  The properties in this relationship show how the fields are arranged.

## DataGrain entity

The *DataGrain* entity describes a description of a specific granularity.  It also inherits from [DataValueSpecification](/types/5/0540-Data-Value-Specification) and adds the following attributes:

* *granularityBasis* - Describes the dimension that controls the granularity.
* *grainStatement* - Defines the granularity of the data in terms of a single row/object.
* *interval* - The time interval between objects of this type.

--8<-- "snippets/abbr.md"