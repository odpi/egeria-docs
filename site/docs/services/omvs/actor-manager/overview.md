<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Actor Manager API

The Actor Manager API provides APIs for user interfaces
that manage the definitions of actors (people, teams, and IT systems) and their related
properties, such as roles, identities, and skills.

## Key Features

- **Actor Profile Management**: Create and maintain profiles for different types of actors,
  including persons, teams, and IT profiles (representing software components or services).
- **Actor Role Management**: Define and assign roles to actors, specifying their responsibilities
  within the organization.
- **User Identity Management**: Manage user identities associated with actor profiles,
  including security group memberships for access control.
- **Contact Details**: Maintain various contact methods (email, phone, etc.) for actors and
  other metadata elements.
- **Contribution Records**: Track the contributions and activity levels of different actors
  within the metadata ecosystem.
- **Assignment Scopes**: Define the organizational or technical scope where an actor's
  role or profile is applicable.
- **Perspectives and Skills**: Capture the professional perspectives and specific skills
  of individuals to aid in collaboration and resource allocation.

## Further information

- [Actor Profile Concept](/concepts/actor-profile/)
- [Actor Role Concept](/concepts/actor-role/)
- [Perspective Concept](/concepts/perspective/)
- [User Identity Concept](/concepts/user-identity/)

----
Sample REST API requests:
- [Egeria-api-actor-manager.http](Egeria-api-actor-manager.http)
- [Egeria-jacquard-actors.http](Egeria-jacquard-actors.http)

---8<-- "snippets/abbr.md"






