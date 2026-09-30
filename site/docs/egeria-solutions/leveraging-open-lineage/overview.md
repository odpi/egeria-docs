
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging Open Lineage

Most processing engines - Apache Spark, Apache Airflow, dbt, ETL tools and countless custom jobs - either produce no lineage information at all, or produce it in their own proprietary format.  [Open Lineage](https://github.com/OpenLineage/OpenLineage) is a sister open source project to Egeria in the [LF AI and Data Foundation](https://lfaidata.foundation/) that gives these engines a common, vendor-neutral way to report what they did: which data they read, what they wrote, and how the two are connected.

Egeria is able to receive, store, route and act on Open Lineage events.  This means it can:

* **Harvest** information about the data stores and processes that are emitting Open Lineage events, adding them to open metadata as they are discovered.
* **Store** the Open Lineage events in an organized way, either in its own file-based log store or in an external Open Lineage-compliant server such as [Marquez](https://marquezproject.github.io/marquez/), so they are available for later analysis.
* **Route** Open Lineage events to other services - both events received from external processing engines, and events that Egeria generates itself from the [governance actions](/concepts/engine-action) it runs.

This makes Open Lineage one of the main ways that *operational* (dynamic, "what actually ran") lineage gets into Egeria's lineage graph, alongside the *design* (static) lineage captured by cataloguing.  See [Lineage Management](/features/lineage-management/overview) for the complete picture of how captured lineage - from Open Lineage and other sources - is stitched together and preserved.


## The Open Lineage standard

When a processing engine such as Apache Spark runs a process, it produces a series of *RunEvents* describing the activity of that process.  The Open Lineage standard defines the format of these events and a single, simple REST API operation, `{{urlroot}}/api/v1/lineage`, that receives them.

![The Open Lineage standard defines the payload for RunEvents as well as a standard URL for a service that acts as a collection point for them.](/features/lineage-management/open-lineage-standard-defines.svg)

A RunEvent has eight parts:

* *eventType* - the type of activity being described.
* *eventTime* - the time of the event.
* *run* - the description of the process instance.
* *job* - the description of the process.
* *inputs* - the data sources used as inputs by the process instance.
* *outputs* - the data sources that hold the output of the process instance.
* *producer* - the name/location of the processing engine producing the events.
* *schemaURL* - the location of the JSON schema that describes the structure of the RunEvent.

![The structure of a RunEvent.](/features/lineage-management/open-lineage-payload-run-event.svg)

Events also carry `additionalProperties` called *facets* - extensions that add detail such as documentation links, schema information, SQL text or data quality metrics.  Any organization or processing engine can define its own custom facets alongside the standard ones.

See [The Open Lineage Standard](/features/lineage-management/overview/#the-open-lineage-standard) for the full set of standard facets and how they are structured.


## Egeria's Open Lineage support

Egeria offers two ways to capture Open Lineage events from processing engines, depending on how the engine publishes them.

Many processing engines publish through the Open Lineage project's own *proxy backend* - a lightweight side-car that receives events over the API and republishes them to a Kafka topic.  Egeria's [Open Lineage Event Receiver :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#open-lineage-event-receiver-integration-connector){ target=gh } integration connector listens on that topic:

![Receiving events via the Kafka topic populated by the proxy backend.](/features/lineage-management/open-lineage-async-egeria-integration.svg)

Alternatively, Egeria's [integration daemon](/concepts/integration-daemon) can implement the Open Lineage API directly, so a local processing engine can send its events straight to Egeria without needing a proxy backend or a Kafka topic in between:

![Receiving events via the Open Lineage API directly into the integration daemon.](/features/lineage-management/open-lineage-direct-egeria-integration.svg)

### The Open Lineage connectors

However they arrive, events are handed to the integration daemon's context manager, which distributes them to whichever [integration connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors) have registered as listeners.  Five connectors are supplied by Egeria, falling into two groups: those that *acquire or create* Open Lineage events, and those that *process or distribute* them.

| Connector Name                                                                                                        | Purpose                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Open Lineage Event Receiver :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#open-lineage-event-receiver-integration-connector){ target=gh }**          | Receives Open Lineage events from a Kafka topic and passes them, via the integration daemon, to any other connectors in the same daemon that have registered as Open Lineage listeners.              |
| **[Governance Action Open Lineage :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#governance-action-open-lineage-integration-connector){ target=gh }**    | Listens for [engine actions](/concepts/engine-action) executing in the open metadata ecosystem and generates the equivalent Open Lineage events for them - so Egeria's own governance processing shows up in the same lineage picture as external processing engines. |
| **[API-based Open Lineage Log Store :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#api-based-open-lineage-log-store-integration-connector){ target=gh }**| Registers as a listener and forwards every event it receives on to a remote server that implements the Open Lineage API, such as Marquez.                                                            |
| **[File-based Open Lineage Log Store :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#file-based-open-lineage-log-store-integration-connector){ target=gh }**| Registers as a listener and writes every event it receives to its own file, in JSON format, in a nominated folder - organized by the namespace and job name in the event.                          |
| **[Open Lineage Cataloguer :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#open-lineage-cataloguer-integration-connector){ target=gh }**                  | Registers as a listener and catalogues what the events describe: jobs become [Processes](/types/2/0215-Software-Components), datasets become data assets (matched to assets already catalogued by other connectors where possible), and inputs and outputs are linked to the process with lineage relationships.  It maintains the [*RunMetrics*](/types/2/0215-Software-Components) classification on each process and, optionally, the [*DataScope*](/types/2/0210-Data-Stores) classification on the data assets, captures data quality results as survey reports and catalogues each run as a *TransientEmbeddedProcess*.  See [Cataloguing the events](#cataloguing-the-events) below.       |

The diagram below shows all five working together in a single integration daemon:

![The pre-built integration connectors supplied by Egeria.](/features/lineage-management/open-lineage-integration-connectors.svg)

1. A third-party processing engine sends Open Lineage events either directly to Egeria's Open Lineage API endpoint, or via a proxy backend to a Kafka topic.
2. The Open Lineage Event Receiver picks up events from the Kafka topic and hands them to the integration daemon's context manager.
3. The Governance Action Open Lineage connector registers a listener for engine actions running in the open metadata ecosystem, generates Open Lineage events to represent that processing, and hands them to the context manager too - so both sources of events flow through the same pipeline.
4. Any connector wanting to receive events - the two log store connectors and the cataloguer - registers a listener with the context manager, and from then on receives every event that arrives.
5. The API-based and file-based Open Lineage Log Store connectors write each event to their configured destination (a remote Open Lineage API server, or a local file), while the Open Lineage Cataloguer uses each event to make sure the job and datasets it describes are represented in open metadata and linked by lineage.

Because any combination of these connectors can be configured in the same integration daemon, you can, for example, catalog processes *and* archive the raw events to Marquez *and* forward Egeria's own governance action activity into the same picture, all at once.


### Cataloguing the events

The Open Lineage Cataloguer maps each run event into open metadata as it arrives.  The namespace and name that Open Lineage gives each job and dataset are extracted from the technology itself, following the [Open Lineage naming conventions](https://openlineage.io/docs/spec/naming/), so they are the most reliable identity for a resource.  The cataloguer's first job is to use them to find the elements that already describe the resource, so that the lineage from the events joins up with what other connectors have catalogued rather than building a parallel picture.

#### Datasets

The lineage is attached to the elements that describe the *physical* landscape - the tables, topics and files catalogued by Egeria's technology connectors.  The cataloguer finds every element that describes a dataset:

* elements whose *resourceName* and *namespacePath* are the dataset's name and namespace;
* elements catalogued by technology connectors, found through the endpoints of their connections.  For example, the dataset `sales.public.orders` in the namespace `postgres://db` is matched to the *RelationalTable* that the PostgreSQL connectors catalogued for the database whose endpoint is `jdbc:postgresql://db:5432/sales`.  The spelling of the scheme and any default port are normalized before the comparison.  Kafka topics, local files and Unity Catalog tables are matched in the same way;
* for a dataset in the `egeria` namespace, the element whose qualified name is the dataset's name.  This is how Egeria's own governance actions name data that has no Open Lineage identity.

The matches fall into two groups:

* **Physical elements.**  One of them is chosen to receive the lineage: elements catalogued by technology connectors are preferred over elements created from Open Lineage events, and the oldest is preferred within each group.  Any other physical match is linked to the chosen element with a *PeerDuplicateLink* for the [duplicate management](/features/duplicate-management/overview) process to resolve.
* **Abstractions** - *TabularDataSet* and *TabularDataSetCollection* assets, such as the data sets offered by digital products.  They never receive lineage themselves.  Instead each is linked to the physical element that it is a view over with a [*DataSetContent*](/types/2/0210-Data-Stores) relationship.

The cataloguer only updates the properties, schema, names and lifecycle of assets that it created itself.  Elements catalogued by technology connectors are left as their connectors maintain them, apart from gaining an owner and the Open Lineage identity if they have none.

#### Datasets and jobs that are not catalogued yet

When nothing describes a dataset or job, the cataloguer creates it from the [catalog template](/features/templated-cataloguing/overview) for its technology, so that it has the right open metadata type and technology type (*deployedImplementationType*).

* **Datasets.**  The technology is identified by the namespace scheme.  For example, a `snowflake://` dataset becomes a *Snowflake Table* (a *DataSet*), an `s3://` dataset becomes an *Amazon S3 Object* (a *DataFile*), or an *Amazon S3 Folder* when the name ends with `/`, and a `kafka://` dataset becomes an *Apache Kafka Topic*.  Templates cover the relational databases, data warehouses, NoSQL stores, object and file stores, document management systems and event streams named in the Open Lineage naming conventions.  A dataset from an unrecognized technology becomes a generic *DataStore*, which can be retyped to a more specific subtype later.
* **Jobs.**  The technology is identified by the *jobType* job facet.  For example, an Airflow task becomes an *Apache Airflow Task*, and its parent job becomes an *Apache Airflow DAG*.  Spark jobs, Debezium connector tasks and SQL jobs are handled in the same way.  A job whose technology is unrecognized becomes a generic *DeployedSoftwareComponent*.

The new asset is named `{typeName}::{namespace}::{name}`, with the namespace and name in its *namespacePath* and *resourceName*.  Its description, formula, ownership and other details are taken from the job and dataset facets.  The templates are in the Core Content Pack, and the table templates for PostgreSQL, SQL Server, Oracle, Db2 and Unity Catalog are in those technologies' content packs.

#### Jobs and lineage

* The **job** is matched in the same way as a dataset, by its *namespacePath* and *resourceName*.  Parent and root jobs named in the *parent* run facet become processes that own the job through *ProcessHierarchy* relationships.  Job dependencies become *ControlFlow* relationships.
* **Lineage** is recorded as *DataFlow* relationships from the inputs to the process and from the process to the outputs.  When a dataset is a table, the *DataFlow* is recorded both for the table and for the asset that holds it - the database schema or database - so the lineage can be seen at the asset level as well as in detail.  The column lineage facets become *DataMapping* relationships between the columns, and between the tables that hold them.
* **Run metrics** - run count, failures, first and last run times, last run duration and status, rows and bytes read and written - are maintained in the [*RunMetrics*](/types/2/0215-Software-Components) classification of the process.
* Optionally, the cataloguer also catalogues each **run** as a *TransientEmbeddedProcess* owned by the job's process.  It can also capture the statistics and data quality facets as a survey report per event, with one annotation per assertion, and maintain the [*DataScope*](/types/2/0210-Data-Stores) classification of each output asset from the times and statistics of the writes.

#### Governance action runs and information supply chains

Egeria defines two custom run facets, described in [Egeria's Open Lineage Facets](/openlineage/facets):

* **`egeria_governanceAction`** is added by the Governance Action Open Lineage connector to the events it creates for Egeria's own [engine actions](/concepts/engine-action).  A run with this facet is not catalogued as a new job.  Instead its lineage is attached to the [governance action process](/concepts/governance-action-process) that the run is part of.  Provisioning services connect their own lineage to this same element, so the lineage from every run of the process meets there.  The *RunMetrics* classification is kept on the [process step](/concepts/governance-action-process-step), because each step runs separately.  The governance action process instance represents the run.
* **`egeria_informationSupplyChain`** can be added by any producer - for example an Apache Airflow DAG - to name the [information supply chain](/concepts/information-supply-chain) that the run belongs to.

Every lineage relationship that the cataloguer creates from an event, and every *DataSetContent* link to an abstraction, is tagged with the event's information supply chain.  The supply chain is taken from the `egeria_informationSupplyChain` facet or, if there is none, from the `egeria_governanceAction` facet.  The same data can take part in several supply chains, so a relationship is only reused when it is tagged with the same one.

Everything the cataloguer records is structural or is a "latest value": it is designed to keep the catalog current as events stream in, while leaving anything that needs the history of many runs to the analysis services described below.


## Storing events: the Open Lineage Log Store

The Open Lineage log store is a destination where events can be written so they can be queried later - both by people investigating an issue, and by governance processes validating that the operational environment is behaving as expected (see [Governing expectations](/features/lineage-management/overview/#governing-expectations)).  The implementation is pluggable.

Using the File-based Open Lineage Log Store, the log store is simply a directory (folder) in the filesystem, with one file per event:

![An example deployment of Egeria capturing and processing Open Lineage events into a file-based log store.](/features/lineage-management/open-lineage-example-deployment.svg)

Using the API-based Open Lineage Log Store, the same events are instead sent to a server implementing the Open Lineage API - such as Marquez, which also provides its own API for querying the events it has captured:

![The same deployment, but using Marquez as the Open Lineage log store instead of the file system.](/features/lineage-management/open-lineage-example-deployment-marquez.svg)

Both can be run side by side if you want a local archive as well as a queryable service.


## Analysing the log store: the Lovelace services

A stream of run events is a series of observations.  Some of the most useful facts about a pipeline - how often a job really runs, how long it typically takes, whether a table is rebuilt or accumulates, what proportion of a dataset's quality checks pass - only emerge from that series.  Deriving them as each event arrives would mean rewriting the process or asset on every run; deriving them from the log store on a schedule is cheaper and gives better answers.

Three [Lovelace services :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/lovelace-insights){ target=gh } do this analysis.  They are governance action services orchestrated by the Babbage Analytical Engine, and each can be enabled independently so that a deployment runs only the analyses it wants.  Each reads the file-based log store (supplied as its `openLineageLogStore` action target, or through the `logStoreDirectory` request parameter) for the last `analysisWindowDays` days - 30 by default - and updates only the processes and assets that it can identify uniquely from the namespace and name in the events, using the same rules as the cataloguer.

| Service                                | Reads                                                                     | Records                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Profile OpenLineage Runs**           | The START, COMPLETE, FAIL and ABORT events of each job's runs.            | The run profile in the *additionalProperties* of the process's [*RunMetrics*](/types/2/0215-Software-Components) classification: runs per day, failure rate, the mean, median and range of the interval between runs, how regular that interval is and an inferred schedule (such as HOURLY or DAILY), typical and worst-case duration, and the mean data volume per run.  |
| **Refine OpenLineage Data Scope**      | The writes (with lifecycle, subset and statistics facets) and reads of each dataset. | The [*DataScope*](/types/2/0210-Data-Stores) classification of the asset: whether the store is REPLACED, PARTITIONED or APPENDED by its writers, the data collection window (restarted at the latest rebuild, or extended back to the earliest known write), and the rates of writes and reads.                                                     |
| **Summarise OpenLineage Data Quality** | The data quality assertions of each dataset and the tests of each job.    | A survey report per dataset (and per job) holding a *QualityAnnotation* per quality dimension whose score is the pass rate over the window, plus an overall pass rate, so that the current quality of a dataset can be read without scanning the run history.                                                                              |

The services are supplied in the Open Lineage content pack, so a deployment that loads the pack for the connectors has them available to Babbage as well.  Running the cataloguer without the analysis services still gives complete lineage and current values; running the analysis services without the cataloguer still works for processes and assets that are already catalogued, but nothing new is created.


## From Open Lineage events to a connected lineage graph

Capturing Open Lineage events is only the first stage.  The jobs and data sources named in the events still need to be linked to each other - and to the rest of the catalog - to produce a single connected lineage graph, a process Egeria calls *stewardship* (deduplication and stitching).  From there, lineage can be viewed directly through open metadata queries, or exported to a [Lineage Warehouse](/concepts/lineage-warehouse) for large-scale, long-term analysis.

See [Lineage Management](/features/lineage-management/overview) for the full architecture, including how design and operational lineage combine, how stitching works, and how the resulting graphs are preserved and used.


## Related information

* [Lineage Management](/features/lineage-management/overview) - the complete lineage story: capture, stewardship and preservation.
* [Open Lineage project](https://github.com/OpenLineage/OpenLineage) - the standard itself, including the full facet specifications.
* [Egeria's Open Lineage Facets](/openlineage/facets) - the custom facets that Egeria defines, and their schemas.
* [Integration Daemon](/concepts/integration-daemon) - the server that hosts the Open Lineage connectors.
* [Lineage Warehouse](/concepts/lineage-warehouse) - where preserved lineage graphs are stored for analysis.

--8<-- "snippets/abbr.md"
