---
hide:
- toc
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Incident Report

An *incident report* describes a situation that needs special attention (such as a governance action detecting that a value is out of line with expectations defined in a policy or rule). It provides a focus point to coordinate efforts to resolve the situation.

As the incident is handled, details of the cause, affected resources and actions taken are attached to the incident report to create a complete record of the incident for future analysis.

![incident](/features/incident-reporting/incident-report.svg)

Incident reports are typically created by [governance services](/concepts/governance-service), [integration connectors](/concepts/integration-connectors) or an external incident management tools such as GitHub or Jira.


!!! education "Further information"
    * For a description of how incidents are created and managed see [Incident Reporting](/features/incident-reporting/overview)
    * The [0470](/types/4/0470-Incident-Reporting) open metadata type model shows the structure of the incident report. It is a [Referenceable](/types/0/0010-Base-Model/#referenceable), so it can support comments and linked classifications and tags.


--8<-- "snippets/abbr.md"
