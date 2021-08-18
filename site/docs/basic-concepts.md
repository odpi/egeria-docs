<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# General concepts

## Application Programming Interface (API)

An API is a well-defined interface that can be called from a remote process.
There are many styles and protocols available to enable calls to APIs. The most popular at the moment is
the [REST API :material-dock-window:](https://en.wikipedia.org/wiki/Representational_state_transfer){ target=wikipedia }
style that piggy-backs on top of the HTTP protocol that powers the Internet. Egeria makes extensive use of REST APIs.

??? education "Further information"
    Details of the different types of APIs provided by Egeria can be found in the [developer guide](/egeria-docs/guides/developer).
    In addition, it is possible to automatically catalog details of the APIs that your organization uses:
    
    - [Cataloguing API :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/api-integrator){ target=gh }

## Event

An event is a message that describes a specific situation, or more typically a change in situation.
It is sent on a [topic](#topic) to share its information with other servers.

??? education "Further information"
    Details of the different types of events used by Egeria

    - [OMRS topic events](/egeria-docs/services/omrs/metadata-events/#omrs-events) - for open metadata repository cohorts
    - [InTopic Events](/egeria-docs/services/omas/client-server/#in-topic) - for outgoing events to an Open Metadata Access Service (OMAS)
    - [OutTopic Events](/egeria-docs/services/omas/client-server/#out-topic) - for incoming events from an Open Metadata Access Service (OMAS)

    In addition, it is possible to automatically catalog details of the types of events that your organization uses:
    
    - [Cataloguing topics and event types for an event broker :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/topic-integrator){ target=gh }

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
[open metadata topic connector](/egeria-docs/connectors/runtime/#open-metadata-topic-connectors).

??? education "Further information"
    - [Configuring the event broker for Egeria](/egeria-docs/concepts/event-bus.md)
    - [Cataloguing topics and event types for an event broker :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/topic-integrator){ target=gh }

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

    - [OMRSTopic](/egeria-docs/services/omrs/metadata-events/#omrs-event-topic) - for open metadata repository cohorts
    - [InTopic](/egeria-docs/services/omas/client-server/#in-topic) - for sending events to an Open Metadata Access Service (OMAS)
    - [OutTopic](/egeria-docs/services/omas/client-server/#out-topic) - for receiving events from an Open Metadata Access Service (OMAS)

    In addition, it is possible to automatically catalog details of the event brokers that your organization uses:
    
    - [Cataloguing topics and event types for an event broker :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/integration-services/topic-integrator){ target=gh }

--8<-- "snippets/abbr.md"
