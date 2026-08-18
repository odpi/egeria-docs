<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Organization Insight

An open metadata ecosystem is built by many hands.  People catalogue resources, write definitions, review findings and correct mistakes, and automated services work alongside them doing the same kinds of work at a different scale.  *Organization Insight* is about seeing that contribution: who - and what - is doing the work, how much of it there is, and where in the organization it is happening.

The capability is delivered by the *Lovelace* insight services, orchestrated by the [Babbage Analytical Engine](/patterns/harvest-and-publish/overview), and supplied in the `OrganizationInsightContentPack`.  Each service watches the ecosystem and records what it observes as metadata, so the observations can be queried, published and reported on like anything else.

## Increasing Karma

### Why karma points exist

[Karma points](/concepts/karma-point) recognize actors - both individuals and automation - for their contributions to open metadata: creating information, correcting or enhancing it, linking it together, and removing what is obsolete.

The purpose is recognition rather than measurement for its own sake.  Maintaining an open metadata ecosystem depends on people doing work that benefits colleagues they may never meet, and that work is easy to overlook.  Karma points make it visible, and they support the gamification of contribution - league tables, acknowledgement of the people whose effort keeps the catalog trustworthy.  Because points are awarded to automation as well as people, it is worth maintaining separate league tables for the two: an integration connector will always out-contribute a person by volume, and comparing them is meaningless.

### How points are awarded

Karma points are awarded by the *LovelaceKarmaPointAwardsService*, a [watchdog action service](/concepts/watchdog-action-service) that runs in the *EgeriaWatchdog* [governance engine](/concepts/governance-engine) under the request type **Award Karma Points**.

When it starts, the service registers a listener for changes to open metadata.  From then on:

1. Every change event other than a refresh event is a candidate for a reward.  The service takes the `updatedBy` user from the element's version information, or the `createdBy` user where there is no update user - so the point goes to whoever actually made the change.
2. It looks up the [actor profile](/features/people-roles-organizations/overview) associated with that userId.  **Only users with a profile earn karma points.**  This is why a [user identity](/types/1/0110-Actors) has to be created and linked to an actor profile for everyone whose contribution you want recognized - a userId that belongs to no profile has nowhere to accumulate a total.
3. The total itself lives in a [ContributionRecord](/types/1/0125-Contribution) attached to the actor profile.  If the profile already has one, its `karmaPoints` value is incremented.  If it does not, the service creates one, starting the total at 1.
4. The mapping from userId to contribution record is cached, so subsequent awards for the same user skip the lookup entirely.

The design is deliberately cheap: the service is on the path of every metadata change in the ecosystem, so the update has to cost as little as possible.  Updates are synchronized to avoid two threads updating the same contribution record at once, and anything unexpected in the metadata is ignored rather than investigated, in the interests of speed.  A missed karma point is not worth slowing the ecosystem down for.

The engine action below shows the service running, requested by the Babbage Analytical Engine integration connector that orchestrates the Lovelace services:

--8<-- "snippets/engine-actions/award-karma-points-(egeriawatchdog)-mermaid-graph.md"

### Using the results

The contribution record carries an `isPublic` flag that determines whether an actor's totals may be shared with colleagues or are visible only through their own user identities, so recognition does not have to mean exposure for those who would rather it did not.

Because the totals are ordinary metadata, they can be queried directly, shown in Egeria's user interfaces, and published as part of the *Organization Observability* family of the [Open Metadata Digital Product Catalog](/patterns/harvest-and-publish/overview) for teams that want to report on contribution over time.

## Enterprise Oracle

--8<-- "snippets/work-in-progress.md"

The Enterprise Oracle will provide insight into the amount and type of activity occurring in different parts of the organization - not just who is contributing, but where the energy in the ecosystem is concentrated, which areas are actively curated and which are quietly going stale.

!!! info "Related information"

    * [Karma point](/concepts/karma-point) - what earns a point and how it is awarded.
    * [Model 0125 Contribution](/types/1/0125-Contribution) - the contribution record and its relationship to the actor profile.
    * [Karma points](/features/people-roles-organizations/overview/#karma-points) - how contribution fits into the wider picture of people, roles and organizations.
    * [Organization Insight Content Pack](/content-packs/observability-content-pack/overview) - the connector definitions that deliver these services.

--8<-- "snippets/abbr.md"
