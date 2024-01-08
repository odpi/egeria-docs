<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0603 Survey Reports

A *SurveyReport* entity is created each time a [survey action service](/concepts/survey-action-service) runs.

It acts as a parent entity to the [annotations](0610-Annotations.md) created by the execution of the survey action service.  These annotations contain the findings of the survey.

![UML](0603-Survey-Reports.svg)

## SurveyReport entity

The *SurveyReport* entity is a [*Referenceable*](/types/0/0010-Base-Model) entity that describes both the context behind the request to run the survey action service, and the execution status of the survey action service.

* *displayName* is a short identifier that helps a consumer describe or choose a report.
* *description* gives more information about the analysis performed.
* *purpose* provides additional reasons, or expectations of the initiator of the survey request.
* *analysisParameters* describe the request parameters passed to the survey action service when it started.

As the survey action services runs, the *SurveyReport* entity is updated as follows:

* *startDate* - this date/time is filled out when the survey action service starts.  If it is null, it means the survey action service is waiting to start.
* *analysisStep* - this is filled out by the survey action service as it runs to show where it is in its analysis.  This is useful for long-running services.
* *completionDate* - this date/time is filled out when the survey action service disconnects (completes).  If it is null, it means the survey action service has not completed.
* *completionMessage* is optionally filled in once the survey action service is completed.  It is typically only used if the survey action service encountered an error or was unable to complete all steps.  If the *completionDate* is set, but the *completionMessage* is not set, it is reasonable to assume that the survey action service completed successfully. 

## EngineActionSurveyReport relationship

The *EngineActionSurveyReport* relationship links a *SurveyReport* entity to the [*EngineAction*](/types/4/0463/Engine-Actions) entity used to coordinate the execution of the survey action service.

## AssetSurveyReport relationship

The *AssetSurveyReport* relationship links a *SurveyReport* entity to the [*Asset*](/types/0/0010-Base-Model) entity that represents the real-world resource being analysed.

--8<-- "snippets/abbr.md"