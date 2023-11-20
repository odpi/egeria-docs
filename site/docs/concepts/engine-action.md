---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Engine Action

An *engine action* describes a specific invocation of a [governance service](/concepts/governance-service) that needs to be performed on one or more metadata elements, or their counterparts in the digital landscape.

An engine action is represented by an [*EngineAction*](/types/4/0463-Engine-Actions) entity in the open metadata ecosystem.  It contains details such as:

* The [governance request type](/concepts/governance-request-type) that identifies which governance service to call.
* The request parameters that provide parameters to the governance service.
* The [governance engine](/concepts/governance-engine) that will run the [governance service](/concepts/governance-service).

It is linked to:

* The source (cause) of the engine action, such as an [incident report](/concepts/incident-report).
* Any additional target elements that need to be acted upon.

This *EngineAction* metadata entity is used to coordinate the desired activity in the governance engine, record its current state and act as a record of the activity for future audits.

Engine actions can be created through the [Open Governance Service API](/services/gaf-metadata-management). Some governance services (for example, the  [Watchdog Governance Action Service](/guides/developer/governance-action-services/watchdog-governance-service)) can initiate other engine actions directly.  

Governance services produce output strings called [*guards*](/concepts/guard) that indicate specific conditions or outcomes.  These guards can be used to trigger new engine actions.  The choreography of which engine action to run next based on the outcome of an engine action is defined in a [Governance Action Process](/concepts/governance-action-process). Triggered engine actions are linked to their predecessor, so it is possible to trace through which engine actions ran, and why.

If the start date of the engine action is in the future, the [Engine Host Services](/services/engine-host-services) running in the same [Engine Host](/concepts/engine-host) OMAG Server as the nominated governance engine will schedule the governance service to run soon after the requested start date.  If the start date is left blank, the requested governance service is run as soon as possible.

!!! tip "*Governance Action* was renamed to *Engine Action* in release 4.4"
    If you have been using Egeria for a while, you may be familiar with the term *Governance Action* as the mechanism used to control the execution of automated actions in the Engine Hosts.  In [release 4.4](/release-notes/4-4), *Governance Action* was renamed to *Engine Action* to create a greater name differentiation between the concepts that are used to define the governance behaviour and those used to control the execution of this behaviour.

--8<-- "snippets/abbr.md"
