<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

??? get "getServerTypeClassification"
    Return the derived server type that is created from the classification of the server configuration.

    === "Java"

        ```java
        String adminUserId = "garygeeke";
        String serverName = "active-metadata-server"
        String adminPlatformURLRoot = "https://127.0.0.1:9443";

        OMAGServerConfigurationClient configurationClient = new OMAGServerConfigurationClient(adminUserId, 
                                                                                              serverName, 
                                                                                              adminPlatformURLRoot);

        ServerTypeClassificationSummary serverTypeClassification = configurationClient.getServerTypeClassification();
        ```
        The `getServerTypeClassification()` method throws `OMAGConfigurationErrorException` if there is insufficient content in the server's configuration document to determine the type of server. 

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
        GET {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/server-type-classification
        ```
        If there is insufficient content in the server's configuration document, you may get a response like this.
        ```json
        {
            "class": "ServerClassificationResponse",
            "relatedHTTPCode": 500,
            "exceptionClassName": "org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException",
            "exceptionCausedBy": "org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException",
            "actionDescription": "getServerTypeClassification",
            "exceptionErrorMessage": "OMAG-ADMIN-500-001 Method getServerTypeClassification for OMAG server active-metadata-store returned an unexpected exception of org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException with message OMAG-ADMIN-400-019 OMAG server active-metadata-store has been called with a configuration document that has no services configured",
            "exceptionErrorMessageId": "OMAG-ADMIN-500-001",
            "exceptionErrorMessageParameters": [
                "active-metadata-store",
                "getServerTypeClassification",
                "org.odpi.openmetadata.adminservices.ffdc.exception.OMAGConfigurationErrorException",
                "OMAG-ADMIN-400-019 OMAG server active-metadata-store has been called with a configuration document that has no services configured"
            ],
            "exceptionSystemAction": "The function requested failed.",
            "exceptionUserAction": "This is likely to be either a configuration, operational or logic error. Validate the request. Look at the user action for the embedded exception since this will provide the most specific information."
        }
        ```