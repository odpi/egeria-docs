<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Karma Point

A karma point is a reward given to an actor for making a contribution to open metadata.  This may be for:

* Creating some information
* Correcting or enhancing some information
* Linking information together
* Removing obsolete information

## How karma points are awarded

Karma points are awarded automatically by the *Simon Contribution Recorder* - a [nanny connector](/features/metadata-observability/overview#the-simon-contribution-recorder) that runs in the *OpenMetadataObservability* [integration group](/concepts/integration-group) of the [Core Content Pack](/content-packs/core-content-pack/overview), alongside the Pepys Activity Observer.

Simon listens to the events that report changes to open metadata.  Each change earns one karma point for the user responsible for it - the `updatedBy` user recorded in the element's (or relationship's) version information, or the `createdBy` user where it has not been updated.  Refresh events report no change, so earn nothing.

The points are gathered in memory as the events arrive, and are added to the user's [ContributionRecord](/types/1/0125-Contribution) on each refresh of the connector (every 12 minutes by default).  The contribution record is linked to the [actor profile](/concepts/actor-profile) for the user through the *Contribution* relationship, and is created the first time the user earns a point.  The running total is held in the record's `karmaPoints` property.

!!! attention "Karma points need a profile"
    Points are awarded through the userId that made the change, but they can only be accumulated if that userId is linked to an actor profile.  Create a [user identity](/types/1/0110-Actors) linked to an actor profile for every user whose contribution you want recognized - otherwise their changes earn nothing.  The points of users with no profile are discarded, and listed in the audit log on each refresh.

## People and automation

Automation contributes to open metadata as well as people, and at a very different scale - an integration connector will always out-contribute a person by volume.  By default, Simon awards karma points to people only: its `ignoredUserIdPatterns` configuration property lists the patterns of the userIds that are not awarded points, and the Core Content Pack sets it to `.*npa` and `.*engine`, which match the non-personal accounts of Egeria's servers, connectors and governance engines.

The patterns can be changed to recognize the work of automation too.  If you do, keep separate league tables for people and for automation, since comparing them is meaningless.  Simon never awards points to itself, whatever the patterns say - each update it makes to a contribution record is itself a change.

## Using karma points

Karma points support recognition and gamification: league tables, and acknowledgement of the people whose work keeps the catalog trustworthy.  Because the totals are ordinary metadata, they can be queried, sorted and published like any other open metadata.

!!! info "Related information"
    * [Organization Insight](/egeria-solutions/organization-insight/overview) - the solution that recognizes contribution to open metadata.
    * [The Simon Contribution Recorder](/features/metadata-observability/overview#the-simon-contribution-recorder) - how the karma points are gathered and recorded.
    * [Karma points](/features/people-roles-organizations/overview/#karma-points)
    * [Model 0125 Contribution](/types/1/0125-Contribution)

--8<-- "snippets/abbr.md"
