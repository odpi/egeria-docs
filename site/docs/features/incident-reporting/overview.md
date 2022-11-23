<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Incident Reporting

When errors, unexpected situations or special requests occur, it is not always obvious how they should be handled. An *incident report* is a metadata entity that describes a situation that needs special attention. It provides a focus point to coordinate efforts to resolve the situation.

The incident report is created when the situation is detected.  The originator and known affected resources are linked to it.

As the incident is handled, details of the cause, additional affected resources, related incident reports and actions taken are attached to the incident report to create a complete record of the incident for future analysis.

There is a status in the incident report that records the progress to resolving the situation:

* Raised
* Reviewed
* Validated
* Resolved
* Invalid
* Ignored
* Other

The people working on the incident can add notes to the incident report's note log to communicate the diagnosis, steps taken and decisions made.

![Incident Report](/features/incident-reporting/incident-report.svg)

!!! info "Overview of the Incident Management process"

    1. When an incident occurs, an incident report is created.  There is support to create an incident on most [Open Metadata Access Services (OMASs)](/services/omas), [Open Metadata Integration Services (OMISs)](/services/omis) supporting [integration connectors](/concepts/integration-connector) and the [Open Metadata Engine Services (OMESs)](/services/omes) supporting [governance services](/concept/governance-service). 
    2. the request is routed to [Metadata Access Store](metadata-access-store) and an [IncidentReport](/types/4/0470-Incident-Reporting) entity linked to metadata describing the originator and any impacted resources is saved to its open metadata repository.
    3. The content of incident report is managed via the [Stewardship Action OMAS](/services/omas/stewardship-action/overview)'s interface.  This could be through direct calls to the API or via an [integration connector](/concepts/integration-connector) running in the [Stewardship Integrator OMIS](/services/omis/stewardship-integraotr/overview)

    ![Incident Management](/features/incident-reporting/incident-management.svg)


???+ example "An Incident Management Example"
    In this example, there is a [governance service](/concepts/governance-service) called *LDAP Verifier Governance Action Service* that is running in an [Engine Host](/concepts/engine-host).  It is responsible for detecting whether there are any unexpected entries in Coco Pharmaceuticals' LDAP server that support access control.

    It detects an unexpected member in the `founders` security group for a userId called `matt-darker`.  Is this a valid entry and Egeria's list of user identities is out of date, or is this part of a cyber-attack?  The governance action service creates an incident report identifying the security group and the unexpected userId.

    The creation of the incident report in the open metadata ecosystem causes an event to be published by the [Stewardship Action OMAS](/services/omas/stewardship-action/overview).  It is picked up by an [integration connector](/concepts/integration-connector) called `Incident Manager Integration Connector`.  This integration connector publishes the incident report to Coco Phamaceuticals' security incident management system as an `issue`, where it is picked up by the security team to work on.  Any relevant updates made to the `issue` in the security incident management system are detected by `Incident Manager Integration Connector` and reflected back in the incident report in the open metadata ecosystem.

    ![Incident Management Example](/features/incident-reporting/incident-management-example.svg)

--8<-- "snippets/abbr.md"