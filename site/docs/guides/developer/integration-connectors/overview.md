<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Building Integration Connectors

---8<-- "docs/connectors/integration/integration-connector-intro.md"


## Writing the Connector Provider

---8<-- "docs/guides/developer/connector-provider-intro.md"

---8<-- "docs/guides/developer/implementing-a-connector-provider.md"


!!! example "Example: connector provider for the Kafka Monitor Integration Connector"
    For example, the [`KafkaMonitorIntegrationProvider` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafka/KafkaMonitorIntegrationProvider.java){ target=gh } is used to instantiate connectors that are monitoring an Apache Kafka broker. Therefore, its name and description refer to Kafka, and the connectors it instantiates are of type [`KafkaMonitorIntegrationConnector :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-integration-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/integration/kafka/KafkaMonitorIntegrationConnector.java){ target=gh }.


## Integration connector interface

---8<-- "docs/guides/developer/integration-connectors/integration-connector-interface.md"


## Two approaches to designing the connections for an integration connector 

Figure 3 shows the approach used for a dedicated connector to a specific third party technology deployment.

![Figure 3](explicit-endpoints.svg)
> **Figure 3:** An explicit endpoint is added to the integration connector's connection in its configuration

Figure 4 shows the approach used to catalog all instances of a particular type of technology.

![Figure 4](learned-endpoints.svg)
> **Figure 4:** No endpoint is configured in the integration connector's connection.

Location is determined from the endpoints that are stored in open metadata.  The connector registers a listener with the context and it listens for events relating to endpoint of the appropriate values.

An integration connector can choose to support one of these patterns or switch dynamically depending on the presence of the endpoint in the connector's configuration. 

??? education "Further information"
    - [Open Connector Framework (OCF)](/frameworks/ocf/overview) that defines the behavior of all connectors.
    - [Configuring an integration daemon](/guides/admin/servers/configuring-an-integration-daemon) to understand how to set up an integration connector.
    - [Developer guide](/guides/developer) for more information on writing connectors.

--8<-- "snippets/abbr.md"
