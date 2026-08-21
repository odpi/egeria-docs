<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Project

A *project* organizes a specific piece of activity.  It gathers together the people who are doing the work, the resources they need, the timeline they are working to and the criteria by which the outcome will be judged.

Projects in open metadata cover a wide range.  At one end is a formal, funded programme of work with a project manager, a budget and a set of dependent sub-projects.  At the other is a personal project that someone creates to organize a corner of their own work.  Both use the same type, because both benefit from the same thing: a place to record what is being attempted, by whom, and how it is going.

A project is also an [anchor](/concepts/anchor).  The [collections](/concepts/collection) of resources being used, the [external references](/concepts/external-reference) to the project's home page or plan, its [meetings](/concepts/meeting) and its [to dos](/concepts/to-do) all hang off the project and are managed with it.

## Describing the work

* *mission* - the hoped-for outcome, in free text.
* *projectScope* - what is in and out of scope.
* *successCriteria* - how the outcome will be judged.
* *plannedStartDate* / *plannedCompletionDate* - the intended timeline.
* *actualStartDate* / *actualCompletionDate* - what actually happened.
* *projectStatus*, *projectHealth* and *priority* - how the project is progressing.
* *dataProcessingPurposes* - the formal purposes for which the project may process data.  These are the purposes described in [data processing descriptions](/concepts/data-processing-description), and they are what make it possible to check that a project's use of personal data has been agreed.

## Kinds of project

Rather than defining a separate type for each style of project, open metadata classifies the *Project* entity:

* **Campaign** - a collection of related projects working towards a common goal, usually a transformation that needs action from several independent teams.
* **Task** - a small piece of work assigned to a single person, linked to its parent project.
* **PersonalProject** - an informal project created by one person to organize part of their own work.  These usually have no project manager and are not part of a project hierarchy.
* **StudyProject** - a focused analysis of a topic, person, object or situation.
* **Experiment** - a project conducted to test a *hypothesis*, which is recorded on the classification.

Separately, the **ProjectClassification** classification records the *approach* (the methodology used), the *managementStyle* and the *resultsUsage*.  This is for organizations that vary their governance according to where an idea sits on the path from research through proof of concept and pilot to production - an experimental prototype and a product development project need different levels of ceremony, and the classification is what lets the difference be applied automatically.

## Connecting projects to people and to each other

* *ProjectHierarchy* breaks a project down into smaller projects that different teams can run on their own timelines with their own budgets.
* *ProjectDependency* records that one project needs the results of another before it can complete.
* *AssignmentScope* links the project to the [actors](/concepts/actor) doing the work, including the [person role](/concepts/person-role) that coordinates it; each role in turn identifies whoever is currently appointed to it.

???+ info "Additional information"
    * The *Project* type, its classifications and its relationships are described in [Model 0130 Projects](/types/1/0130-Projects).
    * The [Project Manager API](/services/omvs/project-manager/overview) provides the operations for defining projects, appointing teams and project managers, and maintaining status, actions and meeting notes.

--8<-- "snippets/abbr.md"
