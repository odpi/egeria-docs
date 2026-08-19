---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connector Provider


--8<-- "docs/guides/developer/connector-provider-intro.md"

## Writing the Connector Provider

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"


!!! example "Example: connector provider for the Kafka Monitor Integration Connector"
    For example, the [`KafkaMonitorIntegrationProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-audit-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafkaaudit/DistributeAuditEventsFromKafkaProvider.java){ target=gh } is used to instantiate connectors that are monitoring an Apache Kafka broker. Therefore, its name and description refer to Kafka, and the connectors it instantiates are of type [`KafkaMonitorIntegrationConnector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-audit-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafkaaudit/DistributeAuditEventsFromKafkaConnector.java){ target=gh }.



--8<-- "snippets/abbr.md"
