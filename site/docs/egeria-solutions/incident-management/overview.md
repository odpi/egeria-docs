<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Incident Management

However good the defences, things will go wrong.  An account is used from an unexpected place, a server is found running software that nobody recognises, a supplier reports a breach, or a security tool raises an alert that nobody is sure how to interpret.  How well an organization responds depends on whether the incident is noticed quickly, whether the right people are brought together, whether they can find out what is affected, and whether the lessons are captured so that it is less likely to happen again.

Egeria's *Incident Management* solution supports this lifecycle.  It does not replace a dedicated incident management or ticketing system.  Instead, it connects the incident to the open metadata that describes the affected resources, their owners and the governance definitions that apply, and keeps a lasting record that can be analysed after the incident is closed.

## Raising an incident

An incident is recorded in open metadata as an [incident report](/concepts/incident-report).  It can be raised by a person, by an external tool, or automatically:

* [governance services](/concepts/governance-service) running in an [engine host](/concepts/engine-host) can create an incident report when they detect something that is out of line with the organization's policies - for example, an unexpected member of a security group.
* [integration connectors](/concepts/integration-connector) can create incident reports from events in the technology they monitor.
* [notification types](/concepts/notification-type) monitored by the [Notification Manager](/services/omvs/notification-manager/overview) can create an incident report when a significant event occurs on a monitored resource.

When it is created, the incident report is linked to its originator and to the resources it is known to affect, using the [*ImpactedResource*](/types/4/0470-Incident-Reporting) relationship, which records the severity of the impact on each one.

## Classifying incidents

Incidents are much easier to analyse if they are classified consistently.  The categories the organization uses - for example, the types of vulnerability that the security team tracks, such as remote code execution, privilege escalation or exposed credentials - are defined as [*ReferenceDataValue*](/types/5/0545-Reference-Data) elements, grouped into a [*ReferenceDataSet*](/types/5/0545-Reference-Data), and maintained through the [Reference Data API](/services/omvs/reference-data/overview).  The appropriate value is attached to each incident report with the [*ReferenceValueAssignment*](/types/5/0545-Reference-Data) relationship.

Since the incident report is also linked to the resources it affects, this makes it easy to see which types of vulnerability are being found, and which resources they are found in.

## Working the incident

The incident report records the progress of the incident through its status - *Raised*, *Reviewed*, *Validated*, *Resolved*, *Invalid*, *Ignored* or *Other* - so that it is clear which incidents still need attention.

Because the affected resources are linked into the open metadata graph, the people working on the incident can quickly answer questions such as:

* Who owns the affected system, and who should be told?
* What data does it hold, and how sensitive is that data?
* Which other systems and information supply chains depend on it?
* What software is it running, and when was it last patched?
* Which policies and controls apply to it, and which risks were recorded against it?

As the investigation proceeds, the people involved add notes to the incident report's note log describing their diagnosis, the steps taken and the decisions made.  Further affected resources, related incident reports and the [context events](/types/4/0475-Context-Events) that describe the root cause can be linked as they are discovered.

Most organizations already have an incident management or ticketing system that the security team works in.  An integration connector can publish each incident report to that system and keep the two synchronized, so that the people resolving the incident can work in their usual tool while the open metadata record stays complete.

???+ example "An example of incident management"
    The [Incident Reporting](/features/incident-reporting/overview) feature page describes an example in which a governance service detects an unexpected member of an LDAP security group.  It is not clear whether Egeria's list of user identities is out of date, or whether this is part of a cyber-attack.  The governance service creates an incident report, which an integration connector passes to the security team's incident management system.  Updates made there are reflected back into the incident report.

## Learning from incidents

Once an incident is closed, the incident report remains as a record of what happened, what was affected and what was done.  Over time, this record becomes a valuable source of insight:

* recurring incidents on the same resources, or of the same type, point to weaknesses that need a lasting fix.
* incidents that were not anticipated by the [threat model](/egeria-solutions/threat-modelling/overview) indicate new threats or risks that should be added to the risk register.
* the time taken to move incidents from *Raised* to *Resolved* is a measure of how effective the response process is.
* the controls that failed to prevent an incident are candidates for review in the [security strategy](/egeria-solutions/defining-security-strategy/overview).

!!! summary "Usage"
    Incident management closes the loop in the security program.  The strategy defines the controls, threat modelling identifies the risks, and incidents show where reality differs from the plan.  Feeding what is learned back into the risks and controls is what makes the program improve over time rather than simply respond.

## Example

Coco Pharmaceuticals' [data security strategy](/practices/coco-pharmaceuticals/scenarios/building-a-data-security-strategy/overview) includes the obligation that *Security Incidents Must Be Logged, Reported, and Reviewed*, measured by the *Security Incident Mean Time to Containment* metric.  The company's earlier experience of [investigating suspicious activity](/practices/coco-pharmaceuticals/scenarios/investigating-suspicious-activity/overview) around its supplier database showed how much harder an investigation is when the information needed is scattered across spreadsheets and personal knowledge.

!!! education "Further information"
    * [Incident Reporting](/features/incident-reporting/overview) describes how incident reports are created and managed.
    * [0470 Incident Reporting](/types/4/0470-Incident-Reporting) describes the open metadata types used.

--8<-- "snippets/abbr.md"
