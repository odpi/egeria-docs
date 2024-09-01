<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0462 Governance Action Processes

The types on this page describe how to create reusable "templates" that are used to drive governance actions in open metadata.  There are two approaches:

* A [governance action type](/concepts/governance-action-type) describes a single step action.
* A [governance action process](/concepts/governance-action-process) describes a sequence of steps in a process flow.  The process flow is defined in open metadata so that it can be shared with processing engines throughout the open metadata ecosystem.  

In Egeria, the [Open Governance Service](/services/gaf-metadata-management) provides services for defining governance action types and process flows and is responsible for converting each step in the flow into an [engine action](/concepts/engine-action) when the process executes.

![UML](0462-Governance-Action-Processes.svg)

## GovernanceActionType entity

The *GovernanceActionType* entity describes a type of call to a [governance service](/concepts/governance-service) running in a [governance engine](/concepts/governance-engine).  The engine to call is defined using the *GovernanceActionExecutor* relationship.  When the governance action type is used to initiate some activity, it results in the creation of an [Engine Action](/concepts/engine-action) to control the call to the governance service running in the linked governance engine.

It inherits from [Referenceable](/types/0/0010-Base-Model) and so has a unique name (*qualifiedName*) and *additionalProperties* attributes.  In addition, this type adds:

* *domainIdentifier* links the action to a specific [governance domain](/concepts/governance-domain).
* *displayName* - human-readable name for messages and user interfaces.
* *description* - description of the governance action that is taken.
* *waitTime* - the minimum number of minutes that the engine action should wait before starting.  This is in addition to any requested start time from the initiating user.

## GovernanceActionExecutor relationship

The *GovernanceActionExecutor* relationship identifies the [governance service](/concepts/governance-service) that will run when the [engine action](/concepts/engine-action) is started.

* *requestType* - identifies the [governance request type](/concepts/governance-request-type) that links to the [governance service](/concepts/governance-service) in the [governance engine definition](/concepts/governance-engine-definition).
* *requestParameters* - additional request parameters to pass to the governance service when called.
* *requestParameterFilter* - lists the names of the request parameters to remove from the requestParameters supplied by the caller.
* *requestParameterMap* - provides a translation map between the supplied names in the requestParameters and the names supported by the implementation of the governance service.
* *actionTargetFilter* - lists the names of the action targets to remove from the supplied action targets.
* *actionTargetMap* - provides a translation map between the supplied name of an action target and the name supported by the implementation of the governance service.

## TargetForActionType relationship

The *TargetForActionType* relationship identifies an element that should be passed to the [engine action](/concepts/engine-action) as a [TargetForAction](/types/4/0463-Engine-Actions) when it is started.  The caller may also add additional action targets.  It has the following attribute.

* *actionTargetName* is an identifier used by the resulting governance service to determine how to use the associated element.

## GovernanceActionProcess entity

The *GovernanceActionProcess* entity is the root of the governance action process.  It gives the process its unique name and defines the first step through the *GovernanceActionProcessFlow* relationship.

GovernanceActionProcess inherits from [Process](/types/0/0010-Base-Model) so that it can be linked into the governance program as a technical control. See the [GovernanceProcessImplementation](/types/4/0430-Technical-Controls) relationship.  It adds the *domainIdentifier* attribute to link the process to a specific [governance domain](/concepts/governance-domain).

## GovernanceActionProcessFlow relationship

The *GovernanceActionFlow* relationship defines the first *GovernanceActionProcessStep* to run in a governance action process.   It includes an optional *guard* attribute that can be used by the processing engine for logging and predefined *requestParameters* to pass to the governance service when called.

## GovernanceProcessStep entity

The *GovernanceActionProcessStep* entity defines a [governance action process step](/concepts/governance-action-process-step).  This represents a step in a governance action process.  Its attributes provide a template for initializing an [engine action](/concepts/engine-action) when the step in the process runs.

GovernanceActionProcessStep is a *GovernanceActionType* and so has all of the attributes of that type of entity.  In addition, this type adds:

* *ignoreMultipleTriggers* - indicates that a governance action should only be triggered once from this governance action process step, no matter how many times the appropriate guards are produced.  This is important for long-running governance actions that may be triggered by multiple instances of previous steps but is held waiting for the mandatory guard.

## NextGovernanceProcessStep relationship

The *NextGovernanceProcessStep* relationship identifies the next step in the process flow.

* *guard* - identifies the guard produced by the previous step that will cause this step to execute.
* *mandatoryGuard* - indicates that this guard must be produced before the follow-on step is processed.

The follow-on action runs when all of its mandatory guards are produced by previous steps.  It runs as many times as a matching guard is produced unless ignoreMultipleTriggers is set in which case it will run once for that guard.

## GovernanceActionProcessInstance entity

The *GovernanceActionProcessInstance* entity describes a running instance of a *GovernanceActionProcess*.  It is linked to its process using the [ProcessHierarchy](/types/2/0215-Software-Components) relationship.


???+ deprecated "Deprecated types"
    The *ignoreMultipleTriggers* attribute in the *NextGovernanceProcessStep* has been deprecated.  It is now located in the *GovernanceActionType* entity.
    The *supportedGuards* attribute in the *GovernanceActionType* has been deprecated in favour of the *producedGuards* entity.

--8<-- "snippets/abbr.md"