
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Db2 for Linux, UNIX and Windows estate

[IBM Db2 for Linux, UNIX and Windows](https://www.ibm.com/products/db2) (Db2 LUW - the distributed/open-systems edition of Db2, formerly known as Db2 UDB, as distinct from Db2 for z/OS) is a long-standing presence in many enterprise data estates, often running alongside PostgreSQL, Microsoft SQL Server and Oracle.  As with any large estate, it is easy to lose track of what each server and database actually contains, whether it is still needed, and how much it can be trusted.

Egeria's *Db2 for Linux, UNIX and Windows connectors* give you oversight of this estate without needing to log into every server and inspect it by hand.  They can:

* **Survey** a Db2 LUW server, or an individual database, to build a picture of what it contains - how many schemas, tables, views and columns it has, how large they are, and how actively they are being used - and capture that picture as a survey report.
* **Catalog** a server or a database, turning it into an open metadata asset that can be searched, classified, linked to glossary terms and governed alongside the rest of your data landscape - with the schemas, tables and columns underneath it catalogued automatically.
* Do both of these using **standard governance action processes**, so the same repeatable, automatable pattern is used whether you are onboarding one database or an entire estate of servers.

Because the survey works from Db2's own system catalog views, it can build this picture without needing read access to the business data stored in your tables. See [How the survey avoids touching your business data](#how-the-survey-avoids-touching-your-business-data) below.

This solution follows the same pattern as [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview), [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview) and [Leveraging your Oracle Database estate](/egeria-solutions/leveraging-oracle/overview) - if you are already familiar with any of those, the Db2 LUW connectors will feel very familiar.  There is one important architectural difference, though: **Db2 for Linux, UNIX and Windows has no catalog view that spans multiple databases** - every one of its system catalog views is already scoped to whichever single database the connection is attached to.  This means, unlike PostgreSQL, Microsoft SQL Server and Oracle, a Db2 LUW server cannot list its own databases for you - see [Discovering databases on a Db2 LUW server](#discovering-databases-on-a-db2-luw-server) below.


## Db2 for Linux, UNIX and Windows Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for Db2 LUW are:

* *Db2 for Linux, UNIX and Windows Database Server* - A database server running IBM Db2 for Linux, UNIX and Windows software.  Db2 for LUW is a multi-model relational database management system.
* *Db2 for Linux, UNIX and Windows database manager (RDBMS)* - The Db2 LUW capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).
* *Db2 for Linux, UNIX and Windows Relational Database* - A database hosted on a Db2 LUW server.
* *Db2 for Linux, UNIX and Windows Relational Database Schema* - A database schema hosted on a relational Db2 LUW database capable of being called through a JDBC Driver.
* *Db2 for Linux, UNIX and Windows Tabular Data Set* - A database table hosted on a Db2 LUW database that has the tabular data set interface.
* *Db2 for Linux, UNIX and Windows Tabular Data Set Collection* - A database schema hosted on a Db2 LUW database that has the tabular data set collection interface.

As with PostgreSQL, Microsoft SQL Server and Oracle, a Db2 LUW resource has up to a four-level name: *serverName.databaseName.schemaName.tableName.columnName*.


## Connectors to Db2 for Linux, UNIX and Windows

The [Db2 LUW connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/db2luw-server-connectors) extend the generic [JDBC connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) with Db2-specific queries against its system catalog, and reuse the same generic JDBC Database Cataloguer used by PostgreSQL, Microsoft SQL Server and Oracle to catalogue what is inside a database once it has been found:

| Connector Name                     | Connector Type                                                     | Purpose                                                                                                                                         |
|--------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC Resource Connector**        | [Digital Resource Connector](/concepts/digital-resource-connector)   | Provides access to a database via the standard JDBC `DataSource` interface.  Used by the survey and integration connectors below to connect to Db2 LUW. |
| **Db2 for Linux, UNIX and Windows Server Cataloguer** | [Integration Connector](/concepts/integration-connector) | Catalogs the databases found on a Db2 LUW server, creating a *RelationalDatabase* asset (with a JDBC connection) for each one, then hands off to the JDBC Database Cataloguer below for the contents of each database. |
| **JDBC Database Cataloguer**       | [Integration Connector](/concepts/integration-connector)             | Catalogs the schemas, tables, columns, primary keys and foreign keys found inside a single database, whichever relational technology hosts it (including Db2 LUW). |
| **Db2 for Linux, UNIX and Windows Server Survey**  | [Survey Action Service](/concepts/survey-action-service) | Surveys all (or a named subset of) the databases hosted by a Db2 LUW server.                                                                      |
| **Db2 for Linux, UNIX and Windows Database Survey** | [Survey Action Service](/concepts/survey-action-service) | Surveys the schemas, tables and columns of a single, already catalogued, Db2 LUW database.                                                       |
| **Db2 for Linux, UNIX and Windows Tabular Data Set Connector** | [Digital Resource Connector](/concepts/digital-resource-connector) | Reads and writes the data in a single Db2 LUW table once it is being used as part of a pipeline or data product.                     |
| **Db2 for Linux, UNIX and Windows Tabular Data Set Collection Connector** | [Digital Resource Connector](/concepts/digital-resource-connector) | Manages a collection of Db2 LUW tables as a set of tabular data sets.                                                     |

These connectors, their templates and the associated reference data are delivered together in the *DB2LUWContentPack*.


## Discovering databases on a Db2 LUW server

PostgreSQL's `pg_database`, Microsoft SQL Server's `sys.databases` and Oracle's `v$pdbs` each let a single connection list every database (or pluggable database) the server hosts.  Db2 LUW has no equivalent - each database maintains its own independent system catalog (`SYSCAT`/`SYSIBMADM`), and there is no view anywhere that lists sibling databases from a connection to one of them.

As a result, both the **Db2 LUW Server Survey** and the **Db2 LUW Server Cataloguer** build their candidate list of databases like this:

* If `includeDatabaseList` is supplied (and is not empty or `*`), exactly those named databases are processed.
* Otherwise, only the single database already named in the connector's own connection is processed - the one it was configured to connect to in the first place.

In practice, this means `includeDatabaseList` is not just a narrowing filter here the way it is for PostgreSQL, Microsoft SQL Server and Oracle - it is how you tell Egeria about every database beyond the one the connector already knows about.  If you have five databases on a Db2 LUW server and want all five catalogued, you must name all five in `includeDatabaseList`; there is no "catalogue everything you find" option as there is for the other relational connectors.  `excludeDatabaseList` still works as a filter on top of whichever candidate list results.


## Surveying a Db2 LUW server or database

A survey is the recommended first step when you encounter a Db2 LUW server you don't already have documented in Egeria.  It answers the question "what is actually in here?" before you commit to cataloguing anything.

There are two survey action services, matching the two levels you can point a survey at:

* The **Db2 LUW Server Survey** works through the candidate database list described above, connecting to each database in turn and gathering statistics - unlike Oracle's single CDB-root connection, there is no shared connection to gather sizes from up front, so a fresh connection is made per database.
* The **Db2 LUW Database Survey** does the same job for a single database that has already been catalogued as an asset - useful when you only want to refresh the picture of one database rather than re-survey the whole server.

Both survey services record their findings as a series of **annotations** attached to a **survey report**, which in turn is linked to the asset that was surveyed (the server or the database).  These are the same annotation types produced by the PostgreSQL, Microsoft SQL Server and Oracle surveys - the Db2 LUW stats extractor implements the same interfaces, just sourcing its numbers from Db2's own catalog and monitoring views (`SYSCAT.SCHEMATA`, `SYSCAT.TABLES`, `SYSCAT.VIEWS`, `SYSCAT.COLUMNS`, `SYSSTAT.COLUMNS`, `SYSCAT.COLDIST`, `SYSCAT.INDEXES`, `SYSCAT.TRIGGERS`, `SYSIBMADM.ADMINTABINFO`, `SYSIBMADM.MON_TAB_STATS`) instead of `pg_catalog`, `sys.*` or Oracle's `all_*`/`v$` views.  See [Open Survey Framework](/frameworks/osf/overview) for background on survey reports and annotations generally.

### The annotations produced

The survey builds up its picture one level at a time - database, then schema, then table, then column - and produces one *Resource Measure Annotation* ([0660](/types/6/0660-Resource-Measures)) for each element it finds:

| Annotation Type                          | Attached to                | What it captures                                                                                                                   |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Database Measurements**        | The database (or server)   | Overall size (the sum of `SYSIBMADM.ADMINTABINFO`'s per-table sizes), and counts of schemas/tables/views/columns.  Rows fetched and updated are always reported as zero at this level - see below. |
| **Capture Database Schema Measurements** | Each schema in the database| Total size of the tables in the schema; counts of tables, views, Materialized Query Tables and columns.                                |
| **Capture Database Table Measurements**  | Each table/view             | Size in bytes; owner; whether it is a table, view or Materialized Query Table; whether it has indexes, triggers or row-level security; row insert/update/delete counts; the query definition (for views). |
| **Capture Database Column Measurements** | Each column                 | Data type, declared width, whether nulls are allowed, an estimate of the number of distinct values, and a single most-common value with its frequency. |

A few things work slightly differently from PostgreSQL, Microsoft SQL Server and Oracle, reflecting Db2's own architecture:

* There is no direct catalog view giving total database size without calling the `SYSPROC.GET_DBSIZE_INFO` stored procedure (which needs a `CALL` statement with `OUT` parameters rather than a plain query) - so, like table size, database size is a metadata-only approximation: the sum of `SYSIBMADM.ADMINTABINFO`'s per-table sizes, reported in bytes after converting from the kilobytes `ADMINTABINFO` uses natively.
* Db2 LUW has no cross-database equivalent of PostgreSQL's `pg_stat_database` or Microsoft SQL Server's `sys.dm_db_index_usage_stats` - so at the *database* level, rows fetched and rows updated are always reported as zero; only the table-level counts, taken from `SYSIBMADM.MON_TAB_STATS`, are complete.
* Db2 LUW has no `CREATE RULE`-style feature, so *Has Rules* is always reported as `false` for every table, just as with Microsoft SQL Server and Oracle.
* *Has Row Security* is read directly from `SYSCAT.TABLES.ROWSECURITY`, which reflects whether Db2's Row and Column Access Control (RCAC) is enabled on the table.
* A Materialized Query Table (MQT - Db2's equivalent of a PostgreSQL materialized view) is reported as a `MaterializedView` table type, identified by `SYSCAT.TABLES.TYPE = 'S'`.
* Where PostgreSQL's `pg_stats` gives an array of several *most common values*, Db2's `SYSCAT.COLDIST` view already stores the single most-frequent value directly (as a `TYPE='F'`, `SEQNO=1` row) - so, unlike Oracle, no extra calculation is needed to derive it from a frequency histogram.
* The survey excludes Db2's own system schemas - anything starting `SYS` plus the built-in `NULLID`, `SQLJ` and `DB2GSE` schemas - so only application schemas are profiled, in the same spirit as PostgreSQL excluding its `postgres` database, Microsoft SQL Server excluding its four system databases, and Oracle excluding its `SYS`/`SYSTEM` users.

??? example "Example annotations from surveying the `EMPLOYEE` database"
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
        "Column data type": "INTEGER",
        "Not Null": "true",
        "Average Column Width": "4",
        "Number Of Distinct Values": "3",
        "Most Common Values": "2",
        "Most Common Values Frequency": "412"
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: db2luw-survey-report-annotations.png - the annotations produced by a Db2 LUW server survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed asset in the Egeria UI.)*


### How the survey avoids touching your business data

Just as with PostgreSQL, Microsoft SQL Server and Oracle, the survey connectors only ever query Db2's own system catalog and monitoring views - `SYSCAT.SCHEMATA`, `SYSCAT.TABLES`, `SYSCAT.VIEWS`, `SYSCAT.COLUMNS`, `SYSSTAT.COLUMNS`, `SYSCAT.COLDIST`, `SYSCAT.INDEXES`, `SYSCAT.TRIGGERS`, `SYSIBMADM.ADMINTABINFO` and `SYSIBMADM.MON_TAB_STATS`.  It never runs a `SELECT` against your business tables.  This means:

* The database user configured for the survey only needs `CONNECT` privilege on the databases being surveyed, plus `SELECT` access to the system catalog views (typically already granted to `PUBLIC` on a default Db2 LUW installation) - it does not need `SELECT` grants on any business table.
* Row counts, sizes and activity levels come from Db2's own catalog and monitoring statistics, not from scanning the tables themselves.

The same nuance that applies to PostgreSQL, Microsoft SQL Server and Oracle applies here too: the *Most Common Value* and *Most Common Values Frequency* measurements on a column do contain one real, representative data value.  This comes from `SYSCAT.COLDIST`, which reflects statistics Db2 itself already collected (typically via `RUNSTATS`, whether run manually or by automatic table maintenance) - not from a live read performed by the Egeria connector.  If you need to exclude that level of detail for particularly sensitive columns, use the include/exclude controls described next.


## Controlling what is surveyed or catalogued

Once you have decided which databases a Db2 LUW server survey or cataloguer should process (see [Discovering databases on a Db2 LUW server](#discovering-databases-on-a-db2-luw-server) above), you can narrow further using the same configuration properties as PostgreSQL, Microsoft SQL Server and Oracle:

At the **server** level (both the Db2 LUW Server Survey and the Db2 LUW Server Cataloguer integration connector honour these):

| Configuration Property      | Purpose                                                                                          | Example                     |
|------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `includeDatabaseList`       | The databases to survey/catalogue.  Required to process more than the one database the connector's own connection already names - see above. | `["EMPLOYEE", "PATIENT"]`   |
| `excludeDatabaseList`       | The named databases are skipped, even if they appear in `includeDatabaseList` or are the connector's own connected database. | `["dbBoring", "dbNotUsed"]` |

Once inside a specific database, the **JDBC Database Cataloguer** integration connector offers the same include/exclude pattern one level down, for schemas, tables, views and columns - this is the same generic connector, and the same properties, as used for PostgreSQL, Microsoft SQL Server and Oracle:

| Configuration Property      | Purpose                                                        |
|------------------------------|--------------------------------------------------------------------|
| `includeSchemaNames` / `excludeSchemaNames` | Which schemas to catalogue (or skip).                 |
| `includeTableNames` / `excludeTableNames`   | Which tables to catalogue (or skip).                  |
| `includeViewNames` / `excludeViewNames`     | Which views to catalogue (or skip).                   |
| `includeColumnNames` / `excludeColumnNames` | Which columns to catalogue (or skip).                 |

An `include...` list always wins over the corresponding `exclude...` list - use it when you only want a handful of named schemas/tables/columns out of a much larger database, and the `exclude...` lists when you want everything *except* a short list of items you know you don't want.

These properties are set as `configurationProperties` on the integration connector, or passed as `requestParameters` when the governance action process configures the connector for you (see below).


## Cataloguing a Db2 LUW server or database

Cataloguing turns what the survey found into open metadata assets you can search, classify and link to the rest of your metadata - glossary terms, governance definitions, data products, and so on.  Egeria provides a template for the server and for a database, and a matching *CreateAsCatalogTarget* governance action process for each that creates the asset from the template and then configures the right integration connector to keep it synchronized:

* **Db2 LUW Server** - creates the *SoftwareServer* asset and starts the **Db2 LUW Server Cataloguer**, which catalogues the databases named in `includeDatabaseList` (or, if none are given, just the one database the connector's own connection names).
* **Db2 LUW Relational Database** - creates the *RelationalDatabase* asset and starts the **JDBC Database Cataloguer** against it, which catalogues its schemas, tables, columns, primary keys and foreign keys.

There is no separate schema-level template or governance action process for Db2 LUW (the same as Microsoft SQL Server and Oracle, and unlike PostgreSQL, which offers one) - a database's schemas are still catalogued and become their own *Db2 for Linux, UNIX and Windows Relational Database Schema* assets, just always as part of cataloguing the whole database.

Because cataloguing a server automatically configures the JDBC Database Cataloguer for the databases it is told about, running the top-level *DB2LUWServer::CreateAsCatalogTarget* process catalogues everything named in `includeDatabaseList` in one go - just remember that, unlike the other three relational connectors, this list is how the databases get found in the first place, not just a narrowing filter.  Use the database-level process when you only want to catalogue a specific database on a server you have already surveyed.

<!-- SCREENSHOT PLACEHOLDER: db2luw-catalogued-assets.png - the resulting RelationalDatabase / DeployedDatabaseSchema / RelationalTable assets shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued database, schema, table and column assets shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the *DB2LUWContentPack*.  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `DB2LUWServer:CreateAndSurveyGovernanceActionProcess`                  | Creates the *Db2 for Linux, UNIX and Windows Server* asset and runs the Db2 LUW Server Survey against it, printing out the resulting report. |
| `DB2LUWServer::CreateAsCatalogTargetGovernanceActionProcess`           | Creates the *Db2 for Linux, UNIX and Windows Server* asset and configures the Db2 LUW Server Cataloguer to catalogue its databases. |
| `DB2LUWServer:DeleteAssetWithTemplateGovernanceActionProcess`          | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.              |
| `DB2LUWDatabase:CreateAndSurveyGovernanceActionProcess`                 | Creates a *Db2 for Linux, UNIX and Windows Relational Database* asset and runs the Db2 LUW Database Survey against it.       |
| `DB2LUWDatabase::CreateAsCatalogTargetGovernanceActionProcess`          | Creates a *Db2 for Linux, UNIX and Windows Relational Database* asset and configures the JDBC Database Cataloguer to catalogue it. |
| `DB2LUWDatabase:DeleteAssetWithTemplateGovernanceActionProcess`         | Deletes the database asset (and everything anchored to it) using the same template properties used to create it.            |

Each *CreateAndSurvey* process runs the same three steps as its PostgreSQL, Microsoft SQL Server and Oracle equivalents: create the asset, run the survey, then print the resulting report; each *CreateAsCatalogTarget* process runs two steps: create the asset, then attach it as a catalog target to the appropriate integration connector.


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

### Survey a Db2 LUW server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "DB2LUWServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalDB2LUW1",
    "hostIdentifier" : "localhost",
    "portNumber" : "50000",
    "databaseName" : "EMPLOYEE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "DB2LUW Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Db2 for Linux, UNIX and Windows database server.",
    "includeDatabaseList" : "EMPLOYEE,PATIENT"
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same Db2 LUW server (and the databases named above)
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "DB2LUWServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalDB2LUW1",
    "hostIdentifier" : "localhost",
    "portNumber" : "50000",
    "databaseName" : "EMPLOYEE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "DB2LUW Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Db2 for Linux, UNIX and Windows database server.",
    "includeDatabaseList" : "EMPLOYEE,PATIENT"
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

Notice `databaseName` is required even when creating the *server* asset - it is the database the connector uses to establish its first JDBC connection to the server (Db2 LUW, unlike PostgreSQL and Microsoft SQL Server, has no "serverless" connection string that omits a database name).  If you leave out `includeDatabaseList` entirely, only that one database gets surveyed or catalogued - add it explicitly, as shown above, to process more than one.

### Using pyegeria

This follows exactly the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the Db2 LUW process names, default port (50000) and the extra `databaseName`/`includeDatabaseList` parameters substituted in:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what Db2 LUW governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="DB2LUW",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey a Db2 LUW server
request_parameters = {
    "serverName" : "LocalDB2LUW1",
    "hostIdentifier" : "localhost",
    "portNumber" : "50000",
    "databaseName" : "EMPLOYEE",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "DB2LUW Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Db2 for Linux, UNIX and Windows database server.",
    "includeDatabaseList" : "EMPLOYEE,PATIENT",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "DB2LUWServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "DB2LUWServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

To follow progress of the integration connectors once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["DB2LUWServerCataloguer", "JDBCDatabaseCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: db2luw-integration-daemon-status.png - display_integration_daemon_status() output showing the Db2 LUW Server Cataloguer and JDBC Database Cataloguer connectors running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the Db2 LUW connectors.)*


## Related information

* [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - the equivalent solution for PostgreSQL; the two follow the same pattern and share the JDBC Database Cataloguer.
* [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview) - the equivalent solution for Microsoft SQL Server, which shares Db2 LUW's lack of a schema-level template.
* [Leveraging your Oracle Database estate](/egeria-solutions/leveraging-oracle/overview) - the equivalent solution for Oracle, another multi-database relational platform, though one where the server-wide database list *can* be auto-discovered.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
