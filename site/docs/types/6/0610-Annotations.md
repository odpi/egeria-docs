<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0610 Annotations


An annotation captures specific discovered characteristics of a real-world digital resource.

Annotations are created by the analysis steps in the survey action service.
The attributes of the annotation capture the details of the analysis.
There are subclasses of Annotation to capture additional details.
Each annotation is linked to the report it was generated from.
It also links to other elements that the annotation relates to.
Strings are used in many of the attributes to keep the model open
for capturing analysis from third-party tools.

![UML](0610-Annotations.svg)

## Annotation entity

The *Annotation* entity inherits from [*OpenMetadataRoot*](/types/0/0010-Base_Model) and adds the following attributes:

* *annotationType* - descriptive string that acts as an identifier for the specific annotation type.  This is a simple means to sub-type any one of the annotation subclasses.
* *summary* - a human-readable string to describe the annotation.
* *confidence* - an indicator of the certainty that the annotation is correct.
* *expression* - this attribute is used to provide more detail on how the asset is related to the annotation.
* *explanation* - another description field to assist human analysts reviewing the analysis results.
* *analysisStep* - identifier of the step in the survey action service that detected the annotation.
* *jsonProperties* - the properties that were used to initiate the survey action service.
* *additionalProperties* - additional properties published by the survey action service.

The types that follow provide more specialized annotations.

* **[0615 Schema Extraction](0615-Schema-Extraction.md)**
* **[0620 Resource Profiling](0620-Resource-Profiling.md)**
* **[0625 Data Class Discovery](0625-Data-Class-Discovery.md)**
* **[0630 Semantic Discovery](0630-Semantic-Discovery.md)**
* **[0635 Classification Discovery](0635-Classification-Discovery.md)**
* **[0640 Quality Scores](0640-Quality-Scores.md)**
* **[0650 Relationship Discovery](0650-Relationship-Discovery.md)**
* **[0660 Measurements](0660-Resource-Measures.md)**
* **[0690 Request for Action](0690-Request-for-Action.md)**

## DataFieldAnnotation entity

The *DataFieldAnnotation* type is used as a marker to indicate that the annotations that inherit from it will typically refer to a single schema attribute (data field) rather than the whole resource.

## ReportedAnnotation relationship

The *ReportedAnnotation* relationship links an annotation to the [*SurveyReport*](/types/6/0603-Survey-Reports) entity.  It is used with [survey action services](/concepts/survey-action-service).

## AssociatedAnnotation relationship

The *AssociatedAnnotation* relationship links an annotation to an element that it describes.

## AnnotationExtension relationship

The *AnnotationExtension* relationship allows an annotation from a later run of the survey action service to add information to an annotation from a previous run.

## DiscoveredAnnotation relationship

The *DiscoveredAnnotation* relationship links an annotation to the [*OpenDiscoveryAnalysisReport*](0605-Open-Discovery-Analysis-Reports.md) entity.  It is only used with [open discovery services](/concepts/open-discovery-service).

--8<-- "snippets/abbr.md"