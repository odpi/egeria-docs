<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0117 IT Profiles

Often [IT infrastructure](/egeria-docs/types/0/0030-Hosts-and-Platforms) runs as a background process with its own user identity. The ability to create an IT profile helps to identify which pieces of IT infrastructure is responsible for specific activity.

## ITProfile

`ITProfile` extends ['ActorProfile'](/egeria-docs/types/1/0110-Actors/#actorprofile) to describe a piece of IT infrastructure.
The `ActorProfile` links to the `UserIdentity` entities for this piece of IT infrastructure.

## ITInfrastructureIdentity

`iTinfrastructureProfile` links the actor profile to the [`ITInfrastructure`](/egeria-docs/types/0/0030-Hosts-and-Platform) asset that represents the specific piece of IT Infrastructure that it represents.


![UML](0117-IT-Profiles.svg "Describing an engine's user identities")

--8<-- "snippets/abbr.md"
