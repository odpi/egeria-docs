<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


The [open metadata topic connector](/concepts/open-metadata-topic-connector) provides a publish-subscribe service that allows a producer to publish events to subscribed consumers.  Events are organized into topics.  A producer publishes an event to a topic and the consumers register a listener to receive all events from a topic.  It is the type of connector implemented by specific [event buses](/concepts/event-bus) such as [Apache Kafka](https://kafka.apache.org/).

![Open Metadata Topic Connector](/connectors/resource/open-metadata-topic-connector.svg)

The Open Metadata Topic Connector implements the [OpenMetadataTopicConnector](https://odpi.github.io/egeria/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic/OpenMetadataTopicConnector.html) interface. This supports both the event producer and event consumer interfaces.  It assumes the event payload can be received as a string. Typically, this event payload is encoded in JSON but other formats are possible.

???+ info "Use of Open Metadata Topic Connector in Egeria"
    The Open Metadata Topic Connectors are used by Egeria to read and write [events](/concepts/basic-concepts/#event) that contain notifications describing changes in open metadata.    For example, the Open Metadata Topic Connectors connect servers into an [open metadata repository cohort](/concepts/cohort-member) and exchange notifications through the [Open Metadata Access Services (OMAS)'s](/services/omas) topics called the [InTopic](/concepts/in-topic) and [OutTopic](/concepts/out-topic).  In all of these cases, an open metadata topic connector is nested inside a [specific runtime topic connector](/concepts/event-bus) that supports the event type in use.  The use of the open metadata topic connector in this way means that only one connector need be implemented for each type of event bus - rather than one for each type of event that Egeria supports.

    ![Open Metadata Topic Connector](/connectors/resource/open-metadata-topic-connector-in-egeria.svg)


--8<-- "snippets/abbr.md"
