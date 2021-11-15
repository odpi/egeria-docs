<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0110 Actors

*Actors* are the people, teams or IT processes that drive activity in the digital landscape.  
 
## ActorProfile
 
An `ActorProfile` describes an entity to store and link information about the actor in open metadata.
 
## ContactDetails
 
`ContactDetails` describe the mechanisms to contact an actor - this is typically linked to actor profiles for people and teams.
 
## UserIdentity

Most metadata repositories are run in a secure mode requiring incoming requests to include the requester’s security credentials. Therefore we have an identifier for each unique logged on security identity (aka userId). This identity is recorded in the header of the metadata elements when they are created or updated. 

`UserIdentity` provides a structure for storing details about a particular userId. Initially we have a simple string for the userId - but this could be extended to include more sophisticated identification information.

## ProfileIdentity

`ProfileIdentity` links the `ActorProfile` to one or more `UserIdentity` entities.  This allows the calling user's profile to be retrieved from the incoming userId.  The attributes for `ProfileIdentity` help to pick the right `UserIdentity` when navigating from the `ActorProfile` to multiple `UserIdentity` entities:

- `roleTypeName`: the type of role that the `UserIdentity` is used for.
- `roleGUID`: the unique identifier of the specific role that the `UserIdentity` is used for.
- `description`: a human readable description of the use of the `UserIdentity` by the actor.

![UML](0110-Actors.svg "Collecting information about user identities and the people and systems behind them")


The subtypes of *ActorProfile* add further information about actors:

- [Person](/egeria-docs/types/1/0112-People) for profiles describing individuals.
- [Team](/egeria-docs/types/1/0115-Teams) for profiles describing teams.
- [ITProfile](/egeria-docs/types/1/0117-IT-Profiles) for profiles describing specific IT processes and systems.


--8<-- "snippets/abbr.md"
