<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0463 Engine Actions

A *EngineAction* entity is an [*Action*](/types/1/0013-Actions) used to control the execution of a single call to a [governance service](/concepts/governance-service).

The creation of an *EngineAction* entity typically triggers the execution of a [governance service](/concepts/governance-service) in a [governance engine](/concepts/governance-engine). As the governance service runs, the governance engine adds information to the EngineAction describing the status of the governance service and the actions taken against specific [resources](/concepts/resources). Once the action is complete, the *EngineAction* entity acts as an audit record for the actions taken.

![UML](0463-Engine-Actions.svg)

## EngineAction entity

The *EngineAction* entity has the following attributes used to gather information about the work that needs to be completed and the context for that work:

* *domainIdentifier* - Identifier of the governance domain that recognizes this action. Zero typically means 'any' domain.
* *requestType* - The request type used to call the governance service.
* *requestParameters* - Request parameters to pass to the governance service when called.
* *requesterUserId* - User identity for the person, process or engine that requested this action.
* *executorEngineGUID* - Unique identifier of the governance engine nominated to run the request.
* *executorEngineName* - Unique name of the governance engine nominated to run the request.
* *processName* - Unique name of the process that initiated this request (if applicable).
* *processStepGUID* - Unique identifier of the governance action process step that initiated this request (if applicable).
* *processStepName* - Unique name of the governance action process step that initiated this request (if applicable).
* *governanceActionTypeGUID* - Unique identifier of the governance action type that initiated this request (if applicable).
* *governanceActionTypeName* - Unique name of the governance action type that initiated this request (if applicable).
* *mandatoryGuards* - The list of guards that must be received before this engine action can progress.
* *receivedGuards* - List of guards received from the previous governance service(s).
* *processingEngineUserId* - User identity of the governance engine running in the engine host server that has claimed responsibility for executing this engine action.
* *completionGuards* - List of guards returned by the governance service.
* *completionMessage* - Message to provide additional information on the results of acting on the target by the actor or the reasons for any failures.
 

--8<-- "snippets/abbr.md"