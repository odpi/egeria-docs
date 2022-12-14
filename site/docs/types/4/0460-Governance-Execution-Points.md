<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0460 Governance Execution Points

A [*governance execution point*](/concepts/governance-execution) defines specific activity that is implementing a requirement of the governance program.  

![UML](0460-Governance-Execution-Points.svg)

## ExecutionPointDefinition entity

An execution point is represented by an *ExecutionPointDefinition* entity.  There are three subtypes:

* *ControlPointDefinition* describes a decision that must be made to resolve a situation.  The decision is typically passed to a human, but it could be an analytical process.
* *EnforcementPointDefinition* describes an action that is taken to enforce a governance control.
* *VerificationPointDefinition* describes a test that must be made to determine if a particular condition is true.  The result is logged, and typically follow-on actions are initiated if the result is not what was expected.

The *ExecutionPointDefinition* entities are created during the design of the governance program.  They characterize the types of implementation components that are needed to support the governance requirements.  

## ExecutionPointUse relationship

*ExecutionPointDefinition* entities are linked to the appropriate [Governance Definition](/types/4/0401-Governance-Definitions) using the *ExecutionPointUse* relationship. Typically, the governance definitions linked to the governance execution point definitions are [Governance Controls](/types/4/0420-Governance-Controls).

## ControlPoint, VerificationPoint and EnforcementPoint classifications

The classifications *ControlPoint*, *VerificationPoint* and *EnforcementPoint* are used to label entities describing implementation components such as [Processes](/types/0/0010-Base-model) with the type of execution point and its qualified name that they implement. They are often found on elements such as:

* [Governance Action Types](/types/4/0462-Governance-Action-Types)
* [Governance Actions](/types/4/0463-Governance-Actions)

These classifications can be used to drive additional audit logging when the implementation component is running. Logging information about the activities of these components with the qualifiedName of the execution point definition makes it easier to correlate the activity with the governance definitions. 




--8<-- "snippets/abbr.md"