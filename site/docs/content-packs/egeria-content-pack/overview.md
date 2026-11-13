<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria Content Pack

The *EgeriaContentPack* lets Egeria catalog and monitor its own infrastructure.  It supplies templates for describing [OMAG Server Platforms](/concepts/omag-server-platform) and the [OMAG Servers](/concepts/omag-server) they host, technology types for each of Egeria's services, and an integration connector that keeps the catalog entries for running platforms and their servers up to date.  This gives a good starting point for understanding the structure and status of an Egeria deployment.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `EgeriaContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base technology types, the *EgeriaGovernance* engine and the generic create, catalog and delete governance services.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

An OMAG Server Platform is described by a *SoftwareServerPlatform* asset created from the *OMAG Server Platform* template.  The `create-omag-server-platform` request type creates it, and `catalog-omag-server-platform` attaches it as a [catalog target](/concepts/catalog-target) of the *OMAGServerPlatformCataloguer* integration connector.  The cataloguer also catalogs, without being asked, the platform that it is calling to retrieve metadata.  On each refresh it asks each platform for the servers it is running, and maintains a *SoftwareServer* asset for each one using the server templates in this pack.  The services configured in each server are recorded as *SoftwareService* elements, typed with the technology types listed below and linked to the server with *SupportedSoftwareCapability*, and the connectors the services use are recorded as *DeployedConnector* elements.  The connector is described in the [egeria-system-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/egeria-system-connectors){ target=gh } module.  While it works, the cataloguer can raise the exceptions defined in the Core Content Pack, such as *Clear Text Password Exception* when a platform user account has a clear text password, or *Missing User Identity Exception* when an account has no matching *UserIdentity*.

## Technology types and templates

The base technology types for Egeria's runtime - *OMAG Server Platform*, *Metadata Access Store*, *View Server*, *Integration Daemon*, *Engine Host* and so on - are defined in the Core Content Pack.  This pack links them to their templates:

| Technology type | Template creates | Qualified name |
|---|---|---|
| OMAG Server Platform | A *SoftwareServerPlatform* with its *User Token Manager* (*UserAuthenticationManager*) capability, endpoint and connection | `OMAG Server Platform::~{platformURLRoot}~::~{platformName}~` |
| Metadata Access Server | A *SoftwareServer* with its *Open Metadata Repository Access APIs* capability, endpoint and connection | `Metadata Access Server::~{platformURLRoot}~::~{serverName}~` |
| View Server | A *SoftwareServer* with its *Open Metadata and Governance End User APIs* capability | `View Server::~{platformURLRoot}~::~{serverName}~` |
| Integration Daemon | A *SoftwareServer* with its *Integration Connector Status APIs* capability | `Integration Daemon::~{platformURLRoot}~::~{serverName}~` |
| Engine Host | A *SoftwareServer* with its *Governance Engine Status APIs* capability | `Engine Host::~{platformURLRoot}~::~{serverName}~` |

The templates are described further in the [Template Catalog](/catalog-templates).

The pack also adds 55 technology types of the form *SoftwareService*, one for each of Egeria's services.  They cover the platform services (*Administration Services*, *Platform Operational Services*, *Server Operations*), the framework and repository services (*Open Metadata Repository Services (OMRS)*, *Open Metadata Store Services*, *Open Governance Framework Services*, *Connected Asset Services*, *Open Metadata Security Services*, *Conformance Suite Services*), the server services (*Integration Daemon Services*, *Engine Host Services* and the *Governance Action*, *Survey Action*, *Watchdog Action* and *Repository Governance* OMES), and the view services, from *Action Author API* to *Valid Metadata API*.

## Integration connectors

The pack defines the *EgeriaIntegrationGroup* (`Egeria:IntegrationGroup:Egeria`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| OMAGServerPlatformIntegrationConnector | `OMAGServerPlatformCataloguer` (user `omagspcatnpa`, refreshes every 60 minutes) | Catalogs the OMAG Servers known to the OMAG Server Platforms attached as catalog targets. |

## Governance engines

The request types for OMAG Server Platforms are added to the *EgeriaGovernance* engine defined in the Core Content Pack.

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *EgeriaGovernance* - Egeria Governance Engine | `create-omag-server-platform` | Create Asset Governance Service | Creates an asset for the platform from its template. |
| | `catalog-omag-server-platform` | Add Catalog Target to Asset Governance Service | Attaches the platform's asset to the OMAG Server Platform cataloguer. |
| | `delete-omag-server-platform` | Delete Asset Governance Service | Deletes the platform's asset using the template properties used to create it. |
| *EgeriaSurvey* - Egeria Survey Engine | (none) | | Defined for specialist surveys of Egeria's platforms and servers, but no survey services are registered with it in this release. |

The governance engines run in an [engine host](/concepts/engine-host).

## Graphs

The solution blueprint for the content pack shows the OMAG Server Platform cataloguer and the governance action types that set it up.

--8<-- "snippets/blueprints/content-packs/egeria-content-pack-solution-blueprint-mermaid-graph.md"

The technology type report for *OMAG Server Platform*, taken from Egeria's quickstart, shows how the template, integration connector and governance action types are linked to the technology type.

??? info "Technology type report for OMAG Server Platform"
    --8<-- "snippets/technology-types/omag-server-platform-technology-report-mermaid-graph.md"

!!! summary "Usage"
    The Egeria Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart.  For other deployments, load it into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run the `create-omag-server-platform` and `catalog-omag-server-platform` governance action types with the platform's URL root and name to start cataloguing it.

    [Leveraging Egeria](/egeria-solutions/leveraging-egeria/overview) shows how to use this content to catalog your Egeria deployment.

--8<-- "snippets/abbr.md"
