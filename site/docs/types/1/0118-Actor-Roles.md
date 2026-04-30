<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0118 Actor Roles

Roles describe collections of responsibilities.  These responsibilities can be fulfilled by a person, team or engine.

Open metadata separates the [ActorProfile](/type/1/0110-Actors) from the roles they perform. This is because people often perform many roles and these change over time. Also roles may be put in place before the actor is appointed to it and the actor appointed can change from time to time.


![UML](0118-Actor-Roles.svg "Describing the role for an actor profile")

## ActorRole entity

The *ActorRole* entity describes a collection of responsibilities that are intended to be performed by an actor. It is a type of [Actor](/type/1/0110-Actors) that adds these new attributes:

* *actorRoleGroups* - a list of role groups that the role is a part of.
* *scope* - the scope of the role.  This is often replaced or augmented by the [ScopedBy](/types/1/0120-Assignment-Scopes) relationship.

## PersonRole entity

The *PersonRole* entity describes an actor role that is intended to be performed by a person.
It is extended by the ['GovernanceRole'](/types/4/0445-Governance-Roles/#governancerole) type.

## PersonRoleAppointment

The *PersonRole* entity is linked to a *Person* entity with the *PersonRoleAppointment* relationship to show that the person has been appointed.  It is common for [effectivity dates](/features/effectivity-dates) to be set on this relationship.

## TeamRole entity

The *EacmRole* entity describes an actor role that is intended to be performed by a [team]().
It is extended by the ['GovernanceRole'](/types/4/0445-Governance-Roles/#governancerole) type.

## PersonRoleAppointment

The *PersonRole* entity is linked to a *Person* entity with the *PersonRoleAppointment* relationship to show that the person has been appointed.  It is common for [effectivity dates](/features/effectivity-dates) to be set on this relationship.

## PersonRole entity

The *PersonRole* entity describes an actor role that is intended to be performed by a person.
It is extended by the ['GovernanceRole'](/types/4/0445-Governance-Roles/#governancerole) type.

## PersonRoleAppointment

The *PersonRole* entity is linked to a *Person* entity with the *PersonRoleAppointment* relationship to show that the person has been appointed.  It is common for [effectivity dates](/features/effectivity-dates) to be set on this relationship.

## Further information

[People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about people is populated and used.

The [Actor Manager](/services/omvs/actor-manager/overview) provides support for managing actor profiles and roles.

The [People Organizer](/services/omvs/people-organizer/overview) supports the definition of team structures.

--8<-- "snippets/abbr.md"
