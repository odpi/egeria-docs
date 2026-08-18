<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata OutTopic

The *Open Metadata OutTopic* is an [event topic](/concepts/basic-concepts) used to send metadata change notifications out from a [metadata access server](/concepts/metadata-access-server) to the services that need to react to them - typically the [governance servers](/concepts/governance-server) and [view servers](/concepts/view-server), but also any external technology that has been connected to the topic.

The OutTopic is what makes the open metadata ecosystem event-driven rather than poll-driven.  Instead of a governance service repeatedly asking whether anything has changed, it subscribes to the OutTopic and is told.  A [watchdog action service](/concepts/watchdog-action-service) monitoring for a situation, an [integration connector](/concepts/integration-connector) keeping a third party catalog in step, or a listener maintaining a search index all work this way.

Each [Open Metadata Access Service (OMAS)](/services/omas) has its own OutTopic, and publishes the events that are relevant to its own area of interest.  A consumer therefore subscribes to the topic of the service whose subject matter it cares about, rather than filtering the whole stream.

The topic itself is accessed through an [open metadata topic connector](/concepts/open-metadata-topic-connector), which is nested inside the runtime connector for whichever [event bus](/concepts/event-bus) technology the deployment uses - Apache Kafka, for example.  This means the event format is independent of the messaging technology carrying it.

???+ info "Additional information"
    * [Open metadata topic connector](/concepts/open-metadata-topic-connector) describes how events are read from and written to the topic.
    * [Notification type](/concepts/notification-type) describes how the situations detected from these events are defined, and who is told about them.

--8<-- "snippets/abbr.md"
