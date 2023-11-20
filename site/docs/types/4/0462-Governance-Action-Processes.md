<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0462 Governance Action Processes

The types on this page are used to define the process flow for a [governance action process](/concepts/governance-action-process).  The process flow is defined in open metadata so that it can be shared with processing engines throughout the open metadata ecosystem.  In Egeria, the [Governance Engine OMAS](/services/omas/governance-engine/overview) provides services for defining these process flows and is responsible for converting each step in the flow into an [engine action](/concepts/engine-action when the process executes.

![UML](0462-Governance-Action-Processes.svg)

## GovernanceActionProcess

The *GovernanceActionProcess* entity is the root of the governance action process.  It gives the process its unique name and defines the first step through the *GovernanceActionProcessFlow* relationship.

GovernanceActionProcess inherits from [Process](/types/0/0010-Base-Model) so that it can be linked into the governance program as a technical control. See the [GovernanceProcessImplementation](/types/4/0430-Technical-Controls) relationship.  It adds the *domainIdentifier* attribute to link the process to a specific [governance domain](/concepts/governance-domain).

## GovernanceActionProcessFlow

The *GovernanceActionFlow* relationship defines the first [engine action](/concepts/engine-action to run in a governance action process.   It includes an optional *guard* attribute that can be used by the processing engine for logging.

## GovernanceProcessStep

The *GovernanceActionProcessStep* entity defines a [governance action process step](/concepts/governance-action-process-step).  This represents a step in a governance action process.  Its attributes provide a template for initializing an [engine action](/concepts/engine-action when the step in the process runs.

GovernanceActionProcessStep is a [Referenceable](/types/0/0010-Base-Model) and so has a unique name (*qualifiedName*) and *additionalProperties* attributes.  In addition, this type adds

* *domainIdentifier* links the action to a specific [governance domain](/concepts/governance-domain).
* *displayName* - human-readable name for messages and user interfaces.
* *description* - description of the step.
* *producedGuards* - used to help the individual/tool that is constructing the flow for the governance action process to verify that all the necessary guards have been accounted for.
* *ignoreMultipleTriggers* - indicates that a governance action should only be triggered once from this governance action process step, no matter how many times the appropriate guards are produced.  This is important for long-running governance actions that may be triggered by multiple instances of previous steps but is held waiting for the mandatory guard.
* *waitTime* - the minimum number of minutes that the governance action should wait before starting.

## GovernanceProcessStepExecutor

The *GovernanceProcessStepExecutor* relationship identifies the [governance service](/concepts/governance-service) that will run when the [engine action](/concepts/engine-action is started.

* *requestType* - identifies the [governance request type](/concepts/governance-request-type) that links to the [governance service](/concepts/governance-service) in the [governance engine definition](/concepts/governance-engine-definition).
* *requestParameters* identifies additional request parameters that are passed to the governance service when it runs.

## NextGovernanceProcessStep

The *NextGovernanceProcessStep* relationship identifies the next step in the process flow.

* *guard* - identifies the guard produced by the previous step that will cause this step to execute.
* *mandatoryGuard* - indicates that this guard must be produced before the follow-on step is processed.

The follow-on action runs when all of its mandatory guards are produced by previous steps.  It runs as many times as a matching guard is produced unless ignoreMultipleTriggers is set in which case it will run once for that guard.

???+ deprecated "Deprecated types"
    The *ignoreMultipleTriggers* attribute in the *NextGovernanceProcessStep* has been deprecated.

--8<-- "snippets/abbr.md"