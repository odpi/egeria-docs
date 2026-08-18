<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Actor Profile

An *actor profile* represents a person, a group of people, or an automated process operating in the open metadata ecosystem.  It provides the identity, capabilities and purpose behind the userId that arrives with a request.

Metadata repositories run in a secure mode, so every request carries a security identity and every element records the userId that created or last updated it.  On its own, a userId is just a string.  The actor profile is what turns it into someone - or something - the organization knows about.

## Types of profile

* A [personal profile](/concepts/personal-profile) describes an individual.
* A [team](/concepts/team) profile describes a group of people.
* An [IT profile](/concepts/it-profile) describes a piece of IT infrastructure or an automated process.

## Profiles, identities and roles

A profile is linked to one or more [user identities](/concepts/user-identity) using the *ProfileIdentity* relationship.  People and systems frequently have several - a normal account, an elevated account, a service account - and the relationship records which role each identity is used for, so the right one can be picked when navigating from the profile.

The profile says who the actor *is*.  What they are responsible for is described separately by the [actor roles](/concepts/actor-role) they are appointed to.  Keeping the two apart means an appointment can change without disturbing the identity, and a role can outlive whoever currently holds it.

Alongside the profile sit the actor's [contact methods](/concepts/contact-method), their [perspective](/concepts/perspective) and skills, and their contribution record.

???+ info "Additional information"
    * The *ActorProfile* type, the *UserIdentity* type and the *ProfileIdentity* relationship are described in [Model 0110 Actors](/types/1/0110-Actors).
    * [People, Roles and Organizations](/features/people-roles-organizations/overview) describes how metadata about people is populated and used.
    * The [Actor Manager API](/services/omvs/actor-manager/overview) supports the maintenance of actor profiles.

--8<-- "snippets/abbr.md"
