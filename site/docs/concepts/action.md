---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Action

An *action* is a [process](/concepts/process) that describes an activity typically triggered by an event or detected situation.  There are three specialized types of action supported by Egeria:

* A [To Do](/concepts/to-do) is an action that must be performed by a third party, typically a person.
* A [Meeting](/concepts/to-do) is an action where people gather to discussion and come to agreement.  Meetings often trigger other actions.
* An [Engine Action](/concepts/engine-action) is an automated action that is performed by a [governance engine](/concepts/governance-engine).

Other types of actions from third party systems can also be captured using the base [*Action*](/types/0/0013-Actions) type, or by creating new subtypes.


--8<-- "snippets/abbr.md"
