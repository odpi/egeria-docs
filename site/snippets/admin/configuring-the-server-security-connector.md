<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

## Configure the server security connector

Metadata that is being aggregated from different sources is likely to need comprehensive access controls.

Egeria provides [fine-grained security control for metadata access](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/common-services/metadata-security). It is implemented in a [server metadata security connector](/concepts/server-metadata-security-connector) that is called whenever requests are made for to the server.

Security is configured for a specific [OMAG Server](/concepts/omag-server) by adding a connection for this connector to the server's [configuration document](/concepts/configuration-document) using the following command.

!!! post "POST - configure security connector"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/security/connection
    ```

    This passes in a connection used to create the server security connector in the request body.  

    ```json
    {
        "class": "Connection",
        "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "{fullyQualifiedJavaClassName}"
        }
    }
    ```

??? example "Example: set up the Open Metadata Access Security Connector"
    For example, this is the connection that sets up the [Open Metadata Access Security Connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors/open-metadata-access-security-connector){ target=gh }.  It is a `VirtualConnection` because the security connector reads its users, groups and access controls from a [secrets store](/concepts/secrets-store-connector), whose connection is embedded inside it.  The quickstart uses the YAML secrets store connector, and fills in the values written as `~{...}~` from its server properties.

    ```json
    {
        "class": "VirtualConnection",
        "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.openmetadata.metadatasecurity.accessconnector.OpenMetadataAccessSecurityProvider"
        },
        "embeddedConnections": [{
            "class": "EmbeddedConnection",
            "embeddedConnection": {
                "class": "Connection",
                "connectorType": {
                    "class": "ConnectorType",
                    "connectorProviderClassName": "~{secretsStoreProvider}~"
                },
                "endpoint": {
                    "class": "Endpoint",
                    "networkAddress": "~{userDirectorySecretsStore}~"
                },
                "configurationProperties": {
                    "secretsCollectionName": "~{userDirectorySecretsCollectionName}~"
                }
            }
        }]
    }
    ```

    The [Security Guide](/guides/security/overview#the-server-metadata-security-connector) explains how this connector checks each request.

### Determine configured security

!!! get "GET - query the server security connector setting"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/security/connection
    ```

??? success "Response indicating no security"
    ```json
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200
    }
    ```

??? success "Response indicating a specific security connector"
    If the response looks more like the JSON below, a connector is configured. The `connectorProviderClassName` tells you which connector is being used.

    ```json hl_lines="8"
    {
        "class": "ConnectionResponse",
        "relatedHTTPCode": 200,
        "connection": {
            "class": "Connection",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "{fullyQualifiedJavaClassName}"
            }
        }
    }
    ```

### Remove configured security

!!! delete "DELETE - remove configured security connector"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/security/connection
    ```

    This removes all authorization checking from the server.
