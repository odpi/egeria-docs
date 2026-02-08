<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0130 Projects

Projects are used to organize a specific activity. They can control the use of resources and associated costs, so they are used appropriately in order to successfully achieve the project's goals.
Related projects can be organized into campaigns. Small items of work, typically performed by a single person, can be defined as tasks for a project.

Notice that the project acts as an anchor for collections of resources that the project is using. Since it is a Referenceable, it can have links to external URLs, such as the project home page, project plan or APIs as well as images (see [0015 Linked Media Types](/types/0/0015-Linked-Media-Types) in Area 0).

![UML](0130-Projects.svg)

## Project entity

The project entity represents a single project.  It inherits from [*Referenceable*](/types/0/0010-Base-Model) and includes attributes for defining the timeframe for the project and its status.

* *mission* describes in free-form text, the hoped for outcome of the project(s) commissioned under this charter.
* *purposes* define a list of formal purposes for the project.  These are inspired by the need to identify processing purposes in the EU's General Data Protection Legislation (GDPR).  These purposes can also be set up in a valid metadata set.
* *successCriteeria* lists the criteria that should be used to evaluate the success of the project.
* *plannedStartDate* defines the expected start date of the project.
* *actualStartDate* defines the actual start date of the project.
* *plannedCompletionDate* defines the expected end date of the project.
* *actualCompletionDate* defines the actual end date of the project.
* *projectScope* defines the scope of the project.
* *projectStatus* defines the status of the project.
* *projectHealth* defines the health of the project.
* *priority* defines the priority of the project.


## Campaign classification

The *Campaign* classification describes a collection of related projects that are working towards a common goal.  Often this goal is a complex transformation that needs actions from independent teams.  The definition of the campaign helps to identify the role of the different projects in achieving the common goal, and providing the umbrella for coordinating specific activities as needed.

A campaign classification is typically attached to either:

* a [*Collection*](/types/0/0021-Collections) entity whose members are the related projects.
* a [*Project*](#project-entity) entity where the related projects are linked by the [*ProjectHierarchy*](#projecthierarchy-relationship) relationship.

## Task classification

The *Task* classification is attached to a *Project* entity to indicate that this entity represents a small piece of work that is typically assigned to a single person (identified via the [*ProjectTeam*](#projectteam-relationship) relationship).  Such a task is linked to a parent project via the [*ProjectHierarchy*](#projecthierarchy-relationship) relationship.

## PersonalProject classification

The *PersonalProject* classification is attached to a *Project* entity to indicate that this entity represents an informal project that has been created by single person (identified via the [*ProjectTeam*](#projectteam-relationship) relationship) to help organize a part of their work.  These projects are typically not linked to into a project hierarchy.  They may be linked to other project entities via the [*ProjectDependency*](#projectdependency-relationship) relationship.

Personal projects do not typically have a [Project Manager](#projectmanagement-relationship) assigned.

## StudyProject classification

The *StudyProject* classifies a project that is a focused analysis of a topic, person, object or situation.

## ProjectHierarchy relationship

Projects can be broken down into smaller projects that can be executed by different teams on different timelines with different project manager(s) and a specific slice of the budget.  The projects that are broken down in this way are linked together using the *ProjectHierarchy* relationship.

## ProjectDependency relationship

A project that needs the results of another project to complete its work can be linked to that project via the *ProjectDependency* relationship.

## ProjectTeam relationship

The *ProjectTeam* relationship links a project to the [*Actors*](/types/1/0110-Actor) that will perform the work defined by the project.

## ProjectManagement relationship

The *ProjectManagement* relationship links a project to the [PersonRole](/types/1/0112-People) entity that will coordinate and track the efforts of the project team.  The role in turn links to the individual(s) appointed to perform the role.

## ProjectManager entity

The *ProjectManager* is a specialized [*PersonRole*](/types/1/0112-People) to represent project management responsibilities.  It is linked to the project to be managed via the [*ProjectManagement*](#projectmanagement-relationship) relationship.

## ProjectClassification classification

The *ProjectClassification* classification is used to classify a project entity by approach (method) and how the intended results are to be used.  For example, the project may be experimental, using an agile development method.  The project classification can be used on any type of project entity.  It is for organizations that adjusts their governance processes and management of projects, iterations and tasks developing an idea as it moves from research, proof of concept, pilot and production/product.  It is expected that the values for the attributes in this classification are controlled using [valid metadata values](/guides/planning/valid-values/overview).

* *approach* defines the methodology used to achieve the project's goals.
* *managementStyle* defines the management style for the project - for example, there may be a management style for experimental prototyping projects, verses a more formal approach for projects that are used to develop a product.
* *resultsUsage* defines how the results of the project are intended to be used.  For example, the results may be used to inform future projects, or to test a theory, or to develop a product.

??? deprecated "Deprecated types"
    - The *ProjectScope* relationship is deprecated in favour of the more generic [*AssignmentScope*](/types/1/0120-Assignment-Scopes). The *description* attribute of the *AssignmentScope* relationship should be used instead of the *scopeDescription* in the ProjectScope relationship; the scopeDescription attribute has been deprecated.  
    - The *status* attribute on *Project* is deprecated in favour of the more specific *projectStatus* attribute, which makes it easier to align with an appropriate valid value set.

--8<-- "snippets/abbr.md"
