<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0118 Actor Roles

Roles describe collections of responsibilities.  These responsibilities can be fulfilled by a person, team or engine.

![UML](0118-Actor-Roles.svg "Describing the role for an actor profile")

## ActorRole entity

Open metadata separates the [ActorProfile](/type/1/0110-Actors) from the roles they perform. This is because people often perform many roles and these change over time. Also roles may be put in place before the person is appointed to it and the person appointed can change from time to time.

## PersonRole entity

The *PersonRole* entity is extended in multiple places to show different types of roles. For example:

- ['TeamLeader'](/types/1/0119-Team-Roles/#teamleader) and ['TeamMember'](/types/1/0119-Team-Roles/#teammember)
- ['GovernanceRole'](/types/4/0445-Governance-Roles/#governancerole)
- ['ProjectManager'](/types/1/0130-Projects)

## PersonRoleAppointment

The *PersonRole* entity is linked to a *Person* entity with the *PersonRoleAppointment* relationship to show that the person has been appointed.  It is common for [effectivity dates](/features/effectivity-dates) to be set on this relationship.


## Further information

The roles within a team are shown on [Model 0119 - Team Roles](/types/1/0119-Team-Roles).

[People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about people is populated and used.

The [Actor Manager](/services/omvs/actor-manager/overview) provides support for managing actor profiles and roles.

The [People Organizer](/services/omvs/people-organizer/overview) supports the definition of team structures.

--8<-- "snippets/abbr.md"
