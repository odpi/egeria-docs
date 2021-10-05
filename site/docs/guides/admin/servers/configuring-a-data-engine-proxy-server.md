<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Configuring a Data Engine Proxy Server

1. Start an [OMAG Server Platform](../../../open-metadata-resources/open-metadata-tutorials/omag-server-tutorial)
1. Configure the Data Engine Proxy Server:

    **POST** following JSON object (following shows an example for IBM DataStage)

    ```json
    {
        "class": "DataEngineProxyConfig",
        "accessServiceRootURL": "{serverURLRoot}",
        "accessServiceServerName": "{MetadataServerName}",
        "dataEngineConnection": {
            "class": "Connection",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.egeria.connectors.ibm.datastage.dataengineconnector.DataStageConnectorProvider"
            },
            "endpoint": {
                "class": "Endpoint",
                "address": "myhost.somewhere.com:9445",
                "protocol": "https"
            },
            "userId": "{dataEngineAccessUserId}",
            "clearPassword": "dataEngineAccessPassword"
        },
        "pollIntervalInSeconds": 60
    }
    ```
    
    to the following address

    ```
    {serverURLRoot}/open-metadata/admin-services/users/{userId}/servers/{serverName}/data-engine-proxy-service/configuration
    ```

    The object *dataEngineConfig* is the information required to implement the specific proxy connector to the data engine. The keys should be modified based on the information needed by the connector.

1. Start the instance of the OMAG Server Platform

    **POST** to the following address
    
    ```
    {serverURLRoot}/open-metadata/admin-services/users/{userId}/servers/{serverName}/instance
    ```

--8<-- "snippets/abbr.md"
