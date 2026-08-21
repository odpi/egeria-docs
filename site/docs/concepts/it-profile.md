<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# IT Profile

An *IT profile* is the [actor profile](/concepts/actor-profile) of an automated process operating in the open metadata ecosystem.

Much of the activity in a metadata ecosystem is not performed by people.  Integration connectors, governance services, engines and background jobs all make requests under their own [user identities](/concepts/user-identity), and those requests appear in the header of every element they create or update.  Without an IT profile, all that is visible is a userId.  With one, it is possible to answer *which piece of infrastructure did this, and who is responsible for it?*

An IT profile:

* Links to the *UserIdentity* entities that the process runs under - often more than one, since a process may use different identities for different purposes.
* Links, via the *ITInfrastructureProfile* relationship, to the [IT infrastructure](/types/0/0030-Operating-Platforms) asset that the profile represents.
* Can be appointed to an [IT profile role](/concepts/it-profile-role), in the same way that a person is appointed to a [person role](/concepts/person-role).  The role defines the capabilities and responsibilities; the profile identifies what is currently fulfilling them.

This is what makes automated activity traceable in the same terms as human activity: the [provenance](/features/metadata-provenance/overview) of metadata created by automation resolves to a described, owned piece of infrastructure rather than an anonymous account.

???+ info "Additional information"
    * The *ITProfile* type is described in [Model 0117 IT Profiles](/types/1/0117-IT-Profiles); the *ActorProfile* it extends is described in [Model 0110 Actors](/types/1/0110-Actors).
    * The [Actor Manager API](/services/omvs/actor-manager/overview) provides the operations for maintaining IT profiles and their user identities.

--8<-- "snippets/abbr.md"
