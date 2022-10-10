<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# JDBC Integration Connector

??? info "Connector details"
    - Connector Category: [Integration Connector](/connectors/#integration-connector)
    - Hosting Service: [Database Integrator OMIS](/services/omis/database-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [jdbc-integration-connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/jdbc-integration-connector){ target=gh }
    - Jar File Name: `jdbc-integration-connector.jar`

## Overview

The JDBC integration connector catalogs a database, extracting schemas, tables, columns, primary and foreign keys. If the information is available, it will also attach the information to access the digital resource.

![Figure 1](jdbc-integration-connector-connection-structure.svg)
> **Figure 1:** Connection information attached to target database

## Configuration

This connector uses the [Database Integrator OMIS](/services/omis/database-integrator/overview)
running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Database Integrator OMIS](/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services).

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="14"
    {
        "connection" : {
            "class": "VirtualConnection",
            "connectorType" : {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.jdbc.JdbcIntegrationConnectorProvider"
            },
            "embeddedConnections":[
                {
                    "class" : "EmbeddedConnection",
                    "embeddedConnection" :{
                        "class" : "Connection",
                        "userId" : "{{userId}}",
                        "clearPassword" : "{{clearPassword}}",
                        "connectorType" : {
                            "class": "ConnectorType",
                            "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.resource.jdbc.JdbcConnectorProvider"
                        },
                        "endpoint":{
                            "class": "Endpoint",
                            "address" : "{{address}}"
                        },
                        "configurationProperties" :{
                            "connectorTypeQualifiedName" : "{{connectorTypeQualifiedName}}"
                        }
                    }
                }
            ]
        }
    }
    ```

    - Replace '{{userId}}' and '{{clearPassword}}' with the database username and password.
    - Replace '{{address}}' with the database jdbc url.
    - Replace '{{connectorTypeQualifiedName}}' with a connector type already saved. Required to construct the connection information   


