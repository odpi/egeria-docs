<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Sample Lineage Event Receiver Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Service: [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [openlineage-integration-connectors :material-github:](https://github.com/odpi/egeria-connector-integration-lineage-event-driven-sample){ target=gh }
    - Jar File Name: `egeria-connector-integration-lineage-sample-1.0-SNAPSHOT.jar`

The Sample Lineage Event Receiver integration connector receives json events from an event topic and publishes them to the lineage integration connectors which use the Lineage Integrator OMIS.
This connector communicates using an Open Metadata Access Services (OMAS), both the connector and the server it is talking to need to be running with Egeria jar at level 3.15-SNAPSHOT or above.
This is important, as the OMAS capability required for this connector is fully functional at this level or above. 

This is a sample [integration connector](https://egeria-project.org/concepts/integration-connector/?h=integration+conne) that shows how
to listen to a topic for json payloads. This integration connector is an extension of the
[Lineage Integrator Open Metadata Integration Service (OMIS)](https://egeria-project.org/services/omis/lineage-integrator/overview/), where it
catalogues lineage information from a third party technology, including processes,
schemas and the data assets they are working with. See [here](https://github.com/odpi/egeria-connector-integration-lineage-event-driven-sample/tree/main/src/test/resources)
for some sample json events in the format that this connector expects.


![Figure 1](sample-lineage-event-receiver-integration-connector.svg)
> **Figure 1:** Operation of the Sample Lineage event receiver integration connector

It uses an embedded [Open Metadata Topic Connector](/concepts/open-metadata-topic-connector) to receive events from the topic.

__Important notice__
The gradle JAR step will include some of the dependencies into the connector JAR, making is a semi-Fat Jar. This makes sure that additional dependencies are automatically deployed together with the connector.

## Configuration

This connector uses the [Lineage Integrator OMIS](/services/omis/lineage-integrator/overview) running in the [Integration Daemon](/concepts/integration-daemon).

The connection definition to use on the [administration commands that configure the Lineage Integrator OMIS](/guides/admin/servers/by-server-type/configuring-an-integration-daemon) is a *VirtualConnection* with an embedded [OpenMetadataTopicConnection](/concepts/open-metadata-topic-connector). 

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="11"
    {
       "connection" : 
                    { 
                        "class" : "VirtualConnection",
                         "qualifiedName": "Egeria:IntegrationConnector:Lineage:OpenLineageEventReceiverConnection",
                        "connectorType": {
                           "class": "ConnectorType",
                           "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.lineage.sample.SampleLineageEventReceiverIntegrationProvider"
                         }
                         "embeddedConnections" : [ {{topicConnection}} ]
                    }
    }
    ```

    - Add the connection for the open metadata topic connector in the `embeddedConnections` section replacing {{topicConnection}}.  This will have the topic name in the endpoint's `networkAddress`.  The example below shows the connection for the [Kafka open metadata topic connector](/connectors/resource/kafka-open-metadata-topic-connector) which supports events from [Apache Kafka](https://kafka.apache.org/).

    !!! example "Kafka topic connection configuration"
        ```json linenums="1" hl_lines="11-40"
        {
           "connection" : 
                        { 
                            "class" : "VirtualConnection",
                            "qualifiedName" : "Egeria:IntegrationConnector:Lineage:OpenLineageEventReceiver Connection",
                            "connectorType" : 
                            {
                                "class" : "ConnectorType",
                                "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.openlineage.OpenLineageEventReceiverIntegrationProvider"
                            },
                            "embeddedConnections" : [
                            {
                                "class": "EmbeddedConnection",
                                "embeddedConnection : 
                                {
                                    "class": "Connection",
                                    "qualifiedName": "Kafka Open Metadata Topic Connector",
                                    "connectorType":
                                    {
                                        "class": "ConnectorType",
                                        "connectorProviderClassName": "org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider"      
                                    },
                                    "endpoint":
                                    {
                                        "class": "Endpoint",
                                        "address": {{sampleLineageTopicName}}
                                    },
                                    "configurationProperties": 
                                    {
                                        "producer": 
                                        {
                                            "bootstrap.servers": {{kafkaEndpoint}}
                                        },
                                        "local.server.id": "{{localServerId}}",
                                        "consumer":
                                        {
                                            "bootstrap.servers": {{kafkaEndpoint}}
                                        }
                                    }
                                }
                            }]
                        }
        }
        ```
        
        - Add the name of the topic in {{sampleLineageTopicName}}; the integration daemon's server id in {{localServerId}} and the endpoint for Apache Kafka (for example localhost:9092) in {{kafkaEndpoint}}.



## Postman
There is a sample postman file [here](https://github.com/odpi/egeria-connector-integration-lineage-event-driven-sample/blob/main/postman/Egeria%20Integration%20Connector%20sample%20event%20Lineage.postman_collection.json) to
configure and start this connector.

## Test Utility
There is a java application that produces events for testing [here](https://github.com/odpi/egeria-connector-integration-lineage-event-driven-sample/blob/main/src/test/java/org/odpi/openmetadata/adapters/connectors/integration/lineage/sample/utils/EventProducerUtility.java). It allows the user to easily submit any of the json files used in the junit.
It is built with the junit tests using the top level gradle file.

## Event json

The event json describes a Process , with a qualified name ("Id") and display name ("Name").
Then there is an Input array of assets and an output array of assets. In the input array are datasets, the output are Kafka topics.
The Output also describes an event schema.

### Assumptions
- No deletion of assets or processes. Lineage is always adding these.
- Where effectivity dates are specified on APIs- none are supplied.
- This is only doing asset design lineage, no column lineage or operational lineage.
- All finds are done by qualifiedName - if more than one element is returned - we use the first.
- Catalog the assets, schema and process if required. This can result in
    - deletion, creation and / or updates of schemaAttributes
    - deletion and / or creation of the Event types
    - creation and / or update of assets
- Save the lineage flow Assets(DataSet) -> Process -> Assets(KafkaTopic)
- Change of the input and output assets results in removals of old dataflows as well as adding the new dataflows.
- All updates are replacements not merges- e.g. schema attributes are replaced not merged
- There is no support for update schematype (EventType) as it only has a title - which is used to derive the qualified name - so there is nothing to update.
- There is no description for schematypes.
- AssetManager is used, so AssetManagerIsHome is true on all calls.
- If an event comes in with different input assets and or output assets, we do not remove the existing lineage relationships.
- The lineage relationships shown here as DataFlow relationships. In practice, it depends on
  what the process is doing as to which lineage relationships should be created.
- The Dataflow relationship qualified name is set to null. This is not appropriate if multiple
  supply chains create a lineage relationship between an asset and process. Dataflow relationships between the assets and process are [multi-link](https://egeria-project.org/concepts/uni-multi-link/?h=multi+link#multi-link-relationships).
- Though it is possible to supply an array of schemas, currently only the first EventType is processed. See [https://github.com/odpi/egeria/issues/7134](https://github.com/odpi/egeria/issues/7134) has been raised to allow
  support of EventTypeLists. This sample will need to be enhanced to make use of these new APIs.


### Example json
{
"Id": "1234567890",
"Name": "TestRes",
"Description": "TestResource",
"Bounded Context": "TestResource",
"Team": "ITG",
"Input": [{
"Id": "C6B7B1B717C840F686EE2426241ED18CE1D053019534F03495E8CD644976FA37",
"Name": "Foo",
"SQL": "select * from foo;"
}],
"Output": [{
"Id": "vertriebskunde-services.agree-kundendaten",
"Name": "Kundendaten",
"Schema-type": "json-schema",
"Schemas": [{
"$id": "https://example.com/person.schema.json",
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "Person",
"type": "object",
"properties": {
"firstName": {
"type": "string",
"description": "The person's first name."
},
"lastName": {
"type": "string",
"description": "The person's last name."
},
"age": {
"description": "Age in years which must be equal to or greater than zero.",
"type": "integer"
},
"derivedAge": {
"description": "Derived Age.",
"type": "integer",
"formula": "test-formula"
},
"derivedAge2": {
"description": "Derived Age.",
"type": "integer",
"formula": "test-formula2"
}
}
}]
}]
}
---8<-- "snippets/abbr.md"
