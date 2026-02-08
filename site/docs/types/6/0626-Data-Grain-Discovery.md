<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0626 Data Grain Discovery

Data grain discovery captures the analysis of the granularity of the values in a data field.  If may involve matching to the granularity specification defined in a [data grain](/concepts/data-grain).

![UML](0626-Data-Grain-Discovery.svg)

## DataGrainAnnotation entity

This annotation records the analysis results into the granularity of the data, typically by comparing values in different rows of the same data field (column).  If data grain specifications are available, they can be listed in *candidateDataGrainGUIDs* or linked to possible data grain elements using the *DataGrainMatch* relationship.

## DataGrainMatch relationship
 
This relationship identifies the matching data grain and the degree to which the data values conformed to the specification in the data grain.
* *threshold* records the percentage of matching values.
* *method* records the analysis method used.  For example, was every value matched or a sampling technique used?  This may affect the resulting confidence of the steward when they confirm the match using the [DataClassAssignment](/types/5/0540-Data-Classes) relationship.

--8<-- "snippets/abbr.md"