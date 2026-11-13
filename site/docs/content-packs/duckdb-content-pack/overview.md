<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# DuckDB Content Pack

The *DuckDBContentPack* contains the reference data, templates, connector definitions and governance services for working with [DuckDB](https://duckdb.org/) databases.  It lets you describe a DuckDB database and its schemas in open metadata, survey what they contain - including the other data sources the database federates - and keep their catalog entries up to date as the database changes.  The connectors it configures are supplied in the *omag-server-platform* distribution, in the [duckdb-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/duckdb-connectors){ target=gh } module, whose jar file includes the DuckDB JDBC driver.

The content pack is found in the `DuckDBContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base connector types and the generic database services, and it is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How DuckDB differs from the other database packs

DuckDB is an embedded, in-process database engine.  A DuckDB database is either a single `.duckdb` file on disk, or an in-memory session (`:memory:`), opened directly through the DuckDB JDBC driver.  There is no database server to connect to, so this pack is *database-tier only*:

* There is no server technology type, server template or server survey.  The pack starts at the *DuckDB Relational Database*.
* The templates are keyed on the database's file path rather than on a server name, host and port.  Both templates take a `databasePath` placeholder (the path to the `.duckdb` file, or `:memory:`), and build the JDBC address `jdbc:duckdb:{databasePath}`.  The qualified names follow the same pattern - for example `DuckDB Relational Database::{databasePath}` - while the display name comes from `databaseName`.
* There are no tabular data set, tabular data set collection or lineage table technology types.

## How the pieces fit together

Each [technology type](/concepts/deployed-implementation-type) in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.  Running *DuckDBDatabase::CreateAsCatalogTarget* creates the database's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *DuckDBDatabaseCataloguer* integration connector.  This connector maintains the database's asset, and hands the cataloguing of its native schemas, tables and columns to the generic *JDBC Database Cataloguer* supplied by the Core Content Pack (configured through its `DuckDBFriendshipGUID` configuration property).

The survey engine gives a one-off, in-depth view of a database, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  *DuckDBDatabase:CreateAndSurvey* creates the asset and runs the survey in one step, then prints the resulting report.

### Federated data sources

DuckDB can query other data sources as if they were local tables, in two ways:

* **Attached databases** - the `ATTACH` statement opens another database (another DuckDB file, a SQLite file, or a remote PostgreSQL or MySQL database).  These are found through DuckDB's `duckdb_databases()` function.
* **External file scans** - views that use functions such as `read_parquet()`, `read_csv()`, `read_json()`, `iceberg_scan()` or `delta_scan()` read files in local storage or an object store without importing them.  These are found by scanning the view definitions returned by `duckdb_views()`.

The DuckDB connectors discover both.  The survey service records them using two annotation types that this pack adds to the valid metadata values:

| Annotation type | Records |
|---|---|
| Capture Attached Data Source | A data source attached to the DuckDB database with its `ATTACH` federation capability. |
| Capture External File Data Source | An external file, or object-store resource, that is scanned by a view defined in the DuckDB database. |

The integration connector catalogs the same findings as resource list relationships from the DuckDB database's asset to the asset for each attached database or external file, reusing an existing asset where it can find one and creating one where it cannot.  Credentials embedded in an `ATTACH` connection string are redacted before they are stored.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| DuckDB Relational Database | A *RelationalDatabase* asset for the database file, with its endpoint and connection | `DuckDBDatabase::CreateAsCatalogTarget`, `DuckDBDatabase:CreateAndSurvey`, `DuckDBDatabase:DeleteAsset` |
| DuckDB Relational Database Schema | A *DeployedDatabaseSchema* asset and its connection | `DuckDBDatabaseSchema::CreateAsCatalogTarget`, `DuckDBDatabaseSchema:DeleteAsset` |

The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *DuckDBIntegrationGroup* (`Egeria:IntegrationGroup:DuckDB`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| DuckDBDatabaseIntegrationConnector | `DuckDBDatabaseCataloguer` (user `duckdbcatnpa`, refreshes every 60 minutes) | Catalogs the DuckDB databases attached as catalog targets, along with their attached and external file data sources. |

The `catalog-duckdb-schema` request type attaches a schema directly to the *JDBCDatabaseCataloguer* in the Core Content Pack's *DatabaseIntegrationGroup*.

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *DuckDBSurvey* - DuckDB Survey Engine | `survey-duckdb-database` | DuckDB Database Survey Service | Surveys the schemas, tables and columns found in a DuckDB database, along with the attached databases and external file scans it uses. |
| *DuckDBGovernance* - DuckDB Governance Engine | `create-duckdb-database`, `create-duckdb-schema` | Create Asset Governance Service | Creates an asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-duckdb-database`, `catalog-duckdb-schema` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target: the *DuckDBDatabaseCataloguer* for a database, the *JDBCDatabaseCataloguer* for a schema. |
| | `delete-duckdb-database`, `delete-duckdb-schema` | Delete Asset Governance Service | Deletes an asset that was created by a template.  The database file itself is unaffected. |

The governance engines run in an [engine host](/concepts/engine-host).

## Technology type report

The technology type report for *DuckDB Relational Database*, taken from Egeria's quickstart, shows how the template, governance action processes, integration connector and governance action types are linked to the technology type.

??? info "Technology type report for DuckDB Relational Database"
    --8<-- "snippets/technology-types/duckdb-relational-database-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *DuckDBDatabase::CreateAsCatalogTarget* with the database's path and name to start cataloguing it.  The database file must be readable from the platform running the integration daemon.

    [Leveraging your DuckDB estate](/egeria-solutions/leveraging-duckdb/overview) describes the survey annotations and the cataloguing in more detail.

--8<-- "snippets/abbr.md"
