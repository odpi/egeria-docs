<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

!!! get "getServerTypeClassification"
    Return the derived server type that is created from the classification of the server configuration.

    === "Java"

        ```java
        OMAGServerConfigurationClient configurationClient = new OMAGServerConfigurationClient(adminUserId, 
                                                                                              serverName, 
                                                                                              adminPlatformURLRoot);

        ServerTypeClassificationSummary serverTypeClassification = configurationClient.getServerTypeClassification();
        ```

    === "Python"

        ```python
        admin_user_id="garygeeke"
        server_name="active-metadata-store"
        admin_platform_url_root="https://127.0.0.1:9443"
        
        config_client=CoreServerConfig(server_name,
                                       admin_platform_url_root,
                                       admin_user_id)
        
        config_client.get_server_classification()
        ```

    === "REST"
        ```
        GET {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-type-classification"
        ```