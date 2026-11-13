<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Oracle Database Content Pack

The *OracleContentPack* contains the reference data, templates, connector definitions and governance services for working with an Oracle Database Server.  It lets you describe an Oracle Database Server, its pluggable databases (PDBs) and their schemas in open metadata, survey what they contain, and keep their catalog entries up to date as the databases change.  The connectors it configures are supplied in the *omag-server-platform* distribution, in the [oracle-server-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/oracle-server-connectors){ target=gh } module, whose jar file includes the Oracle JDBC (ojdbc) client driver.

The content pack is found in the `OracleContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the base connector types and the generic database services, and it is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

Working with Oracle starts with a [technology type](/concepts/deployed-implementation-type).  Each technology type in this pack points to a [template](/concepts/template) for creating its open metadata, and to the services and [governance action processes](/concepts/governance-action-process) that act on resources of that type.  Running a process such as *OracleServer::CreateAsCatalogTarget* creates the server's asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *OracleServerCataloguer* integration connector.  From then on, the cataloguer maintains the pluggable databases it finds in the server, and hands the cataloguing of each pluggable database's schemas, tables and columns to the generic *JDBC Database Cataloguer* supplied by the Core Content Pack.

In Egeria's Oracle model, an *Oracle Relational Database* is a pluggable database, and an *Oracle Relational Database Schema* is an Oracle user.  All of the templates build a JDBC address of the form `jdbc:oracle:thin:@//{hostIdentifier}:{portNumber}/{databaseName}`, so even the server template needs a `databaseName` - the service name to connect to - alongside the host, port and secrets store details.

The survey engine gives a one-off, in-depth view of a server or pluggable database, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the asset and run the survey in one step, then print the resulting report.

## Technology types and templates

| Technology type | Template creates | Governance action processes |
|---|---|---|
| Oracle Database Server | A *SoftwareServer* with its *DatabaseManager* capability, endpoint and connection | `OracleServer::CreateAsCatalogTarget`, `OracleServer:CreateAndSurvey`, `OracleServer:DeleteAsset` |
| Oracle Relational Database | A *RelationalDatabase* asset for a pluggable database, and its connection | `OracleDatabase::CreateAsCatalogTarget`, `OracleDatabase:CreateAndSurvey`, `OracleDatabase:DeleteAsset` |
| Oracle Relational Database Schema | A *DeployedDatabaseSchema* asset (an Oracle user) and its connection | `OracleDatabaseSchema::CreateAsCatalogTarget`, `OracleDatabaseSchema:DeleteAsset` |
| Oracle Tabular Data Set Collection | A *TabularDataSetCollection* for a schema, readable through the [tabular data set connector](/concepts/tabular-data-set-connector) | |
| Oracle Tabular Data Set | A *TabularDataSet* for a single table | |
| Oracle Table | A *DataSet* for a table named in lineage events (OpenLineage names it `oracle://{host}:{port}` + `{serviceName or sid}.{schema}.{table}`) | |
| Oracle database manager (RDBMS) | Describes the database manager capability of a server (no template) | |

The templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines the *OracleIntegrationGroup* (`Egeria:IntegrationGroup:Oracle`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| OracleServerIntegrationConnector | `OracleServerCataloguer` (user `oraclecatnpa`, refreshes every 60 minutes) | Catalogs the pluggable databases found in the Oracle Database Servers attached as catalog targets. |

There is no Oracle-specific database cataloguer.  The `catalog-oracle-database` and `catalog-oracle-schema` request types attach pluggable databases and schemas to the *JDBCDatabaseCataloguer* in the Core Content Pack's *DatabaseIntegrationGroup*.

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *OracleSurvey* - Oracle Database Server Survey Engine | `survey-oracle-server` | Oracle Database Server Survey Service | Surveys the pluggable databases, their tables and columns, found in an Oracle Database Server. |
| | `survey-oracle-database` | Oracle Pluggable Database Survey Service | Surveys the tables and columns found in an Oracle pluggable database. |
| *OracleGovernance* - Oracle Database Server Governance Engine | `create-oracle-server`, `create-oracle-database`, `create-oracle-schema` | Create Asset Governance Service | Creates an asset from its template and passes its GUID on as a new asset action target. |
| | `catalog-oracle-server`, `catalog-oracle-database`, `catalog-oracle-schema` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target: the *OracleServerCataloguer* for a server, the *JDBCDatabaseCataloguer* for a pluggable database or schema. |
| | `delete-oracle-server`, `delete-oracle-database`, `delete-oracle-schema` | Delete Asset Governance Service | Deletes an asset that was created by a template. |

The governance engines run in an [engine host](/concepts/engine-host).

## Technology type reports

The technology type reports, taken from Egeria's quickstart, show how the template, governance action processes, integration connector and governance action types are linked to each technology type.

??? info "Technology type report for Oracle Database Server"
    --8<-- "snippets/technology-types/oracle-database-server-technology-report-mermaid-graph.md"

??? info "Technology type report for Oracle Relational Database"
    --8<-- "snippets/technology-types/oracle-relational-database-technology-report-mermaid-graph.md"

!!! summary "Usage"
    Load this content pack into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *OracleServer::CreateAsCatalogTarget* with the server's name, host, port, service name (`databaseName`) and secrets details to start cataloguing it.

    [Leveraging your Oracle Database estate](/egeria-solutions/leveraging-oracle/overview) walks through surveying and cataloguing a server step by step.

--8<-- "snippets/abbr.md"
