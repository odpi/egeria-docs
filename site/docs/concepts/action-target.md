---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Action Target

An *action target* is a metadata element that is to be processed by an [action](/concepts/action).  

A list of action targets is linked to the action using the [ActionTarget](/types/0/0013-Actions) relationship.  This relationship characterises the way the target should be used (*actionTargetName*), and the processing status (*activityStatus*).

!!! example "Example"
    For example, consider an [engine action](/concepts/engine-action) responsible for verifying that all columns in a database asset are linked to a glossary term with a [semantic assignment](/types/3/0370-Semantic-Assignment) relationship.  The database asset to validate is linked to the engine action as an action target.  

If an engine action is part of a [governance action process](/concepts/governance-action-process), it can also nominate new action targets to be processed by the next engine action in the process.  

!!! example "Example"
    For example, if the engine action described above discovers any columns without a glossary term, it could return a [guard](/concepts/guard) of `incomplete-semantic-assignment` and a list of [relational column](/types/5/0534-Relational-Schemas) elements that need the semantic assignment as the action targets.  A follow-on engine action would receive this list of columns in its action targets when it starts.  Alternatively, the engine action could create and assign a [To Do](/concepts/to-do) to the appropriate steward for correction along with the list of column elements as the todo's action targets.

??? info "Further information"
    The *ActionTarget* open metadata type is described in [Model 0013 Actions](/types/0/0013-Actions).


--8<-- "snippets/abbr.md"
