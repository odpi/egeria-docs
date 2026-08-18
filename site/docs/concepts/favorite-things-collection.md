<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Favorite Things Collection

A *favorite things collection* is a personal list of the metadata elements that someone wants to keep close at hand - the [assets](/concepts/asset), [projects](/concepts/project), [communities](/concepts/community) and colleagues' profiles they return to regularly.

It is an ordinary [collection](/concepts/collection) used as a *home collection*: it is chained off the individual's [personal profile](/concepts/personal-profile) using the *ResourceList* relationship, and its members are linked with *CollectionMembership*.  The same mechanism supports the equivalent lists for a [team](/concepts/team), a [project](/concepts/project) or a [community](/concepts/community).

Keeping these lists in open metadata rather than in a single user interface has two consequences.  Any tool the individual uses can offer the same personalized starting point, and the individual can choose to receive notifications when the elements on their lists change.

A related, automatically maintained list is the *RecentAccess* collection, which a user interface uses to track the elements someone has been working with.  Where a favorite things collection records what the person chose to keep, a recent access collection records where they have been.

???+ info "Additional information"
    * The *Collection* type and its classifications are described in [Model 0021 Collections](/types/0/0021-Collections); the *ResourceList* relationship is in [Model 0019 More Information](/types/0/0019-More-Information).
    * The [My Profile API](/services/omvs/my-profile/overview) supports the personalization built on top of these lists.
    * The [Collection Manager API](/services/omvs/collection-manager/overview) provides the general operations for managing collections.

--8<-- "snippets/abbr.md"
