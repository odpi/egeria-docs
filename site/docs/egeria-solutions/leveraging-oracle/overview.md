
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Oracle Database estate

[Oracle Database](https://www.oracle.com/database/) is a mainstay of enterprise IT, and organizations typically have it running on many servers - supporting production applications, reporting, integration staging areas and one-off analysis databases that were spun up for a project and then forgotten.  As with any large estate, it is easy to lose track of what each server and database actually contains, whether it is still needed, and how much it can be trusted.

Egeria's *Oracle Database connectors* give you oversight of this estate without needing to log into every server and inspect it by hand.  They can:

* **Survey** an Oracle Database Server, or an individual pluggable database, to build a picture of what it contains - how many schemas, tables, views and columns it has, how large they are, and how actively they are being used - and capture that picture as a survey report.
* **Catalog** a server or a pluggable database, turning it into an open metadata asset that can be searched, classified, linked to glossary terms and governed alongside the rest of your data landscape - with the schemas, tables and columns underneath it catalogued automatically.
* Do both of these using **standard governance action processes**, so the same repeatable, automatable pattern is used whether you are onboarding one database or an entire estate of servers.

Because the survey works from Oracle's own data dictionary views, it can build this picture without needing read access to the business data stored in your tables. See [How the survey avoids touching your business data](#how-the-survey-avoids-touching-your-business-data) below.

This solution follows the same pattern as [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) and [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview) - if you are already familiar with either of those, the Oracle connectors will feel very familiar.  The main difference is architectural: Oracle Database is *multitenant*, so a single *Oracle Database Server* asset hosts multiple *pluggable databases (PDBs)* rather than the flat list of databases PostgreSQL and Microsoft SQL Server present, and this shapes how the connectors connect and what they exclude, as called out below.


## Oracle Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for Oracle Database are:

* *Oracle Database Server* - A database server running the Oracle Database software.  Oracle Database is a multi-model relational database management system.
* *Oracle database manager (RDBMS)* - The Oracle Database capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).
* *Oracle Relational Database* - A pluggable database (PDB) hosted on an Oracle Database Server.
* *Oracle Relational Database Schema* - A database schema (Oracle user) hosted on a relational Oracle database capable of being called through a JDBC Driver.
* *Oracle Tabular Data Set* - A database table hosted on an Oracle Database that has the tabular data set interface.
* *Oracle Tabular Data Set Collection* - A database schema hosted on an Oracle Database that has the tabular data set collection interface.

As with PostgreSQL and Microsoft SQL Server, an Oracle resource has up to a four-level name: *serverName.databaseName.schemaName.tableName.columnName* - except here `databaseName` is a pluggable database, and `schemaName` is an Oracle *user*, since Oracle schemas and users are the same thing.


## Connectors to Oracle Database

The [Oracle Database connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/oracle-server-connectors) extend the generic [JDBC connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) with Oracle-specific queries against its data dictionary, and reuse the same generic JDBC Database Cataloguer used by PostgreSQL and Microsoft SQL Server to catalogue what is inside a pluggable database once it has been found:

| Connector Name                     | Connector Type                                                     | Purpose                                                                                                                                         |
|--------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC Resource Connector**        | [Digital Resource Connector](/concepts/digital-resource-connector)   | Provides access to a database via the standard JDBC `DataSource` interface.  Used by the survey and integration connectors below to connect to Oracle (via the `ojdbc11` driver). |
| **Oracle Database Server Cataloguer** | [Integration Connector](/concepts/integration-connector)          | Catalogs the pluggable databases found on an Oracle Database Server, creating a *RelationalDatabase* asset (with a JDBC connection) for each one, then hands off to the JDBC Database Cataloguer below for the contents of each pluggable database. |
| **JDBC Database Cataloguer**       | [Integration Connector](/concepts/integration-connector)             | Catalogs the schemas, tables, columns, primary keys and foreign keys found inside a single database, whichever relational technology hosts it (including Oracle). |
| **Oracle Database Server Survey**  | [Survey Action Service](/concepts/survey-action-service)             | Surveys all (or a selected subset of) the pluggable databases hosted by an Oracle Database Server.                                                |
| **Oracle Pluggable Database Survey** | [Survey Action Service](/concepts/survey-action-service)           | Surveys the schemas, tables and columns of a single, already catalogued, Oracle pluggable database.                                              |
| **Oracle Tabular Data Set Connector** | [Digital Resource Connector](/concepts/digital-resource-connector) | Reads and writes the data in a single Oracle table once it is being used as part of a pipeline or data product.                                  |
| **Oracle Tabular Data Set Collection Connector** | [Digital Resource Connector](/concepts/digital-resource-connector) | Manages a collection of Oracle tables as a set of tabular data sets.                                                                 |

These connectors, their templates and the associated reference data are delivered together in the *OracleContentPack*.

??? info "Getting table and column comments back from the JDBC driver"
    Oracle's JDBC driver does not return table and column `REMARKS` (comments) via `DatabaseMetaData` unless it is explicitly told to.  If you want the cataloguer to pick up comments you have added in the database, add `"additionalConnectionProperties" : {"remarksReporting" : "true"}` to the connector's configuration properties - this is passed straight through to the driver.  Without it, Egeria's catalogued assets simply have no description sourced from the database.


## Surveying an Oracle Database Server or pluggable database

A survey is the recommended first step when you encounter an Oracle server you don't already have documented in Egeria.  It answers the question "what is actually in here?" before you commit to cataloguing anything.

There are two survey action services, matching the two levels you can point a survey at:

* The **Oracle Database Server Survey** connects to the server's *CDB root* (the container database that owns the pluggable databases) and queries `v$pdbs` to find the PDBs it hosts.  It then works through each qualifying PDB in turn, gathering statistics.
* The **Oracle Pluggable Database Survey** does the same job for a single PDB that has already been catalogued as an asset - useful when you only want to refresh the picture of one database rather than re-survey the whole server.

Both survey services record their findings as a series of **annotations** attached to a **survey report**, which in turn is linked to the asset that was surveyed (the server or the database).  These are the same annotation types produced by the PostgreSQL and Microsoft SQL Server surveys - the Oracle stats extractor implements the same interfaces, just sourcing its numbers from Oracle's data dictionary views (`v$pdbs`, `cdb_data_files`, `all_tables`, `all_tab_columns`, `all_tab_col_statistics`, `all_tab_histograms`, `all_tab_modifications`, `all_indexes`, `all_triggers`, `all_policies`, `all_views`, `all_mviews`) instead of `pg_catalog` or `sys.*`.  See [Open Survey Framework](/frameworks/osf/overview) for background on survey reports and annotations generally.

### The annotations produced

The survey builds up its picture one level at a time - database, then schema, then table, then column - and produces one *Resource Measure Annotation* ([0660](/types/6/0660-Resource-Measures)) for each element it finds:

| Annotation Type                          | Attached to                | What it captures                                                                                                                   |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Database Measurements**        | The database (or server)   | Overall size (from `cdb_data_files`), and counts of schemas/tables/views/columns.  Rows fetched and updated are always reported as zero at this level - see below. |
| **Capture Database Schema Measurements** | Each schema (Oracle user) in the database | Total size of the tables in the schema; counts of tables, views, materialized views and columns.                          |
| **Capture Database Table Measurements**  | Each table/view             | Size in bytes; owner; whether it is a table, view or materialized view; whether it has indexes, triggers or row-level security (Oracle's Virtual Private Database policies); row insert/update/delete counts; the query definition (for views). |
| **Capture Database Column Measurements** | Each column                 | Data type, average width, whether nulls are allowed, an estimate of the number of distinct values, and a single most-common value with its estimated frequency. |

A few things work slightly differently from PostgreSQL and Microsoft SQL Server, reflecting Oracle's own architecture:

* Cataloguing and surveying only ever consider pluggable databases that are currently open in `READ WRITE` mode - a PDB that is mounted but not open, read-only, or the internal `PDB$SEED` template PDB used to create new PDBs, is always skipped, in the same way that PostgreSQL skips its `postgres` maintenance database and Microsoft SQL Server skips its four fixed system databases.
* Oracle has no cross-PDB equivalent of PostgreSQL's `pg_stat_database` or Microsoft SQL Server's `sys.dm_db_index_usage_stats` that can be queried from the CDB root without the separately-licensed Diagnostics Pack (AWR) - so at the *database* level, rows fetched and rows updated are always reported as zero; only the table-level counts, taken from `all_tab_modifications`, are complete.
* Oracle has no `CREATE RULE`-style feature, so *Has Rules* is always reported as `false` for every table, just as with Microsoft SQL Server.
* Where PostgreSQL's `pg_stats` gives an array of several *most common values*, Oracle's column statistics (`all_tab_col_statistics`/`all_tab_histograms`) are used to report a single most-common value and its estimated frequency, in the same way as Microsoft SQL Server's histogram DMV.
* An Oracle *schema* is an Oracle *user* - the survey excludes Oracle-maintained system users (`SYS`, `SYSTEM` and the rest) via `all_users.oracle_maintained = 'N'`, so only application schemas are profiled.

??? example "Example annotations from surveying the `EMPLOYEE` pluggable database"
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture Database Measurements",
      "summary": "Capture summary statistics about a database.",
      "explanation": "This annotation retrieves statistics about a database and its usage.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "Database Name": "EMPLOYEE",
        "Data size": "10485760",
        "Number of schemas": "1",
        "Number of tables": "2",
        "Number of columns": "10",
        "Rows Fetched": "0",
        "Rows Inserted": "0",
        "Rows Updated": "0",
        "Rows Deleted": "0"
      }
    }
    ```
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture Database Table Measurements",
      "summary": "Capture summary statistics about a database table.",
      "explanation": "This annotation retrieves statistics about individual columns and aggregates them into a summary for the table.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "Table Qualified Name": "EMPLOYEE.HR.EMPLOYEE",
        "Table Name": "EMPLOYEE",
        "Resource Owner": "HR",
        "Table Type": "Table",
        "Table Size": "262144",
        "Number of columns": "8",
        "Number Of Rows Inserted": "612",
        "Number Of Rows Updated": "44",
        "Number Of Rows Deleted": "0",
        "Has Indexes": "true",
        "Has Rules": "false",
        "Has Triggers": "false",
        "Has Row Security": "false"
      }
    }
    ```
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture Database Column Measurements",
      "summary": "Capture summary statistics about a database column.",
      "explanation": "This annotation retrieves statistics about an individual column.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "Column qualified name": "EMPLOYEE.HR.EMPLOYEE.EMPSTATUS",
        "Column name": "EMPSTATUS",
        "Column data type": "NUMBER",
        "Not Null": "true",
        "Average Column Width": "4",
        "Number Of Distinct Values": "3",
        "Most Common Values": "2",
        "Most Common Values Frequency": "412"
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: oracle-survey-report-annotations.png - the annotations produced by an Oracle Database Server survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed asset in the Egeria UI.)*


### How the survey avoids touching your business data

Just as with PostgreSQL and Microsoft SQL Server, the survey connectors only ever query Oracle's own data dictionary views - `v$pdbs`, `cdb_data_files`, `all_tables`, `all_tab_columns`, `all_tab_col_statistics`, `all_tab_histograms`, `all_tab_modifications`, `all_indexes`, `all_triggers`, `all_policies`, `all_views`, `all_mviews` and `all_users`.  It never runs a `SELECT` against your business tables.  This means:

* The database account configured for the survey only needs `CONNECT` privilege plus `SELECT_CATALOG_ROLE` (or equivalent grants on the individual `ALL_*`/`V$` views) - it does not need `SELECT` grants on any business table.
* Row counts, sizes and activity levels come from Oracle's own statistics and data dictionary, not from scanning the tables themselves.

The same nuance that applies to PostgreSQL and Microsoft SQL Server applies here too: the *Most Common Value* and *Most Common Values Frequency* measurements on a column do contain one real, representative data value.  This comes from `all_tab_histograms`, which reflects statistics that Oracle itself already collected (typically via automatic optimizer statistics gathering) - not from a live read performed by the Egeria connector.  If you need to exclude that level of detail for particularly sensitive columns, use the include/exclude controls described next.


## Controlling what is surveyed or catalogued

By default, surveying or cataloguing an Oracle Database Server processes every pluggable database it hosts that is open in `READ WRITE` mode (the internal `PDB$SEED` template is always skipped, regardless of this setting).  You can narrow - or widen - this using configuration properties on the connector, in exactly the same way as PostgreSQL and Microsoft SQL Server:

At the **server** level (both the Oracle Database Server Survey and the Oracle Database Server Cataloguer integration connector honour these):

| Configuration Property      | Purpose                                                                                          | Example                     |
|------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `includeDatabaseList`       | Only the named pluggable databases are surveyed/catalogued.  If unset, null or `*`, all PDBs except those excluded are processed. | `["EMPLOYEE", "PATIENT"]`   |
| `excludeDatabaseList`       | The named pluggable databases are skipped.                                                        | `["pdbBoring", "pdbNotUsed"]` |

Once inside a specific pluggable database, the **JDBC Database Cataloguer** integration connector offers the same include/exclude pattern one level down, for schemas, tables, views and columns - this is the same generic connector, and the same properties, as used for PostgreSQL and Microsoft SQL Server:

| Configuration Property      | Purpose                                                        |
|------------------------------|--------------------------------------------------------------------|
| `includeSchemaNames` / `excludeSchemaNames` | Which schemas (Oracle users) to catalogue (or skip).  |
| `includeTableNames` / `excludeTableNames`   | Which tables to catalogue (or skip).                  |
| `includeViewNames` / `excludeViewNames`     | Which views to catalogue (or skip).                   |
| `includeColumnNames` / `excludeColumnNames` | Which columns to catalogue (or skip).                 |

An `include...` list always wins over the corresponding `exclude...` list - use it when you only want a handful of named schemas/tables/columns out of a much larger database, and the `exclude...` lists when you want everything *except* a short list of items you know you don't want.

These properties are set as `configurationProperties` on the integration connector, or passed as `requestParameters` when the governance action process configures the connector for you (see below).


## Cataloguing an Oracle Database Server or pluggable database

Cataloguing turns what the survey found into open metadata assets you can search, classify and link to the rest of your metadata - glossary terms, governance definitions, data products, and so on.  Egeria provides a template for the server and for a pluggable database, and a matching *CreateAsCatalogTarget* governance action process for each that creates the asset from the template and then configures the right integration connector to keep it synchronized:

* **Oracle Database Server** - creates the *SoftwareServer* asset and starts the **Oracle Database Server Cataloguer**, which discovers and catalogues its pluggable databases (subject to the include/exclude lists above).
* **Oracle Relational Database** - creates the *RelationalDatabase* asset and starts the **JDBC Database Cataloguer** against it, which catalogues its schemas, tables, columns, primary keys and foreign keys.

There is no separate schema-level template or governance action process for Oracle (the same as Microsoft SQL Server, and unlike PostgreSQL, which offers one) - a database's schemas are still catalogued and become their own *Oracle Relational Database Schema* assets, just always as part of cataloguing the whole pluggable database.

Because cataloguing a server automatically configures the JDBC Database Cataloguer for the PDBs it finds, you typically only need to run the top-level *OracleServer::CreateAsCatalogTarget* process to catalogue an entire server - the discovery of databases, schemas, tables and columns cascades from there.  Use the database-level process when you only want to catalogue a specific pluggable database on a server you have already surveyed.

<!-- SCREENSHOT PLACEHOLDER: oracle-catalogued-assets.png - the resulting RelationalDatabase / DeployedDatabaseSchema / RelationalTable assets shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued database, schema, table and column assets shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the *OracleContentPack*.  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `OracleServer:CreateAndSurveyGovernanceActionProcess`                 | Creates the *Oracle Database Server* asset and runs the Oracle Database Server Survey against it, printing out the resulting report. |
| `OracleServer::CreateAsCatalogTargetGovernanceActionProcess`          | Creates the *Oracle Database Server* asset and configures the Oracle Database Server Cataloguer to catalogue its pluggable databases. |
| `OracleServer:DeleteAssetWithTemplateGovernanceActionProcess`         | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.              |
| `OracleDatabase:CreateAndSurveyGovernanceActionProcess`                | Creates an *Oracle Relational Database* asset and runs the Oracle Pluggable Database Survey against it.                      |
| `OracleDatabase::CreateAsCatalogTargetGovernanceActionProcess`         | Creates an *Oracle Relational Database* asset and configures the JDBC Database Cataloguer to catalogue it.                   |
| `OracleDatabase:DeleteAssetWithTemplateGovernanceActionProcess`        | Deletes the database asset (and everything anchored to it) using the same template properties used to create it.            |

Each *CreateAndSurvey* process runs the same three steps as its PostgreSQL and Microsoft SQL Server equivalents: create the asset, run the survey, then print the resulting report; each *CreateAsCatalogTarget* process runs two steps: create the asset, then attach it as a catalog target to the appropriate integration connector.


### Using the REST API

The REST calls below assume you have a running view server (`view-server` in these examples) and have already obtained a bearer token.

```http
@baseURL=https://localhost:9443
@viewServer=view-server

### Get a bearer token
# @name Token
POST {{baseURL}}/api/token
Content-Type: application/json

{
  "userId" : "peterprofile",
  "password" : "secret"
}

> {% client.global.set("token", response.body); %}

### Survey an Oracle Database Server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "OracleServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalOracle1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1521",
    "databaseName" : "FREE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Oracle Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Oracle Database Server."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same Oracle Database Server (and its pluggable databases)
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "OracleServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalOracle1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1521",
    "databaseName" : "FREE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Oracle Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Oracle Database Server."
  }
}

> {% client.global.set("catalogInstanceGUID", response.body.guid); %}

### Check progress of an engine action started by either process above
GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/engine-actions/active?startFrom=0&pageSize=5
Authorization: Bearer {{token}}

### Retrieve the flow definition and progress of a specific process instance
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/governance-officer/governance-action-processes/{{catalogInstanceGUID}}/graph
Authorization: Bearer {{token}}
```

Notice the `databaseName` request parameter is required even when creating the *server* asset - unlike PostgreSQL and Microsoft SQL Server, Oracle's EZCONNECT JDBC URL syntax always requires a service name after `host:port`, so the CDB root's service name (here, `FREE`, the default pluggable database service in the free Oracle container image) has to be supplied up front to let the connector reach the CDB root at all.

To limit which pluggable databases are processed, add `includeDatabaseList` or `excludeDatabaseList` into the `requestParameters` of either call - for example:

```json
"requestParameters" : {
  "serverName" : "LocalOracle1",
  "hostIdentifier" : "localhost",
  "portNumber" : "1521",
  "databaseName" : "FREE",
  "secretsStorePathName" : "secrets/integration.omsecrets",
  "secretsCollectionName" : "Oracle Server Secret",
  "excludeDatabaseList" : "pdbBoring,pdbNotUsed"
}
```

### Using pyegeria

This follows exactly the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the Oracle process names, default port (1521) and the extra `databaseName` parameter substituted in:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what Oracle governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="Oracle",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey an Oracle Database Server
request_parameters = {
    "serverName" : "LocalOracle1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1521",
    "databaseName" : "FREE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "Oracle Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Oracle Database Server.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "OracleServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "OracleServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

To follow progress of the integration connectors once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["OracleServerCataloguer", "JDBCDatabaseCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: oracle-integration-daemon-status.png - display_integration_daemon_status() output showing the Oracle Database Server Cataloguer and JDBC Database Cataloguer connectors running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the Oracle connectors.)*


## Related information

* [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - the equivalent solution for PostgreSQL; the two follow the same pattern and share the JDBC Database Cataloguer.
* [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview) - the equivalent solution for Microsoft SQL Server, which shares Oracle's lack of a schema-level template.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
