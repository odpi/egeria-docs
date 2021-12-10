<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0110 Actors

*Actors* are the people, teams or IT processes that drive activity in the digital landscape.  
 
## ActorProfile
 
An `ActorProfile` describes an entity to store and link information about the actor in open metadata.

- `name` - the display name of the profile - such as the preferred name of a person, the commonly used name for a team or a process.  This name is not necessarily unique.

- `description` - the description of the actor that this profile represents.
 
## ContactDetails
 
`ContactDetails` describe the mechanisms to contact an actor - this is typically linked to actor profiles for people and teams.

- `contactMethodType` - the type of communication method:

  - EMAIL - email
  - PHONE - landline or mobile
  - CHAT - instant messaging
  - PROFILE - add message to actor profile
  - ACCOUNT - via an application account
  - OTHER - another type of contact method
  
- `contactMethodService` - the type of service to call to invoke this contact method.

- `contactMethodValue` - the address or account name or number to use for this contact method.
 
## UserIdentity

Most metadata repositories are run in a secure mode requiring incoming requests to include the requester’s security credentials. Therefore we have an identifier for each unique logged on security identity (aka userId). This identity is recorded in the header of the metadata elements when they are created or updated. 

`UserIdentity` provides a structure for storing details about a particular userId. Initially we have a simple string for the userId - but this could be extended to include more sophisticated identification information.

- `distinguishedName` - the fully qualified name in LDAP.

## ProfileIdentity

`ProfileIdentity` links the `ActorProfile` to one or more `UserIdentity` entities.  This allows the calling user's profile to be retrieved from the incoming userId.  The attributes for `ProfileIdentity` help to pick the right `UserIdentity` when navigating from the `ActorProfile` to multiple `UserIdentity` entities:

- `roleTypeName`: the type of role that the `UserIdentity` is used for.
- `roleGUID`: the unique identifier of the specific role that the `UserIdentity` is used for.
- `description`: a human readable description of the use of the `UserIdentity` by the actor.

![UML](0110-Actors.svg "Collecting information about user identities and the people and systems behind them")


## Further information

The subtypes of *ActorProfile* add further information about actors:

- [Person](/egeria-docs/types/1/0112-People) for profiles describing individuals.
- [Team](/egeria-docs/types/1/0115-Teams) for profiles describing teams.
- [ITProfile](/egeria-docs/types/1/0117-IT-Profiles) for profiles describing specific IT processes and systems.

[People, Roles and Organizations](/egeria-docs/features/people-roles-organizations/overview) describes how metadata about people is populated and used.

The following APIs support actor profiles:

- The [Community Profile OMAS](/egeria-docs/services/omas/community-profile/overview) provides support for managing metadata about people and teams.

- The [Organization Integrator OMIS](/egeria-docs/services/omis/organization-integrator/overview) supports the synchronization of information about people and teams between open metadata and external systems.

- The [IT Infrastructure OMAS](/egeria-docs/services/omas/it-infrastructure/overview) provides support for managing profile and user identity metadata for assets such as processes and connectors.

- The [Infrastructure Integrator OMIS](/egeria-docs/services/omis/infrastructure-integrator/overview) supports the synchronization of IT profiles between open metadata and external system definitions.

- The [Security Manager OMAS](/egeria-docs/services/omas/security-manager/overview) provides support for retrieving metadata for all types of actor profiles and user identities metadata.

- The [Security Integrator OMIS](/egeria-docs/services/omis/security-integrator/overview) supports the publishing of all types of actor profiles and user identities between open metadata and external security management systems.

--8<-- "snippets/abbr.md"
