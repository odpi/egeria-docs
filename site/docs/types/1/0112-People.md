<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0112 People, their personal network and their roles

This model describes the metadata elements that describe a person and their roles and contribution in the organization.

![UML](0112-People.svg "Describing the profile for a person")

## Person

`Person` extends [`ActorProfile`](/types/1/0110-Actors/#actorprofile) to capture more information about a person. Many of the properties are inspired by the LDAP `inetOrgPerson` attributes (see [RFC 2798](https://datatracker.ietf.org/doc/rfc2798/)).

Typically the `name` is set to a person's preferred name.  The `qualifiedName` may be the identifier from an external system or the `employeeNumber` and/or some combination of names to ensure it is unique.  Then the properties are as follows:

- `title` takes the courtesy title of the person.
- `givenNames` is set to a space separated list of names that are not the person's surname (or family name).
- `initials` takes the first letter of each of a person's given names.   The format may include spaces, periods or both to separate the initials.
- `surname` holds the person's family name.
- `fullName` allows the storage of the full legal name, leaving the `displayName` for the person's preferred name and the `qualifiedName` as the employee serial/personnel number plus .
- `jobTitle` is for the person's job title if that is in use in the organization.
- `employeeNumber` is the unique identifier in use in the organization to identify the person - often related to an employment or partnership contract.
- `employeeType` code used by the organization, typically to identify the type of contract they have with the organization.
- `preferredLanguage` is on or more spoken or written language identifiers preferred by the person.
- `isPublic` indicates whether the information in the profile can be shared with colleagues or is only visible to the user(s) that connect with one of the linked user identities or systems that are part of the open metadata ecosystem.

## Peer

The *Peer* relationship links two people together as peers in an organization.  Peers represents a list of a person's close/important colleagues. The perspective on who is a close/important colleague is a personal perspective. Therefore the *Peer* relationship separates the concept of who has linked to a person (*myFollowers*) from who they have specifically linked to (*myPeers*).

## Contribution Record

The *ContributionRecord* accumulates achievements of an individual. Specifically Egeria supports [Karma Points](/concepts/karma-point). These are awarded for participation in open metadata and governance. The number of karma points awarded to the individual is recorded in their *ContributionRecord* entity.

- `isPublic` indicates whether the values in the contribution record can be shared with colleagues or is only visible to user(s) that connect with one of the linked user identities or systems that are part of the open metadata ecosystem.
- `karmaPoints` captures the total number of points that the individual has earned from their activity.


## Further information

[People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about people is populated and used.

The [Community Profile OMAS](/services/omas/community-profile/overview) provides support for managing a [person's profile](/concepts/personal-profile). It also supports the ability to query a person's [roles](/concepts/personal-roles) and their [peer network](/concepts/peer-network).

The [Organization Integrator OMIS](/services/omis/organization-integrator/overview) supports the synchronization of information about people between open metadata and external systems.

--8<-- "snippets/abbr.md"
