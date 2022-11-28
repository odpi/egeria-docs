<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0463 Governance Actions

A [Governance action](/concepts/governance-action) describes some processing that is part of the governance of an organization's asset or the metadata tht describes them.

![UML](0463-Governance-Actions.svg)

## GovernanceAction

A *GovernanceAction* entity is used to control the execution of a single governance action instance. 

The creation of a GovernanceAction entity typically triggers the execution of a [governance service](/concepts/governance-service) in a [governance engine](/concepts/governance-engine).
As the governance service runs, the governance engine adds information to the GovernanceAction describing the
status of the governance service and the actions taken against specific [resources](/concepts/resources) (see [TargetForAction](#targetforaction)).
Once the action is complete,
the GovernanceAction acts as an audit record for the actions taken.

## TargetForAction

The *TargetForAction* relationship links the governance action to the [action targets](/concepts/action-target) for the governance service that will run.  The governance service can update the status of its processing of the action targets in the properties of each TargetForAction relationship.

## GovernanceActionRequestSource

The *GovernanceActionRequestSource* relationship links the first GovernanceAction in a process to the cause/originator of the action.  This could be, for example, a [governance action process](/concepts/governance-action-process), another governance action or a [RequestForActionAnnotation](/types/6/0690-Request-for-Action).

## GovernanceActionStatus

The *GovernanceActionStatus* indicates the execution status of the governance action.

| Enumeration | Value | Name | Description                                                                                            |
| --- | --- | --- |--------------------------------------------------------------------------------------------------------|
| REQUESTED    |  0  | Requested | The governance action has been created and is pending.                                                 |
| APPROVED     |  1  | Approved | The governance action is approved to run.                                                              |
| WAITING      |  2  | Waiting | The governance action is waiting for its start time or the right conditions to run.                    |
| ACTIVATING   |  3  | Activating | The governance action service for the governance action is being initialized in the governance engine. |
| IN_PROGRESS  |  4  | In Progress| The governance engine is running the associated governance action service for the governance action.   |
| ACTIONED     |  10 | Actioned | The governance action service for the governance action has successfully completed processing.         |
| INVALID      |  11 | Invalid | The governance action has not been run because it is not appropriate (for example, a false positive).  |
| IGNORED      |  12 | Ignored | The governance action has not been run because a different governance action was chosen.               |
| FAILED       |  13 | Failed | The governance action service for the governance action failed to execute.                             |
| OTHER        |  99 | Other | Undefined or unknown governance action status.                                                         |

## NextGovernanceAction

The GovernanceAction is also linked to any follow-on activities through the *NextGovernanceAction* relationship, so it is possible to trace through a chain of actions. The *guard* describes the [output guard](/concepts/guard) produced by the previous action(s) that will trigger (or triggered) the next action(s).  

If the guard is mandatory (ie *mandatoryGuard* = true),
a next action can not run until a previous action has produced this guard. If *ignoreMultipleTriggers* = true, the next action is only triggered once. If it is false then the next action is triggered each time the guard is produced by the previous action(s).


???+ deprecated "Deprecated types"
    The following relationship types were deprecated in favour of attributes in the *GovernanceAction* to reduce the processing load in maintaining these relationships.

    - *GovernanceActionExecutor* - Use *executorEngineGUID*, *executorEngineName*, *requestType* and *requestParameters* properties in *GovernanceAction* entity to identify the governance engine that will run the service that will execute the action.  The specific service is identified by the requestType property.  The governance engine is typically either a [DiscoveryEngine](/types/6/0601-Open-Discovery-Engine) or a [GovernanceActionEngine](/types/4/0461-Governance-Engines).
    - *GovernanceActionTypeUse* - Use *governanceActionTypeGUID*, *governanceActionTypeName* and *processName* properties in *GovernanceAction* entity to identify the governance action type (and any associated governance action process) that acted as a template when this governance action was initiated.
    
--8<-- "snippets/abbr.md"