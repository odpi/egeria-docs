---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0463 Governance Actions

A **GovernanceAction** describes some processing that is part of the governance
of an organization's asset or the metadata tht describes them.

The creation of a GovernanceAction typically triggers
services in the [governance engines](../../../open-metadata-implementation/admin-services/docs/concepts/engine-host.md).
As the services run, they add information to the GovernanceAction describing the
activities run and the actions taken against specific resources (see **TargetForAction**).
Once the action is complete,
the GovernanceAction acts as an audit record for the actions taken.

The **GovernanceActionRequestSource** links the first GovernanceAction
in a chain to the cause/originator of the action.  This could be, for example,
a [GovernanceProcess](/egeria-docs/types/4/0430-Technical-Controls) or a
[RequestForActionAnnotation](/egeria-docs/types/6/0690-Request-for-Action).

The GovernanceAction is also linked to
any follow on activities through the **NextGovernanceAction**
relationship so it is possible to trace through a chain of actions.
The **guard** describes the output guard from the previous action(s)
that will trigger the next action(s).  
If the guard is mandatory (ie **mandatoryGuard** = true),
a next action can not run until a previous action has produced this guard.
If **ignoreMultipleTriggers** = true, the next action is only triggered once.
If it is false then the next action is triggered each time the guard is produced
by the previous action(s).

![UML](0463-Governance-Actions.svg)

??? deprecated "Deprecated types"
    - **GovernanceActionExecutor** - Use *executorEngineGUID*, *executorEngineName*, *requestType* and *requestParameters* properties in *GovernanceAction* entity to identify the governance engine that will run the service that will execute the action.  The specific service is identified by the requestType property.  The governance engine is typically either a [DiscoveryEngine](/egeria-docs/types/6/0601-Open-Discovery-Engine) or a [GovernanceActionEngine](/egeria-docs/types/4/0461-Governance-Engines).
    
--8<-- "snippets/abbr.md"