<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

A governance action service is a specialized [connector](/concepts/connector) that performs monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request.  It runs in the [Governance Action Open Metadata Engine Service (OMES)](/services/omes/governance-action) hosted by the [Engine Host OMAG Server](/concepts/engine-host).

![Governance Action Service](/connectors/governance-action/governance-action-service.svg)

It is possible to implement complex governance actions in a single governance action service.  Alternatively there are five specialized types of governance action services that help you to break down your governance function into reusable components that can be choreographed by [governance action processes](/concepts/governance-action-process)to maximise the flexibility of your governance automation:
  
* *[Watchdog Governance Action Service](/guides/developer/governance-action-services/overview/#watchdog-governance-action-service)* listens for changes to metadata and initiates [governance actions](/concepts/governance-action), [governance action processes](/concepts/governance-action-process) or an [incident report](/concepts/incident-report).
  
* *[Verification Governance Action Service](/guides/developer/governance-action-services/overview/#verification-governance-action-service)* validates that the metadata elements, relationships and classification are set up as they should be.  For example, it may check that a new asset has an owner, is set up with [governance zones](/concepts/governance-zone) and includes a connection and a schema there possible.  It produces [guards](/concepts/guard) that define what needs to be done.
  
* *[Triage Governance Action Service](/guides/developer/governance-action-services/overview/#triage-governance-action-service)* runs triage rules to determine how to manage a situation or request. Often this involves a human decision maker.   It may initiate an external workflow, wait for manual decision or create a [ToDo](/concepts/to-do) for a specific person.
  
* *[Remediation Governance Action Service](/guides/developer/governance-action-services/overview/#remediation-governance-action-service)* makes updates to metadata elements, relationships between them and classifications. Examples of remediation governance action services are duplicate linking and consolidating.

* *[Provisioning Governance Action Service](/guides/developer/governance-action-services/overview/#provisioning-governance-action-service)*  invokes a provisioning service whenever a provisioning request is made.  Typically, the provisioning service is an external service.  It may also create lineage metadata to describe the work of the provisioning engine.

The definition of the connector interfaces for governance action services is defined in the [governance-action-framework :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/frameworks/governance-action-framework) module.

  
--8<-- "snippets/abbr.md"