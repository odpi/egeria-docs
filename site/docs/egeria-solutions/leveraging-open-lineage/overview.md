
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
| **[Open Lineage Cataloguer :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors/README.md#open-lineage-cataloguer-integration-connector){ target=gh }**                  | Registers as a listener and ensures the jobs described in the events are catalogued as [Processes](/types/2/0215-Software-Components) in open metadata.  Depending on its configuration, it may also catalog each run as a *TransientEmbeddedProcess* linked to the job's process entity.       |

The diagram below shows all five working together in a single integration daemon:

![The pre-built integration connectors supplied by Egeria.](/features/lineage-management/open-lineage-integration-connectors.svg)

1. A third-party processing engine sends Open Lineage events either directly to Egeria's Open Lineage API endpoint, or via a proxy backend to a Kafka topic.
2. The Open Lineage Event Receiver picks up events from the Kafka topic and hands them to the integration daemon's context manager.
3. The Governance Action Open Lineage connector registers a listener for engine actions running in the open metadata ecosystem, generates Open Lineage events to represent that processing, and hands them to the context manager too - so both sources of events flow through the same pipeline.
4. Any connector wanting to receive events - the two log store connectors and the cataloguer - registers a listener with the context manager, and from then on receives every event that arrives.
5. The API-based and file-based Open Lineage Log Store connectors write each event to their configured destination (a remote Open Lineage API server, or a local file), while the Open Lineage Cataloguer uses each event to make sure the job it describes is represented as a `Process` asset in open metadata.

Because any combination of these connectors can be configured in the same integration daemon, you can, for example, catalog processes *and* archive the raw events to Marquez *and* forward Egeria's own governance action activity into the same picture, all at once.


## Storing events: the Open Lineage Log Store

The Open Lineage log store is a destination where events can be written so they can be queried later - both by people investigating an issue, and by governance processes validating that the operational environment is behaving as expected (see [Governing expectations](/features/lineage-management/overview/#governing-expectations)).  The implementation is pluggable.

Using the File-based Open Lineage Log Store, the log store is simply a directory (folder) in the filesystem, with one file per event:

![An example deployment of Egeria capturing and processing Open Lineage events into a file-based log store.](/features/lineage-management/open-lineage-example-deployment.svg)

Using the API-based Open Lineage Log Store, the same events are instead sent to a server implementing the Open Lineage API - such as Marquez, which also provides its own API for querying the events it has captured:

![The same deployment, but using Marquez as the Open Lineage log store instead of the file system.](/features/lineage-management/open-lineage-example-deployment-marquez.svg)

Both can be run side by side if you want a local archive as well as a queryable service.


## From Open Lineage events to a connected lineage graph

Capturing Open Lineage events is only the first stage.  The jobs and data sources named in the events still need to be linked to each other - and to the rest of the catalog - to produce a single connected lineage graph, a process Egeria calls *stewardship* (deduplication and stitching).  From there, lineage can be viewed directly through open metadata queries, or exported to a [Lineage Warehouse](/concepts/lineage-warehouse) for large-scale, long-term analysis.

See [Lineage Management](/features/lineage-management/overview) for the full architecture, including how design and operational lineage combine, how stitching works, and how the resulting graphs are preserved and used.


## Related information

* [Lineage Management](/features/lineage-management/overview) - the complete lineage story: capture, stewardship and preservation.
* [Open Lineage project](https://github.com/OpenLineage/OpenLineage) - the standard itself, including the full facet specifications.
* [Integration Daemon](/concepts/integration-daemon) - the server that hosts the Open Lineage connectors.
* [Lineage Warehouse](/concepts/lineage-warehouse) - where preserved lineage graphs are stored for analysis.

--8<-- "snippets/abbr.md"
