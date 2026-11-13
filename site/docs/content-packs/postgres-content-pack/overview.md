<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# PostgreSQL Content Pack

The *PostgresContentPack* contains the reference data, templates, connector definitions and governance services for working with [PostgreSQL](https://www.postgresql.org/), an advanced open source relational database.  It lets you describe a PostgreSQL server, its databases and their schemas in open metadata, survey what they contain, and keep their catalog entries up to date as the databases change.  The connectors it configures are supplied in the *omag-server-platform* distribution, in the [postgres-server-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/postgres-server-connectors){ target=gh } module, whose jar file includes the PostgreSQL JDBC driver.

The content pack is found in the `PostgresContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base connector types and the generic database services, and it is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

Working with PostgreSQL starts with a [technology type](/concepts/deployed-implementation-type).  Each technology type in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.  Running a process such as *PostgreSQLServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *PostgreSQLServerCataloguer* integration connector.  From then on, the cataloguer maintains the databases it finds in the server, and hands the cataloguing of each database's schemas, tables and columns to the generic *JDBC Database Cataloguer* supplied by the Core Content Pack.

The server template connects through the server's default `postgres` database (`jdbc:postgresql://{hostIdentifier}:{portNumber}/postgres`), so it needs only the server's name, host, port and secrets store details.  The database templates add the `databaseName`, and the schema and tabular data set templates add `?currentSchema={schemaName}` to the address.

The survey engine gives a one-off, in-depth view of a server or database, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the asset and run the survey in one step, then print the resulting report.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| PostgreSQL Server | A *SoftwareServer* with its *DatabaseManager* capability, endpoint and connection | `PostgreSQLServer::CreateAsCatalogTarget`, `PostgreSQLServer:CreateAndSurvey`, `PostgreSQLServer:DeleteAsset` |
| PostgreSQL Relational Database | A *RelationalDatabase* asset and its connection | `PostgreSQLDatabase::CreateAsCatalogTarget`, `PostgreSQLDatabase:CreateAndSurvey`, `PostgreSQLDatabase:DeleteAsset` |
| PostgreSQL Relational Database Schema | A *DeployedDatabaseSchema* asset and its connection | `PostgreSQLDatabaseSchema::CreateAsCatalogTarget`, `PostgreSQLDatabaseSchema:DeleteAsset` |
| PostgreSQL Tabular Data Set Collection | A *TabularDataSetCollection* for a schema, readable through the [tabular data set connector](/concepts/tabular-data-set-connector) | |
| PostgreSQL Tabular Data Set | A *TabularDataSet* for a single table | |
| PostgreSQL Table | A *DataSet* for a table named in lineage events (OpenLineage names it `postgres://{host}:{port}` + `{database}.{schema}.{table}`) | |
| PostgreSQL database manager (RDBMS) | Describes the database manager capability of a server (no template) | |

The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *PostgreSQLIntegrationGroup* (`Egeria:IntegrationGroup:PostgreSQL`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| PostgreSQLServerIntegrationConnector | `PostgreSQLServerCataloguer` (user `postgrescatnpa`, refreshes every 60 minutes) | Catalogs the databases found in the PostgreSQL Servers attached as catalog targets. |

There is no PostgreSQL-specific database cataloguer.  The `catalog-postgres-database` and `catalog-postgres-schema` request types attach databases and schemas to the *JDBCDatabaseCataloguer* in the Core Content Pack's *DatabaseIntegrationGroup*.

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *PostgreSQLSurvey* - PostgreSQL Survey Engine | `survey-postgres-server` | PostgreSQL Server Survey Service | Surveys the databases, their tables and columns, found in a PostgreSQL server. |
| | `survey-postgres-database` | PostgreSQL Database Survey Service | Surveys the tables and columns found in a PostgreSQL database. |
| *PostgreSQLGovernance* - PostgreSQL Governance Engine | `create-postgres-server`, `create-postgres-database`, `create-postgres-schema` | Create Asset Governance Service | Creates an asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-postgres-server`, `catalog-postgres-database`, `catalog-postgres-schema` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target: the *PostgreSQLServerCataloguer* for a server, the *JDBCDatabaseCataloguer* for a database or schema. |
| | `delete-postgres-server`, `delete-postgres-database`, `delete-postgres-schema` | Delete Asset Governance Service | Deletes an asset that was created by a template. |

The governance engines run in an [engine host](/concepts/engine-host).

## Solution blueprint

The pack's [solution blueprint](/concepts/solution-blueprint) shows the solution components that this pack defines - the cataloguer, the governance action types and the governance action processes - and how they link to the PostgreSQL technology and to the *JDBC Database Cataloguer*.

--8<-- "snippets/blueprints/content-packs/postgresql-content-pack-solution-blueprint-mermaid-graph.md"

## Technology type reports

The technology type reports, taken from Egeria's quickstart, show how the template, governance action processes, integration connector and governance action types are linked to each technology type.

??? info "Technology type report for PostgreSQL Server"
    --8<-- "snippets/technology-types/postgresql-server-technology-report-mermaid-graph.md"

??? info "Technology type report for PostgreSQL Relational Database"
    --8<-- "snippets/technology-types/postgresql-relational-database-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *PostgreSQLServer::CreateAsCatalogTarget* with the server's name, host, port and secrets details to start cataloguing it.

    [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) walks through surveying and cataloguing a server step by step.

--8<-- "snippets/abbr.md"
