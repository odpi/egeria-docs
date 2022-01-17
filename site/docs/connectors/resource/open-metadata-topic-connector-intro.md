---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


The [open metadata topic connector](/egeria-docs/concepts/open-metadata-topic-connector) provides a topic interface for a generic string event.  It is the type of connector implemented by specific [event buses](/egeria-docs/concepts/event-bus).

The Open Metadata Topic Connectors are used by Egeria to read and write [events](/egeria-docs/concepts/basic-concepts/#event) to a [topic](/egeria-docs/concepts/basic-concepts/#topic) managed by an [event broker](/egeria-docs/concepts/basic-concepts/#event-broker).  These events contain notifications relating to changes in metadata and the topic provides an asynchronous event exchange service hosted in the event broker.  It is typically [wrapped in a connector](/egeria-docs/concepts/connection/virtual-connections) that supports a specific event type.  For example, the Open Metadata Topic Connectors connect servers into an [open metadata repository cohort](/egeria-docs/concepts/cohort-member) and exchange notifications through the [Open Metadata Access Services (OMAS)'s](/egeria-docs/services/omas) topics called the [InTopic](/egeria-docs/concepts/in-topic) and [OutTopic](/egeria-docs/concepts/out-topic).  In all of these cases, an open metadata topic connector is nested inside of the specific topic connector.  The use of the open metadata topic connector in this way means that only one connector need be implemented for each type of event bus - rather than one for each type of event that Egeria supports.

![Open Metadata Topic Connector](/egeria-docs/connectors/resource/open-metadata-topic-connector.svg)


--8<-- "snippets/abbr.md"
