---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Apache Kafka estate

--8<-- "snippets/work-in-progress.md"

### Apache Kafka Connectors

* The [Kafka Open Metadata Topic Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/event-bus-connectors/open-metadata-topic-connectors/kafka-open-metadata-topic-connector) implements a [resource connector](/concepts/digital-resource-connector) for a topic that exchanges Java Objects as JSON payloads across an [Apache Kafka](https://kafka.apache.org/) event bus.   It is configured in the Egeria [OMAG Servers](/concepts/omag-server) through the [Event Bus Configuration](/concepts/event-bus).  This the connector that is used by default in the Egeria runtimes to exchange events (notifications between the [OMAG Servers](/concepts/omag-server)).
* The [Kafka Monitor Topic integration connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors) automatically maintains the open metadata instances for the topics hosted on an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka }.
* The [Kafka Audit Topic integration connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-audit-integration-connector) validates that topics that are active in an [Apache Kafka server :material-dock-window:](https://kafka.apache.org/){ target=kafka } are also catalogued in open metadata.  Creates an audit log record for each topic that is not catalogued.
* The [Sample Lineage Integration Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors)  is a sample connector to listen for lineage events (not in an [open lineage format](#open-lineage-events)) and catalog the associated assets, processes, schema and lineage.                                                                                                                                                              |

--8<-- "snippets/abbr.md"