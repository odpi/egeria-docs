<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Kafka Topics Audit Integration Connector

??? info "Connector details"
    - Connector Category: [Integration Connector](/connectors/integration-connector)
    - Hosting Service: [Topic Integrator OMIS](/services/omis/topic-integrator)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [kafka-topics-audit-connector :material-github:](https://github.com/odpi/egeria-dev-projects/tree/master/kafka-topics-audit-connector){ target=gh }
    - Jar File Name: `kafka-topics-audit-connector.jar`

## Overview

The kafka topics audit integration connector monitors an Apache Kafka server and validates that a  [KafkaTopic](/types/2/0223-Events-and-Logs) asset is catalogued for each topic that is known to the server.


![Figure 1](kafka-topics-audit-integration-connector.svg)
> **Figure 1:** Operation of the kafka topics audit integration connector


## Configuration

This connector uses the [Topic Integrator OMIS](/services/omis/topic-integrator/overview)
running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Topic Integrator OMIS](/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services).

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="14"
    {
       "connection" : 
                    { 
                        "class" : "Connection",
                        "qualifiedName" : "TopicMonitorConnection",
                        "connectorType" : 
                        {
                            "class" : "ConnectorType",
                            "connectorProviderClassName" : "org.odpi.openmetadata.devprojects.connectors.integration.kafka.KafkaTopicsAuditIntegrationProvider"
                        },
                        "endpoint" :
                        {
                            "class" : "Endpoint",
                            "address" : "{{serverURL}}"
                        }
                    }
    }
    ```

    - Replace `{{serverURL]}` with the network address of Kafka's bootstrap server (for example, `localhost:9092`).

---8<-- "snippets/abbr.md"