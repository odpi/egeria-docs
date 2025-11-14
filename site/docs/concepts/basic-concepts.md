<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Basic technology concepts

## Application Programming Interface (API)

An API is a well-defined interface that can be called from a remote process.
There are many styles and protocols available to enable calls to APIs. The most popular at the moment is
the [REST API :material-dock-window:](https://en.wikipedia.org/wiki/Representational_state_transfer){ target=wikipedia }
style that piggybacks on top of the HTTP protocol that powers the Internet. Egeria makes extensive use of REST APIs.

??? education "Further information"
    Details of the different types of APIs provided by Egeria can be found in the [developer guide](/guides/developer/guide).
    In addition, it is possible to automatically catalog details of the APIs that your organization uses:
    
    - [Cataloguing API](/services/omis/api-integrator/overview)

## Event

An event is a message that describes a specific situation, or more typically a change in situation.
It is sent on a [topic](#topic) to share its information with other servers.

??? education "Further information"
    Details of the different types of events used by Egeria

    - [OMRS topic events](/concepts/metadata-events) - for open metadata repository cohorts
    - [InTopic Events](/concepts/in-topic) - for outgoing events to an Open Metadata Access Service (OMAS)
    - [OutTopic Events](/concepts/out-topic) - for incoming events from an Open Metadata Access Service (OMAS)

    In addition, it is possible to automatically catalog details of the types of events that your organization uses:
    
    - [Cataloguing topics and event types for an event broker :material-github:](/services/omis/topic-integrator/overview){ target=gh }

## Event Broker

An event broker is an infrastructure service that provides a publish-subscribe capability
through [topics](#topic).

There are many different event broker implementations with greater or
lesser reliability and performance.
Egeria's default event broker is [Apache Kafka :material-dock-window:](https://kafka.apache.org/){ target=kafka }.
This is an open source event broker with a high level of performance, scalability and reliability.

Many organizations establish a standard choice of their event
broker service which is why Egeria uses connectors to connect to the event broker so that Apache Kafka can be swapped out
for a different event broker implementation.
As such, each topic is accessed through an
[open metadata topic connector](/connectors/#open-metadata-topic-connectors).

??? education "Further information"
    - [Configuring the event broker for Egeria](/concepts/event-bus)
    - [Cataloguing topics and event types for an event broker](/services/omis/topic-integrator/overview)

## Topic

A topic is a service provided by an [event broker](#event-broker) that offers
a publish-subscribe capability for a specific type of event.

Multiple servers can read and write events to a topic.
Each topic maintains information about the events that a server has not read so that
it can receive each event even if it restarts.
Typically the events are processed in a first-in-first-out (FIFO)
order, but that is not necessarily guaranteed since it depends on the type and configuration of the event broker.

??? education "Further information"
    Details of the different types of topics used by Egeria

    - [OMRSTopic](/concepts/metadata-events) - for open metadata repository cohorts
    - [InTopic](/concepts/in-topic) - for sending events to an Open Metadata Access Service (OMAS)
    - [OutTopic](/concepts/out-topic) - for receiving events from an Open Metadata Access Service (OMAS)

    In addition, it is possible to automatically catalog details of the event brokers that your organization uses:
    
    - [Cataloguing topics and event types for an event broker](/services/omis/topic-integrator/overview)}

## Engine

An *engine* is a software capability that is programmable to automate specific processes.  Typically these processes manipulate and store data.

Below are examples of engines:

* Workflow engine - for automating processes that coordinate the activity of people and systems.
* Data movement engine - for automating the movement of data from one store to another.
* Data virtualization engine - for automating the federation and transformation
of data in response to a real-time query.
* Reporting engine - for extracting data and formatting into specific reports.
* Analytics engine - for executing analytical processes.

The metadata used by an engine relates to the processing it is performing and the data sources it is working with.

Most engines have associated tools to create the process definitions and manage the metadata, leaving the engines themselves to run the automated processes and create lineage metadata.

## Master data manager

A *master data manager* is a capability in a software server to manage an authoritative
collection of master data, typically about people, organizations, products and accounts.

Master data managers that hold information about the people and organizations using open metadata
integrate their data through the [Community Profile OMAS](../../../community-profile).

## Asset Manager

An *asset manager* is typically a service that provides a catalog of [assets](/concepts/asset).  It is responsible for maintaining details of the assets including their characteristics, ownership, assessments and governance requirements.

Often an asset manager is specialized for particular types of assets. For example, you may see a **data catalog** cataloging information about data sets and data stores for a data lake. A Configuration Management Database (CMDB) is an asset manager of infrastructure assets.

### Open metadata support for asset managers

An asset manager may integrate with the open metadata ecosystem using one of three methods:

* as a [cohort member](/concepts/cohort-member) through the [Open Metadata Repository Services (OMRS) connectors](/connectors/#repository-and-event-mapper-connectors) or 

* using the [Catalog Integrator Open Metadata Integration Service (OMIS)](/services/omis/catalog-integrator/overview) through an [integration connector](/concepts/integration-connector) or

* through direct calls to the [Asset Manager Open Metadata Access Service (OMAS)](/services/omas/asset-manager/overview).

The [Metadata Server Exchange](/patterns/metadata-server-exchange/overview) solution provides more information on these options.

## Subsystem

A subsystem is a component within a software server or software server platform that supports one or more services.  Subsystems can be decomposed into smaller subsystems.


--8<-- "snippets/abbr.md"
