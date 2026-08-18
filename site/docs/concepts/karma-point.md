<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Karma Point

A karma point is a reward given to an actor for making a contribution to open metadata.  This may be for:

* Creating some information
* Correcting or enhancing some information
* Linking information together
* Removing obsolete information

Karma points are awarded to automation as well as to people, since both contribute to the open metadata ecosystem.

## How karma points are awarded

Karma points are awarded automatically by the *LovelaceKarmaPointAwardsService* - a [watchdog action service](/concepts/watchdog-action-service) that runs in the *EgeriaWatchdog* [governance engine](/concepts/governance-engine) and is supplied in the `OrganizationInsightContentPack`.

The service listens for changes to open metadata.  For each change, it identifies the user responsible - the `updatedBy` user recorded in the element's version information, or the `createdBy` user where the element has not been updated - and awards that user a karma point.

The point is accumulated in a [ContributionRecord](/types/1/0125-Contribution) linked to the [actor profile](/concepts/actor-profile) for that user, via the *Contribution* relationship.  If the profile does not yet have a contribution record, one is created.  The running total is held in the record's `karmaPoints` property, and the `isPublic` property controls whether it may be shared with colleagues.

!!! attention "Karma points need a profile"
    Points are awarded through the userId that made the change, but they can only be accumulated if that userId is linked to an actor profile.  Create a [user identity](/types/1/0110-Actors) linked to an actor profile for every user whose contribution you want recognized - otherwise their changes earn nothing.

## Using karma points

Karma points support recognition and gamification: league tables, and acknowledgement of the people whose work keeps the catalog trustworthy.  Since points are earned by automation as well as by people, it is usual to keep separate league tables for the two.

!!! info "Related information"
    * [Organization Insight](/egeria-solutions/organization-insight/overview) - the solution that awards and reports on karma points.
    * [Karma points](/features/people-roles-organizations/overview/#karma-points)
    * [Model 0125 Contribution](/types/1/0125-Contribution)

--8<-- "snippets/abbr.md"
