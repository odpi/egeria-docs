---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Open Metadata Topic Connectors

The open metadata topic connector provides a topic interface to a generic string event.

It is the interface implemented by specific [event buses](/egeria-docs/concepts/event-bus).

Topic connectors for specific types of events (such as the [OMRS Topic Connector](/egeria-docs/services/omrs/connectors/omrs-topic-connector)) are configured with an instance of an open metadata topic connector embedded inside it.

The open metadata topic connector means that only one connector need be implemented for each type of event bus - rather than one for each type of topic that Egeria supports.

Implementations of this type of connector are located in the [adapters/open-connectors/repository-services-connectors/audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/event-bus-connectors){ target=gh } module.

## Open metadata topic connector interface

The [open metadata repository services (OMRS)](/egeria-docs/services/omrs) api module, [repository-services-apis](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic), provides the base classes for implementing an open metadata topic connector.  

There are two parts to this API:

- `sendEvent` for sending events to other systems/applications.
- `registerListener` for registering a listener that is called each time an event is received from the event broker.

The definition of the connector interface for these connectors is defined in the `repository-services-apis` module in the [org.odpi.openmetadata.repositoryservices.connectors.openmetadatatopic :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic){ target=gh } Java package.

--8<-- "snippets/abbr.md"
