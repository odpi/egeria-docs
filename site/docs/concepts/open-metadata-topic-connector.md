---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->
  
# Open Metadata Topic Connectors

The open metadata topic [connectors](connector.md) support the base `Open Metadata Topic` used for asynchronous event passing between members of the open metadata ecosystem. They typically delegate calls to their interface to an EventBroker.  For example, the Kafka Open Metadata Topic Connector sends and receives events through Apache Kafka.

An open metadata topic connectors passes an event as a String containing a JSON document. They are designed to be embedded in virtual topic connectors that support a specific bean implementation for the event and manage the parsing of the JSON string into a Java bean.  The virtual topic connectors delegate all of the event communications to the open metadata topic connectors.

For example, the open metadata modules that support asynchronous communication implement virtual topic connectors that wrap the open metadata topic connectors. Figure 1 shows these virtual topic connectors working with the Apache Kafka implementation of the open metadata topic connector.

![Figure 1](nested-topic-connectors.svg)
> **Figure 1:** Nested topic connectors

If a new implementation of the open metadata topic connector was implemented for a different event broker, the virtual topic connectors would continue to work as before.  The only change is that the [connection](connection.md) for the open metadata topic connector would provide the configuration for the 

## Implementing an open metadata topic connector

The [open metadata repository services (OMRS)](/egeria-docs/services/omrs) api module, [repository-services-apis](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/openmetadatatopic), provides the base classes for implementing an open metadata topic connector.  

There are two parts to this API:

- `sendEvent` for sending events to other systems/applications.
- `registerListener` for registering a listener that is called each time an event is received from the event broker.

--8<-- "snippets/abbr.md"
