---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Topic Integrator Open Metadata Integration Service (OMIS)

The Topic Integrator OMIS supports the exchange of topic-based assets and the open metadata ecosystem.
Typically, these topics are managed by an event broker such as Apache Kafka.

It supports a type of [integration connector](/concepts/integration-connector)
that are able to create [Topic](/types/2/0223-Events-and-Logs)
assets along with descriptions of the structures of events that pass through the topic.
Optionally, this metadata can be tied to an [EventBroker](/types/0/0050-Applications-and-Processes).

Figure 1 shows the types of metadata that integrators connectors can create with this integration service.

![Figure 1](/services/omas/data-manager/topic-model.svg)
> **Figure 1:** Topic metadata supported by the Topic Integrator OMIS 

The structure of an event is called an [EventType](/types/5/0535-Event-Schemas).
The details of this structure such as the data fields in the event are described using
[SchemaAttributes and SchemaTypes](/concepts/schema).

Figure 2 shows the open metadata types used to represent the metadata created through this service.

![Figure 2](/services/omas/data-manager/topic-open-metadata-types.svg)
> **Figure 2:** Topic open metadata types supported by the Topic Integrator OMIS 

If an EventBroker is defined, any topic created is automatically linked to it using the
[ServerAssetUse](/types/0/0045-Servers-and-Assets)
relationship.
When an event type is created for the topic,
the service automatically inserts the
[AssetSchemaType](/types/5/0503-Asset-Schema) relationship,
[EventTypeList](/types/5/0535-Event-Schemas) entity and
[SchemaTypeOption](/types/5/0501-Schema-Elements) relationship
in between the topic and the event type.

Any schema attributes created through this interface will use the
[EventSchemaAttribute](/types/5/0535-Event-Schemas) subtype
to allow for find requests that only return schema information for events.  The schema attributes also use
the [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/concepts/schema).

This integration service is paired with the [Data Manager](/services/omas/data-manager/overview)
Open Metadata Access Service (OMAS).

---8<-- "snippets/abbr.md"