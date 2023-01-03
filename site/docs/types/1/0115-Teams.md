<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0115 Teams

Team are groups of people organized to support a specific goal or responsibility of the organization.  

![UML](0115-Teams.svg "Describing a team")

## Team

A team is a group of people who are working to a common goal. This is recorded in the `Team` entity which is an extension of ['ActorProfile'](/types/1/0110-Actors/#actorprofile). 

## TeamLeadership and TeamMembership

The responsibilities of a team are divided into roles described by ['PersonRole'](/types/1/0112-People/#personrole).  This in turn links to the people or person appointed to fulfil the role.  The `TeamLeadership` and `TeamMembership` relationships link the team to its roles and allow a distinction to be made between the leaders and members of the team. A team can have multiple leadership and membership roles.

## TeamStructure

`TeamStructure` is used to link teams into an organization's hierarchical department structure.  Typically the 



## TeamLeader and TeamMember

`TeamLeader` and `TeamMember` extend from ['PersonRole'](/types/1/0112-People/#personrole). They provide a base type to distinguish between roles that are leadership roles and those which are not.

## Related types

[Organization](/types/4/0440-Organizational-Controls/#organization) is the top-level team of an organization.

Long-standing teams are often responsible for particular [*business capabilities*](/types/4/0440-Organizational-Controls/#businesscapability).  Teams can also be linked to [projects](/types/1/0130-Projects).

## Further information

[People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about teams is populated and used.

The [Community Profile OMAS](/services/omas/community-profile/overview) provides support for managing team structure.

The [Organization Integrator OMIS](/services/omis/organization-integrator/overview) supports the synchronization of team information between open metadata and external systems.


--8<-- "snippets/abbr.md"
