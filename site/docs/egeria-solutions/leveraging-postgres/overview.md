
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your PostgreSQL estate

Many organizations have hundreds of [PostgreSQL](https://www.postgresql.org/) databases spread across many servers.  Some support production applications, others are extracts created for a specific project, working copies used for analysis, or temporary databases that have outlived the task they were created for.  Over time, it is easy to lose track of what each database contains, whether it is still in active use, how up-to-date its data is, and how much it can be trusted.

Egeria's *PostgreSQL connectors* give you oversight of this estate without needing to log into every server and inspect it by hand.  They can:

* **Survey** a PostgreSQL server, or an individual database, to build a picture of what it contains - how many schemas, tables, views and columns it has, how large they are, and how actively they are being used - and capture that picture as a survey report.
* **Catalog** all, or a selected subset, of the databases, schemas, tables and columns found by a survey, turning them into open metadata assets that can be searched, classified, linked to glossary terms and governed alongside the rest of your data landscape.
* Do both of these using **standard governance action processes**, so the same repeatable, automatable pattern is used whether you are onboarding one database or an entire estate of servers.

Because the survey works from PostgreSQL's own system catalog (`pg_catalog`), it can build this picture without needing read access to the business data stored in your tables. See [How the survey avoids touching your business data](#how-the-survey-avoids-touching-your-business-data) below.


## PostgreSQL Technology Type Names

The technology type names (aka [deployed implementation types](/concepts/deployed-implementation-type)) added to Egeria's reference data for PostgreSQL are:

* *PostgreSQL Server* - A database server running the PostgreSQL software.  PostgreSQL is an advanced open source relational database.
* *PostgreSQL database manager (RDBMS)* - The PostgreSQL capability that manages collections of data called relational databases which in turn are organized into a tabular format and accessed via the Structured Query Language (SQL).
* *PostgreSQL Relational Database* - A database hosted on a PostgreSQL server.
* *PostgreSQL Relational Database Schema* - A database schema hosted on a PostgreSQL relational database server capable of being called through a JDBC Driver.
* *PostgreSQL Tabular Data Set* - A database table hosted on a PostgreSQL relational database server that has the tabular data set interface.
* *PostgreSQL Tabular Data Set Collection* - A database schema hosted on a PostgreSQL relational database server that has the tabular data set collection interface.

As a result of this structure, a PostgreSQL resource has up to a four-level name: *serverName.databaseName.schemaName.tableName.columnName*, with the database schema defaulting to `public` if none is specified.


## Connectors to PostgreSQL

The [PostgreSQL connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/postgres-server-connectors) extend the generic [JDBC connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) with PostgreSQL-specific queries against its system catalog.

--8<-- "snippets/blueprints/components/postgresql-server-mermaid-graph.md"

| Connector Name                          | Connector Type                                                      | Purpose                                                                                                                                                     |
|------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC Resource Connector**             | [Digital Resource Connector](/concepts/digital-resource-connector)   | Provides access to a database via the standard JDBC `DataSource` interface.  Used by the survey and integration connectors below to connect to PostgreSQL.  |
| **PostgreSQL Server Cataloguer**        | [Integration Connector](/concepts/integration-connector)             | Catalogs the databases found on a PostgreSQL server, creating a *RelationalDatabase* asset (with a JDBC connection) for each one.                            |
| **JDBC Database Cataloguer**            | [Integration Connector](/concepts/integration-connector)             | Catalogs the schemas, tables, columns, primary keys and foreign keys found inside a single database, whichever relational technology hosts it (including PostgreSQL). |
| **PostgreSQL Server Survey**            | [Survey Action Service](/concepts/survey-action-service)             | Surveys all (or a selected subset of) the databases hosted by a PostgreSQL server.                                                                            |
| **PostgreSQL Database Survey**          | [Survey Action Service](/concepts/survey-action-service)             | Surveys the schemas, tables and columns of a single, already catalogued, PostgreSQL database.                                                                 |
| **PostgreSQL Tabular Data Set Connector**| [Digital Resource Connector](/concepts/digital-resource-connector)   | Reads and writes the data in a single PostgreSQL table once it is being used as part of a pipeline or data product.                                          |
| **PostgreSQL Tabular Data Set Collection Connector** | [Digital Resource Connector](/concepts/digital-resource-connector) | Manages a collection of PostgreSQL tables as a set of tabular data sets.                                                                                     |

These connectors, their templates and the associated reference data are all delivered together in the [PostgreSQL Content Pack](/content-packs/postgres-content-pack/overview).


## Surveying a PostgreSQL server or database

A survey is the recommended first step when you encounter a PostgreSQL server you don't already have documented in Egeria.  It answers the question "what is actually in here?" before you commit to cataloguing anything.

There are two survey action services, matching the two levels you can point a survey at:

* The **PostgreSQL Server Survey** connects to the server (via the built-in `postgres` maintenance database) and queries `pg_database` to find the databases it hosts.  It then works through each qualifying database in turn, gathering statistics.
* The **PostgreSQL Database Survey** does the same job for a single database that has already been catalogued as an asset - useful when you only want to refresh the picture of one database rather than re-survey the whole server.

Both survey services record their findings as a series of **annotations** attached to a **survey report**, which in turn is linked to the asset that was surveyed (the server or the database).  See [Open Survey Framework](/frameworks/osf/overview) for background on survey reports and annotations generally.

### The annotations produced

The survey builds up its picture one level at a time - database, then schema, then table, then column - and produces one *Resource Measure Annotation* ([0660](/types/6/0660-Resource-Measures)) for each element it finds:

| Annotation Type                          | Attached to                | What it captures                                                                                                                   |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Database Measurements**        | The database (or server)   | Overall size, and counts of schemas/tables/views/columns; rows fetched, inserted, updated and deleted; session and active time; when statistics were last reset. |
| **Capture Database Schema Measurements** | Each schema in the database| Total size of the tables in the schema; counts of tables, views, materialized views and columns.                                       |
| **Capture Database Table Measurements**  | Each table/view             | Size in bytes; owner; whether it is a table, view or materialized view; whether it has indexes, rules, triggers or row security; row insert/update/delete counts; the query definition (for views). |
| **Capture Database Column Measurements** | Each column                 | Data type, average width, size, whether nulls are allowed, the number of distinct values, and the most common values with their frequencies. |

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
        "Data size": "9871360",
        "Number of schemas": "1",
        "Number of tables": "2",
        "Number of columns": "10",
        "Rows Fetched": "18432",
        "Rows Inserted": "612",
        "Rows Updated": "44",
        "Rows Deleted": "0",
        "Session Time": "451220.5",
        "Active Time": "38221.2",
        "Last statistics reset": "2026-06-01"
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
        "Table Qualified Name": "EMPLOYEE.public.EMPLOYEE",
        "Table Name": "EMPLOYEE",
        "Resource Owner": "postgres",
        "Table Type": "Table",
        "Table Size": "245760",
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
        "Column qualified name": "EMPLOYEE.public.EMPLOYEE.EMPSTATUS",
        "Column name": "EMPSTATUS",
        "Column data type": "int4",
        "Not Null": "true",
        "Average Column Width": "4",
        "Number Of Distinct Values": "3",
        "Most Common Values": "{1,2,3}",
        "Most Common Values Frequency": "{0.62,0.31,0.07}"
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: postgres-survey-report-annotations.png - the annotations produced by a PostgreSQL Server survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed asset in the Egeria UI.)*


### How the survey avoids touching your business data

The survey connectors only ever query PostgreSQL's own system catalog - the `pg_catalog` schema and its views (`pg_database`, `pg_stat_database`, `pg_tables`, `pg_stats`, `pg_views`, `pg_matviews`, and the `pg_table_size()`/`pg_column_size()` functions).  They never run a `SELECT` against your business tables.  This means:

* The database user configured for the survey only needs `CONNECT` privilege on the databases being surveyed - it does not need `SELECT` grants on any business table.
* Row counts, sizes and activity levels come from PostgreSQL's internal statistics collector, not from scanning the tables themselves.

One nuance worth knowing: the *Most Common Values* and *Most Common Values Frequency* measurements on a column do contain a small number of real, representative data values.  These come from `pg_stats`, which PostgreSQL itself populates by sampling the table whenever `ANALYZE` runs (typically as part of routine autovacuum activity) - not from a live read performed by the Egeria connector.  If you need to exclude that level of detail for particularly sensitive columns, use the include/exclude controls described next.


## Controlling what is surveyed or catalogued

By default, surveying or cataloguing a PostgreSQL server processes every database it hosts (except the built-in `postgres` maintenance database, which is always skipped).  You can narrow - or widen - this using configuration properties on the connector.

At the **server** level (both the PostgreSQL Server Survey and the PostgreSQL Server Cataloguer integration connector honour these):

| Configuration Property      | Purpose                                                                                          | Example                     |
|------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
| `includeDatabaseList`       | Only the named databases are surveyed/catalogued.  If unset, null or `*`, all databases except those excluded are processed. | `["EMPLOYEE", "PATIENT"]`   |
| `excludeDatabaseList`       | The named databases are skipped.  Defaults to `["postgres"]` if not set.                          | `["dbBoring", "dbNotUsed"]`  |

Once inside a specific database, the **JDBC Database Cataloguer** integration connector offers the same include/exclude pattern one level down, for schemas, tables, views and columns:

| Configuration Property      | Purpose                                                        |
|------------------------------|--------------------------------------------------------------------|
| `includeSchemaNames` / `excludeSchemaNames` | Which schemas to catalogue (or skip).                 |
| `includeTableNames` / `excludeTableNames`   | Which tables to catalogue (or skip).                  |
| `includeViewNames` / `excludeViewNames`     | Which views to catalogue (or skip).                   |
| `includeColumnNames` / `excludeColumnNames` | Which columns to catalogue (or skip).                 |

An `include...` list always wins over the corresponding `exclude...` list - use it when you only want a handful of named schemas/tables/columns out of a much larger database, and the `exclude...` lists when you want everything *except* a short list of items you know you don't want (temporary tables, staging areas, columns holding especially sensitive data, and so on).

These properties are set as `configurationProperties` on the integration connector, or passed as `requestParameters` when the governance action process configures the connector for you (see below).


## Cataloguing a PostgreSQL server, database or schema

Cataloguing turns what the survey found into open metadata assets you can search, classify and link to the rest of your metadata - glossary terms, governance definitions, data products, and so on.  Egeria provides a [template](/catalog-templates/postgres-server-templates) for each level of the PostgreSQL hierarchy, and a matching *CreateAsCatalogTarget* governance action process that creates the asset from the template and then configures the right integration connector to keep it synchronized:

* **PostgreSQL Server** - creates the *SoftwareServer* asset and starts the **PostgreSQL Server Cataloguer**, which discovers and catalogues its databases (subject to the include/exclude lists above).
* **PostgreSQL Relational Database** - creates the *RelationalDatabase* asset and starts the **JDBC Database Cataloguer** against it, which catalogues its schemas, tables, columns, primary keys and foreign keys.
* **PostgreSQL Relational Database Schema** - creates the *DeployedDatabaseSchema* asset scoped to a single schema, again backed by the JDBC Database Cataloguer.

Because cataloguing a server automatically configures the JDBC Database Cataloguer for the databases it finds, you typically only need to run the top-level *PostgreSQLServer::CreateAsCatalogTarget* process to catalogue an entire server - the discovery of databases, schemas, tables and columns cascades from there.  Use the database- or schema-level processes when you only want to catalogue a specific part of a server that you have already surveyed.

<!-- SCREENSHOT PLACEHOLDER: postgres-catalogued-assets.png - the resulting RelationalDatabase / DeployedDatabaseSchema / RelationalTable assets shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued database, schema, table and column assets shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the [PostgreSQL Content Pack](/content-packs/postgres-content-pack/overview).  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `PostgreSQLServer:CreateAndSurveyGovernanceActionProcess`             | Creates the *PostgreSQL Server* asset and runs the PostgreSQL Server Survey against it, printing out the resulting report.  |
| `PostgreSQLServer::CreateAsCatalogTargetGovernanceActionProcess`      | Creates the *PostgreSQL Server* asset and configures the PostgreSQL Server Cataloguer to catalogue its databases.           |
| `PostgreSQLServer:DeleteAssetWithTemplateGovernanceActionProcess`     | Deletes the server asset (and everything anchored to it) using the same template properties used to create it.             |
| `PostgreSQLDatabase:CreateAndSurveyGovernanceActionProcess`           | Creates a *PostgreSQL Relational Database* asset and runs the PostgreSQL Database Survey against it.                        |
| `PostgreSQLDatabase::CreateAsCatalogTargetGovernanceActionProcess`    | Creates a *PostgreSQL Relational Database* asset and configures the JDBC Database Cataloguer to catalogue it.               |
| `PostgreSQLDatabase:DeleteAssetWithTemplateGovernanceActionProcess`   | Deletes the database asset (and everything anchored to it) using the same template properties used to create it.           |
| `PostgreSQLDatabaseSchema::CreateAsCatalogTargetGovernanceActionProcess` | Creates a *PostgreSQL Relational Database Schema* asset and configures the JDBC Database Cataloguer to catalogue it.     |
| `PostgreSQLDatabaseSchema:DeleteAssetWithTemplateGovernanceActionProcess`| Deletes the schema asset (and everything anchored to it) using the same template properties used to create it.           |

Below are the flows for the two most commonly used processes, showing the request parameters each one accepts:

=== "CreateAndSurvey"

    --8<-- "snippets/governance-action-processes/postgresqlserver:createandsurvey-mermaid-graph.md"

=== "CreateAsCatalogTarget"

    --8<-- "snippets/governance-action-processes/postgresqlserver::createascatalogtarget-mermaid-graph.md"


### Using the REST API

The REST calls below assume you have a running view server (`view-server` in these examples) and have already obtained a bearer token - see the [full `.http` collection](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/postgres-server-connectors/Postgres-cataloguing.http) in the Egeria repository for the complete set of requests.

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

### Survey a PostgreSQL server
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "PostgreSQLServer:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalPostgreSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "5442",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "PostgreSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "PostgreSQL database server."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same PostgreSQL server (and its databases)
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "PostgreSQLServer::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "serverName" : "LocalPostgreSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "5442",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "PostgreSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "PostgreSQL database server."
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
  "serverName" : "LocalPostgreSQL1",
  "hostIdentifier" : "localhost",
  "portNumber" : "5442",
  "secretsStorePathName" : "secrets/integration.omsecrets",
  "secretsCollectionName" : "PostgreSQL Server Secret",
  "excludeDatabaseList" : "dbBoring,dbNotUsed"
}
```

### Using pyegeria

The [`survey-and-catalog-postgres.ipynb`](https://github.com/odpi/egeria-workspaces/blob/main/workbooks/cataloguing-and-surveys/postgres/survey-and-catalog-postgres.ipynb) notebook in `egeria-workspaces` walks through this end to end.  The essentials:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what PostgreSQL governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="PostgreSQL",
    property_names=["displayName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey a PostgreSQL server
request_parameters = {
    "serverName" : "LocalPostgreSQL1",
    "hostIdentifier" : "localhost",
    "portNumber" : "5442",
    "secretsStorePathName" : "secrets/integration.omsecrets",
    "secretsCollectionName" : "PostgreSQL Server Secret",
    "versionIdentifier" : "1.0",
    "description" : "PostgreSQL database server.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "PostgreSQLServer:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the server too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "PostgreSQLServer::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

`pyegeria`'s `AutomatedCuration` client also has purpose-built, higher-level calls if you would rather drive the template and survey steps individually rather than through the combined governance action process - `create_postgres_server_element_from_template()` to create the server asset from its template, and `initiate_postgres_server_survey()` / `initiate_postgres_database_survey()` to run just the survey against an existing asset.

To follow progress of the integration connectors once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["PostgreSQLServerCataloguer", "JDBCDatabaseCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: postgres-integration-daemon-status.png - display_integration_daemon_status() output showing the PostgreSQL Server Cataloguer and JDBC Database Cataloguer connectors running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the PostgreSQL connectors.)*


## Related information

* [PostgreSQL Content Pack](/content-packs/postgres-content-pack/overview) - the connectors, templates and reference data bundle described on this page.
* [PostgreSQL Server Templates](/catalog-templates/postgres-server-templates) - the templates used when cataloguing PostgreSQL resources.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
