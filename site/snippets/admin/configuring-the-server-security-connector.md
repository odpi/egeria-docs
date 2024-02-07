<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

## Configure the server security connector

Metadata that is being aggregated from different sources is likely to need comprehensive access controls.

Egeria provides [fine-grained security control for metadata access](/services/metadata-security-services). It is implemented in a [server metadata security connector](/concepts/server-metadata-security-connector) that is called whenever requests are made for to the server.

Security is configured for a specific [OMAG Server](/concepts/omag-server) by adding a connection for this connector to the server's [configuration document](/concepts/configuration-document)using the following command.

!!! post "POST - configure security connector"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/security/connection
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

??? example "Example: set up the sample server security connector"
    For example, this is the connection that would set up the [sample server security connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } provided for the Coco Pharmaceuticals case study:

    ```json
    {
        "class": "Connection",
        "connectorType": {
            "class": "ConnectorType",
            "connectorProviderClassName": "org.odpi.openmetadata.metadatasecurity.samples.OpenMetadataServerSecurityProvider"
        }
    }
    ```

### Determine configured security

!!! get "GET - query the server security connector setting"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/security/connection
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
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/security/connection
    ```

    This removes all authorization checking from the server.
