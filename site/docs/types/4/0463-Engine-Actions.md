<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0463 Engine Actions

An [Engine action](/concepts/engine-action) describes some processing that is part of the governance of an organization's asset or the metadata that describes them.

![UML](0463-Engine-Actions.svg)

## EngineAction entity

A *EngineAction* entity is an [*Action*](/types/1/0137-Actions) used to control the execution of a single call to a [governance service](/concepts/governance-service). 

The creation of an *EngineAction* entity typically triggers the execution of a [governance service](/concepts/governance-service) in a [governance engine](/concepts/governance-engine). As the governance service runs, the governance engine adds information to the EngineAction describing the status of the governance service and the actions taken against specific [resources](/concepts/resources) (see [TargetForAction](#targetforaction)). Once the action is complete, the *EngineAction* entity acts as an audit record for the actions taken.

## TargetForAction relationship

The *TargetForAction* relationship links the engine action to the [action targets](/concepts/action-target) for the governance service that will run.  The governance service can update the status of its processing of the action targets in the properties of each TargetForAction relationship.

## EngineActionRequestSource relationship

The *EngineActionRequestSource* relationship links the first *EngineAction* entity in a process to the cause/originator of the action.  This could be, for example, a [governance action process](/concepts/governance-action-process), another engine action or a [RequestForActionAnnotation](/types/6/0690-Request-for-Action) linked to a [discovery analysis report](/concepts/discovery-analysis-report).

## EngineActionStatus enumeration

The *EngineActionStatus* indicates the execution status of the governance action.

| Enumeration | Value | Name | Description                                                                                         |
| --- | --- | --- |-----------------------------------------------------------------------------------------------------|
| REQUESTED    |  0  | Requested | The governance action has been created and is pending.                                              |
| APPROVED     |  1  | Approved | The governance action is approved to run.                                                           |
| WAITING      |  2  | Waiting | The governance action is waiting for its start time or the right conditions to run.                 |
| ACTIVATING   |  3  | Activating | The governance service for the governance action is being initialized in the governance engine. |
| IN_PROGRESS  |  4  | In Progress| The governance engine is running the associated governance service for the governance action.  |
| ACTIONED     |  10 | Actioned | The governance service for the governance action has successfully completed processing.        |
| INVALID      |  11 | Invalid | The governance action has not been run because it is not appropriate (for example, a false positive). |
| IGNORED      |  12 | Ignored | The governance action has not been run because a different governance action was chosen.            |
| FAILED       |  13 | Failed | The governance action service for the governance action failed to execute.                          |
| OTHER        |  99 | Other | Undefined or unknown governance action status.                                                      |

## NextEngineAction relationship

The *EngineAction* entity is also linked to any follow-on activities through the *NextEngineAction* relationship, so it is possible to trace through a chain of actions. The *guard* describes the [output guard](/concepts/guard) produced by the previous action(s) that will trigger (or triggered) the next action(s).  

If the guard is mandatory (ie *mandatoryGuard* = true), a next governance action can not run until a previous governance action has produced this guard.


???+ deprecated "Deprecated types"
    The following relationship types were deprecated in favour of attributes in the *EngineAction* to reduce the processing load in maintaining these relationships.

    - *EngineActionExecutor* - Use *executorEngineGUID*, *executorEngineName*, *requestType* and *requestParameters* properties in *EngineAction* entity to identify the governance engine that will run the service that will execute the action.  The specific service is identified by the requestType property.  The governance engine is typically either a [DiscoveryEngine](/types/6/0601-Open-Discovery-Engine) or a [EngineActionEngine](/types/4/0461-Governance-Engines).
    - *GovernanceActionProcessStepUse* - Use *processStepGUID*, *processStepName* and *processName* properties in *EngineAction* entity to identify the engine action type (and any associated governance action process) that acted as a template when this engine action was initiated.
    - *GovernanceActionProcessStepGUID* - Use *processStepGUID* attribute in the *EngineAction* entity to identify the governance action process step (and any associated governance action process) that acted as a template when this engine action was initiated.
    - *GovernanceActionProcessStepName* - Use *processStepName* attribute in the *EngineAction* entity to identify the governance action process step (and any associated governance action process) that acted as a template when this engine action was initiated.

    The *ignoreMultipleTriggers* attribute in the *NextEngineAction* has been deprecated.
    
--8<-- "snippets/abbr.md"