<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0137 Actions for People

In an ideal world, most governance activity is automated by the [Governance Engines](/types/4/0461-Governance-Engines/#governanceengines). However, there are inevitably actions that require a person, or an external agent, to perform. These actions may be simply be to read some information, or to approve a change or something more substantial.


![UML](0137-Actions.svg "Describing an action for a person")

## Action entity

The *Action* entity provides a common base class for the *ToDo* entity and the [*EngineAction*](/types/4/0463-Egnine-Actions) entity.

## ToDo entity

A *ToDo* entity is a [*Referenceable*](/types/0/0010-Base-Model) that describes an item of work for an [*Actor*](/types/1/0110-Actors) to perform.  This work is performed outside the open metadata ecosystem.  

The additional attributes are:

* name - Name or title of the todo/action.
* description - Description of the required action.
* toDoType - Type of to do - typically managed in a valid value set and used in stewardship automation.
* creationTime - When the requested action was identified.
* priority - How urgent is this action?
* dueTime - When the requested action needs to be completed.
* status - How complete is the action? (See ToDoStatus)
* completionTime - When the requested action was completed.


## ToDoStatus enumeration

The *ToDoStatus* describes the status of the *ToDo* entity to help the assigned actor understand whether work is outstanding.

* Open - No action has been taken.
* InProgress - Work is underway to complete the action.
* Waiting - Work is blocked waiting for resource of another action to complete.
* Complete - The action has been completed successfully.
* Abandoned - Work has stopped on the action and will not recommence.

## ToDoSource relationship

The *ToDoSource* links the source for the action, such as a person, meeting or a governance action, to the ToDo entity.

## Actions relationship

The *Actions* relationship links the ToDo entity to the reason or cause of the necessary action.  This is so we can distinguish between the creator (source) of the ToDo and the element (specific rule, project, incident report, deliverable, situation or plan of action) that is being supported/resolved by the action.  The *meetingType* attribute

## ActionTarget relationship

The *ActionTarget* relationship associates a *ToDo* entity with one or more elements to work on. The attributes are:

* actionTargetName - The name to identify the action target to the actor that processes it.
* status - The status of the work on this element
* startDate - Date/time that work started on this element.
* completionDate - Date/time that work stopped on this element.
* completionMessage - Message to provide additional information on the results of acting on the target by the actor or the reasons for any failures.

## ActionAssignment relationship

The *ActionAssignment* relationship identifies the [*Actor*](/types/1/0110-Actor) that has been assigned to perform the action desribed by the *ToDo* entity.

--8<-- "snippets/abbr.md"
