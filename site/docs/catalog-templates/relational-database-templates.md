<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relational Database Templates

Egeria's content packs for relational databases share one design for their [catalog templates](/catalog-templates).  The [PostgreSQL Templates](/catalog-templates/postgres-server-templates) page describes that design in detail, with diagrams of the elements each template creates and of the way the templates, processes and connectors work together.  This page summarizes the shared design and then describes what is different for each of the other databases:

* [Microsoft SQL Server](#microsoft-sql-server) - [Microsoft SQL Server Content Pack](/content-packs/mssql-content-pack/overview)
* [Oracle Database](#oracle-database) - [Oracle Content Pack](/content-packs/oracle-content-pack/overview)
* [Db2 for Linux, UNIX and Windows](#db2-for-linux-unix-and-windows) - [Db2 for Linux, UNIX and Windows Content Pack](/content-packs/db2luw-content-pack/overview)
* [DuckDB](#duckdb) - [DuckDB Content Pack](/content-packs/duckdb-content-pack/overview)

## The shared design

Each server-based database pack (PostgreSQL, Microsoft SQL Server, Oracle and Db2) supplies six templates, one per [technology type](/concepts/deployed-implementation-type):

| Level | Template creates | Qualified name pattern |
|---|---|---|
| Server | *SoftwareServer* with a *DatabaseManager* capability, an endpoint and a connection | `<Server technology type>::~{serverName}~` |
| Database | *RelationalDatabase* with an endpoint and a connection | `<Database technology type>::~{serverName}~::~{databaseName}~` |
| Schema | *DeployedDatabaseSchema* with an endpoint and a connection | `<Schema technology type>::~{serverName}~::~{databaseName}~.~{schemaName}~` |
| Schema as tabular data | *TabularDataSetCollection* | `<technology type>::~{serverName}~::~{databaseName}~.~{schemaName}~` |
| Table as tabular data | *TabularDataSet* | `<technology type>::~{serverName}~::~{databaseName}~.~{schemaName}~.~{tableName}~` |
| Table in lineage | *DataSet* with no connection | `<Table technology type>::~{namespacePath}~::~{resourceName}~` |

The connections of the first five templates are virtual connections that name the shared *Relational Database JDBC Connector* and embed a connection to the *YAML File Secrets Store Connector*, so the credentials are supplied through the `secretsStorePathName` and `secretsCollectionName` placeholders rather than stored in open metadata.  The two tabular data set templates wrap that JDBC connection in a further connection to the product's own tabular data set connector, which presents a schema or table as [tabular data](/concepts/tabular-data-set-connector).  The lineage-style table template is named the way [OpenLineage](/features/lineage-management/overview) names the product's tables.

Every server, database and schema technology type has a *CreateAsCatalogTarget* and a *DeleteAsset* [governance action process](/concepts/governance-action-process), and servers and databases also have *CreateAndSurvey*.  Cataloguing a server attaches it to the pack's server cataloguer, which creates each database it finds from the database template and passes it to the Core Content Pack's *JDBCDatabaseCataloguer* to catalog its schemas, tables and columns.

The differences between the packs are in the JDBC addresses and in the placeholders each level needs.

## Microsoft SQL Server

| Template | Endpoint network address | Extra placeholders |
|---|---|---|
| Microsoft SQL Server | `jdbc:sqlserver://~{hostIdentifier}~:~{portNumber}~` | |
| Microsoft SQL Server Relational Database | `jdbc:sqlserver://~{hostIdentifier}~:~{portNumber}~;databaseName=~{databaseName}~` | `databaseName`, `databaseDescription` |
| Microsoft SQL Server Relational Database Schema, Tabular Data Set Collection and Tabular Data Set | `jdbc:sqlserver://~{hostIdentifier}~:~{portNumber}~;databaseName=~{databaseName}~` | `schemaName`, `schemaDescription` (and `tableName`, `tableDescription` for a table) |

SQL Server's JDBC URL has no schema parameter, so the schema is passed to the connector in the connection's `databaseSchema` configuration property.  The tabular data set templates use the *Microsoft SQL Server Tabular Data Set Connector* and *Microsoft SQL Server Tabular Data Set Collection Connector*.  The lineage-style *Microsoft SQL Server Table* template uses the OpenLineage namespace `mssql://{host}:{port}` and name `{database}.{schema}.{table}`.

The processes are `MSSQLServer::CreateAsCatalogTarget`, `MSSQLServer:CreateAndSurvey` and `MSSQLServer:DeleteAsset`, with matching `MSSQLDatabase` and `MSSQLDatabaseSchema` processes (no *CreateAndSurvey* for schemas).  The server cataloguer runs as `MSSQLServerCataloguer`.

??? info "Technology type report for Microsoft SQL Server"
    --8<-- "snippets/technology-types/microsoft-sql-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Microsoft SQL Server Relational Database"
    --8<-- "snippets/technology-types/microsoft-sql-server-relational-database-technology-report-mermaid-graph.md"

## Oracle Database

In Oracle, the unit that is catalogued as a *RelationalDatabase* is a pluggable database (PDB), and `databaseName` is the PDB's service name.  An Oracle JDBC connection always names a service, so the *server* template takes `databaseName` too - for the server, supply the service name of the container database (CDB) root, which is where the cataloguer and survey find the pluggable databases the server hosts.

| Template | Endpoint network address | Extra placeholders |
|---|---|---|
| Oracle Database Server | `jdbc:oracle:thin:@//~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `databaseName` |
| Oracle Relational Database | `jdbc:oracle:thin:@//~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `databaseName`, `databaseDescription` |
| Oracle Relational Database Schema, Tabular Data Set Collection and Tabular Data Set | `jdbc:oracle:thin:@//~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `schemaName`, `schemaDescription` (and `tableName`, `tableDescription` for a table) |

Every Oracle JDBC connection in the templates sets two driver properties in its `additionalConnectionProperties` configuration property: `oracle.jdbc.timezoneAsRegion=false` and `remarksReporting=true` (so that table and column comments are returned with the metadata).  The tabular data set templates use the *Oracle Tabular Data Set Connector* and *Oracle Tabular Data Set Collection Connector*.  The lineage-style *Oracle Table* template uses the OpenLineage namespace `oracle://{host}:{port}` and name `{serviceName or sid}.{schema}.{table}`.

The processes are `OracleServer::CreateAsCatalogTarget`, `OracleServer:CreateAndSurvey` and `OracleServer:DeleteAsset`, with matching `OracleDatabase` and `OracleDatabaseSchema` processes.  The server cataloguer runs as `OracleServerCataloguer`.

??? info "Technology type report for Oracle Database Server"
    --8<-- "snippets/technology-types/oracle-database-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Oracle Relational Database"
    --8<-- "snippets/technology-types/oracle-relational-database-technology-report-mermaid-graph.md"

## Db2 for Linux, UNIX and Windows

A Db2 JDBC connection is made to a database, so, as with Oracle, the server template takes `databaseName` and also passes it to the connector in the connection's `databaseName` configuration property.

| Template | Endpoint network address | Extra placeholders |
|---|---|---|
| Db2 for Linux, UNIX and Windows Database Server | `jdbc:db2://~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `databaseName` |
| Db2 for Linux, UNIX and Windows Relational Database | `jdbc:db2://~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `databaseName`, `databaseDescription` |
| Db2 for Linux, UNIX and Windows Relational Database Schema, Tabular Data Set Collection and Tabular Data Set | `jdbc:db2://~{hostIdentifier}~:~{portNumber}~/~{databaseName}~` | `schemaName`, `schemaDescription` (and `tableName`, `tableDescription` for a table) |

The tabular data set templates use the *Db2 for Linux, UNIX and Windows Tabular Data Set Connector* and *Db2 for Linux, UNIX and Windows Tabular Data Set Collection Connector*.  The lineage-style template is for the *Db2 Table* technology type, with the OpenLineage namespace `db2://{host}:{port}` and name `{database}.{schema}.{table}`.

The processes are `DB2LUWServer::CreateAsCatalogTarget`, `DB2LUWServer:CreateAndSurvey` and `DB2LUWServer:DeleteAsset`, with matching `DB2LUWDatabase` and `DB2LUWDatabaseSchema` processes.  The server cataloguer runs as `DB2LUWServerCataloguer`.

??? info "Technology type report for Db2 for Linux, UNIX and Windows Database Server"
    --8<-- "snippets/technology-types/db2-for-linux-unix-and-windows-database-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Db2 for Linux, UNIX and Windows Relational Database"
    --8<-- "snippets/technology-types/db2-for-linux-unix-and-windows-relational-database-technology-report-mermaid-graph.md"

## DuckDB

DuckDB is an embedded database: it runs inside the process that opens it, and a database is a file (or an in-memory session).  So the DuckDB Content Pack has no server template, and only two templates in all.

| Technology type | Template creates | Qualified name pattern | Endpoint network address |
|---|---|---|---|
| DuckDB Relational Database | *RelationalDatabase* with an endpoint and a connection | `DuckDB Relational Database::~{databasePath}~` | `jdbc:duckdb:~{databasePath}~` |
| DuckDB Relational Database Schema | *DeployedDatabaseSchema* with an endpoint and a connection | `DuckDB Relational Database Schema::~{databasePath}~::~{schemaName}~` | `jdbc:duckdb:~{databasePath}~` |

`databasePath` is the path of the DuckDB database file, or the literal value `:memory:` for an in-memory session; it takes the place of `serverName` in the qualified names.  `databaseName` is still used for the display names and the connection's configuration properties.  The connections name the same JDBC connector and embed a secrets store connection, like the other packs.  There are no tabular data set or lineage-style templates for DuckDB.

The processes are `DuckDBDatabase::CreateAsCatalogTarget`, `DuckDBDatabase:CreateAndSurvey` and `DuckDBDatabase:DeleteAsset`, with `DuckDBDatabaseSchema::CreateAsCatalogTarget` and `DuckDBDatabaseSchema:DeleteAsset` for schemas.  The database cataloguer runs as `DuckDBDatabaseCataloguer`.

??? info "Technology type report for DuckDB Relational Database"
    --8<-- "snippets/technology-types/duckdb-relational-database-technology-report-mermaid-graph.md"

!!! summary "Usage"
    For each server, store its credentials in a YAML secrets store and run the server technology type's *CreateAsCatalogTarget* process with `serverName`, `hostIdentifier`, `portNumber`, the secrets store placeholders and, for Oracle and Db2, `databaseName`.  For DuckDB, run *DuckDBDatabase::CreateAsCatalogTarget* with the database file's path.

    The step-by-step guides are [Leveraging Microsoft SQL Server](/egeria-solutions/leveraging-mssql/overview), [Leveraging Oracle](/egeria-solutions/leveraging-oracle/overview), [Leveraging Db2 for Linux, UNIX and Windows](/egeria-solutions/leveraging-db2luw/overview) and [Leveraging DuckDB](/egeria-solutions/leveraging-duckdb/overview).

--8<-- "snippets/abbr.md"
