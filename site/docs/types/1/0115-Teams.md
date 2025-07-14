<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0115 Teams

Team are groups of people organized to support a specific goal or responsibility of the organization.  

![UML](0115-Teams.svg "Describing a team")

## Team entity

A team is a group of people who are working to a common goal. This is recorded in the *Team* entity which is an extension of [ActorProfile](/types/1/0110-Actors/#actorprofile). 

## TeamStructure relationship

*TeamStructure* is used to link teams into an organization's hierarchical department structure.  Typically the 

## Organization

*Organization* is a special type of team that is the root of a hierarchy of teams and represents a collection of people and resources with a particular purpose such as a business, non-profit organization or governance department.

## Further information

Long-standing teams are often responsible for particular [*business capabilities*](/types/4/0440-Organizational-Controls/#businesscapability).  Teams can also be linked to [projects](/types/1/0130-Projects).

The roles within a team are shown on [Model 0119 - Team Roles](/types/1/0119-Team-Roles).

[People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about teams is populated and used.

The [People Organizer OMVS](/services/omvs/people-organizer/overview) provides support for managing team structure.

The [Organization Integrator OMIS](/services/omis/organization-integrator/overview) supports the synchronization of team information between open metadata and external systems.


--8<-- "snippets/abbr.md"
