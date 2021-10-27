<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Lineage

Lineage shows how data flows from its origins to its various destinations. This includes details of the processing along the way.  It is used to understand:
 
* whether the data used in reports and analytics models has come from the correct sources and has passed through the correct processing (traceability of data).
  
* what would be the impact on downstream processing and consumers if something was changed (impact analysis).

* whether the operational processes that implement the data flows are executing correctly.


## The lineage graph

Lineage is typically envisaged as a graph showing processes interacting with different data stores.   Some processes copy data from one store to another.  Other processes may retrieve data from multiple stores and combine them to produce a new value that is stored in another store.  The result is that a logical flow of data emerges from the interaction. 

Figure 1 shows some examples of different types of processes and data stores.

On the left here is an Apache Spark job that reads from a file, looks up a value in an Apache Hive table, makes a calculation and writes the results to an Apache Kafka topic. On the right, an API is called that invokes a microservice.  The microservice updates a data store.  This data store is also loaded by an ETL job and any changes to it are copied to other stores via a data replication service.  This second example illustrates that the data in the data store may have come from two sources, either the API caller or the data sources used by the ETL job.


![Figure 1](lineage-examples.svg)
> **Figure 1:** Examples of processes

As the importance of lineage is understood, it is becoming common that individual technologies provide a lineage view of their processing similar to figure 1.  This is very useful to the immediate users of that technology.  However from an enterprise perspective these technologies do not run in isolation.  Enterprises need to be able to link the lineage from these technologies together to to show how data flows from its original sources to its ultimate destinations.

Figure 2 shows a flow of data through multiple technologies.  It begins with a Relational Database (RDB). This is read by an ETL job that writes all or some of its contents to an Apache Hive table. An Apache Spark job is initiated through an API that reads from the Apache Hive table and invokes an Apache Airflow DAG (process) that writes the information into an Apache Avro file and an event to an Apache Kafka topic. 

![Figure 2](lineage-capture.svg)
> **Figure 2:** The lineage graph emerges

You can also imagine that this flow is only a part of something much bigger.  For example, what is responsible for maintaining the data in the relational database?  Which technologies are consuming the events in the Apache Kafka topic.  Lineage graphs can get very large.

Figure 3 abstracts the example shown in figure 2.  From this you can see that the flow is not a simple progression from left to right.  API calls can pass data in either direction for example. 

![Figure 3](basic-concept-of-lineage.svg)
> **Figure 3:** The abstract lineage graph

There are also often systems that act as a hub, with many processes extracting data, performing processing and then storing the results back into the same system.  Other stores act as a consolidation point, receiving data from many systems and then distributing to multiple downstream stores.  So the graph also involves loops and fan-in-fan-out structures.

## Lineage management

Figure 4 shows Egeria's architecture for lineage.  There are three parts to it:

* *Lineage capture* - through the [integration daemon](/egeria-docs/concepts/integration-daemon) and [Data Engine Proxy](/egeria-docs/concepts/data-engine-proxy) servers, metadata about data sources and the processing around them is captured and shared through open metadata.

* *Stewardship* - the lineage information from each of the technologies is linked together.  Where the naming of data sources and processes is consistent, this assembling of the lineage graph is automatic.  However, experience shows that if it can be different, it will be different. Many technologies make there own choices in naming and so governance action services along with human stewardship is required to match and link the graph together.  The governance action services run in the [Engine Host](/egeria-docs/concepts/engine-host) server.  They automatically add the relationships between the lineage contributions from each technology which may need to be verified by a human steward.  The human steward may also manually add relationships where there is no well known pattern that can be encoded in a governance action services.  The stewardship phase also involves analysis of the lineage to ensure the digital landscape is operating as it should.

* *Preservation and Use* - Once the lineage graphs are assembled, the lineage can be viewed and analysed from a business perspective.  Could, for example, the operation of the digital landscape be optimized?  Lineage is accessible through standard open metadata queries. However, since the lineage data is large, lineage is automatically captured and stored in the [Open Lineage Server](/egeria-docs/concepts/open-lineage-server) server.  This optimizes the lineage graphs for quick retrieval and analysis.  Its presence allows lineage data to be regularly archived from the operational open metadata ecosystem.  This is particularly important in regulated industries where lineage for critical reports may need to be kept for many years.

The three parts of the lineage architecture are summarized in figure 4.

![Figure 4](lineage-architecture.svg)
> **Figure 4:** The lineage architecture showing the three phases of (1) lineage capture through egeria's automated cataloguing capabilities, (2) automated and human stewardship coordinated by the engine host server to stitch the lineage contributions together into full data flows, and finally (3) lineage preservation and use in the open lineage server.

## Lineage capture

Capturing lineage has both a static and a dynamic aspect to it.  

- The *static* aspect involves cataloguing of all of the [resources](/egeria-docs/concepts/resource) that make up your digital landscape.  This defines all of the players such as the data sources and processing engines and how they link together.  

- The *dynamic* aspect captures information about the activity that happens day-to-day and its effects.

Each of these aspects have their challenges.

- the cataloguing of your digital landscape typically involves many different techniques since there are many choices of technologies typically deployed.  These techniques expose inconsistencies in naming, formats and detail.  It is also possible that the same resource is catalogued multiple times.  Ths is why the lineage architecture includes [stewardship](#lineage-stewardship) to reconcile these differences.

- Processing engines either produce no dynamic lineage information (this is the most common) or it is formatted in a unique proprietary format that needs to be transformed before it can linked with the equivalent information from another processing engine.

- When dynamic lineage information is captured, it produces a huge amount of data, much of which is of low value, or only valuable for a short period of time.  It needs to be actively pruned to prevent it from overwhelming the digital landscape.

### Design lineage verses operational lineage

The static and dynamic aspects of lineage are typically referred to as design lineage and operational lineage respectively.

So design lineage describes the digital resources and their linkages that are known at the time they are deployed.  Some tools, such as ETL engines, produce design lineage in their tools as part of their design process.  Other technologies rely on design lineage captured in the dev-ops pipeline or the automatic cataloguing of digital resources as they are added to the pre-production or production environment.

Operational lineage is the lineage information produced by a data processing engine when it runs processes. It enables an organization to ensure that processes run at the right time, using the right data and produce the right results.  It primarily focuses on capturing the dynamic aspects of lineage, but may also identify parts of the digital landscape that has not yet been catalogued.

### Lineage Styles

Figure 5 illustrates the difference between design lineage and operational lineage for a process copying data from one database to another.  At deployment time the lineage shows the relationships between the process and the two databases.  If the data in the destination database is incorrect, the lineage relationships shows that they could be caused by the behavior of the process, or the values in the source database.

Similarly, if there is a proposal to change the schema of either databases, the lineage relationships identify that the process is likely to be impacted by this change and it will need updating at the same time. 
 
![Figure 5](operational-lineage.svg)
> **Figure 5:** The design lineage known at deployment describes how a particular process reads data from the source database and writes to destination database.  The operational lineage captures a process instance each time the process runs which may include details of the amount of data processed and any errors or issues encountered.

The operational lineage shown at the bottom of figure 5 captures process instance information each time the process runs.  It is then possible to see how often it runs, and how much data it processes each time.  This could uncover that the quality problem identified in the destination database was caused by the fact that although the process should run every hour, it had not run for a week and so the values from the source database have not been transferred.

Some process cause resources to be created, moved and deleted.  This blurs the boundary between design lineage and operational lineage since the operational lineage needs to cause the cataloging of resources that were dynamically created or modified which is logically contributing to design lineage.  

This blurring between design lineage and operational lineage is particularly true when processing files. The next set of images (figures 6-10) show different patterns of lineage that can be chosen for particular circumstances.  The choice comes down to the value that the detail brings against its cost of capture and processing.

They each show a process that reads a file created dynamically by a predecessor process and after some calculation, writes the result to a destination file.

At deployment time, the files do not exist and so the process is not connected to any files except, potentially [templates](../templated-cataloguing) for the operational cataloguing of files when the process is running.

It is not until the process runs that its lineage is capture.  Figures 6-10 show different choices in the level of detail that could be captured.  figure 6 begins with the capture of every run of the process (that is its process instances) linked the the particular file that was processed.

![Figure 6](operational-lineage-files-detailed.svg)
> **Figure 6:** New files are read and created each time the process runs.  The operational lineage shows which files are associated with each run of the process.

Figure 6 provides complete information, but imagine it running every second, every day of the week.  There would be a huge amount of lineage created and it may not be necessary.

In figure 7, only the files are dynamically captured and linked to the process for design lineage.  No process instances are captured. This may not matter if the process runs regularly and the creation times of the files are sufficient to correlate them with the processing.

![Figure 7](operational-lineage-files-no-process-instances.svg)
> **Figure 7:** New files are read and created each time the process runs; these are catalogued and linked to the process as soon as they are detected; however no operation lineage is captured so it is not possible to know which process instance created each file.  

In figure 8, the attempt to link each of the destination files to the process has been abandoned and only the folder is linked.  The source files are still linked to the process instances because, for example, it is important to know when they were processed.

![Figure 8](operational-lineage-files-no-destination-file-linkage.svg)
> **Figure 8:** New files are catalogued in the destination - but only the folder that they belong to is linked to the process.  This is very efficient if all files in the folder come from the process.  However if multiple processes are populating the folder, there is no information on which process created each destination file.

Figure 9 shows that the process instances are not captured and the source files are linked directly to the process.  If this always done in a timely manner then the creation time of the relationship may be sufficient to know when the process instance that worked on the source file ran.

![Figure 9](operational-lineage-files-no-process-instances-destination-folder-linkage.svg)
> **Figure 9:** In this example, sources files are linked to the process, but again the destination is only shown at the folder level.

Finally in figure 10, the files are being catalogued, but they are not linked to the process.  

![Figure 10](operational-lineage-folder-level.svg)
> **Figure 10:** This final example shows no linkage between the process and the files.  The new files are just catalogued in their folder as they are created.

It is also possible that even the cataloguing of the files themselves is not useful since they are processed as a collection and each file is effectively like a row in a database table.

Each of the patterns show in figures 6-10 is valuable for different reasons.  It is important to keep your use case in mind when designing lineage capture.  *More* is not always better.  It is also necessary to understand the thought process behind the lineage capture when making use of the lineage at a later date.

### The OpenLineage Standard

[OpenLineage](https://github.com/OpenLineage/OpenLineage) is a sister open source project to Egeria in the [LF AI and Data Foundation](https://lfaidata.foundation/).  It is very welcome since it defines a standard for [*operational lineage*](#design-lineage-verses-operational-lineage).
 
 Figure 11 shows the scope of the standard.  When a processing engine such as *Apache Spark* runs a process, it produces a series of events called *RunEvents* that describe the activity of the process.  The standard covers the format of the events and a simple REST API that receives the events.  The REST API only has one operation called `{{urlroot}}/api/v2/lineage` that takes a single event as the request body.

![Figure 11](open-lineage-standard-defines.svg)
> **Figure 11:** The OpenLineage standard defines the payload for *RunEvents* as well as a standard URL for a service that acts as a collection point for RunEvents.

Processes can log information about their internal structure.  Figure 12 shows a process with three steps.

![Figure 12](open-lineage-example-process.svg)
> **Figure 12:** a three step process: (1) run quality analysis, (2) categorize data file and (3) move the data file to its destination.

Figure 13 shows the events from an instance of this process.  Notice each event has an *eventType* that describes the type of action that the process instance took.  The *runId* identifies the process instance.  The sub-process instances are linked to the top-level process instance via the *parentRunId*.

![Figure 13](open-lineage-example-events.svg)
> **Figure 13:** RunEvents from a three step process show the start and end of each process along with additional events to report on its findings such as a data quality assessment.

### RunEvent format

Figure 14 shows the structure of a run event.  It has 8 parts to it:

- *eventType* - the type of activity being described.
- *eventTime* - the time of the event as a `ZonedDateTime`.
- *run* - the description of the process instance.
- *job* - the description of the process.
- *inputs* - the data sources that were used as inputs by the process.
- *outputs* - the data sources that are output by the process.
- *producer* - the name/location of the processing engine producing the events.
- *schemaURL* - the location of the JSON schema that describes the structure of the RunEvent.

![Figure 14](open-lineage-payload-run-event.svg)
> **Figure 14:** The structure of a RunEvent

The *namespace* groups related processes together, for example the processes from the same subsystem or business process.  The OpenLineage standard provides suggested naming conventions for the *name* of jobs and data sources.

Throughout the RunEvent are `additionalProperties`.  These allow extensions to be added to the event.  These extensions are called *facets*.  The OpenLineage standard defines a number of standard facets and any organization or processing engine can define their own custom facets.

Figures 15-19 show the current set of standard facets defined by OpenLineage.

![Figure 15](open-lineage-payload-run-facets.svg)
> **Figure 15:** Standard Run facets


![Figure 16](open-lineage-payload-job-facets.svg)
> **Figure 16:** Standard Job facets


![Figure 17](open-lineage-payload-data-set-facets.svg)
> **Figure 17:** Standard DataSet facets that can be used in both the inputs or outputs section.


![Figure 18](open-lineage-payload-input-data-set-facets.svg)
> **Figure 18:** Standard InputDataSet facets


![Figure 19](open-lineage-payload-output-data-set-facets.svg)
> **Figure 19:** Standard OutputDataSet facets


### Integrating with the OpenLineage standard

Any server can implement the OpenLineage REST API.  Figure 20 shows [Marquez](https://marquezproject.github.io/marquez/), the reference implementation of the standard, acting as the back end to receive OpenLineage events from a spark processing engine.

![Figure 20](open-lineage-reference-implementation-marquez.svg)
> **Figure 20:** Marquez capturing the OpenLineage events.

The disadvantage of the API is that the server supporting it must be available whenever the processing engine is running.

The OpenLineage project provides a simple implementation of the OpenLineage API called the *proxy backend* (figure 21).  This is designed to act as a side car to the processing engine that can distribute the OpenLineage events to multiple external consumers through a kafka topic.

![Figure 21](open-lineage-proxy-backend.svg)
> **Figure 21:** The proxy backend transfers RunEvents received on its API to a Kafka topic 

Since the proxy backend is only supporting one processing engine it can be managed by the same team as the processing engine and hence its availability can be matched to the needs of the processing engine.

### Egeria's OpenLineage support

Egeria offers two approaches to capture OpenLineage events from the processing engines.  The first (figure 22) uses an [integration connector](/egeria-docs/connectors/integration/kafka-open-lineage-receiver-integration-connector) listening on the kafka topic(s) populated by the proxy backends tied to each of the processing engines.

![Figure 22](open-lineage-async-egeria-integration.svg)
> **Figure 22:** Receiving events via the Kafka topic populated by the proxy backend

Egeria's [integration daemon](/egeria-docs/concepts/integration-daemon) also supports the OpenLineage API for local processing engines.  It is one of the operations supported by the [Lineage Integrator OMIS](/egeria-docs/services/omis/lineage-integrator/overview).

![Figure 23](open-lineage-direct-egeria-integration.svg)
> **Figure 23:** Receiving events via the OpenLineage API directly into the integration daemon

The Lineage Integrator OMIS inside the integration daemon hosts the integration connectors that [process the OpenLineage events](/egeria-docs/connectors/#lineage).  They are divided in to two groups:

- the integration connectors that are acquiring or creating the OpenLineage events.

- the integration connectors that are processing or distributing the OpenLineage events.

They are connected to each other by the Lineage Integrator OMIS:

* An integration connector may register a listener to receive OpenLineage events that are received through the API or are published by another integration connector.

* An integration connector may request that an OpenLineage event is published to other integration connectors that have registered an OpenLineage event listener in the same Lineage Integrator OMIS instance.

* An integration connector may register a listener to the Asset Manager OMAS's OutTopics and issue requests to the Asset Manager's REST API in order to correlate the metadata in the open metadata ecosystem with the content of the OpenLineage events.  

Figure 24 illustrates these mechanism with the [five pre-build integration connectors](/egeria-docs/connectors/#lineage) supplied by Egeria.

![Figure 24](open-lineage-integration-connectors.svg)
> **Figure 24:** The pre-built integration connectors supplied by Egeria

The numbers on the diagram refer to the notes below.

1. A third party technology (processing engine) sends OpenLineage events to Egeria's OpenLineage API endpoint.  This is passed to the Lineage Integrator OMIS's context manager.

2. A third party technology is using the proxy backend to publish OpenLineage event to a Kafka topic.

3. The [Kafka OpenLineage Receiver](/egeria-docs/connectors/integration/kafka-open-lineage-receiver-integration-connector) integration connector is receiving OpenLineage events from the Kafka topic.  It passes them to the Lineage Integrator OMIS's context manager via its own context.

4. The [Governance Action OpenLineage](/egeria-docs/connectors/integration/governance-action-open-lineage-integration-connector) integration connector has registered a listener to receive events about the [governance actions](/egeria-docs/concepts/governance-action) that are being processed in the open metadata ecosystem.  

5. The Governance Action OpenLineage integration connector creates OpenLineage events to represent the processing by the governance actions and passes them to the Lineage Integrator OMIS's context manager via its own context.

6. An integration connector that wishes to receive OpenLineage events must register a listener with the Lineage Integrator OMIS's context manager via its own context.  Once it is registered, it receives all OpenLineage events that are subsequently passed to the context manager.

7. The [API-based OpenLineage Log Store](/egeria-docs/connectors/integration/api-based-open-lineage-log-store-integration-connector) registers a listener for OpenLineage events and passes each one received to a remote server supporting the OpenLineage API.

8. The [File-based OpenLineage Log Store](/egeria-docs/connectors/integration/file-based-open-lineage-log-store-integration-connector) registers a listener for OpenLineage events and stores each event received as a file in a nominated folder on the file system.

9. The [OpenLineage Cataloguer](/egeria-docs/connectors/integration/open-lineage-cataloguer-integration-connector) registers a listener for OpenLineage events and ensures the jobs describe in them are catalogued as [Processes](/egeria-docs/types/2/0215-Software-Components) in open metadata.  Depending on its configuration, it may also catalog each run as a *TransientEmbeddedProcess*.

### OpenLineage Log Store

The OpenLineage log store is a destination where OpenLineage events can be written.  This enables them to be queried by governance processes that are validating the behavior of the operational environment.

Figure 25 shows the capture of OpenLineage events into the OpenLineage log store which is a directory (folder) in the filesystem.  The content of the log store is later queried by the *ProcessValidatorConnector* (a [governance action service](/egeria-docs/concepts/governance-action-service) running in an [engine host](/egeria-docs/concepts/engine-host)) to determine if the [processes are operating as expected](#governing-expectations).

![Figure 25](open-lineage-example-deployment.svg)
> **Figure 25:** An example deployment of Egeria that is capturing and processing OpenLineage events. On the left hand side the integration connectors running in the integration daemon are capturing the events, storing them in the OpenLineage log store and creating additional metadata as appropriate.  On the right hand side of the diagram, are the stewardship processes that are stitching together the lineage and validating that the digital landscape is operating as expected.

The implementation of the OpenLineage log store is pluggable so an OpenLineage log store could be implemented as a server such as [Marquez](https://marquezproject.github.io/marquez/).  This is shown in figure 26.

![Figure 26](open-lineage-example-deployment-marquez.svg)
> **Figure 26:** Using Marquez as the OpenLineage log store.  This is the same diagram as figure 25 except tha Marquez has replaced the file system as the log store.  Marquez provides an API to simplify the processing of the OpenLineage events.

## Lineage stewardship

### Stitching

### Governing expectations

## Lineage preservation and use

### Building a lineage warehouse

### User views

#### Vertical lineage

#### Horizontal lineage

## Summary

Egeria's lineage support is comprehensive both in its capability and reach. Since the lineage is an integral part of the open metadata type system, metadata captured for lineage is useful for other purposes such as governance and quality management. Similarly, metadata captured to support a data catalog becomes part of the lineage graph.

By using open metadata, metadata is captured once and used for many purposes.

## Further reading

* [Lineage representation](lineage-representation.md) using Open Metadata Types
* [File Lineage solution using Egeria](/egeria-docs/scenarios/file-lineage/overview)

APIs for capturing lineage
* [Asset Manager Open Metadata Access Service (OMAS)](/egeria-docs/services/omas/asset-manager/overview)
* [Open Metadata Integration Services (OMISs)](/egeria-docs/services/omis)

APIs for retrieving lineage
* [Open Lineage Services](/egeria-docs/services/open-lineage-services)
* [Asset Owner](/egeria-docs/services/omas/asset-owner/overview) and
[Asset Consumer](/egeria-docs/services/omas/asset-consumer/overview) through the
[Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview).


--8<-- "snippets/abbr.md"