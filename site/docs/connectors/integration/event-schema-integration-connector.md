<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Event Schema Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Service: [Topic Integrator OMIS](/services/omis/topic-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [event-schema-integration-connector :material-github:](https://github.com/odpi/egeria-connector-integration-event-schema){ target=gh }
    - Jar File Name: `event-schema-integration-connector.jar`

This ist the Egeria integration connector for event schemas. It retrieves the information of event schemas by querying the subjects and schemas of a Confluent&trade; api-compatible schema registry, then creates or updates the appropriate Egeria metadata so that it always mirrors the schema registry content.

The Egeria metadata that is created are [Event Type Lists](https://egeria-project.org/types/5/0535-Event-Schemas/#eventtypelist), [Event Types](https://egeria-project.org/types/5/0535-Event-Schemas/#eventtype), [Event Schema Attributes](https://egeria-project.org/types/5/0535-Event-Schemas/#eventschemaattribute). Schema attributes are created recursively to represent deeper structured Avro Schemas. That means, schema attributes can have [Nested Schema Attributes Relationships](https://egeria-project.org/types/5/0505-Schema-Attributes/?h=nestedsche#nestedschemaattribute-relationship).

Each created Event Type is linked to a [Kafka Topic](https://egeria-project.org/types/2/0223-Events-and-Logs/?h=kafkatopic#kafkatopic) which must already be in place - possibly created by a [Strimzi Monitor Integration Connector](https://egeria-project.org/connectors/integration/strimzi-monitor-integration-connector/?h=strimzi). The connector tries to match the EventTypes to an existing topic in Egeria using the part of the subject name of the schema up to the last hyphen (`-`). If the subject name does not contain any hypens the complete name is considered as the topic. If no topic is found the schema is ignored and a warning is logged in the audit log.

This connector needs to be configured. The following steps can be performed using the postman collection to set this connector up.


![Figure 1](event-schema-integration-connector.svg)
> **Figure 1:** Operation of the Event Schema integration connector

__Important notice__

The gradle JAR step will include some of the dependencies into the connector JAR, making is a semi-Fat Jar. This makes sure that additional dependencies are automatically deployed together with the connector.


## Configuration

This connector uses the [Topic Integrator OMIS](/services/omis/topic-integrator/overview) running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Topic Integrator OMIS](/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services).

!!! example "Connection configuration"
```json linenums="1" hl_lines="14"
    {
    "class": "IntegrationServiceRequestBody",
    "omagserverPlatformRootURL": "{{EGERIA_MDS_URL}}",
    "omagserverName": "{{EGERIA_MDS_SERVER}}",
    "connectorUserId": "{{EGERIA_USER}}",
    "integrationConnectorConfigs": [
        {
            "class": "IntegrationConnectorConfig",
            "connectorName": "EventSchemaIntegrator",
            "typeName": "Event Schema Integration Connector",
            "connection": {
                "class": "Connection",
                "connectorType": {
                    "class": "ConnectorType",
                    "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.eventschema.EventSchemaIntegrationProvider"
                },
                "configurationProperties": {
                    "topicNamespace": "{{TOPIC_NAMESPACE}}"
                },
                "endpoint": {
                    "class": "Endpoint",
                    "address": "{{SCHEMA_REGISTRY_ENDPOINT}}"
                }
            },
            "metadataSourceQualifiedName": "{{EVENT_SCHEMA_SOURCE_NAME}}",
            "refreshTimeInterval": "{{EVENT_SCHEMA_CONNECTOR_REFRESH_INTERVAL}}",
            "permittedSynchronization": "FROM_THIRD_PARTY"
        }
    ]
}
```
Set the following variables with valid value:

| Variable | Description | Sample |
|----------|-------------|--------|
| EVENT_SCHEMA_CONNECTOR_REFRESH_INTERVAL| Time in seconds between the refresh of the metadata by the connector| `5` |
| EVENT_SCHEMA_SOURCE_NAME| Metadata source qualified name used for the created metadata. This must match the metadata source qualified name of the KafkaTopics to be matched against.| `my-event-metadata-source` |
| EGERIA_MDS_URL| URL of the platform hosting the [Metadata Access Point](https://egeria-project.org/concepts/metadata-access-point/) to use for the integration of the event schema metadata | `https://localhost:8443` |
| EGERIA_MDS_SERVER| Name of the metadata server | `mds1` |
| EGERIA_USER| Name of the user | `garygeeke` |
| EGERIA_SERVER| Name of the integration server | `evtschema1` |
| EGERIA_URL| URL of the platform hosting the integration server | `https://localhost:9443` |
| TOPIC_NAMESPACE| Namespace in which the topics are found which are used to map the EventTypes to. This is used as a prefix to find the correct topic. | `customer_topics` |
| SCHEMA_REGISTRY_ENDPOINT| The URL of the Schema Registry. | `https://my-schemaregistry:8081`|




## Running locally for testing

You will need to have an OMAG platform with a configured metadata server and activated DataManager OMAS. You will also have a Docker client installed locally and a running Docker daemon.

### Run gradle build
On a terminal,
* navigate to the folder that this README.md is in.
* run ```./gradlew clean build```

### Build Docker image
* run `docker build -t event-schema-integration-connector .` 

### Run Docker container
* run `docker run event-schema-integration-connector`.


---8<-- "snippets/abbr.md"
