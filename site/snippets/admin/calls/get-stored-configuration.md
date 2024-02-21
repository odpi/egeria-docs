<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


??? get "getStoredConfiguration"
    Return the stored configuration document for the server.

    === "Java"

        ```java
        String adminUserId = "garygeeke";
        String serverName = "active-metadata-server"
        String adminPlatformURLRoot = "https://127.0.0.1:9443";

        OMAGServerConfigurationClient configurationClient = new ConfigurationManagementClient(adminUserId, 
                                                                                              adminPlatformURLRoot);

        OMAGServerConfig omagServerConfig = configurationClient.getOMAGServerConfig(serverName);
        ```

    === "Python"

        ```python
        admin_user_id="garygeeke"
        server_name="active-metadata-store"
        admin_platform_url_root="https://127.0.0.1:9443"
        
        config_client=CoreServerConfig(server_name,
                                       admin_platform_url_root,
                                       admin_user_id)
        
        config_client.get_stored_configuration()
        ```

    === "REST"

        ```
        GET {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/configuration
        ```