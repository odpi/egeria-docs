<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Unity Catalog Content Pack

The *UnityCatalogContentPack* contains the reference data, templates, connector definitions and governance services for working with [Unity Catalog](https://www.unitycatalog.io/) (UC).  Unity Catalog is an operational data platform "catalog of catalogs": each catalog holds schemas, and each schema holds tables, volumes (folders of files), functions and registered models, giving every resource a three-part name *catalogName.schemaName.resourceName*.  This pack lets you describe Unity Catalog servers and their contents in open metadata, survey them, keep open metadata and Unity Catalog synchronized in both directions, and provision new resources into Unity Catalog from open metadata.  The connectors it configures are supplied in the *omag-server-platform* distribution, in the [unity-catalog-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/unity-catalog-connectors){ target=gh } module, and work with the open source (OSS) version of Unity Catalog.

The content pack is found in the `UnityCatalogContentPack.omarchive` file in the `content-packs` directory of the distribution.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and depends on two other content packs, which must be loaded first:

* The [Core Content Pack](/content-packs/core-content-pack/overview) supplies the base connector types and the generic governance services that create, catalog and delete assets.
* The [Files Content Pack](/content-packs/files-content-pack/overview) supplies the file reference data and the folder survey annotation types.  A Unity Catalog volume, and the storage location of a table, are folders of files, and the volume survey reuses Egeria's folder survey service, so it produces the file annotations (file counts, file extensions, file types, missing file reference data and so on) that the Files Content Pack defines.

## How the pieces fit together

Working with Unity Catalog starts with a [technology type](/concepts/deployed-implementation-type).  Each technology type in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.

**Cataloguing.**  Running *UnityCatalogServer::CreateAsCatalogTarget* creates the server's asset from its template (a *SoftwareServer* with a *Unity Catalog REST API* capability, an endpoint at `{hostURL}:{portNumber}` and a connection) and attaches it as a [catalog target](/concepts/catalog-target) of the *UnityCatalogServerSynchronizer* integration connector.  This connector maintains the open metadata description of the catalogs it finds in the server, and hands the contents of each catalog to the *UnityCatalogInsideCatalogSynchronizer*, which exchanges the schemas, tables, volumes, functions and registered models in that catalog with the open metadata ecosystem.  Elements that originate in Unity Catalog are kept in step with Unity Catalog; elements that originate in open metadata are kept in step in the other direction.  The connectors' work is scoped by the [metadata collection](/concepts/metadata-collection) that represents the Unity Catalog server.

**Provisioning.**  The five *Provision* processes create a new catalog, schema, volume, table or function element from its template in the Unity Catalog server's metadata collection.  The integration connectors pick it up on their next refresh and create the matching resource in Unity Catalog.  New catalogs linked to a Unity Catalog server's metadata element are provisioned in the same way.

**Surveying.**  The survey engine gives a one-off, in-depth view of a server, catalog, schema or volume, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the server's asset and run the server survey in one step, then print the resulting report.

**Databricks.**  The pack also has a technology type and template for a *Databricks Unity Catalog Server*, whose template adds secrets store details for the connection.  Its processes reuse the OSS Unity Catalog services: `catalog-unity-catalog-server` attaches it to the same *UnityCatalogServerSynchronizer*, and `survey-unity-catalog-server` surveys it.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Unity Catalog Server | A *SoftwareServer* with its *Unity Catalog REST API* capability (*APIManager*), endpoint and connection | `UnityCatalogServer::CreateAsCatalogTarget`, `UnityCatalogServer:CreateAndSurvey`, `UnityCatalogServer:DeleteAsset` |
| Databricks Unity Catalog Server | A *SoftwareServer* with its *Databricks Unity Catalog REST API* capability, endpoint, connection and secrets store connection | `DatabricksUnityCatalogServer::CreateAsCatalogTarget`, `DatabricksUnityCatalogServer:CreateAndSurvey`, `DatabricksUnityCatalogServer:DeleteAsset` |
| Unity Catalog Catalog | A *Namespace* for a catalog | Provision Governance Action Process for UnityCatalogCatalog |
| Unity Catalog Schema | A *DeployedDatabaseSchema* for a schema | Provision Governance Action Process for UnityCatalogSchema |
| Unity Catalog Table | A *VirtualRelationalTable*, with a *DataFolder* for its storage location; a second template creates a table named in lineage events from its `namespacePath` and `resourceName` | Provision Governance Action Process for UnityCatalogTable |
| Unity Catalog Volume | A *DataFolder* whose connection points at the volume's local storage location | Provision Governance Action Process for UnityCatalogVolume |
| Unity Catalog Function | A *DeployedAPI* for a function | Provision Governance Action Process for UnityCatalogFunction |
| Unity Catalog Registered Model | A *DeployedAnalyticsModel* for a registered model | |
| Unity Catalog Registered Model Version | An *AnalyticsModelRun* for one version of a registered model | |

The templates for resources inside Unity Catalog are keyed on the server's network address and the resource's three-part name, for example `Unity Catalog Table::{serverNetworkAddress}::{ucCatalogName}.{ucSchemaName}.{ucTableName}`.  The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *UnityCatalogIntegrationGroup* (`Egeria:IntegrationGroup:UnityCatalog`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).  Both connectors are registered in it.

| Connector | Runs as | Purpose |
|---|---|---|
| UnityCatalogServerIntegrationConnector | `UnityCatalogServerSynchronizer` (user `ucservernpa`, refreshes every 60 minutes) | Synchronizes the catalogs found in the Unity Catalog servers attached as catalog targets, and hands the contents of each catalog to the inside catalog synchronizer. |
| UnityCatalogAssetExchange | `UnityCatalogInsideCatalogSynchronizer` (user `uccatcatnpa`, refreshes every 60 minutes) | Exchanges the schemas, tables, volumes, functions and registered models found in a Unity Catalog catalog with the open metadata ecosystem. |

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *UnityCatalogSurvey* - Unity Catalog Survey Engine | `survey-unity-catalog-server` | OSS Unity Catalog Server Survey Service | Surveys the catalogs found in a Unity Catalog server. |
| | `survey-unity-catalog-catalog` | OSS Unity Catalog Inside Catalog Survey Service | Surveys the schemas and data resources in a catalog. |
| | `survey-unity-catalog-schema` | OSS Unity Catalog Inside Schema Survey Service | Surveys the tables, functions and volumes in a schema. |
| | `survey-unity-catalog-volume` | Unity Catalog Volume Folder (directory) Survey Service | Surveys the files in a volume's directory and the directories beneath it, using the folder survey service. |
| *UnityCatalogGovernance* - Unity Catalog Governance Engine | `create-unity-catalog-server`, `create-databricks-unity-catalog-server` | Create Asset Governance Service | Creates the server's asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-unity-catalog-server` | Add Catalog Target to Asset Governance Service | Attaches a server's asset to the *UnityCatalogServerSynchronizer* as a catalog target. |
| | `delete-unity-catalog-server`, `delete-databricks-unity-catalog-server` | Delete Asset Governance Service | Deletes a server's asset that was created by a template. |
| | `provision-unity-catalog-resource` | Provision Unity Catalog Resources | Creates a catalog, schema, volume, table or function element from its template, ready for the integration connectors to add it to Unity Catalog. |

The survey services record their findings with the annotation types this pack adds to the valid metadata values: summary metrics for a server, catalog, schema, table and column, the list of catalogs in a server, the table sizes in a catalog, and a log of the resources found.  The governance engines run in an [engine host](/concepts/engine-host).

## Solution blueprint

The pack's [solution blueprint](/concepts/solution-blueprint) shows the solution components that this pack defines - the two synchronizers, the governance action types and the governance action processes - and how they link to the Unity Catalog technology.

--8<-- "snippets/blueprints/content-packs/unity-catalog-content-pack-solution-blueprint-mermaid-graph.md"

## Technology type report

The technology type report for *Unity Catalog Server*, taken from Egeria's quickstart, shows how the templates, governance action processes, integration connectors and governance action types are linked to the technology type.

??? info "Technology type report for Unity Catalog Server"
    --8<-- "snippets/technology-types/unity-catalog-server-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load the Core and Files content packs, then this one, into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add them to the server's start-up archives.  Then run *UnityCatalogServer::CreateAsCatalogTarget* with the server's name, host URL and port to start synchronizing it.

    [Leveraging your Unity Catalog estate](/egeria-solutions/leveraging-unity-catalog/overview) explains the Unity Catalog model, the synchronization and the provisioning in more detail.

--8<-- "snippets/abbr.md"
