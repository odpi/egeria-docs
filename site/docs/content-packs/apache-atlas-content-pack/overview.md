<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Apache Atlas Content Pack

The *ApacheAtlasContentPack* contains the reference data, templates, connector definitions and governance services for working with [Apache Atlas](https://atlas.apache.org).  It lets you describe an Apache Atlas server in open metadata, survey the types and instances it holds, and exchange metadata - glossaries, classifications, data sets and lineage - between Apache Atlas and the open metadata ecosystem.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `ApacheAtlasContentPack.omarchive` file in the `content-packs` directory of the distribution.  Unlike most of the technology content packs, it is not loaded into the quickstart's *active-metadata-store*, so load it yourself when you want to work with Apache Atlas.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base technology types and the generic governance services.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and the connectors are in the [apache-atlas-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors){ target=gh } module.

## How the pieces fit together

Working with an Apache Atlas server starts with its [technology type](/concepts/deployed-implementation-type).  The *Apache Atlas Server* technology type points to a [template](/concepts/template) for creating the server's open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on it.  Running *ApacheAtlasServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *ApacheAtlasExchange* integration connector.  From then on, the connector exchanges metadata with the server.  Which metadata is exchanged, and in which direction, is controlled by the configuration properties of the connector's connection: it can publish glossaries, categories and active terms from the open metadata ecosystem into Apache Atlas, bring Apache Atlas glossaries into open metadata, share the data sets that Apache Atlas has catalogued, and extract the lineage it has captured.

The survey engine gives a one-off view of the server, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The survey measures the server's overall metrics, extracts the types it defines, and profiles the numbers of instances, classifications, labels, business metadata and relationships attached to each type.  The *ApacheAtlasServer:CreateAndSurvey* process creates the asset, runs the survey and prints out the report in one step.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Apache Atlas Server | A *SoftwareServer* (`Apache Atlas Server::~{serverName}~`) with its *Metadata Catalog* (*InventoryCatalog*) capability, endpoint and connection | `ApacheAtlasServer::CreateAsCatalogTarget`, `ApacheAtlasServer:CreateAndSurvey`, `ApacheAtlasServer:DeleteAsset` |

The pack also defines the twelve annotation types used in the survey report.  One, *Apache Atlas Server Metrics*, holds the server's metrics; one, *Apache Atlas Type Analysis*, holds the types extracted from the server; and ten profile the instances of each type, such as *Apache Atlas Attached Classification Types*, *Apache Atlas Attached Labels* and *Apache Atlas End 1 Attached Relationship Types*.  The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *ApacheAtlasIntegrationGroup* (`Egeria:IntegrationGroup:ApacheAtlas`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| ApacheAtlasServerIntegrationConnector | `ApacheAtlasExchange` (user `atlascatnpa`, refreshes every 60 minutes) | Exchanges metadata with the Apache Atlas servers attached as catalog targets. |

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *ApacheAtlasSurvey* - Apache Atlas Survey Engine | `survey-apache-atlas-server` | Apache Atlas Survey Service | Discovers the types, and the number of instances of each, in an Apache Atlas server. |
| *ApacheAtlasGovernance* - Apache Atlas Governance Engine | `create-apache-atlas-server` | Create Asset Governance Service | Creates the server's asset from its template. |
| | `catalog-apache-atlas-server` | Add Catalog Target to Asset Governance Service | Attaches the server's asset to the Apache Atlas integration connector. |
| | `delete-apache-atlas-server` | Delete Asset Governance Service | Deletes the server's asset using the template properties used to create it. |

The governance engines run in an [engine host](/concepts/engine-host).

## Solution blueprint

The graph below shows the solution blueprint shipped in the content pack.  It was generated from an earlier load of the pack, since the quickstart does not load it.

--8<-- "snippets/blueprints/content-packs/apache-atlas-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Make sure an integration daemon is running the *ApacheAtlasIntegrationGroup* and an engine host is running the *ApacheAtlasSurvey* and *ApacheAtlasGovernance* engines.  Then run *ApacheAtlasServer::CreateAsCatalogTarget* with the server's name and connection details to start exchanging metadata with it, or *ApacheAtlasServer:CreateAndSurvey* to survey it.

    [Leveraging Apache Atlas](/egeria-solutions/leveraging-apache-atlas/overview) describes how Egeria works with Apache Atlas.

--8<-- "snippets/abbr.md"
