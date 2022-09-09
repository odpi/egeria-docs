<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Execution Points

A *governance execution point* defines specific activity that supports a requirement of a [governance control](/concepts/governance-definition/#governance-control). It characterizes the types of implementation components that are needed to support the governance requirement. Often execution points need to be integrated with the normal activity of the business, but they may also represent additional standalone activity.

There are three types of execution points:

* A *Control Point* is a place in the processing where a decision needs to be made.  It may be a choice on whether to tolerate a reported situation or to resolve it - or it may be a decision on how to solve it.

* A *Verification Point* describes processing that is testing if a desired condition is true.  Quality rules are examples of verification points.  The result of a verification point is the output of the test.  It may, for example, be a boolean, classification or a set of invalid values.

* An *Enforcement Point* describes processing that enforces a specific condition.  For example, data may need to be encrypted at a certain point in the processing. The encryption processing is an enforcement point.

Governance execution points are created during the design of the governance domain.  They are linked to the governance controls to allow traceability from the requirement to the specification of the new activity that is required.  Components that implement the activity described in the execution point are classified with the execution point information.


## Open Metadata Types

A governance execution point is represented in open metadata by an [*ExecutionPointDefinition* entity](/types/4/0460-Execution-Points). The *ExecutionPointDefinition* entities are created during the design of the governance program.  They are linked to the governance controls that they support using the *ExecutionPointUse* relationship.

The classifications *ControlPoint*, *VerificationPoint* and *EnforcementPoint* are used to label entities describing implementation components such as [Processes](/types/0/0010-Base-model) with the type of execution point and the qualified name of the corresponding definition if any. They are often found on elements such as:

* [Governance Action Types](/types/4/0462-Governance-Action-Types)
* [Governance Actions](/types/4/0463-Governance-Actions)

These classifications can be used to drive additional audit logging when the implementation component is running. Logging information about the activities of these components with the qualifiedName of the execution point definition makes it easier to correlate the activity with the governance definitions.

--8<-- "snippets/abbr.md"
