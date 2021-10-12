<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0115 Teams

## Team

A team is a group of people who are working to a common goal. The ['ActorProfile'](/egeria-docs/types/1/0110-Actors/#actorprofile) is extended to capture more information about a team. This is recorded in the *Team* entity.

## TeamLeader

The roles within the team divide into *TeamLeader* and *TeamMember*. A team can have multiple leaders and members. These roles extend from ['PersonRole'](/egeria-docs/types/1/0112-People/#personrole) which links the role to the person appointed.

![UML](0115-Teams.svg "Describing a team")

--8<-- "snippets/abbr.md"
