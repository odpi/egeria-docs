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
* **[0620 Resource Profiling](0620-Resource-Profiling.md)**
* **[0625 Data Class Discovery](0625-Data-Class-Discovery.md)**
* **[0630 Semantic Discovery](0630-Semantic-Discovery.md)**
* **[0635 Classification Discovery](0635-Classification-Discovery.md)**
* **[0640 Quality Scores](0640-Quality-Scores.md)**
* **[0650 Relationship Discovery](0650-Relationship-Discovery.md)**
* **[0660 Measurements](0660-Resource-Measures.md)**
* **[0690 Request for Action](0690-Request-for-Action.md)**

In addition, there are types for the manual design of data schemas as part of a data specification.

* **[0617 Data Field Modelling](0617-Data-Field-Modelling.md)**

![UML Packages](area-6-discovery-overview.svg)

Egeria's [Survey Action Framework (SAF)](/frameworks/saf/overview) supports the development and execution of [survey action services](/concepts/survey-action-services).  These services run in the [Survey Action OMES](/services/omes/survey-action/overview) hosted in an [Engine Host](/concepts/engine-host).  Survey action services use connectors from the [Open Connector Framework (OCF)](/frameworks/ocf/overview) to connect to the data assets and access the known metadata about them.


--8<-- "snippets/abbr.md"
