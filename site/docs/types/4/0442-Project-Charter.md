<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0442 Project Charter

The access to resources for a [project](/types/1/0130-Projects) may be partially controlled by its type or mission.  The project charter adds information to a project that can be used to govern it.

![UML](0442-Project-Charter.svg)

## ProjectCharter

The *ProjectCharter* entity describes the reasons why a particular project exists.  It is often established before the project itself is set up.

* *displayName* provides a name to the charter.
* *mission* describes in free-form text, the hoped for outcome of the project(s) commissioned under this charter.
* *projectType* is a type for the project.  These types, such as "clinical-trial", "manufacturing-improvement", "security-assessment", ..., "incident-investigation" are chosen by the organization and can be encoded in a [valid metadata set](/guides/planning/valid-values/overview).
* *purposes* define a list of formal purposes for the project.  These are inspired by the need to identify processing purposes in the EU's General Data Protection Legislation (GDPR).  These purposes can also be set up in a valid metadata set.

## ProjectCharterLink

The *ProjectCharterLink* relationship connects a *ProjectCharter* entity to one or more *Project* entities.  It allows the same project charter to be used by multiple related projects.  However, a project charter is typically so specific that it is added to only one project. 


--8<-- "snippets/abbr.md"