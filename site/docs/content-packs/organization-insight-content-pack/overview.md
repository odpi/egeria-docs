<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Organization Insight Content Pack

The *OrganizationInsightContentPack* supplies the *Lovelace* insight services that analyze what the open metadata ecosystem holds and record what they find as metadata.  At present it supplies one service, the *zone membership profiler*, which counts the elements of each type in each [governance zone](/concepts/governance-zone).  The services are supplied in the *omag-server-platform* distribution.

The content pack is found in the `OrganizationInsightContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the *Babbage Analytical Engine* integration connector, the *EgeriaGovernance* governance engine that the services are registered with, and the content pack's folders.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

The services follow the [Metadata Insight](/patterns/metadata-insight/overview) pattern, and are two of Egeria's *nanny* components - the components that look after the open metadata ecosystem itself:

* The *Babbage Analytical Engine* is named after [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage), who designed the Analytical Engine.  It is an [integration connector](/concepts/integration-connector) (`BabbageAnalyticalEngine`, user `babbagenpa`) in the *BabbageIntegrationGroup* (`Egeria:IntegrationGroup:Babbage`), and is defined in the Core Content Pack.  Its [catalog targets](/concepts/catalog-target) are [governance action types](/concepts/governance-action-type).
* The *Lovelace services* are named after [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace), who wrote the first programs for Babbage's Analytical Engine.  Each one is a [governance service](/concepts/governance-service) registered with a governance engine under its own request type, and a governance action type that calls it.

This content pack registers its service with the *EgeriaGovernance* engine, and attaches the service's governance action type to Babbage as a catalog target.  On each refresh (once a day by default), Babbage checks each of its catalog targets in turn.  If there is already an engine action for the governance action type that is requested, waiting or running, Babbage moves on; otherwise it initiates the governance action type.  So a short-running [governance action service](/concepts/governance-action-service), such as the zone membership profiler, runs once per Babbage refresh, while a long-running [watchdog action service](/concepts/watchdog-action-service) would be started once and restarted if it ever stopped.  The governance engine runs in an [engine host](/concepts/engine-host).

A Lovelace service can also be run on its own by initiating its governance action type.  Other content packs add their own Lovelace services in the same way: the Core Content Pack adds *Build Member Popularity Profile*, and the [Open Lineage Content Pack](/content-packs/open-lineage-content-pack/overview) adds three services that analyze OpenLineage logs.

## Lovelace services

| Governance action type | Babbage catalog target | Request type (engine) | Governance service | What it does |
|---|---|---|---|---|
| `EgeriaGovernance::build-zone-membership-profile` | *Build Zone Membership Profile* | `build-zone-membership-profile` (*EgeriaGovernance*) | Lovelace Zone Membership Profiler Governance Action Service (`zone-membership-profile-governance-service`) | Counts the elements that are members of each governance zone, by type, and stores the counts in the zone's *ZoneMembershipProfile* classification (see [model 0424](/types/4/0424-Governance-Zones)). |

The zone membership profiler keeps three views of each zone: the anchor elements whose *ZoneMembership* classification names the zone (`totalMembership`, `typeMembership`), the elements that are members because their anchor is in the zone (`anchoredTotalMembership`, `anchoredTypeMembership`), and the two combined (`allTotalMembership`, `allTypeMembership`).  The time of the analysis is recorded in `analysisTime`.  The service has no request parameters or action targets, and produces the `service-completed` or `service-failed` guard.

!!! info "Karma points"
    Karma points used to be awarded by a Lovelace watchdog action service supplied in this content pack.  From release 6.3 they are awarded by the *Simon Contribution Recorder* integration connector, which is supplied in the Core Content Pack and described in [Organization Insight](/egeria-solutions/organization-insight/overview).

## Solution blueprint

The solution blueprint for the content pack, taken from Egeria's quickstart, shows Babbage scheduling the Lovelace service.

--8<-- "snippets/blueprints/content-packs/organization-insight-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives, alongside the Core Content Pack.  The zone membership profile of each governance zone is then refreshed each time Babbage runs.

    [Organization Insight](/egeria-solutions/organization-insight/overview) describes how contribution and activity in the open metadata ecosystem are observed, and [Metadata Observability](/features/metadata-observability/overview#the-babbage-analytical-engine-and-the-lovelace-services) describes Babbage and all of the Lovelace services.

--8<-- "snippets/abbr.md"
