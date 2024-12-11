<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# JDBC Integration Connector

!!! info "Connector details"
    - Connector Category: [Integration Connector](/concepts/integration-connector)
    - Hosting Service: [Database Integrator OMIS](/services/omis/database-integrator/overview)
    - Hosting Server: [Integration Daemon](/concepts/integration-daemon)
    - Source Module: [jdbc-integration-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/jdbc-integration-connector){ target=gh }
    - Jar File Name: `jdbc-integration-connector.jar`


The JDBC integration connector connects to a relational database and extracts its database schema information and catalogs it as open metadata.

![Figure 1](jdbc-integration-connector.svg)
> **Figure 1:** JDBC integration connector accessing a database and cataloguing its schemas in a metadata access server

It uses an embedded [JDBC Digital Resource Connector](/connectors/resource/jdbc-resource-connector) to access the database.

## Catalogued elements

The JDBC integration connector catalogs a database asset, database schema assets, tables, views, columns, primary and foreign keys. 

![Figure 2](/types/5/database-example.svg)
> **Figure 2:** Open metadata types used to catalog a database

If the endpoint information is available, it will also attach the connection information to access the database through the [JDBC Digital Resource Connector](/connectors/resource/jdbc-resource-connector).

![Figure 3](jdbc-integration-connector-connection-structure.svg)
> **Figure 3:** Connection information attached to catalogued database enables consumers of the database to get access to the database contents

## Configuration

This connector uses the [Database Integrator OMIS](/services/omis/database-integrator/overview) running in the [Integration Daemon](/concepts/integration-daemon).

This is its connection definition to use on the [administration commands that configure the Database Integrator OMIS](/guides/admin/servers/by-server-type/configuring-an-integration-daemon).

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="14"
    {
        "connection" : 
        {
            "class": "VirtualConnection",
            "connectorType" : 
            {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.jdbc.JdbcIntegrationConnectorProvider"
            },
            "embeddedConnections":
            [
                {
                    "class" : "EmbeddedConnection",
                    "embeddedConnection" :
                    {
                        "class" : "Connection",
                        "userId" : " ... ",
                        "clearPassword" : " ... ",
                        "connectorType" : 
                        {
                            "class": "ConnectorType",
                            "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.resource.jdbc.JdbcConnectorProvider"
                        },
                        "endpoint":
                        {
                            "class": "Endpoint",
                            "address" : " ... "
                        }
                    }
                }
            ],
            "configurationProperties": 
            {
                "catalog" : " ... ",
                "includeSchemaNames": [],
                "excludeSchemaNames": [],
                "includeTableNames": [],
                "excludeTableNames": [],
                "includeViewNames": [],
                "excludeViewNames": [],
                "includeColumnNames": [],
                "excludeColumnNames": []
            }
        }
    }
    ```

- `userId`: user
- `clearPassword`: password
- `address`: jdbc format address
- `catalog` (optional): null or missing means catalog will not be used during querying, empty string means objects that belong to no catalog will be queried, actual value means objects belonging to specified catalog will be queried
- `include/exclude` (optional): lists with database object names to filter out the import, no wildcards supported 


