<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

??? post "setBasicServerProperties"
    Set up the basic server properties in a single request. If any values are left blank, they are cleared in the server configuration document.

    === "Java"

        ```java
        String adminUserId = "garygeeke";
        String serverName = "active-metadata-server"
        String adminPlatformURLRoot = "https://127.0.0.1:9443";

        OMAGServerConfigurationClient configurationClient = new OMAGServerConfigurationClient(adminUserId, 
                                                                                              serverName, 
                                                                                              adminPlatformURLRoot);


        String organizationName = "Coco Pharmaceuticals";
        String serverDescription = "This server supports the governance teams";
        String serverUserId = "cocomds2npa";
        String serverPassword = "secret";
        String serverURLRoot = "https://localhost:9443"
        int    maxPageSize = 1000

        configurationClient.setBasicServerProperties(organizationName,
                                                     serverDescription,
                                                     serverUserId,
                                                     serverPassword,
                                                     serverURLRoot,
                                                     maxPageSize);
        ```

    === "Python"

        ```python
        admin_user_id="garygeeke"
        server_name="active-metadata-store"
        admin_platform_url_root="https://127.0.0.1:9443"
        
        config_client=CoreServerConfig(server_name,
                                       admin_platform_url_root,
                                       admin_user_id)
        
        local_server_description="This server supports the governance teams"
        organization_name="Coco Pharmaceuticals"
        local_server_url="https://127.0.0.1:9443"
        local_server_user_id="cocomds2npa"
        local_server_password="secret"
        max_page_size = 1000
        
        config_client.set_basic_server_properties(local_server_description,
                                                  organization_name,
                                                  local_server_url,
                                                  local_server_user_id,
                                                  local_server_password,
                                                  max_page_size)
        ```

    === "REST"
        ```
        POST {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-properties
        ```
        with a request body of:
        ```json
        {
          "localServerDescription" : "This server supports the governance teams",
          "organizationName" : "Coco Pharmaceuticals",
          "localServerURL" : "https://localhost:9443",
          "localServerUserId" : "cocomds2npa",
          "localServerPassword" : "secret",
          "maxPageSize" : 600
        }
        ```