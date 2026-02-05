---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Action

An *action* is a [process](/concepts/process) that describes an activity typically triggered by an event or detected situation.  There are five specialized types of action supported by Egeria:

* A [To Do](/concepts/to-do) is where request is made for information or services from a third party, typically a person.
* A [Meeting](/concepts/meeting) is an action where people gather to discussion and come to agreement.  Meetings often trigger other actions.
* A [Review](/concepts/review) is an action where specific information is reviewed to determine whether it is correct or not.
* A [Notification](/concepts/notification) is an action where .
* An [Engine Action](/concepts/engine-action) is an automated action performed by a [governance engine](/concepts/governance-engine).

Other types of actions from third party systems can also be captured using the base [*Action*](/types/0/0013-Actions) type, or by creating new subtypes.

??? info "Further information"
    The *Action* open metadata type is described in [Model 0013 Actions](/types/0/0013-Actions).

--8<-- "snippets/abbr.md"
