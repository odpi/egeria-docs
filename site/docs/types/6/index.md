---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Area 6 Models - Discovery Surveys and Analysis

Area 6 provides structures for recording the results of automated discovery surveys of resources as annotations to associated assets in the metadata repository.

Discovery surveys require different types of analysis. This analysis may run just once, say when the asset is created, on demand or based on an event or schedule.

A particular type of analysis is implemented in a [survey action service](/concepts/survey-action-service). Within the survey action service are one to many analysis steps. Each step performs some sort of analysis that may result in an [annotation](/concepts/survey-report/#annotations) for one or more assets.

The annotations from a particular run of a survey action service are grouped together into a [survey report](/concepts/survey-report).  The annotations may be reviewed and approved by a steward. The steward may convert the annotation to a harden metadata type, or they may flag the annotation as invalid. When the survey action service is rerun, the new annotations can be matched to the annotations from the previous run. The steward's actions will impact how the new annotations are processed.

* **[0603 Survey Report](0603-Survey-Reports.md)**
* **[0610 Annotation](0610-Annotations.md)**
* **[0611 Annotation Reviews](0612-Annotation-Reviews.md)**
* **[0615 Schema Extraction](0615-Schema-Extraction.md)**

* **[0616 Data Field Modelling](0616-Data-Field-Discovery.md)**

* **[0620 Resource Profiling](0620-Resource-Profiling.md)**
* **[0625 Data Class Discovery](0625-Data-Class-Discovery.md)**
* **[0630 Semantic Discovery](0630-Semantic-Discovery.md)**
* **[0635 Classification Discovery](0635-Classification-Discovery.md)**
* **[0640 Quality Scores](0640-Quality-Scores.md)**
* **[0650 Relationship Discovery](0650-Relationship-Discovery.md)**
* **[0660 Measurements](0660-Resource-Measures.md)**
* **[0690 Request for Action](0690-Request-for-Action.md)**

![UML Packages](area-6-discovery-overview.svg)

Egeria's [Survey Action Framework (SAF)](/frameworks/saf/overview) supports the development and execution of [survey action services](/concepts/survey-action-services).  These services run in the [Survey Action OMES](/services/omes/survey-action/overview) hosted in an [Engine Host](/concepts/engine-host).  Survey action services use connectors from the [Open Connector Framework (OCF)](/frameworks/ocf/overview) to connect to the data assets and access the known metadata about them.

## A moment of transition

You may notice that some of the types in the UML models are coloured grey.  These types are exclusively for the [open discovery services](/concepts/open-discovery-service) which are now deprecated and replaced by the [survey action services](/concepts/survey-action-framework).  The type descriptions remain in the models to help people migrate their open discovery services to the survey action framework.

The main differences are that the [*OpenDiscoveryAnalysisReport*](0605-Open-Discovery-Analysis-Reports.md) becomes the [*SurveyReport*](0603-Survey-Reports.svg) and the schema extraction process now uses [*SchemaElement*](/type/5/0501-Schema-Elements) entities rather than [*DataField*](0616-Data-Field-Discovery.md) entities.

* **[0601 Open Discovery Engines and Services](0601-Open-Discovery-Engine.md)**
* **[0605 Discovery Analysis Report](0605-Open-Discovery-Analysis-Reports.md)**
* **[0616 Data Field Discovery](0616-Data-Field-Discovery.md)**
* **[0617 Data Field Analysis](0617-Data-Field-Analysis.md)**

--8<-- "snippets/abbr.md"
