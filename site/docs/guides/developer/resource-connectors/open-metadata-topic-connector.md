<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Open Metadata Topic Connectors

The open metadata topic connector provides a topic interface to a generic string event.

It is the interface implemented by specific [event buses](/concepts/event-bus).

Topic connectors for specific types of events (such as the [OMRS Topic Connector](/services/omrs/component-descriptions/connectors/omrs-topic-connector)) are configured with an instance of an open metadata topic connector embedded inside it.

The open metadata topic connector means that only one connector need be implemented for each type of event bus - rather than one for each type of topic that Egeria supports.

Implementations of this type of connector are located in the [adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors){ target=gh } module.  There are two implementations: one for [Apache Kafka](https://kafka.apache.org/){ target=kafka } (`KafkaOpenMetadataTopicConnector`) and an in-memory implementation (`InMemoryOpenMetadataTopicConnector`) that is useful for testing.

## Open metadata topic connector interface

The definition of the connector interface for these connectors is defined in the [open metadata repository services (OMRS)](/services/omrs) `repository-services-apis` module in the [org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic){ target=gh } Java package.

The `OpenMetadataTopic` interface has two methods:

- `sendEvent(String event)` for sending events to other systems/applications.
- `registerListener(OpenMetadataTopicListener newListener)` for registering a listener that is called each time an event is received from the event broker.  A listener implements the `OpenMetadataTopicListener` interface, which has a single method: `processEvent(String event)`.

## Implementing an open metadata topic connector

An open metadata topic connector extends the abstract `OpenMetadataTopicConnector` class, which extends the OCF's `ConnectorBase` and implements `OpenMetadataTopic`.  The base class manages the registered listeners:

- `registerListener()` stores the listener and returns the name of the topic, which is taken from the network address of the connection's endpoint.
- `start()` reads the topic name from the endpoint and an optional `sleepTime` configuration property, and starts a listener thread.
- The listener thread repeatedly calls `checkForIncomingEvents()` and passes each event returned to every registered listener, sleeping for `sleepTime` between checks.
- `disconnect()` stops the listener thread.

The implementation must therefore:

- implement `sendEvent()` to publish an event to the event bus.
- override `checkForIncomingEvents()` to return the list of `IncomingEvent` objects received from the event bus since the last call.  (The older `checkForEvents()` method, which returns a list of strings, is deprecated.)
- override `start()` and `disconnect()` to connect to and disconnect from the event bus, calling the superclass's methods.

The connector provider extends `OpenMetadataTopicProvider`, which is a subclass of `OpenConnectorProviderBase`.

--8<-- "snippets/abbr.md"
