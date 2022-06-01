<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data class

Data classes provide the specification of a logical data type. This goes beyond the type used to store the data value and includes a specification of the values that are found in this logical type.  For example, a credit card number is typically stored as a string.  However, it has a well-defined pattern of four groups of four digits.  The data class allows the capture of the specification of a credit card number type that can be used by discovery engines to find more information out about the data values within a resource.

Data classes can be specialized to define the logical data type more precisely than the implementing technology can support.  The specialization relationship enables automated curation and stewards to move up and down the levels of specialization.

![Address specialization](/features/data-quality/address-data-class-specialization.svg)

Complex data types can be broken down into fields to allow more detailed understanding of its content.
The data classes can be augmented with valid value sets and validation rules to enable [automated quality processes](/features/data-quality/overview) to be metadata-driven.

![Address composition](/features/data-quality/address-data-class-composition.svg)

Data classes can be linked to glossary terms to show how data fo a specific meaning is implemented.

![Semantic context](/features/data-quality/data-quality-semantic-context.svg)


!!! education "Further information"

    - [Using Data classes in data quality management](/features/data-quality/overview)
    - [Data class discovery annotation](/features/discovery-and-stewardship/overview/#data-class-discovery)
    - [DataClass open metadata type](/types/5/0540-Data-Classes)

--8<-- "snippets/abbr.md"