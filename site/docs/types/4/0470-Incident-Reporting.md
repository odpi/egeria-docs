<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0470 Incident Reporting

The incident report is used to record that an incident (such as data breach, software error, quality failure detected) has occurred.  Many organizations have a dedicated incident management system (such as ServiceNow, GitHub or Jira).  Open metadata supports the management of incident reports, either directly, or as a proxy to an incident in an incident management system.  Where the incident is described in open metadata, it can be linked to the assets that are affected and its resolution can be governed through governance action processes.

An incident report may be related to the [context event(s)](/types/4/0475-Context-Events) that describe the root cause of the incident via the [ContextEventEvidence](/types/4/0475-Context-Events) relationship.

![UML](0470-Incident-Reporting.svg)

## IncidentReport entity

The *IncidentReport* entity is a [*Report*](/types/2/0239-Reports) that describes the incident, when it occurred and its current status.

## IncidentReportStatus enumeration

The *IncidentReportStatus* enumeration provides the valid values for the status describing the progress made to resolving the issue described in the incident report.

* Raised - The incident report has been raised but no processing has occurred.
* Reviewed - The incident report has been reviewed, possibly classified but no action has been taken.
* Validated - The incident report records a valid incident and work is underway to resolve it.
* Resolved - The reported incident has been resolved.
* Invalid - The incident report does not describe a valid incident and has been closed.
* Ignored - The incident report is valid but has been closed with no action.
* Other - Another incident report status.

## ImpactedResource relationship

The *ImpactedResource* relationship allows an *IncidentReport* entity to be linked to [*Referenceable*](/types/0/0010-Base-Model) entities that describe resources that are impacted by the incident.  For example, it may link an incident report to a [*SoftwareServer*](/types/0/0040-Software-Servers) that is unavailable.  The *severityLevelIdentifier* describes the severity of the impact on the *Referenceable* entity.  Its value is taken from the list of severities defined using the [Valid Metadata Values](/guides/planning/valid-metadata/overview) services.


--8<-- "snippets/abbr.md"