<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Configuring a Data Engine Proxy Server

## Overview 

Each [type of OMAG Server](/concepts/omag-server/#types-of-omag-server) is configured by creating a [configuration document](/concepts/configuration-document). For data engine proxy server, following can be configured:

![Configuration for an data engine proxy server](data-engine-proxy-config.svg)


??? info "Configuring the basic properties"
    --8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

??? info "Configuring the audit log"
    --8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

??? info "Configuring the server security connector"
    --8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md"

??? info "Configuring the Data Engine Proxy Services"
    ## Configuring Data Engine Proxy Services 
    
    ???+ intermediate "Course-grained helper command"
        !!! post "POST - Configure Date Engine Proxy Services"
            ```
            {{serverURLRoot}}/open-metadata/admin-services/users/{{userId}}/servers/{{serverName}}/data-engine-proxy-service/configuration
        
            ```
        
            ```json
            {
                "class": "DataEngineProxyConfig",
                "accessServiceRootURL": "{{{metadata-server-platform-url}}}",
                "accessServiceServerName": "{{metadata-server-name}}",
                "dataEngineConnection": {
                    "class": "Connection",
                    "connectorType": {
                        "class": "ConnectorType",
                        "connectorProviderClassName": "org.odpi.egeria.connectors.ibm.datastage.dataengineconnector.DataStageConnectorProvider"
                    },
                    "endpoint": {
                        "class": "Endpoint",
                        "address": "{{data-engine-endpoint}}",
                        "protocol": "https"
                    },
                    "userId": "{{data-engine-user}}",
                    "clearPassword": "{{data-engine-password}}"
                },
                "pollIntervalInSeconds": 60
            }
            ```
    #### Configuration Reference
    
    | Property               | Description | Is mandatory |
    |------------------------|---|---|
    | dataEngineConnection   | OCF connection configuration object that defines the connector type and its properties. Refer to specific connector for detailed reference. Example provided for [IBM Data Stage connector](https://github.com/odpi/egeria-connector-ibm-information-server/tree/main/datastage-adapter).  | Yes |
    |  pollIntervalInSeconds | The polling interval in seconds to call the sequence extracting metadata. | Yes | 
    
    #### Removing the Data Engine Services from the server configuration
    
    ???+ intermediate "Course-grained helper command"
        !!! delete  "DELETE - Remove Data Engine Configuration from the server"
            ```
            {{serverURLRoot}}/open-metadata/admin-services/users/{{userId}}/servers/{{serverName}}/data-engine-proxy-service/configuration
            ```
    
--8<-- "snippets/abbr.md"
