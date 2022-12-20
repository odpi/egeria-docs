<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Strimzi Monitor Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Service: [Topic Integrator OMIS](/services/omis/topic-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [srimzi-integration-connector :material-github:](https://github.com/odpi/egeria-connector-integration-topic-strimzi){ target=gh }
    - Jar File Name: `strimzi-integration-connector.jar`

This Egeria integration connector for [Strimzi](https://strimzi.io/) topics. It obtains the Kafka
topic information by querying the custom resource definitions (CRDs) in Strimzi, then creates the appropriate Egeria metadata,
adding, deleting and updating the Egeria metadata so that is always mirrors the trimzi content.

The Egeria metadata that is created is a [KafkaTopic](https://egeria-project.org/types/2/0223-Events-and-Logs/?h=kafkatopic).

This integration connector needs to be configured. The following steps can be performed using the postman collection to set this connector up.
The connector takes Kafka topic information including the description, partitions and replicas and pushes that information into
Egeria.


![Figure 1](strimzi-monitor-integration-connector.svg)
> **Figure 1:** Operation of the Strimzi monitor integration connector

__Important notice__

The gradle JAR step will include some of the dependencies into the connector JAR, making is a semi-Fat Jar. This makes sure that additional dependencies are automatically deployed together with the connector.


## Configuration

This connector uses the [Topic Integrator OMIS](/services/omis/topic-integrator/overview) running in the [Integration Daemon](/concepts/integration-daemon).

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
                            "connectorProviderClassName" : "org.odpi.openmetadata.adapters.connectors.integration.strimzi.StrimziMonitorIntegrationProvider"
                        },
                        "endpoint" :
                        {
                            "class" : "Endpoint",
                            "address" : "{{serverURL}}"
                        }
                    }
    }
    ```

    - Replace `{{serverURL]}` with the network address of the Strimzi server.


`configurationProperties` parameters

| Event mapper configuration parameter name | default      | Description                                                   |
|-------------------------------------------|--------------|---------------------------------------------------------------|
| topicNamePrefix                           | empty string | This is a prefix for the topic names that will be monitored.  |
| token                                     | null         | security token required to make calls to Strimzi.             |
| descriptionAnnotationField                | null         | the name of the field in the CRD to get the topic description |



## Running locally for testing

You will need to have an omag platform with the connector jar, a metadata server called cocoMDS1 defined.
The below process is how you configure the Strimzi integration connector manually.

Import the [postman collection]([Postman collection](https://github.com/odpi/egeria-connector-integration-topic-strimzi/blob/main/postman/Strimzi%20integration%20connector%20configuration.postman_collection.json)) into [Postman](https://www.postman.com/)
The required values should be supplied as postman environment variables for this script.

Then run the scripts in order. Steps 1 through 3 to configure the connector.

* Step 3 is where the integration connector configuration parameters are passed into the connector.
* Step 4 Starts the connector.
* Step 5 shows how to retrieve the configuration

The configuration only needs to occur once (unless you want to change it), so subsequently you only need to issue step 4 to start it.

## Testing mutations
Import the [postman collection](https://github.com/odpi/egeria-connector-integration-topic-strimzi/blob/main/postman/Strimzi%20REST%20calls.postman_collection.json) into [Postman](https://www.postman.com/)

Set the postman variables you want and run the create, delete and update scripts.

---8<-- "snippets/abbr.md"
