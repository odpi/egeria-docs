<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0112 People, their personal network and their roles

## Person

`Person` extends [`ActorProfile`](/egeria-docs/types/1/0110-Actors/#actorprofile) to capture more information about a person.

- `fullName` allows the storage of the full legal name, leaving the `displayName` for the person's preferred name and the `qualifiedName` as the employee serial/personnel number.
- `jobTitle` is for the person's job title if that is in use in the organization.
- `isPublic` indicates whether the information in the profile can be shared with colleagues or is only visible to the user(s) that connect with one of the linked user identities or systems that are part of the open metadata ecosystem.

## Peer

The *Peer* relationship links two people together as peers in an organization.  Peers represents a list of a person's close/important colleagues. The perspective on who is a close/important colleague is a personal perspective. Therefore the *Peer* relationship separates the concept of who has linked to a person (*myFollowers*) from who they have specifically linked to (*myPeers*).

## Contribution Record

The *ContributionRecord* accumulates achievements of an individual. Specifically Egeria supports [Karma Points](/egeria-docs/concepts/karma-point). These are awarded for participation in open metadata and governance. The number of karma points awarded to the individual is recorded in their *ContributionRecord* entity.

- `isPublic` indicates whether the values in the contribution record can be shared with colleagues or is only visible to user(s) that connect with one of the linked user identities or systems that are part of the open metadata ecosystem.
- `karmaPoints` captures the total number of points that the individual has earned from their activity.

## PersonRole

Open metadata separates the person from the roles they perform. This is because people often perform many roles and these change over time. Also roles may be put in place before the person is appointed to it and the person appointed can change from time to time.

The PersonRole entity is extended in multiple places to show different types of roles. For example:

- ['TeamLeader'](/egeria-docs/types/1/0115-Teams/#teamleader) and ['TeamMember'](/egeria-docs/types/1/0115-Teams/#teammember)
- ['GovernanceRole'](/egeria-docs/types/4/0445-Governance-Roles/#governancerole)
- ['ProjectManager'](/egeria-docs/types/1/0130-Projects)

## PersonRoleAppointment

The *PersonRole* entity is linked to a *Person* entity with the *PersonRoleAppointment* relationship to show that the person has been appointed.  It is common for [effectivity dates](/egeria-docs/features/effectivity-dates) to be set on this relationship.






![UML](0112-People.svg "Describing the profile for a person")


The [Community Profile OMAS](/egeria-docs/services/omas/community-profile/overview) provides support for a person's profile.  See [personal profile](/egeria-docs/concepts/personal-profile). It also supports the ability to query a person's roles (see [personal roles](/egeria-docs/concepts/personal-roles)) and their peer network (see [peer network](/egeria-docs/concepts/peer-network))


--8<-- "snippets/abbr.md"
