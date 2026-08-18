<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Report

A *report* is a collection of data items assembled to describe a particular situation.  It is an [asset](/concepts/asset) - specifically a type of data set - so it can be catalogued, governed, secured and included in [lineage](/features/lineage-management/overview) in exactly the same way as any other data.

A report is an *instance*: it is the output produced on a particular occasion, covering a particular period.  The definition it was produced from is a separate element called a [report type](/concepts/report-type).

## What a report records

Alongside the normal asset properties, a report captures:

* *purpose* - why the report exists.
* *author* and *lastModifier* - the userIds of the person or process that produced the report and last changed it.
* *startTime* and *completionTime* - the start and end of the time period that the report's content covers.  This is what makes a report different from most other data sets: its content is only meaningful in the context of a period of time.
* *createdTime* and *lastModificationTime* - when the report itself was created and last modified.
* *completionMessage* - any message issued by the process that created the report.

Three relationships place the report in its context:

* *ReportOriginator* links the report to the element - typically a [process](/concepts/process) - that created it.
* *ReportSubject* links the report to the elements it is about.
* *ReportDependency* links a report to a related report.  This relationship carries a sense of time, so a sequence of reports covering successive periods can be followed.

## Specialized reports

Egeria defines a number of specialized report types that are produced by its own runtime:

* A [survey report](/concepts/survey-report) records the results of a survey of one or more digital resources.
* An [incident report](/concepts/incident-report) describes a particular incident or situation that is affecting the operation of the organization.
* A *connector activity report* describes the activity of a connector during a certain time period.  The [integration report](/concepts/integration-report) produced by an [integration connector](/concepts/integration-connector) is an example.

???+ info "Additional information"
    * The *Report* type and its relationships are described in [Model 0239 Reports](/types/2/0239-Reports).
    * [Model 0457 Connector Activity Reports](/types/4/0457-Connector-Activity-Reports), [Model 0470 Incident Reporting](/types/4/0470-Incident-Reporting) and [Model 0603 Survey Reports](/types/6/0603-Survey-Reports) describe the specialized reports.

--8<-- "snippets/abbr.md"
