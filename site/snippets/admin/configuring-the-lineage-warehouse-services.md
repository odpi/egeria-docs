<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configuring the Lineage Warehouse Services

    !!! post "POST - Configure Lineage Warehouse Services"
        ```
        {{serverURLRoot}}/open-metadata/admin-services/users/{{userId}}/servers/{{serverName}}/lineage-warehouse/configuration
        ```
    
        ```json
        {
            "class": "LineageWarehouseConfig",
            "openLineageDescription": "Lineage Warehouse Service is used for the storage and querying of lineage",
            "lineageGraphConnection": {
                "class": "Connection",
                "displayName": "Lineage Graph Connection",
                "description": "Used for storing lineage in the Open Metadata format",
                "connectorType": {
                    "class": "ConnectorType",
                    "connectorProviderClassName": "org.odpi.openmetadata.openconnectors.governancedaemonconnectors.lineagewarehouseconnectors.janusconnector.graph.LineageGraphConnectorProvider"
                },
                "configurationProperties": {
                    "gremlin.graph": "org.janusgraph.core.JanusGraphFactory",
                    "storage.backend": "berkeleyje",
                    "storage.directory": "data/servers/{{ols-server-name}}/repository/berkeley",
                    "index.search.backend": "lucene",
                    "index.search.directory": "data/servers/{{ols-server-name}}/repository/searchindex"
                }
            },
            "accessServiceConfig": {
                "serverName": "{{server-name}}",
                "serverPlatformUrlRoot": "{{server-platform-url}}",
                "user": "admin",
                "password": "secret"
            },
            "inTopicConnection": {
                "class": "VirtualConnection",
                "qualifiedName": "OutTopicConnector.Asset Lineage OMAS",
                "displayName": "OutTopicConnector.Asset Lineage OMAS",
                "description": "Client-side topic connection.",
                "connectorType": {
                    "class": "ConnectorType",
                    "qualifiedName": "Asset Lineage Out Topic Client Connector",
                    "displayName": "Asset Lineage Out Topic Client Connector",
                    "description": "Connector supports the receipt of events on the Asset Lineage OMAS Out Topic.",
                    "connectorProviderClassName": "org.odpi.openmetadata.accessservices.assetlineage.outtopic.connector.AssetLineageOutTopicClientProvider"
                },
                "embeddedConnections": [
                    {
                        "class": "EmbeddedConnection",
                        "displayName": "Topic Event Bus",
                        "embeddedConnection": {
                            "class": "Connection",
                            "connectorType": {
                                "class": "ConnectorType",
                                "qualifiedName": "Egeria:OpenMetadataTopicConnector:Kafka",
                                "displayName": "Apache Kafka Open Metadata Topic Connector",
                                "description": "Apache Kafka Open Metadata Topic Connector supports string based events over an Apache Kafka event bus.",
                                "supportedAssetTypeName": "KafkaTopic",
                                "expectedDataFormat": "PLAINTEXT",
                                "connectorProviderClassName": "org.odpi.openmetadata.adapters.eventbus.topic.kafka.KafkaOpenMetadataTopicProvider"
                                "recognizedConfigurationProperties": [
                                    "producer",
                                    "consumer",
                                    "local.server.id",
                                    "sleepTime"
                                ]
                            },
                            "endpoint": {
                                "class": "Endpoint",
                                "headerVersion": 0,
                                "address": "OMRSTopic.server.omas.omas.assetlineage.outTopic"
                            },
                            "configurationProperties": {
                                "producer": {
                                    "bootstrap.servers": "server:port",
                                    "key.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
                                    "value.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
                                    "group.id": "custom-producer-id",
                                    "kafka.omrs.topic.id": "OMRSTopic"
                                },
                                "consumer": {
                                    "bootstrap.servers": "server:port",
                                    "key.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
                                    "value.deserializer": "org.apache.kafka.common.serialization.StringDeserializer",
                                    "group.id": "custom-consumer-id",
                                    "kafka.omrs.topic.id": "OMRSTopic"
                                }
                            }
                        }
                    }
                ]
            },
            "backgroundJobs": [
                {
                    "jobName": "LineageGraphJob",
                    "jobInterval": 120,
                    "jobEnabled": "false"
                },
                {
                    "jobName": "AssetLineageUpdateJob",
                    "jobInterval": 120,
                    "jobEnabled": "false",
                    "jobDefaultValue": "2021-01-01T00:00:00"
                }
            ]
        }
        ```
    
    #### Configuration reference
    
    | Property | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Is mandatory |
    |---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
    `lineageGraphConnection` | OCF configuration object that defines the Graph store connector type used. See [open-lineage-janus-connector](/connectors/governance-daemon/open-lineage-janus-connector) for more details.                                                                                                                                                                                                                                                                                                            | Yes |
    `accessServiceConfig.serverName` | the name of the metadata server where paired Asset Lineage OMAS is running.                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes |
    `accessServiceConfig.serverPlatformUrlRoot` | The URL of the OMAG server platform running the metadata server where paired Asset Lineage OMAS is running. Also see [start-up information](#start-up-information) section.                                                                                                                                                                                                                                                                                                                            | Yes |
    `accessServiceConfig.user` | The username to access the server running Asset Lineage OMAS.                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes |
    `accessServiceConfig.password` | The user password to access the server running Asset Lineage OMAS. Can be left out for non-secured access.                                                                                                                                                                                                                                                                                                                                                                                             | No |
    `inTopicConnection` | [Connection object](/concepts/connection) that provides the Asset Lineage OMAS topic connection definition . If provided, it will override the default configuration.                                                                                                                                                                                                                                                                                                                                  | No |
    `backgroundJobs[n].jobName` | Key used to match the job name pre-defined in the Lineage Warehouse. Supported values `LineageGraphJob` and `AssetLineageUpdateJob`                                                                                                                                                                                                                                                                                                                                                                  | No |
    `backgroundJobs[n].jobInterval` | Interval (**seconds**) to execute the repetitive task defined by the named job above                                                                                                                                                                                                                                                                                                                                                                                                                   | No |
    `backgroundJobs[n].jobEnabled` | Controls if the job will be running (enabled) or not (disabled). Omitting the item in the `backgroundJobs` list had the same effect as setting the job to disable.                                                                                                                                                                                                                                                                                                                                     | No |
    `backgroundJobs[n].jobDefaultValue` | Setting initial value for the task, only used in case of `AssetLineageUpdateJob`. When configured and not present in the store this value becomes the starting point in time to poll for updates. After successful update initial value is no longer used and last known value form the store. The value should be always specified in standard internet data-time format `YYYY-MM-DDThh:mm:ss`. See [ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) for more info and examples. | No |
     
    
    #### Removing the Lineage Warehouse Services from the server configuration
    
    !!! delete "DELETE - Remove Lineage Warehouse Services from the server"
        ```
        {{serverURLRoot}}/open-metadata/admin-services/users/{{userId]}}/servers/{{serverName}}/open-lineage/configuration
        ```