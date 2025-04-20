<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0625 Data Class Discovery

Data class discovery captures the analysis on how close the values in a data field matches the specification defined in a [data class](/concepts/data-class).

![UML](0625-Data-Class-Discovery.svg)

## DataClassAnnotation entity

This annotation records a possible data class match with the data analyzed by the survey action service.

## DataClassMatch relationship

This relationship identifies the matching data class and the degree to which the data values conformed to the specification in the data class.

* *threshold* records the percentage of matching values.
* *method* records the analysis method used.  For example, was every value matched or a sampling technique used?  This may affect the resulting confidence of the steward when they confirm the match using the [DataClassAssignment](/types/5/0540-Data-Classes) relationship.

--8<-- "snippets/abbr.md"