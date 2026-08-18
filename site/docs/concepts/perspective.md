<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Perspective

A *perspective* describes the context of an [actor](/concepts/actor) and how they are likely to process the information that is presented to them.  It is built from their skills, their background and the situation they are working in at the time.

Two people can be shown exactly the same data and reach different conclusions.  A clinical researcher looking at a table of patient measurements reads it as evidence about a treatment; a data engineer looking at the same table reads it as a set of columns with a particular quality profile.  Neither is wrong - they are viewing the data through different perspectives.  Capturing the perspective alongside the actor allows the [governance program](/practices/governance-basics/overview) to reason about who is capable of performing a particular role, who needs additional explanation when data is delivered to them, and which audiences a piece of documentation is written for.

## Perspectives and skills

A perspective is attached to the actor's [profile](/concepts/actor-profile) or [role](/concepts/actor-role).  Alongside it, the individual capabilities of the actor are described using *skills*.  Related skills are grouped into a *skill set*, which is a specialized [collection](/concepts/collection).  An actor is linked to a skill set using the *AssociatedSkills* relationship.

This separation is deliberate:

* A *skill* is a discrete, transferable capability - for example, *Python*, *pharmacovigilance* or *SQL tuning*.  Skills are reusable definitions that many actors can point to.
* A *perspective* is the combined viewpoint that emerges from an actor's skills, background and current context.  It is the lens, rather than the individual pieces of glass.

Skills are also useful on their own.  When work is assigned - such as a [to do](/concepts/to-do) raised by a [request for action](/concepts/request-for-action) - the skill sets of the candidate actors can be used to select someone able to complete it.

???+ info "Additional information"
    * The *Perspective*, *Skill* and *SkillSet* open metadata types are described in [Model 0145 Perspectives](/types/1/0145-Perspectives).
    * The [Actor Manager API](/services/omvs/actor-manager/overview) provides the operations for maintaining perspectives and skills, along with the profiles and roles they are attached to.

--8<-- "snippets/abbr.md"
