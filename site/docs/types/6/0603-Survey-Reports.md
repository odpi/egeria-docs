<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0603 Survey Reports

A *SurveyReport* entity is created each time a [survey action service](/concepts/survey-action-service) runs.  It acts as a parent entity to the [annotations](0610-Annotations.md) created by the execution of the survey action service.  These annotations contain the findings of the survey.

![UML](0603-Survey-Reports.svg)

## SurveyReport entity

The *SurveyReport* entity is a [*Report*](/types/2/0239-Reports) entity that describes both the context behind the request to run the survey action service, and the execution status of the survey action service.

* *analysisParameters* describe the request parameters passed to the survey action service when it started.
* *analysisStep* - this is filled out by the survey action service as it runs to show where it is in its analysis.  This is useful for long-running services.

The [ReportOriginator](/types/2/0239-Reports) relationship links the survey report to the [EngineAction](/types/4/0463-Engine-Actions) that is controlling the execution of the survey.  The [ReportSubject](/types/2/0239-Reports) relationship links the survey report to the asset that described the digital resource being surveyed.

--8<-- "snippets/abbr.md"