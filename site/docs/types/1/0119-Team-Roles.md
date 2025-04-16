<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0119 Team Roles

[Teams](/types/1/0115_Teams) are groups of people organized to support a specific goal or responsibility of the organization.  

![UML](0119-Team-Roles.svg "Describing the team membership")


## TeamLeadership and TeamMembership relationships

The responsibilities of a team are divided into roles described by ['PersonRole'](/types/1/0112-People/#personrole).  This in turn links to the people or person appointed to fulfil the role.  The *TeamLeadership* and *TeamMembership* relationships link the team to its roles and allow a distinction to be made between the leaders and members of the team. A team can have multiple leadership and membership roles.

## TeamLeader and TeamMember entities

*TeamLeader* and *TeamMember* extend from [PersonRole](/types/1/0112-People/#personrole). They provide a base type to distinguish between roles that are leadership roles and those which are not.



--8<-- "snippets/abbr.md"
