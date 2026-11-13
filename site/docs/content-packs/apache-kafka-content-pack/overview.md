<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Apache Kafka Content Pack

The *ApacheKafkaContentPack* contains the reference data, templates, connector definitions and governance services for working with [Apache Kafka](https://kafka.apache.org/).  It lets you describe an Apache Kafka server (broker) in open metadata, survey the topics it manages, and keep a catalog of its topics up to date as they are created and removed.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `ApacheKafkaContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base technology types, the generic governance services and the *Apache Kafka Topic* technology type and template.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and the connectors are in the [apache-kafka-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors){ target=gh } module.

## How the pieces fit together

Working with an Apache Kafka server starts with its [technology type](/concepts/deployed-implementation-type).  The *Apache Kafka Server* technology type points to a [template](/concepts/template) for creating the server's open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on it.  Running *ApacheKafkaServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *ApacheKafkaCataloguer* integration connector.  From then on, on each refresh the cataloguer creates a *Topic* asset for each new topic known to the server, from the Core Content Pack's *Apache Kafka Topic* template (or a template named in its `templateName` configuration property), and links it to the server's event broker capability with *CapabilityAssetUse*.  When a topic disappears from the server, the cataloguer removes that link, logging that the topic was deleted, but leaves the topic's asset in place.

The survey engine gives a one-off view of the topics a server manages, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *ApacheKafkaServer:CreateAndSurvey* process creates the asset and runs the survey in one step.

Individual topics are described by the *Apache Kafka Topic* technology type and template in the Core Content Pack, which also supplies the `create-kafka-topic` and `delete-kafka-topic` request types and the *ApacheKafkaTopic:DeleteAsset* process.  The [Open Lineage Content Pack](/content-packs/open-lineage-content-pack/overview) uses them to attach a topic to its Kafka listener.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Apache Kafka Server | A *SoftwareServer* (`Apache Kafka Server::~{serverName}~`) with its *EventBroker* capability, endpoint and connection | `ApacheKafkaServer::CreateAsCatalogTarget`, `ApacheKafkaServer:CreateAndSurvey`, `ApacheKafkaServer:DeleteAsset` |
| Apache Kafka Event Broker | Describes the event broker capability of a server (no template) | |
| Apache Kafka Topic (from the Core Content Pack) | A *Topic* (`Topic::~{serverName}~.~{fullTopicName}~::inOut`) | `ApacheKafkaTopic:DeleteAsset` (Core Content Pack), `HarvestOpenLineageEvents::CreateAsCatalogTarget` (Open Lineage Content Pack) |

The pack also defines two annotation types for the survey report: *Apache Kafka Topic List* and *Apache Kafka Topic Inventory*.  The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *ApacheKafkaIntegrationGroup* (`Egeria:IntegrationGroup:ApacheKafka`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| KafkaTopicIntegrationConnector | `ApacheKafkaCataloguer` (user `kafkacatnpa`, refreshes every 60 minutes) | Catalogs the topics found in the Apache Kafka servers attached as catalog targets. |

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *ApacheKafkaSurvey* - Apache Kafka Survey Engine | `survey-kafka-server` | Apache Kafka Server Survey Service | Connects to a server (broker) and creates a survey report listing the topics it manages. |
| *ApacheKafkaGovernance* - Apache Kafka Governance Engine | `create-apache-kafka-server` | Create Asset Governance Service | Creates the server's asset from its template. |
| | `catalog-apache-kafka-server` | Add Catalog Target to Asset Governance Service | Attaches the server's asset to the Apache Kafka cataloguer. |
| | `delete-apache-kafka-server` | Delete Asset Governance Service | Deletes the server's asset using the template properties used to create it. |

The governance engines run in an [engine host](/concepts/engine-host).

## Graphs

The solution blueprint for the content pack shows the cataloguer, the governance action types and processes, and the technologies they work with.

--8<-- "snippets/blueprints/content-packs/apache-kafka-content-pack-solution-blueprint-mermaid-graph.md"

The technology type reports below, taken from Egeria's quickstart, show how the templates, governance action processes, integration connectors and governance action types are linked to each technology type.

??? info "Technology type report for Apache Kafka Server"
    --8<-- "snippets/technology-types/apache-kafka-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Apache Kafka Topic"
    --8<-- "snippets/technology-types/apache-kafka-topic-technology-report-mermaid-graph.md"

!!! summary "Usage"
    The Apache Kafka Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart.  For other deployments, load it into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *ApacheKafkaServer::CreateAsCatalogTarget* with the server's name and network address to start cataloguing its topics.

    [Leveraging Apache Kafka](/egeria-solutions/leveraging-apache-kafka/overview) walks through surveying and cataloguing an Apache Kafka server.

--8<-- "snippets/abbr.md"
