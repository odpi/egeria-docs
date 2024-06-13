---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->
  
# Open Metadata Topic Connectors

---8<-- "snippets/connectors/open-metadata-topic-connector-intro.md"

## Use of Open Metadata Topic Connectors in Egeria

The open metadata topic [connector](/concepts/connector) supports the base `Open Metadata Topic` interface that is used for asynchronous event passing between members of the open metadata ecosystem. They typically delegate calls to their interface to an [event broker](/concepts/basic-concepts/#event-broker).  For example, the Kafka Open Metadata Topic Connector sends and receives events through Apache Kafka.

An open metadata topic connectors passes an event as a String containing a JSON document. They are designed to be embedded in virtual topic connectors that support a specific bean implementation for the event and manage the parsing of the JSON string into a Java bean.  The virtual topic connectors delegate all of the event communications to the open metadata topic connectors.

For example, the open metadata modules that support asynchronous communication implement virtual topic connectors that wrap the open metadata topic connectors. Figure 1 shows these virtual topic connectors working with the Apache Kafka implementation of the open metadata topic connector.

![Figure 1](nested-topic-connectors.svg)
> **Figure 1:** Nested topic connectors

If a new implementation of the open metadata topic connector was implemented for a different event broker, the virtual topic connectors would continue to work as before.  The only change is that the [connection](/concepts/connection) for the open metadata topic connector would provide the configuration for the 


--8<-- "snippets/abbr.md"
