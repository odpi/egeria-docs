<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0013 Actions

Actions are [processes](/types/0/0010-Base-Model) triggered by events.  They may be performed by a person, team or automated process.

![UML](0013-Actions.svg "Describing an action")

## Action entity

The *Action* entity provides a common base class for the [ToDo](/types/1/0135-Actions-For-People), [Meeting](/types/1/0135-Actions-For-People), and the [EngineAction](/types/4/0463-Engine-Actions) entities.  It indicates an action that either needs to be taken, is in progress, or has been taken.

## ActionRequester relationship

The *ActionRequester* links the source for the action, such as a person, meeting or a governance action, to the *Action* entity.

## Actions relationship

The *Actions* relationship links the *Action* entity to the reason or cause of the necessary action.  This is so we can distinguish between the creator (source) of the *Action* and the element (specific rule, project, incident report, deliverable, situation or plan of action) that is being supported/resolved by the action. 

## ActionTarget relationship

The *ActionTarget* relationship associates a *ToDo* entity with one or more elements to work on. The attributes are:

* actionTargetName - The name to identify the action target to the actor that processes it.
* status - The status of the work on this element
* startTime - Date/time that work started on this element.
* completionDate - Date/time that work stopped on this element.
* completionMessage - Message to provide additional information on the results of acting on the target by the actor or the reasons for any failures.


--8<-- "snippets/abbr.md"
