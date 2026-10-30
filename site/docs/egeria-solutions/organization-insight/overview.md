<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Organization Insight

An open metadata ecosystem is built by many hands.  People catalogue resources, write definitions, review findings and correct mistakes, and automated services work alongside them doing the same kinds of work at a different scale.  *Organization Insight* is about seeing that contribution: who - and what - is doing the work, how much of it there is, and where in the organization it is happening.

The capability is delivered by Egeria's *nanny connectors* - the integration connectors that look after the open metadata ecosystem itself.  The *Simon Contribution Recorder*, supplied in the [Core Content Pack](/content-packs/core-content-pack/overview), recognizes contribution with karma points; the *Lovelace* insight services, orchestrated by the [Babbage Analytical Engine](/features/metadata-observability/overview#the-babbage-analytical-engine-and-the-lovelace-services) and supplied in the `OrganizationInsightContentPack`, profile what the ecosystem holds.  Each of them watches the ecosystem and records what it observes as metadata, so the observations can be queried, published and reported on like anything else.

## Increasing Karma

### Why karma points exist

[Karma points](/concepts/karma-point) recognize actors - both individuals and automation - for their contributions to open metadata: creating information, correcting or enhancing it, linking it together, and removing what is obsolete.

The purpose is recognition rather than measurement for its own sake.  Maintaining an open metadata ecosystem depends on people doing work that benefits colleagues they may never meet, and that work is easy to overlook.  Karma points make it visible, and they support the gamification of contribution - league tables, acknowledgement of the people whose effort keeps the catalog trustworthy.

### How points are awarded

Karma points are awarded by the *Simon Contribution Recorder*, named in recognition of [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon) (1916-2001), whose study of bounded rationality revolutionized how we understand human decision-making.  It is an [integration connector](/concepts/integration-connector) in the *OpenMetadataObservability* [integration group](/concepts/integration-group) of the Core Content Pack, so it runs in the nanny daemon alongside the Pepys Activity Observer, and needs no configuration to start.

When it starts, Simon registers a listener for the events that report changes to open metadata.  From then on:

1. Every change event other than a refresh event earns a karma point.  Simon takes the `updatedBy` user from the version information of the element or relationship that changed, or the `createdBy` user where there is no update user - so the point goes to whoever actually made the change.  Adding, updating or removing a classification updates the element it is attached to, so the point goes to the user that changed the classification.
2. Users whose userIds match one of the patterns in the `ignoredUserIdPatterns` configuration property earn nothing.  The Core Content Pack sets the patterns to `.*npa` and `.*engine`, so that only the contributions of people are recognized - see [People and automation](/concepts/karma-point#people-and-automation).
3. The points are added to an in-memory tally, held per userId.  On each refresh (every 12 minutes by default), Simon adds each user's tally to the `karmaPoints` in their [ContributionRecord](/types/1/0125-Contribution).  So a busy user costs one read and one update per refresh, rather than one for each change they make.
4. **Only users with an [actor profile](/features/people-roles-organizations/overview) earn karma points.**  This is why a [user identity](/types/1/0110-Actors) has to be created and linked to an actor profile for everyone whose contribution you want recognized - a userId that belongs to no profile has nowhere to accumulate a total.  The first time a user earns points, Simon finds their actor profile through their user identity and creates the contribution record if there is not one already.  It then remembers the record, so the profile is only looked up once.

When it writes, Simon reads the `karmaPoints` stored in the contribution record and adds its tally to that value, so a total that has been set by other means is added to rather than overwritten.

| Situation | What happens | Audit log message |
|---|---|---|
| Points recorded | The number of points and users recorded on the refresh is reported. | SIMON-CONTRIBUTION-RECORDER-0003 |
| The user has no actor profile | The points are discarded, and the users are listed. | SIMON-CONTRIBUTION-RECORDER-0006 |
| Simon's user cannot read or change the actor profile or contribution record - for example, because it is in a [governance zone](/features/governance-zoning/overview) that Simon's user cannot update | Retrying would fail in the same way, so the points are discarded. | SIMON-CONTRIBUTION-RECORDER-0005 |
| Any other failure - most likely the metadata access server being unavailable | The points are kept, and tried again on the next refresh. | SIMON-CONTRIBUTION-RECORDER-0004 |
| An `ignoredUserIdPatterns` pattern is not a valid regular expression | The pattern is skipped, and the others still apply. | SIMON-CONTRIBUTION-RECORDER-0007 |

Points still waiting when the connector shuts down are written as it disconnects.  Simon only sees the changes made while it is running, so changes made while the nanny daemon is down earn nothing.  Run Simon in only one nanny daemon for each set of repositories, or each change earns a point once for every copy of Simon that sees it.

!!! info "Content packs earn nothing"
    Loading a content pack reports each element it adds as a change made by the content pack's originator - "Egeria Project" for the content packs supplied with Egeria.  That is not the userId of anyone with an actor profile, so the points are discarded, and you will see them listed by SIMON-CONTRIBUTION-RECORDER-0006 on the first refresh after a content pack is loaded.

### Using the results

Who may see a contribution record is controlled by the [open metadata security](/features/metadata-security/overview) that applies to the actor profile it is attached to, so recognition does not have to mean exposure for those who would rather it did not.

Because the totals are ordinary metadata, they can be queried directly, shown in Egeria's user interfaces, and published as part of the *Organization Observability* family of the [Open Metadata Digital Product Catalog](/patterns/harvest-and-publish/overview) for teams that want to report on contribution over time.

## Enterprise Oracle

--8<-- "snippets/work-in-progress.md"

The Enterprise Oracle will provide insight into the amount and type of activity occurring in different parts of the organization - not just who is contributing, but where the energy in the ecosystem is concentrated, which areas are actively curated and which are quietly going stale.

!!! info "Related information"

    * [Karma point](/concepts/karma-point) - what earns a point and how it is awarded.
    * [Model 0125 Contribution](/types/1/0125-Contribution) - the contribution record and its relationship to the actor profile.
    * [Karma points](/features/people-roles-organizations/overview/#karma-points) - how contribution fits into the wider picture of people, roles and organizations.
    * [Organization Insight Content Pack](/content-packs/organization-insight-content-pack/overview) - the connector definitions that deliver these services.

--8<-- "snippets/abbr.md"
