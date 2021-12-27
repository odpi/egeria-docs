<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Governance Action Service

A governance action service is a specialized [connector](/egeria-docs/concepts/connector)
that performs monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request.

A governance action service is passed a context as it is started. This provides access to the request type and associated parameters (name-value pairs) used to invoke the governance action service, along with a client to access open metadata through the Governance Engine OMAS.

![Structure of the governance context](governance-context.svg)

This context is then specialized for each type of governance action service. Details of the specific context for each service can be found in the links to the various governance action service types.         

There are five types of governance action services:
  
* **[Watchdog Governance Service](/egeria-docs/guides/developer/governance-action-services/watchdog-governance-service)** listens for changes to metadata and initiates
  [governance actions](/egeria-docs/concepts/governance-action), [governance action processes](/egeria-docs/concepts/governance-action-process)
  or an [incident report](/egeria-docs/concepts/incident-report).
  
* **[Verification Governance Service](/egeria-docs/guides/developer/governance-action-services/verification-governance-service)** validates that the metadata elements, relationships and
  classification are set up as they should be.  For example, it may check that a new asset has an owner, is set up
  with zones and includes a connection and a schema there possible.  It produces [guards](/egeria-docs/concepts/guard)
  that define what needs to be done.
  
* **[Triage Governance Service](/egeria-docs/guides/developer/governance-action-services/triage-governance-service)** runs triage rules to determine how to manage a situation or request.
  Often this involves a human decision maker.   It may initiate an external workflow, wait for manual
  decision or create a **To Do** for a specific person.
  
* **[Remediation Governance Service](/egeria-docs/guides/developer/governance-action-services/remediation-governance-service)** makes updates to metadata elements, relationships between them
  and classifications. Examples of remediation governance action services are duplicate linking and consolidating.

* **[Provisioning Governance Service](/egeria-docs/guides/developer/governance-action-services/provisioning-governance-service)**  invokes a provisioning service whenever a provisioning request is made. 
  Typically the provisioning service is an external service.  It may also create lineage metadata to
  describe the work of the provisioning engine.
  
  
--8<-- "snippets/abbr.md"