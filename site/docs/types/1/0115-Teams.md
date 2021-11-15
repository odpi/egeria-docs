<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0115 Teams

## Team

A team is a group of people who are working to a common goal. This is recorded in the `Team` entity which is an extension of ['ActorProfile'](/egeria-docs/types/1/0110-Actors/#actorprofile). 

## TeamLeadership and TeamMembership

The responsibilities of a team are divided into roles described by ['PersonRole'](/egeria-docs/types/1/0112-People/#personrole).  This in turn links to the people or person appointed to fulfil the role.  The `TeamLeadership` and `TeamMembership` relationships link the team to its roles and allow a distinction to be made between the leaders and members of the team. A team can have multiple leadership and membership roles.

## TeamStructure



![UML](0115-Teams.svg "Describing a team")


## TeamLeader and TeamMember

`TeamLeader` and `TeamMember` extend from ['PersonRole'](/egeria-docs/types/1/0112-People/#personrole). They provide a base type to distinguish between roles that are leadership roles and those which are not.

## Related types
[Organization](/egeria-docs/types/4/0440-Organization-Controls) is the top-level team of an organization.

Long-standing teams are often responsible for particular [*business capabilities*](/egeria-docs/types/4/0440-Organization-Controls).  Team can also be linked to [projects](/egeria-docs/types/1/0130-Projects).



--8<-- "snippets/abbr.md"
