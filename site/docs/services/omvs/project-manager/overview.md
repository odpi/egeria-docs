<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Project Manager API

The Project Manager API provides a REST API to support user interfaces (UIs)
relating to the setup and management of projects and their related elements.

## Key Features

The Project Manager API supports the following key features:

* **Project Management**: Creation, retrieval, update and deletion of project definitions.
* **Project Exploration**: Retrieve projects by name, classification, or search string. Explore project hierarchies and relationship graphs.
* **Project Team Management**: Assign actors (people or teams) to projects with specific roles.
* **Project Hierarchies and Dependencies**: Link projects together to represent work breakdowns or dependencies between different initiatives.
* **Task Management**: Create and manage tasks linked to projects to identify discrete pieces of work.
* **Project Classification**: Classify projects to indicate their approach and style (e.g., Campaign, Task, Study Project).

## Further information

* [Project Concept](/concepts/project/)

Sample requests for the REST API can be found in [Egeria-api-project-manager.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/project-manager/Egeria-api-project-manager.http).

## API Overview

Projects can be organized into a hierarchy and involve many people, or they can be informal, personal projects used by an individual to organize an aspect of their work.  In either case, the people and resources necessary to complete the project can be identified.  The project's definition includes the expected timeline and objective.

The Project Manager API supports:

* The definition of new projects, identifying their scope and timeline.  New projects can be created using a project templates.  The project templates can be created and maintained through the Project Manager API.
* The linking of related project together.
* The classification of projects that are either a campaign, task or a personal project.
* The appointment of a project team and project manager to the project (if applicable).
* The identification of resources such as digital products and assets that are needed to complete the project.
* The maintenance of project status, actions and meeting notes.





---8<-- "snippets/abbr.md"






