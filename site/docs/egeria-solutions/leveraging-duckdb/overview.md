
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your DuckDB estate

[DuckDB](https://duckdb.org/) is different from the other relational databases Egeria connects to: it is an **embedded, in-process OLAP engine**, not a client/server product.  A "DuckDB database" is either a single `.duckdb` file on disk, or an in-memory session - there is no server process to install, start or connect a network client to.  DuckDB is increasingly used as a lightweight analytical engine sitting in front of other data - it can query Parquet, CSV and JSON files directly, and its `ATTACH` capability lets it federate live with other databases (including PostgreSQL, SQLite and other DuckDB files) without copying data.

Egeria's *DuckDB connector* gives you oversight of a DuckDB database's own contents *and* the other data it reaches out to, without needing to open the file yourself:

* **Survey** a DuckDB database to build a picture of what it contains - how many schemas, tables, views and columns it has - and, distinctively, what other data sources it federates with, captured as a survey report.
* **Catalog** the database, turning it into an open metadata asset that can be searched, classified, linked to glossary terms and governed alongside the rest of your data landscape - with its schemas and tables catalogued automatically, and its federation relationships (attached databases and external file scans) catalogued as linked assets in their own right.
* Do both of these using **standard governance action processes**, so the same repeatable, automatable pattern is used as for Egeria's other database connectors.

This solution follows the same broad pattern as [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview), [Leveraging your Microsoft SQL Server estate](/egeria-solutions/leveraging-mssql/overview), [Leveraging your Oracle Database estate](/egeria-solutions/leveraging-oracle/overview) and [Leveraging your Db2 for Linux, UNIX and Windows estate](/egeria-solutions/leveraging-db2luw/overview), but DuckDB's embedded architecture and federation capability make it different enough from all four that it is worth reading this page in full rather than skimming for differences.


## DuckDB Technology Type Names

Because DuckDB has no server tier, Egeria's reference data for it is deliberately smaller than for the other relational databases - there is no *DuckDB Server* or *DuckDB database manager (RDBMS)* entry, and no tabular data set types:

* *DuckDB Relational Database* - An embedded, file-based (or in-memory) database managed by the DuckDB engine and accessed directly through its JDBC driver.
* *DuckDB Relational Database Schema* - A database schema hosted on a relational DuckDB database capable of being called through a JDBC Driver.

A DuckDB resource has up to a three-level name: *databaseName.schemaName.tableName.columnName* - there is no server name, since the database *is* the top-level resource.


## Connectors to DuckDB

The [DuckDB connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/duckdb-connectors) extend the generic [JDBC connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector), and reuse the same generic JDBC Database Cataloguer used by PostgreSQL, Microsoft SQL Server, Oracle and Db2 LUW to catalogue the database's own native schemas and tables:

| Connector Name                     | Connector Type                                                     | Purpose                                                                                                                                         |
|--------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **JDBC Resource Connector**        | [Digital Resource Connector](/concepts/digital-resource-connector)   | Provides access to a database via the standard JDBC `DataSource` interface.  Used by the survey and integration connectors below to connect to DuckDB. |
| **DuckDB Database Cataloguer**     | [Integration Connector](/concepts/integration-connector)             | Catalogs a DuckDB database attached as a catalog target: hands off its native schemas/tables/columns to the JDBC Database Cataloguer, then separately catalogues its federation relationships (attached databases and external file scans) - see [Cataloguing a DuckDB database](#cataloguing-a-duckdb-database) below. |
| **JDBC Database Cataloguer**       | [Integration Connector](/concepts/integration-connector)             | Catalogs the schemas, tables, columns, primary keys and foreign keys found inside a single database, whichever relational technology hosts it (including DuckDB). |
| **DuckDB Database Survey Service** | [Survey Action Service](/concepts/survey-action-service)             | Surveys a single DuckDB database - its schemas, tables and columns, and its federation relationships.                                            |

There is no server-level connector or survey service (DuckDB has no server to survey or catalogue), and no DuckDB-specific tabular data set connector.  These connectors, their template and the associated reference data are delivered together in the *DuckDBContentPack*.


## Surveying a DuckDB database

A survey is the recommended first step when you encounter a DuckDB database you don't already have documented in Egeria.  The **DuckDB Database Survey** service connects directly to the database (no server-level survey exists, since there is no server) and produces two kinds of finding: a structural profile of the database itself, and a report on what it federates with.

### The structural annotations

These reuse the same vendor-neutral annotation types as PostgreSQL, Microsoft SQL Server, Oracle and Db2 LUW, sourced from DuckDB's own catalog metadata table functions (`duckdb_schemas()`, `duckdb_tables()`, `duckdb_views()`, `duckdb_columns()`, `pragma_database_size()`) rather than a `pg_catalog`/`sys.*`/`SYSCAT` equivalent - but because DuckDB is embedded, it has no persistent workload-statistics infrastructure to draw on, so several fields that the other four connectors populate are simply absent here:

| Annotation Type                          | Attached to                | What it captures                                                                                                                   |
|--------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Database Measurements**        | The database                | Overall size (from `pragma_database_size()`), and counts of schemas/tables/columns.  There is no rows fetched/inserted/updated/deleted field at all - DuckDB has no equivalent of PostgreSQL's `pg_stat_database`. |
| **Capture Database Schema Measurements** | Each schema in the database | Counts of tables, views and columns.  There is no total table size field - DuckDB has no per-table byte-size catalog view.               |
| **Capture Database Table Measurements**  | Each table/view             | Table name, type (Table or View), column count, whether it has indexes, and the query definition (for views).  There is no table size, owner, row insert/update/delete counts, has-triggers or has-row-security field - DuckDB has none of these concepts. |
| **Capture Database Column Measurements** | Each column                 | Data type and whether nulls are allowed.  There is no average column width, distinct-value count or most-common-value field - DuckDB does not expose collected column statistics through a catalog view the way the other four connectors' source databases do. |

??? example "Example annotation from surveying the `analytics` database"
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture Database Table Measurements",
      "summary": "Capture summary statistics about a database table.",
      "explanation": "This annotation retrieves statistics about individual columns and aggregates them into a summary for the table.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "Table Qualified Name": "analytics.main.EMPLOYEE",
        "Table Name": "EMPLOYEE",
        "Table Type": "Table",
        "Number of columns": "8",
        "Has Indexes": "false"
      }
    }
    ```

### The federation annotations

DuckDB's `ATTACH` statement can federate the database with another DuckDB file, a PostgreSQL server, a SQLite file, or (via extensions) object storage; and a view can be defined directly over an external file or object-store resource using table functions like `read_parquet()`, `read_csv()`, `read_json()`, `iceberg_scan()` or `delta_scan()`.  None of this is captured by the vendor-neutral annotation types above, so the survey adds two DuckDB-specific annotation types of its own:

| Annotation Type                          | Attached to     | What it captures                                                                                                                   |
|--------------------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Capture Attached Data Source**         | The database      | One annotation per non-internal entry in `duckdb_databases()`: the alias it was `ATTACH`-ed under, its source type, its (password-redacted) location, and whether it is read-only. |
| **Capture External File Data Source**    | The database      | One annotation per external-scan view found in `duckdb_views()`: the view name, the scan function used (`read_parquet()` etc, detected by pattern-matching the view's SQL definition), the file/object-store location, and the inferred format. |

??? example "Example federation annotations"
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture Attached Data Source",
      "summary": "Capture details of a data source that has been attached to the DuckDB database using its ATTACH federation capability.",
      "explanation": "This annotation is created once for each non-internal entry found in DuckDB's duckdb_databases() table function.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "Alias": "mypg",
        "Source Type": "postgres",
        "Location": "host=myhost dbname=mydb user=myuser password=***",
        "Read Only": "true"
      }
    }
    ```
    ```json
    {
      "class": "ResourceMeasureAnnotation",
      "annotationType": "Capture External File Data Source",
      "summary": "Capture details of an external file, or object-store, resource that is scanned by a view defined in the DuckDB database using functions such as read_parquet(), read_csv(), read_json(), iceberg_scan() or delta_scan().",
      "explanation": "This annotation is created once for each external-scan view found in DuckDB's duckdb_views() table function.",
      "analysisStep": "Profiling Associated Resources",
      "resourceProperties": {
        "View Name": "monthly_sales",
        "Scan Function": "read_parquet",
        "Location": "s3://my-bucket/sales/2026/*.parquet",
        "Format": "parquet"
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: duckdb-survey-report-annotations.png - the structural and federation annotations produced by a DuckDB database survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its annotations, as displayed against the surveyed asset in the Egeria UI.)*


### How the survey avoids touching your business data

The survey only ever queries DuckDB's own catalog metadata table functions and `pragma_database_size()` - it never runs a `SELECT` against your business tables, and the `Location` value recorded for an attached data source has any password stripped out of the connection string before it is written to open metadata.


## DuckDB has no controllable "which databases" list

The include/exclude configuration properties that let you narrow a PostgreSQL, Microsoft SQL Server, Oracle or Db2 LUW server survey/cataloguer down to particular databases do not apply here - a DuckDB catalog target is already a single database (there is nothing above it to narrow from).  Once inside that database, the **JDBC Database Cataloguer** integration connector still offers the usual `includeSchemaNames`/`excludeSchemaNames`, `includeTableNames`/`excludeTableNames`, `includeViewNames`/`excludeViewNames` and `includeColumnNames`/`excludeColumnNames` properties, exactly as it does for the other four relational technologies.


## Cataloguing a DuckDB database

Cataloguing a DuckDB database starts the **DuckDB Database Cataloguer** against the *DuckDB Relational Database* asset (created from its template), which does three things on every refresh:

1. **Identifies the asset.**  For a file-based database, it uses the same *FileClassifier* logic that the [Files connectors](/egeria-solutions/leveraging-files/overview) use, so the database's catalogued identity is tied to its canonical (masked) file path.  This step is skipped for an in-memory (`:memory:`) database.
2. **Hands off native cataloguing.**  It attaches the JDBC Database Cataloguer to the database via the same "friendship" pattern used by the PostgreSQL, Microsoft SQL Server, Oracle and Db2 LUW connectors, so the database's own schemas, tables, columns, primary keys and foreign keys are catalogued the standard way.
3. **Catalogues federation relationships.**  This is DuckDB-specific.  It re-issues any configured `attachStatements` (needed because DuckDB does not persist `ATTACH`-ed data sources in the database file between sessions - every new connection has to `ATTACH` them again itself), then:
    - For each **attached database**, it resolves or creates an asset for the attached source - reusing the same file-matching logic as step 1 for a file-backed source (another DuckDB file, or SQLite), or treating it as a network-backed resource otherwise - and links it to the DuckDB database with a *"Database attached to the DuckDB database via ATTACH"* resource-list relationship.  Because there is no friendship-connector-catalogued representation to link to for a foreign network source, its tables are catalogued directly as `TabularDataSet` assets.
    - For each **external file scan**, it resolves the scanned file (or object-store location) as a file asset using the same FileClassifier logic, and links the DuckDB view's columns to the file's columns as `DerivedSchemaTypeQueryTarget` lineage - so a query like `SELECT column FROM monthly_sales` shows up as column-level lineage back to the Parquet file it actually reads from.

Each federation finding is handled defensively - a problem resolving or cataloguing one attached source or external file does not stop the rest of the pass.

<!-- SCREENSHOT PLACEHOLDER: duckdb-catalogued-assets.png - the catalogued DuckDB database, its native RelationalTable assets, and its federation relationships to attached databases and external files, shown in the Egeria UI. -->
*(Screenshot to follow: the catalogued database, its native tables, and its federation relationships to attached sources and external files, shown in the Egeria UI.)*


## Running this through the Automated Curation API

All of the capabilities above are packaged as ready-to-run **governance action processes**, delivered by the *DuckDBContentPack*.  You initiate them through the [Automated Curation](/services/omvs/automated-curation/overview) API of a view server - either directly over REST, or through **pyegeria**.  Because DuckDB has no server tier, there is only one level of process - there is no server-level equivalent the way there is for PostgreSQL, Microsoft SQL Server, Oracle and Db2 LUW:

| Governance Action Process                                            | What it does                                                                                                                 |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `DuckDBDatabase:CreateAndSurveyGovernanceActionProcess`                | Creates the *DuckDB Relational Database* asset and runs the DuckDB Database Survey against it, printing out the resulting report. |
| `DuckDBDatabase::CreateAsCatalogTargetGovernanceActionProcess`         | Creates the *DuckDB Relational Database* asset and configures the DuckDB Database Cataloguer to catalogue it.               |
| `DuckDBDatabase:DeleteAssetWithTemplateGovernanceActionProcess`        | Deletes the database asset (and everything anchored to it) using the same template properties used to create it.            |

Each *CreateAndSurvey* process runs the same three steps as its PostgreSQL, Microsoft SQL Server, Oracle and Db2 LUW equivalents: create the asset, run the survey, then print the resulting report; the *CreateAsCatalogTarget* process runs two steps: create the asset, then attach it as a catalog target to the DuckDB Database Cataloguer.


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

### Survey a DuckDB database
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "DuckDBDatabase:CreateAndSurveyGovernanceActionProcess",
  "requestParameters" : {
    "databasePath" : "/data/databases/analytics.duckdb",
    "databaseName" : "analytics",
    "versionIdentifier" : "1.0",
    "description" : "DuckDB analytical database."
  }
}

> {% client.global.set("surveyInstanceGUID", response.body.guid); %}

### Catalog the same DuckDB database
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/automated-curation/governance-action-processes/initiate
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "processQualifiedName": "DuckDBDatabase::CreateAsCatalogTargetGovernanceActionProcess",
  "requestParameters" : {
    "databasePath" : "/data/databases/analytics.duckdb",
    "databaseName" : "analytics",
    "versionIdentifier" : "1.0",
    "description" : "DuckDB analytical database."
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

Notice there is no `hostIdentifier`/`portNumber` - `databasePath` (or the literal `:memory:` for an in-memory database) is how a DuckDB database is located, since it is a file rather than a network service.  If the database uses `ATTACH` to federate with other data, add `attachStatements` to `requestParameters` so the cataloguer and survey connectors can re-establish those federation relationships on their own connections - for example:

```json
"requestParameters" : {
  "databasePath" : "/data/databases/analytics.duckdb",
  "databaseName" : "analytics",
  "attachStatements" : "INSTALL postgres,LOAD postgres,ATTACH 'host=myhost dbname=mydb user=myuser password=mypassword' AS mypg (TYPE POSTGRES, READ_ONLY)"
}
```

### Using pyegeria

This follows the same pattern as the [PostgreSQL pyegeria walkthrough](/egeria-solutions/leveraging-postgres/overview#using-pyegeria) - just with the DuckDB process names and `databasePath`/`databaseName` substituted for `hostIdentifier`/`portNumber`:

```python
from pyegeria import EgeriaTech, load_mermaid, render_mermaid

view_server = "qs-view-server"
url         = "https://host.docker.internal:9443"
user_id     = "erinoverview"
user_pwd    = "secret"

egeria_tech = EgeriaTech(view_server, url, user_id, user_pwd)
token = egeria_tech.create_egeria_bearer_token()

# See what DuckDB governance action processes are available
elements = egeria_tech.find_elements_by_property_value(
    property_value="DuckDB",
    property_names=["qualifiedName"],
    metadata_element_type_name="GovernanceActionProcess",
)
for element in elements:
    properties = element.get("properties")
    print("* " + properties.get("qualifiedName") + " - " + properties.get("description"))

# Survey a DuckDB database
request_parameters = {
    "databasePath" : "/data/databases/analytics.duckdb",
    "databaseName" : "analytics",
    "versionIdentifier" : "1.0",
    "description" : "DuckDB analytical database.",
}

survey_instance_guid = egeria_tech.initiate_gov_action_process(
    "DuckDBDatabase:CreateAndSurveyGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)

# Watch the process run as a mermaid diagram
load_mermaid()
process_graph = egeria_tech.get_governance_process_graph(survey_instance_guid)
render_mermaid(process_graph.get("governanceActionProcessMermaidGraph"))

# Once you're happy with what the survey found, catalog the database too
catalog_instance_guid = egeria_tech.initiate_gov_action_process(
    "DuckDBDatabase::CreateAsCatalogTargetGovernanceActionProcess",
    None, None, None, request_parameters, None, None,
)
```

To follow progress of the integration connectors once cataloguing has started, use:

```python
from commands.ops.monitor_daemon_status import display_integration_daemon_status

display_integration_daemon_status(
    ["DuckDBDatabaseCataloguer", "JDBCDatabaseCataloguer"],
    integ_server="qs-integration-daemon",
    paging=True,
    width=150,
)
```

<!-- SCREENSHOT PLACEHOLDER: duckdb-integration-daemon-status.png - display_integration_daemon_status() output showing the DuckDB Database Cataloguer and JDBC Database Cataloguer connectors running. -->
*(Screenshot to follow: `display_integration_daemon_status()` output for the DuckDB connectors.)*


## Related information

* [Leveraging your PostgreSQL estate](/egeria-solutions/leveraging-postgres/overview) - the equivalent solution for PostgreSQL, and the source of the JDBC Database Cataloguer that DuckDB's own schemas and tables are catalogued through.
* [Leveraging your Db2 for Linux, UNIX and Windows estate](/egeria-solutions/leveraging-db2luw/overview) - another connector without a server-wide auto-discovery capability, though for a different reason (no cross-database catalog view, rather than no server at all).
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports, annotations and analysis steps.
* [Automated Curation](/services/omvs/automated-curation/overview) - the API used to initiate governance action processes.

--8<-- "snippets/abbr.md"
