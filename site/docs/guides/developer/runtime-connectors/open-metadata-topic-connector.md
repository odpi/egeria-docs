---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Topic Connector

The open metadata topic connector provides a topic interface to a generic string event.

It is the interface implemented by specific [event buses](/egeria-docs/concepts/event-bus).

Topic connectors for specific types of events (such as the [OMRS Topic Connector](../../../services/omrs/omrs-topic-connector.md)) are configured with an instance of an open metadata topic connector embedded inside it.

The open metadata topic connector means that only one connector need be implemented for each type of event bus - rather than one for each type of topic that Egeria supports.

Implementations of this type of connector are located in the [adapters/open-connectors/repository-services-connectors/audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/event-bus-connectors){ target=gh } module.

--8<-- "snippets/abbr.md"
