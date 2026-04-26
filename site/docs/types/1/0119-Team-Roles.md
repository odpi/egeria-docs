<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0119 Roles in a Team

[Teams](/types/1/0115-Teams) are groups of people organized to support a specific goal or responsibility of the organization.  

![UML](0119-Team-Roles.svg "Describing the team membership")


## TeamLeader and TeamMember entities

*TeamLeader* and *TeamMember* extend from [PersonRole](/types/1/0112-People/#personrole). They provide a base type to distinguish between roles that are leadership roles and those which are not.

*PersonRoles* are linked to a team using the [AssignmentScope](/types/1/0120-Assignment-Scopes) relationship to show that roles in a team.



--8<-- "snippets/abbr.md"
