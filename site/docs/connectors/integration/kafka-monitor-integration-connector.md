<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Kafka Monitor Integration Connector

* Connector Category: [Integration Connector](/egeria-docs/concepts/integration-connector)
* Hosting Service: [Topic Integrator OMIS](/egeria-docs/services/omis/topic-integrator/overview)
* Hosting Server: [Integration Daemon](/egeria-docs/concepts/integration-daemon)
* Source Module: [kafka-integration-connector](../../../open-metadata-implementation/adapters/open-connectors/integration-connectors/kafka-integration-connector)
* Jar File Name: kafka-integration-connector.jar

## Overview

The kafka monitor integration connector monitors an Apache Kafka server a
creates a 
[KafkaTopic](../open-metadata-types/0223-Events-and-Logs.md)
asset for each topic that is known to the server.
If the topic is removed from the Apache Kafka Server, its corresponding
KafkaTopic asset is also removed.

![Figure 1](kafka-monitor-integration-connector.png)
> **Figure 1:** Operation of the kafka monitor integration connector


## Configuration

This connector uses the [Topic Integrator OMIS](/egeria-docs/services/omis/topic-integrator/overview)
running in the [Integration Daemon](/egeria-docs/concepts/integration-daemon).

This is its connection definition to use on the 
[administration commands that configure the Topic Integrator OMIS](../../../open-metadata-implementation/admin-services/docs/user/configuring-the-integration-services.md).
Replace `{serverURL}` with the network address of Kafka's bootstrap server (for example, `localhost:9092`).


```json
{
   "connection" : 
                { 
                    "class" : "Connection",
                    "qualifiedName" : "TopicMonitorConnection",
                    "connectorType" : 
                    {
                        "class" : "ConnectorType",
                        "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.kafka.KafkaMonitorIntegrationProvider"
                    },
                    "endpoint" :
                    {
                        "class" : "Endpoint",
                        "address" : "{serverURL}"
                    }
                }
}
```

----
* Return to [Connector Catalog](.)

----
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
Copyright Contributors to the ODPi Egeria project.