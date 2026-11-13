<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Db2 for Linux, UNIX and Windows Content Pack

The *DB2LUWContentPack* contains the reference data, templates, connector definitions and governance services for working with IBM Db2 for Linux, UNIX and Windows (LUW, formerly Db2 UDB).  It lets you describe a Db2 server, its databases and their schemas in open metadata, survey what they contain, and keep their catalog entries up to date as the databases change.  Db2 for z/OS has a different system catalog and is not covered.  The connectors it configures are supplied in the *omag-server-platform* distribution, in the [db2luw-server-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/db2luw-server-connectors){ target=gh } module, whose jar file includes the IBM Data Server Driver for JDBC and SQLJ (`jcc`).

The content pack is found in the `DB2LUWContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base connector types and the generic database services, and it is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

Working with Db2 starts with a [technology type](/concepts/deployed-implementation-type).  Each technology type in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.  Running a process such as *DB2LUWServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *DB2LUWServerCataloguer* integration connector.  From then on, the cataloguer maintains the databases it finds in the server, and hands the cataloguing of each database's schemas, tables and columns to the generic *JDBC Database Cataloguer* supplied by the Core Content Pack.

All of the templates build a JDBC address of the form `jdbc:db2://{hostIdentifier}:{portNumber}/{databaseName}`.  A Db2 JDBC connection is always made to a database, so the server template also asks for a `databaseName` to connect through, alongside the host, port and secrets store details.

The survey engine gives a one-off, in-depth view of a server or database, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the asset and run the survey in one step, then print the resulting report.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Db2 for Linux, UNIX and Windows Database Server | A *SoftwareServer* with its *DatabaseManager* capability, endpoint and connection | `DB2LUWServer::CreateAsCatalogTarget`, `DB2LUWServer:CreateAndSurvey`, `DB2LUWServer:DeleteAsset` |
| Db2 for Linux, UNIX and Windows Relational Database | A *RelationalDatabase* asset and its connection | `DB2LUWDatabase::CreateAsCatalogTarget`, `DB2LUWDatabase:CreateAndSurvey`, `DB2LUWDatabase:DeleteAsset` |
| Db2 for Linux, UNIX and Windows Relational Database Schema | A *DeployedDatabaseSchema* asset and its connection | `DB2LUWDatabaseSchema::CreateAsCatalogTarget`, `DB2LUWDatabaseSchema:DeleteAsset` |
| Db2 for Linux, UNIX and Windows Tabular Data Set Collection | A *TabularDataSetCollection* for a schema, readable through the [tabular data set connector](/concepts/tabular-data-set-connector) | |
| Db2 for Linux, UNIX and Windows Tabular Data Set | A *TabularDataSet* for a single table | |
| Db2 Table | A *DataSet* for a table named in lineage events (OpenLineage names it `db2://{host}:{port}` + `{database}.{schema}.{table}`) | |
| Db2 for Linux, UNIX and Windows database manager (RDBMS) | Describes the database manager capability of a server (no template) | |

The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *DB2LUWIntegrationGroup* (`Egeria:IntegrationGroup:DB2LUW`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| DB2LUWServerIntegrationConnector | `DB2LUWServerCataloguer` (user `db2luwcatnpa`, refreshes every 60 minutes) | Catalogs the databases found in the Db2 for Linux, UNIX and Windows Servers attached as catalog targets. |

There is no Db2-specific database cataloguer.  The `catalog-db2luw-database` and `catalog-db2luw-schema` request types attach databases and schemas to the *JDBCDatabaseCataloguer* in the Core Content Pack's *DatabaseIntegrationGroup*.

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *DB2LUWSurvey* - Db2 for Linux, UNIX and Windows Server Survey Engine | `survey-db2luw-server` | Db2 for Linux, UNIX and Windows Server Survey Service | Surveys the databases, their tables and columns, found in a Db2 server. |
| | `survey-db2luw-database` | Db2 for Linux, UNIX and Windows Database Survey Service | Surveys the tables and columns found in a Db2 database. |
| *DB2LUWGovernance* - Db2 for Linux, UNIX and Windows Server Governance Engine | `create-db2luw-server`, `create-db2luw-database`, `create-db2luw-schema` | Create Asset Governance Service | Creates an asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-db2luw-server`, `catalog-db2luw-database`, `catalog-db2luw-schema` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target: the *DB2LUWServerCataloguer* for a server, the *JDBCDatabaseCataloguer* for a database or schema. |
| | `delete-db2luw-server`, `delete-db2luw-database`, `delete-db2luw-schema` | Delete Asset Governance Service | Deletes an asset that was created by a template. |

The governance engines run in an [engine host](/concepts/engine-host).

## Technology type reports

The technology type reports, taken from Egeria's quickstart, show how the template, governance action processes, integration connector and governance action types are linked to each technology type.

??? info "Technology type report for Db2 for Linux, UNIX and Windows Database Server"
    --8<-- "snippets/technology-types/db2-for-linux-unix-and-windows-database-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Db2 for Linux, UNIX and Windows Relational Database"
    --8<-- "snippets/technology-types/db2-for-linux-unix-and-windows-relational-database-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *DB2LUWServer::CreateAsCatalogTarget* with the server's name, host, port, a database to connect through (`databaseName`) and secrets details to start cataloguing it.

    [Leveraging your Db2 for Linux, UNIX and Windows estate](/egeria-solutions/leveraging-db2luw/overview) walks through surveying and cataloguing a server step by step.

--8<-- "snippets/abbr.md"
