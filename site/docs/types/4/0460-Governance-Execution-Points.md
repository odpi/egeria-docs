---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0460 Governance Execution Points

A [*governance execution point*](/concepts/governance-execution) defines specific activity that is implementing a requirement of the governance program.  It is represented by an *ExecutionPointDefinition* entity.

The *ExecutionPointDefinition* entities are created during the design of the governance program.  They characterize the types of implementation components that are needed to support the governance requirements.  They are linked to the appropriate [Governance Definition](/types/4/0401-Governance-Definitions) using the *ExecutionPointUse* relationship. Typically, the governance definitions linked to the governance execution point definitions are [Governance Controls](/types/4/0420-Governance-Controls).

The classifications *ControlPoint*, *VerificationPoint* and *EnforcementPoint* are used to label entities describing implementation components such as [Processes](/types/0/0010-Base-model) with the type of execution point and its qualified name. They are often found on elements such as:

* [Governance Action Types](/types/4/0462-Governance-Action-Types)
* [Governance Actions](/types/4/0463-Governance-Actions)

These classifications can be used to drive additional audit logging when the implementation component is running. Logging information about the activities of these components with the qualifiedName of the execution point definition makes it easier to correlate the activity with the governance definitions. 

![UML](0460-Governance-Execution-Points.svg)



--8<-- "snippets/abbr.md"