<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0110 Actors

[*Actors*](/concepts/actor) are the people, teams or machines that drive activity in the organization's landscape.  

![UML](0110-Actors.svg "Collecting information about user identities and the people and systems behind them")

## ActorProfile entity
 
An `ActorProfile` describes an entity to store and link information about an actor in open metadata.  It inherits from [`Referenceable`](/types/0/0010-Base-Model) so it has a unique name.

The subtypes of *ActorProfile* add further information about actors:

- [Person](/types/1/0112-People) for profiles describing individuals.
- [Team](/types/1/0115-Teams) for profiles describing teams.
- [ITProfile](/types/1/0117-IT-Profiles) for profiles describing specific IT processes and systems.


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
    
    The [Actor Manager](/services/omvs/actor-manager/overview) API supports the maintenance of actor profiles.

--8<-- "snippets/abbr.md"
