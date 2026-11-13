<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Lineage Content Pack

The *OpenLineageContentPack* contains the connector definitions and governance services for working with [OpenLineage](https://openlineage.io) events.  It lets Egeria capture the run events published by data pipelines and other processing engines, catalog the jobs and datasets they describe as processes and lineage, generate events of its own whenever governance actions run, and save and distribute both kinds of event.  Analysis services then mine the saved events to profile job runs, refine the data scope of datasets and summarise data quality.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `OpenLineageContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the technology types, the Apache Kafka topic template, the *AssetOnboarding* and *EgeriaGovernance* engines and the *Babbage Analytical Engine*.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and the connectors are in the [openlineage-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors){ target=gh } module.

## How the pieces fit together

The connectors in the *OpenLineageIntegrationGroup* all run in the same [integration daemon](/concepts/integration-daemon), which passes the events between them.  Some of the connectors acquire or create events:

* The *OpenLineageKafkaListener* receives the events published to the Apache Kafka topics attached to it as [catalog targets](/concepts/catalog-target) - typically the [open lineage topic](/concepts/open-lineage-topic) fed by an OpenLineage proxy.
* The *OpenLineageGovernanceActionPublisher* listens for governance actions running in the open metadata ecosystem and generates an event each time one starts, completes, fails or is aborted.

The others process or distribute every event published in the daemon:

* The *OpenLineageCataloguer* catalogs what the events describe: jobs become processes, and the inputs and outputs of each run are linked to them with [lineage](/concepts/lineage) relationships attached to the assets already catalogued by Egeria's technology connectors.  It keeps run metrics in the *RunMetrics* classification of each process.
* The three log stores save the events.  The *OpenLineagePostgresPublisher* stores them, with a digest of their runs, datasets, data quality assertions and tests, in the PostgreSQL database schemas attached as catalog targets, and removes them after a configurable number of days.  The *OpenLineageAPIPublisher* sends them to an OpenLineage-compliant API such as a Marquez server.  The *OpenLineageFilePublisher* writes each event as a JSON file.

The *HarvestOpenLineageEvents::CreateAsCatalogTarget* process creates the asset for an Apache Kafka topic and attaches it to the Kafka listener, which is how event capture is usually set up.

The three *Lovelace* analysis services read the events saved by the PostgreSQL log store.  This pack attaches their governance action types to the *Babbage Analytical Engine* (from the Core Content Pack) as catalog targets, so Babbage runs each of them on every refresh.

!!! note "Where the file publisher is registered"
    The *OpenLineageFilePublisher* connector is defined in this content pack, but the code intends it to be registered with the integration group - and so run - by the separate [Open Lineage File Store Content Pack](/content-packs/open-lineage-file-store-content-pack/overview), because it writes a file for every event and nothing removes them.  The shipped `OpenLineageContentPack.omarchive` nevertheless still contains a registration for it, so loading this pack alone also starts the file publisher.

## Integration connectors

The pack defines the *OpenLineageIntegrationGroup* (`Egeria:IntegrationGroup:OpenLineage`), a dynamic [integration group](/concepts/integration-group).  Every connector refreshes every 60 minutes.

| Connector | Runs as | Purpose |
|---|---|---|
| OpenLineageKafkaListenerIntegrationConnector | `OpenLineageKafkaListener` (user `olkafkainnpa`) | Receives the open lineage events published to the Apache Kafka topics attached as catalog targets. |
| OpenLineageGovernanceActionPublisherIntegrationConnector | `OpenLineageGovernanceActionPublisher` (user `olgapubnpa`) | Publishes open lineage events whenever governance actions run in the open metadata ecosystem. |
| OpenLineageCataloguerIntegrationConnector | `OpenLineageCataloguer` (user `olcatnpa`) | Catalogs the resources, processes and lineage detailed in the open lineage events received by the integration daemon. |
| OpenLineagePostgresPublisherIntegrationConnector | `OpenLineagePostgresPublisher` (user `olpgpubnpa`) | Stores open lineage events, and a digest of their runs, datasets, data quality assertions and tests, in each of the PostgreSQL database schemas (*JDBC Relational Database Schema*) attached as catalog targets. |
| OpenLineageAPIPublisherIntegrationConnector | `OpenLineageAPIPublisher` (user `olapipubnpa`) | Publishes open lineage events to the APIs (*Marquez Server*) attached as catalog targets. |
| OpenLineageFilePublisherIntegrationConnector | `OpenLineageFilePublisher` (user `olfilepubnpa`) | Publishes open lineage events as JSON files to the `logs/openlineage` directory, and to any file system directory attached as a catalog target. |

## Governance services

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *AssetOnboarding* - Asset Onboarding Engine (from the Core Content Pack) | `harvest-open-lineage-topic` | Add Catalog Target to Asset Governance Service | Attaches an Apache Kafka topic asset to the Kafka listener as a catalog target. |
| *EgeriaGovernance* - Egeria Governance Engine (from the Core Content Pack) | `profile-open-lineage-runs` | Lovelace OpenLineage Run Profiler Governance Action Service | Records the run profile of each job - frequency, regularity, duration, failure rate and data volume - in the *RunMetrics* classification of the job. |
| | `refine-open-lineage-data-scope` | Lovelace OpenLineage Data Scope Governance Action Service | Refines the *DataScope* classification of each dataset's asset with its write pattern and data collection window. |
| | `summarise-open-lineage-data-quality` | Lovelace OpenLineage Data Quality Summary Governance Action Service | Summarises the data quality assertions and tests recorded for each dataset (and job) into a survey report, with the pass rate of each quality dimension. |

The governance engines run in an [engine host](/concepts/engine-host).

## Governance action process

| Process | Steps |
|---|---|
| `HarvestOpenLineageEvents::CreateAsCatalogTarget` | `create-kafka-topic` creates the topic's asset from the Core Content Pack's *Apache Kafka Topic* template, then `harvest-open-lineage-topic` attaches it to the *OpenLineageKafkaListener*. |

## Solution blueprint

The solution blueprint shows how the events flow from the Open Lineage topic and the open metadata topic through the listener and the governance action publisher to the cataloguer and the log stores, and how Babbage schedules the Lovelace analysis services.

--8<-- "snippets/blueprints/content-packs/open-lineage-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    The Open Lineage Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart.  For other deployments, load it into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *HarvestOpenLineageEvents::CreateAsCatalogTarget* with the details of the Kafka topic that receives your events, and attach a PostgreSQL database schema to the *OpenLineagePostgresPublisher* to keep them.

    [Leveraging Open Lineage](/egeria-solutions/leveraging-open-lineage/overview) describes how to capture and use open lineage events with Egeria.

--8<-- "snippets/abbr.md"
