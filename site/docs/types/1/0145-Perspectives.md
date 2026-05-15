<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0145 Perspectives

Perspectives describe the context of an actor.  This is typically a human actor, but may be a team or digital process (such as an AI).  It describes how a user is likely to understand query results (data) as it is presented to them.

![UML](0145-Perspectives.svg)

## Perspective entity

The *Perspective* entity describes an [Actor](/types/1/0110-Actors) in terms of their context and how they are likely to process information based on their skills, current context and background.

## Skill entity

The *Skill* entity describes a particular skill that a person, team or digital process may possess.

## SkillSet entity

A *SkillSet* entity is a specialized [Collection](/types/0/0021-Collections) that is used to group skills.

## AssociatedSkills relationship

The *AssociatedSkills* relationship is used to link an [Actor](/types/1/0110-Actors) to a *SkillSet* collection.


--8<-- "snippets/abbr.md"
