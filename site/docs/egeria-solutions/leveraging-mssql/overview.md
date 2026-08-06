
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Microsoft SQL Server estate

[Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/) is one of the most widely deployed relational database platforms in enterprise IT, and organizations typically have it running on many servers - supporting production applications, reporting, integration staging areas and one-off analysis databases that were spun up for a project and then forgotten.  As with any large estate, it is easy to lose track of what each server and database actually contains, whether it is still needed, and how much it can be trusted.

Egeria's *Microsoft SQL Server connectors* give you oversight of this estate without needing to log into every server and inspect it by hand.  They can:

* **Survey** a Microsoft SQL Server, or an individual database, to build a picture of what it contains - how many schemas, tables, views and columns it has, how large they are, and how actively they are being used - and capture that picture as a survey report.
* **Catalog** a server or a database, turning it into an open metadata asset that can be searched, classified, linked to glossary terms and governed alongside the rest of your data landscape - with the schemas, tables and columns underneath it catalogued automatically.
* Do both of these using **standard governance action processes**, so the same repeatable, automatable pattern is used whether you are onboarding one database or an entire estate of servers.

Because the survey works from Microsoft SQL Server's own system catalog and dynamic management views, it can build this picture without needing read access to the business data stored in your tables. See [How the survey avoids touching your business data](#how-the-survey-avoids-touching-your-business-data) below.

This solution follows the same pattern as [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - if you are already familiar with the PostgreSQL connectors, the Microsoft SQL Server connectors will feel very familiar, with the differences called out below.


## Microsoft SQL Server Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for Microsoft SQL Server are:

* *Microsoft SQL Server* - A database server running the Microsoft SQL Server software.  Microsoft SQL Server is a relational database management system.
* *Microsoft SQL Server database manager (RDBMS)* - The Microsoft SQL Server capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).
* *Microsoft SQL Server Relational Database* - A database hosted on a Microsoft SQL Server.
* *Microsoft SQL Server Relational Database Schema* - A database schema hosted on a relational Microsoft SQL Server database capable of being called through a JDBC Driver.

As with PostgreSQL, a Microsoft SQL Server resource has up to a four-level name: *serverName.databaseName.schemaName.tableName.columnName*, with the default schema being `dbo` rather than PostgreSQL's `public`.


## Connectors to Microsoft SQL Server

The [Microsoft SQL Server connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/mssql-server-connectors) extend the generic [JDBC connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) with Microsoft SQL Server-specific queries against its system catalog, and reuse the same generic JDBC Database Cataloguer used by PostgreSQL (and any other JDBC-accessible database) to catalogue what is inside a database once it has been found:

| Connector Name                   | Connector Type                                                     | Purpose                                                                                                                                         |
|-----------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC Resource Connector**      | [Digital Resource Connector](/concepts/digital-resource-connector)   | Provides access to a database via the standard JDBC `DataSource` interface.  Used by the survey and integration connectors below to connect to Microsoft SQL Server (via the `mssql-jdbc` driver). |
| **Microsoft SQL Server Cataloguer** | [Integration Connector](/concepts/integration-connector)          | Catalogs the databases found on a Microsoft SQL Server, creating a *RelationalDatabase* asset (with a JDBC connection) for each one, then hands off to the JDBC Database Cataloguer below for the contents of each database. |
| **JDBC Database Cataloguer**     | [Integration Connector](/concepts/integration-connector)             | Catalogs the schemas, tables, columns, primary keys and foreign keys found inside a single database, whichever relational technology hosts it (including Microsoft SQL Server). |
| **Microsoft SQL Server Survey**  | [Survey Action Service](/concepts/survey-action-service)             | Surveys all (or a selected subset of) the databases hosted by a Microsoft SQL Server.                                                            |
| **Microsoft SQL Server Database Survey** | [Survey Action Service](/concepts/survey-action-service)      | Surveys the schemas, tables and columns of a single, already catalogued, Microsoft SQL Server database.                                          |

Unlike the PostgreSQL connectors, there is currently no Microsoft SQL Server-specific tabular data set connector - once a table is catalogued, it can still be worked with through the generic JDBC connectors.

These connectors, their templates and the associated reference data are delivered together in the *MSSQLContentPack*.


## Surveying a Microsoft SQL Server or database

A survey is the recommended first step when you encounter a Microsoft SQL Server you don't already have documented in Egeria.  It answers the question "what is actually in here?" before you commit to cataloguing anything.

There are two survey action services, matching the two levels you can point a survey at:

* The **Microsoft SQL Server Survey** connects to the server and queries `sys.databases` to find the databases it hosts (excluding the four fixed system databases - `master`, `tempdb`, `model` and `msdb` - the equivalent of PostgreSQL's template/system database exclusion).  It then works through each qualifying, online database in turn, gathering statistics.
* The **Microsoft SQL Server Database Survey** does the same job for a single database that has already been catalogued as an asset - useful when you only want to refresh the picture of one database rather than re-survey the whole server.

Both survey services record their findings as a series of **annotations** attached to a **survey report**, which in turn is linked to the asset that was surveyed (the server or the database).  These are exactly the same annotation types produced by the PostgreSQL survey - Microsoft SQL Server's stats extractor implements the same interfaces, just sourcing its numbers from `sys.*` catalog views and dynamic management views (DMVs) instead of `pg_catalog`.  See [Open Survey Framework](/frameworks/osf/overview) for background on survey reports and annotations generally.

### The annotations produced

The survey builds up its picture one level at a time - database, then schema, then table, then column - and produces one *Resource Measure Annotation* ([0660](/types/6/0660-Resource-Measures)) for each element it finds:

| Annotation Type                          | Attached to                | What it captures                                                                                                                   |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Database Measurements**        | The database (or server)   | Overall size, and counts of schemas/tables/views/columns; rows fetched and updated; session/active time and reset date if available. |
| **Capture Database Schema Measurements** | Each schema in the database| Total size of the tables in the schema; counts of tables, views, indexed views and columns.                                            |
| **Capture Database Table Measurements**  | Each table/view             | Size in bytes; owner; whether it is a table, view or indexed view; whether it has indexes, triggers or row-level security; row insert/update/delete counts; the query definition (for views). |
| **Capture Database Column Measurements** | Each column                 | Data type, declared width, whether nulls are allowed, an estimate of the number of distinct values, and the single most common value with its estimated frequency. |

A few things work slightly differently from PostgreSQL, reflecting what Microsoft SQL Server actually exposes:

* Microsoft SQL Server has no database-wide split of inserted/updated/deleted row counts (PostgreSQL's `pg_stat_database` provides this, Microsoft SQL Server doesn't) - so at the *database* level, rows inserted and rows deleted are always reported as zero; only the table-level counts, taken from `sys.dm_db_index_operational_stats`, are complete.
* Microsoft SQL Server has no `CREATE RULE`-style feature, so *Has Rules* is always reported as `false` for every table.
* A column's *Column Size* is its declared width (`max_length` from `sys.columns`), not an estimate of actual stored bytes - Microsoft SQL Server has no metadata-only equivalent of PostgreSQL's `pg_column_size()`.
* Where PostgreSQL's `pg_stats` gives an array of several *most common values*, Microsoft SQL Server's column statistics histogram (`sys.dm_db_stats_histogram`) is used to report a single most-common value and its estimated frequency.
* An indexed view (Microsoft SQL Server's closest equivalent of a PostgreSQL materialized view) is reported as a `MaterializedView` table type.

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
        "Rows Fetched": "22140",
        "Rows Inserted": "0",
        "Rows Updated": "58",
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
        "Table Qualified Name": "EMPLOYEE.dbo.EMPLOYEE",
        "Table Name": "EMPLOYEE",
        "Resource Owner": "dbo",
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
        "Column qualified name": "EMPLOYEE.dbo.EMPLOYEE.EMPSTATUS",
        "Column name": "EMPSTATUS",
        "Column data type": "int",
        "Not Null": "true",
        "Average Column Width": "4",
        "Number Of Distinct Values": "3",
        "Most Common Values": "2",
        "Most Common Values Frequency": "412"
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: mssql-survey-report-annotations.png - the annotations produced by a Microsoft SQL Server survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed asset in the Egeria UI.)*


### How the survey avoids touching your business data

Just as with PostgreSQL, the survey connectors only ever query Microsoft SQL Server's own system catalog views and dynamic management views - `sys.databases`, `sys.master_files`, `sys.tables`, `sys.views`, `sys.columns`, `sys.schemas`, `sys.indexes`, `sys.triggers`, `sys.security_predicates`, and the DMVs `sys.dm_db_index_usage_stats`, `sys.dm_db_index_operational_stats`, `sys.dm_db_partition_stats` and `sys.dm_db_stats_histogram`.  It never runs a `SELECT` against your business tables.  This means:

* The database login configured for the survey only needs `CONNECT` privilege (plus `VIEW SERVER STATE`/`VIEW DATABASE STATE` for the DMVs) - it does not need `SELECT` grants on any business table.
* Row counts, sizes and activity levels come from SQL Server's own statistics and usage counters, not from scanning the tables themselves.

The same nuance that applies to PostgreSQL applies here too: the *Most Common Value* and *Most Common Values Frequency* measurements on a column do contain one real, representative data value.  This comes from `sys.dm_db_stats_histogram`, which reflects statistics that Microsoft SQL Server itself already collected (typically via auto-update statistics) - not from a live read performed by the Egeria connector.  If you need to exclude that level of detail for particularly sensitive columns, use the include/exclude controls described next.


## Controlling what is surveyed or catalogued

By default, surveying or cataloguing a Microsoft SQL Server processes every database it hosts (except the four fixed system databases, which are always skipped).  You can narrow - or widen - this using configuration properties on the connector, in exactly the same way as PostgreSQL:

At the **server** level (both the Microsoft SQL Server Survey and the Microsoft SQL Server Cataloguer integration connector honour these):

| Configuration Property      | Purpose                                                                                          | Example                     |
|------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `includeDatabaseList`       | Only the named databases are surveyed/catalogued.  If unset, null or `*`, all databases except those excluded are processed. | `["EMPLOYEE", "PATIENT"]`   |
| `excludeDatabaseList`       | The named databases are skipped.  (The four system databases are always excluded regardless of this setting.) | `["dbBoring", "dbNotUsed"]`  |

Once inside a specific database, the **JDBC Database Cataloguer** integration connector offers the same include/exclude pattern one level down, for schemas, tables, views and columns - this is the same generic connector, and the same properties, as used for PostgreSQL:

| Configuration Property      | Purpose                                                        |
|------------------------------|--------------------------------------------------------------------|
| `includeSchemaNames` / `excludeSchemaNames` | Which schemas to catalogue (or skip).                 |
| `includeTableNames` / `excludeTableNames`   | Which tables to catalogue (or skip).                  |
| `includeViewNames` / `excludeViewNames`     | Which views to catalogue (or skip).                   |
| `includeColumnNames` / `excludeColumnNames` | Which columns to catalogue (or skip).                 |

An `include...` list always wins over the corresponding `exclude...` list - use it when you only want a handful of named schemas/tables/columns out of a much larger database, and the `exclude...` lists when you want everything *except* a short list of items you know you don't want.

These properties are set as `configurationProperties` on the integration connector, or passed as `requestParameters` when the governance action process configures the connector for you (see below).


## Cataloguing a Microsoft SQL Server or database

Cataloguing turns what the survey found into open metadata assets you can search, classify and link to the rest of your metadata - glossary terms, governance definitions, data products, and so on.  Egeria provides a template for the server and for a database, and a matching *CreateAsCatalogTarget* governance action process for each that creates the asset from the template and then configures the right integration connector to keep it synchronized:

* **Microsoft SQL Server** - creates the *SoftwareServer* asset and starts the **Microsoft SQL Server Cataloguer**, which discovers and catalogues its databases (subject to the include/exclude lists above).
* **Microsoft SQL Server Relational Database** - creates the *RelationalDatabase* asset and starts the **JDBC Database Cataloguer** against it, which catalogues its schemas, tables, columns, primary keys and foreign keys.

There is no separate schema-level template or governance action process for Microsoft SQL Server (unlike PostgreSQL, which offers one) - a database's schemas are still catalogued and become their own *Microsoft SQL Server Relational Database Schema* assets, just always as part of cataloguing the whole database.

Because cataloguing a server automatically configures the JDBC Database Cataloguer for the databases it finds, you typically only need to run the top-level *MSSQLServer::CreateAsCatalogTarget* process to catalogue an entire server - the discovery of databases, schemas, tables and columns cascades from there.  Use the database-level process when you only want to catalogue a specific database on a server you have already surveyed.

<!-- SCREENSHOT PLACEHOLDER: mssql-catalogued-assets.png - the resulting RelationalDatabase / DeployedDatabaseSchema / RelationalTable assets shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued database, schema, table and column assets shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the *MSSQLContentPack*.  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `MSSQLServer:CreateAndSurveyGovernanceActionProcess`                  | Creates the *Microsoft SQL Server* asset and runs the Microsoft SQL Server Survey against it, printing out the resulting report. |
| `MSSQLServer::CreateAsCatalogTargetGovernanceActionProcess`           | Creates the *Microsoft SQL Server* asset and configures the Microsoft SQL Server Cataloguer to catalogue its databases.      |
| `MSSQLServer:DeleteAssetWithTemplateGovernanceActionProcess`          | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.              |
| `MSSQLDatabase:CreateAndSurveyGovernanceActionProcess`                | Creates a *Microsoft SQL Server Relational Database* asset and runs the Microsoft SQL Server Database Survey against it.     |
| `MSSQLDatabase::CreateAsCatalogTargetGovernanceActionProcess`         | Creates a *Microsoft SQL Server Relational Database* asset and configures the JDBC Database Cataloguer to catalogue it.      |
| `MSSQLDatabase:DeleteAssetWithTemplateGovernanceActionProcess`        | Deletes the database asset (and everything anchored to it) using the same template properties used to create it.            |

Each *CreateAndSurvey* process runs the same three steps as its PostgreSQL equivalent: create the asset, run the survey, then print the resulting report; each *CreateAsCatalogTarget* process runs two steps: create the asset, then attach it as a catalog target to the appropriate integration connector.


### Using the REST API

The REST calls below assume you have a running view server (`view-server` in these examples) and have already obtained a bearer token - see the [full `.http` collection](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/mssql-server-connectors/MSSQL-cataloguing.http) in the Egeria repository for the complete set of requests.

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

### Survey a Microsoft SQL Server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "MSSQLServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalMSSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1433",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "MSSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Microsoft SQL Server database server."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same Microsoft SQL Server (and its databases)
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "MSSQLServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalMSSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1433",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "MSSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Microsoft SQL Server database server."
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

To limit which databases are processed, add `includeDatabaseList` or `excludeDatabaseList` into the `requestParameters` of either call - for example:

```json
"requestParameters" : {
  "serverName" : "LocalMSSQL1",
  "hostIdentifier" : "localhost",
  "portNumber" : "1433",
  "secretsStorePathName" : "secrets/integration.omsecrets",
  "secretsCollectionName" : "MSSQL Server Secret",
  "excludeDatabaseList" : "dbBoring,dbNotUsed"
}
```

### Using pyegeria

This follows exactly the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the Microsoft SQL Server process names and default port (1433) substituted in:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what Microsoft SQL Server governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="MSSQL",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey a Microsoft SQL Server
request_parameters = {
    "serverName" : "LocalMSSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "1433",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "MSSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "Microsoft SQL Server database server.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "MSSQLServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "MSSQLServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

To follow progress of the integration connectors once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["MSSQLServerCataloguer", "JDBCDatabaseCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: mssql-integration-daemon-status.png - display_integration_daemon_status() output showing the Microsoft SQL Server Cataloguer and JDBC Database Cataloguer connectors running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the Microsoft SQL Server connectors.)*


## Related information

* [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - the equivalent solution for PostgreSQL; the two follow the same pattern and share the JDBC Database Cataloguer.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
