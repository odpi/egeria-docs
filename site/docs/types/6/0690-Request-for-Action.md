<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0690 Request for Action

A [Request For Action (RfA)](/concepts/request-for-action) identifies an issue detected by a [Survey Action Service](/concepts/survey-action-service) while it is running.

![UML](0690-Request-for-Action.svg)

## RequestForAction entity

The *RequestForAction* entity is a type of [DataFieldAnnotation](/types/6/0610-Annotations) that requests some form of follow on action.  This action may be an automated [governance action](/concepts/governance-action) or, more typically, requires a steward to resolve.  It is not the responsibility of the Survey Action Service to find the means to resolve the issue - it is only responsible for reporting it. 

## RequestForActionTarget relationship

The *RequestForActionTarget* relationship identifies the [Referenceable](/types/0/0010-Base-Model) entity that needs work.  It may be the asset being surveyed, or a different element.

--8<-- "snippets/abbr.md"