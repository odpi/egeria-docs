<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0110 Actors

[*Actors*](/concepts/actor) are the people, teams or machines that drive activity in the organization's landscape.  

![UML](0110-Actors.svg "Collecting information about user identities and the people and systems behind them")

## ActorProfile entity
 
An `ActorProfile` describes an entity to store and link information about an actor in open metadata.  It inherits from [`Referenceable`](/types/0/0010-Base-Model) so it has a unique name.

- `name` - the display name of the profile - such as the preferred name of a person, the commonly used name for a team or a process.  This name is not necessarily unique.

- `description` - the description of the actor that this profile represents.

The subtypes of *ActorProfile* add further information about actors:

- [Person](/types/1/0112-People) for profiles describing individuals.
- [Team](/types/1/0115-Teams) for profiles describing teams.
- [ITProfile](/types/1/0117-IT-Profiles) for profiles describing specific IT processes and systems.

## ProfileLocation relationship

The `ProfileLocation` relationship identifies an association between an ActorProfile and a [Location](/types/0/0025-Locations), such as a person's primary work location.  The `associationType` property records the purpose of the association.  Its value can be defined in a [ValidValueSet](/types/5/0545-Reference-Data).

## ContactDetails entity
 
`ContactDetails` describe the mechanisms to contact an actor - this is typically linked to actor profiles for people and teams.

- `contactMethodType` - the type of communication method:

    * EMAIL - email
    * PHONE - landline or mobile
    * CHAT - instant messaging
    * PROFILE - add message to actor profile
    * ACCOUNT - via an application account
    * OTHER - another type of contact method
  
- `contactMethodService` - the type of service to call to invoke this contact method.

- `contactMethodValue` - the address or account name or number to use for this contact method.
 
## UserIdentity entity

Most metadata repositories are run in a secure mode requiring incoming requests to include the requester’s security credentials. Therefore, we have an identifier for each unique logged on security identity (aka userId). This identity is recorded in the header of the metadata elements when they are created or updated. 

`UserIdentity` provides a structure for storing details about a particular userId. Initially we have a simple string for the userId - but this could be extended to include more sophisticated identification information.

- `distinguishedName` - the fully qualified name in LDAP.

## ProfileIdentity relationship

`ProfileIdentity` links the `ActorProfile` to one or more `UserIdentity` entities.  This allows the calling user's profile to be retrieved from the incoming userId.  The attributes for `ProfileIdentity` help to pick the right `UserIdentity` based on [`PersonRole`](/types/1/0112-People) when navigating from the `ActorProfile` to multiple `UserIdentity` entities:

- `roleTypeName`: the type of role that the `UserIdentity` is used for.
- `roleGUID`: the unique identifier of the specific role that the `UserIdentity` is used for.
- `description`: a human-readable description of the use of the `UserIdentity` by the actor.



!!! info "Further information"
    [People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about people is populated and used.
    
    The following APIs support actor profiles:
    
    - The [Community Profile OMAS](/services/omas/community-profile/overview) provides support for managing metadata about people and teams.

    - The [Organization Integrator OMIS](/services/omis/organization-integrator/overview) supports the synchronization of information about people and teams between open metadata and external systems.

    - The [IT Infrastructure OMAS](/services/omas/it-infrastructure/overview) provides support for managing profile and user identity metadata for assets such as processes and connectors.
    
    - The [Infrastructure Integrator OMIS](/services/omis/infrastructure-integrator/overview) supports the synchronization of IT profiles between open metadata and external system definitions.
    
    - The [Security Manager OMAS](/services/omas/security-manager/overview) provides support for retrieving metadata for all types of actor profiles and user identities metadata.
    
    - The [Security Integrator OMIS](/services/omis/security-integrator/overview) supports the publishing of all types of actor profiles and user identities between open metadata and external security management systems.

--8<-- "snippets/abbr.md"
