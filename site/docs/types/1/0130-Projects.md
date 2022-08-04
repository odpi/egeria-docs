<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0130 Projects

## Projects

Projects are used to organize a specific activity. The project is used to control the use of resources and associated costs, so they are used appropriately in order to successfully achieve the project's goals.

![UML](0130-Projects.svg)

Projects organize resources to build new capability or improve existing capability. Related projects can be organized into campaigns. Small items of work, typically performed by a single person, can be defined as tasks for a project.

Notice that the project acts as an anchor for collections of resources that the project is using. Since it is a Referenceable, it can have links to external URLs, such as the project home page, project plan or APIs as well as images (see [0015 Linked Media Types](/types/0/0015-Linked-Media-Types) in Area 0).

The description attribute should be used instead of the scopeDescription in ProjectScope; the scopeDescription attribute has been deprecated.  

??? deprecated "Deprecated types"
    - *ProjectScope* relationship is deprecated in favour of the more generic [*AssignmentScope*](/types/1/0120-Assignment-Scopes).

--8<-- "snippets/abbr.md"
