---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


## Governance Action

A governance action describes a specific governance activity that needs to be performed on one or more metadata elements, or their counterparts in the digital landscape.

A governance action is [represented as a metadata entity](/egeria-docs/types/4/0463-Governance-Actions) in the open metadata repositories and linked to:

* The source (cause) of the governance action.
* The target elements that need to be acted upon.
* The [governance engine](/egeria-docs/concepts/governance-engine) that will run the [governance service](/egeria-docs/concepts/governance-service) that implements the desired behavior.
  
The governance action metadata entity is used to coordinate the desired activity in the governance engine, record its current state and act as a record of the activity for future audits.

Governance actions can be created through the [Governance Engine OMAS API](/egeria-docs/services/omas/governance-engine/overview). Some governance services (for example, the  [Watchdog Governance Action Service](/egeria-docs/guides/developer/governance-action-services/watchdog-governance-service)) can initiate other governance actions.  

Governance services produce output strings called **guards** that indicate specific conditions or outcomes.  These guards can be used to trigger new governance actions. Triggered governance actions are linked to their predecessor so it possible to trace through the governance actions that ran.

The [governance action process](/egeria-docs/concepts/governance-action-process) defines the flow of governance actions.  It uses [governance action types](/egeria-docs/concepts/governance-action-type) to build up a template of possible governance actions linked via the guards.  When the process runs, its linked governance action types control the triggering of new governance actions.

If the start date of the governance action is in the future, the [Engine Host Services](/egeria-docs/services/engine-host-services) running in the same [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server as the nominated governance engine will schedule the governance service to run soon after the requested start date.  If the start date is left blank, the requested governance service is run as soon as possible.



--8<-- "snippets/abbr.md"
