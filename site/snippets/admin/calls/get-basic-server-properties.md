<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

??? get "getBasicServerProperties"
    Return the basic server properties in a single request.

    === "Java"

        ```java
        String adminUserId = "garygeeke";
        String serverName = "active-metadata-server"
        String adminPlatformURLRoot = "https://127.0.0.1:9443";

        OMAGServerConfigurationClient configurationClient = new OMAGServerConfigurationClient(adminUserId, 
                                                                                              serverName, 
                                                                                              adminPlatformURLRoot);

        BasicServerProperties basicServerProperties = configurationClient.getBasicServerProperties();
        ```

    === "Python"

        ```python
        admin_user_id="garygeeke"
        server_name="active-metadata-store"
        admin_platform_url_root="https://127.0.0.1:9443"
        
        config_client=CoreServerConfig(server_name,
                                       admin_platform_url_root,
                                       admin_user_id)

        config_client.get_basic_server_properties()
        ```

    === "REST"
        ```
        GET {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-properties
        ```
