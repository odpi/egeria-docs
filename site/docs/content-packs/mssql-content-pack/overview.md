<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Microsoft SQL Server Content Pack

The *MSSQLContentPack* contains the reference data, templates, connector definitions and governance services for working with Microsoft SQL Server.  It lets you describe a SQL Server, its databases and their schemas in open metadata, survey what they contain, and keep their catalog entries up to date as the databases change.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `MSSQLContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base connector types and the generic database services, and it is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

Working with a SQL Server starts with a [technology type](/concepts/deployed-implementation-type).  Each technology type in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.  Running a process such as *MSSQLServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *MSSQLServerCataloguer* integration connector.  From then on, the cataloguer maintains the databases it finds in the server, and hands the cataloguing of each database's schemas, tables and columns to the generic *JDBCDatabaseCataloguer* in the *DatabaseIntegrationGroup*, which is supplied by the Core Content Pack.

The survey engine gives a one-off, in-depth view of a server or database, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the asset and run the survey in one step.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Microsoft SQL Server | A *SoftwareServer* with its *DatabaseManager* capability, endpoint and connection | `MSSQLServer::CreateAsCatalogTarget`, `MSSQLServer:CreateAndSurvey`, `MSSQLServer:DeleteAsset` |
| Microsoft SQL Server Relational Database | A *RelationalDatabase* asset and its connection | `MSSQLDatabase::CreateAsCatalogTarget`, `MSSQLDatabase:CreateAndSurvey`, `MSSQLDatabase:DeleteAsset` |
| Microsoft SQL Server Relational Database Schema | A *DeployedDatabaseSchema* asset and its connection | `MSSQLDatabaseSchema::CreateAsCatalogTarget`, `MSSQLDatabaseSchema:DeleteAsset` |
| Microsoft SQL Server Tabular Data Set Collection | A *TabularDataSetCollection* for a schema, readable through the [tabular data set connector](/concepts/tabular-data-set-connector) | |
| Microsoft SQL Server Tabular Data Set | A *TabularDataSet* for a single table | |
| Microsoft SQL Server Table | A *DataSet* for a table named in lineage events (OpenLineage names it `mssql://{host}:{port}` + `{database}.{schema}.{table}`) | |
| Microsoft SQL Server database manager (RDBMS) | Describes the database manager capability of a server (no template) | |

The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *MSSQLIntegrationGroup* (`Egeria:IntegrationGroup:MSSQL`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| MSSQLServerIntegrationConnector | `MSSQLServerCataloguer` (user `mssqlcatnpa`, refreshes every 60 minutes) | Catalogs the databases found in the Microsoft SQL Servers attached as catalog targets. |

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *MSSQLSurvey* - Microsoft SQL Server Survey Engine | `survey-mssql-server` | Microsoft SQL Server Survey Service | Surveys the databases, their tables and columns, found in a server. |
| | `survey-mssql-database` | Microsoft SQL Server Database Survey Service | Surveys the tables and columns found in a database. |
| *MSSQLGovernance* - Microsoft SQL Server Governance Engine | `create-mssql-server`, `create-mssql-database`, `create-mssql-schema` | Create Asset Governance Service | Creates an asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-mssql-server`, `catalog-mssql-database`, `catalog-mssql-schema` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target. |
| | `delete-mssql-server`, `delete-mssql-database`, `delete-mssql-schema` | Delete Asset Governance Service | Deletes an asset that was created by a template. |

The governance engines run in an [engine host](/concepts/engine-host).

## Technology type report

The technology type report for *Microsoft SQL Server*, taken from Egeria's quickstart, shows how the template, governance action processes, integration connector and governance action types are linked to the technology type.

??? info "Technology type report for Microsoft SQL Server"
    --8<-- "snippets/technology-types/microsoft-sql-server-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *MSSQLServer::CreateAsCatalogTarget* with the server's name, host, port and secrets details to start cataloguing it.

    [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview) walks through surveying and cataloguing a server step by step.

--8<-- "snippets/abbr.md"
