<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the view services

[Open Metadata View Services (OMVSs)](/services/omvs) provide task-oriented, domain-specific REST API services for user interfaces, and other non-Java programming environments, such as python, that integrate with the open metadata ecosystem.  The view services call a [metadata access server](/concepts/metadata-access-server) to send and retrieve metadata.

To get a description of each of the view services that are supported by an [OMAG Server Platform](/concepts/omag-server-platform), list the registered view services.

???+ info "List registered view services"
    The registered view services for an [OMAG Server Platform](/concepts/omag-server-platform) are the view services whose implementation is included in the platform's classpath:
    
    !!! get "GET - list registered view services"
        ```
        {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/server-platform/registered-services/view-services
        ```
        
        ??? success "Response from listing registered view services"
            ```json
            {
                "class": "RegisteredOMAGServicesResponse",
                "relatedHTTPCode": 200,
                "services": [
                    {
                        "serviceId": 800,
                        "serviceName": "Glossary Author OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "glossary-author",
                        "serviceDescription": "View Service for glossary authoring.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/glossary-author/overview"
                    },
                    {
                        "serviceId": 803,
                        "serviceName": "Dynamic Infrastructure and Operations OMVS",
                        "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                        "serviceURLMarker": "dino",
                        "serviceDescription": "Explore and operate an open metadata ecosystem.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/dino/overview"
                    },
                    {
                        "serviceId": 801,
                        "serviceName": "Repository Explorer OMVS",
                        "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                        "serviceURLMarker": "rex",
                        "serviceDescription": "Explore open metadata instances.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/rex/overview"
                    },
                    {
                        "serviceId": 806,
                        "serviceName": "Glossary Workflow OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "glossary-workflow",
                        "serviceDescription": "Create glossary terms and organize them into categories as part of a controlled workflow process. It supports the editing glossary and multiple states.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/glossary-workflow/overview/"
                    },
                    {
                        "serviceId": 807,
                        "serviceName": "My Profile OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "my-profile",
                        "serviceDescription": "Manage information about the logged on user as well as their preferences.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/my-profile/overview/"
                    },
                    {
                        "serviceId": 802,
                        "serviceName": "Type Explorer OMVS",
                        "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                        "serviceURLMarker": "tex",
                        "serviceDescription": "Explore the open metadata types in a repository or cohort.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/tex/overview"
                    },
                    {
                        "serviceId": 804,
                        "serviceName": "Server Author OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "server-author",
                        "serviceDescription": "Author server configuration.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/server-author/overview/"
                    },
                    {
                        "serviceId": 805,
                        "serviceName": "Glossary Browser OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "glossary-browser",
                        "serviceDescription": "View glossary terms and categories within a glossary.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/glossary-browser/overview/"
                    },
                    {
                        "serviceId": 808,
                        "serviceName": "Asset Catalog OMVS",
                        "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                        "serviceURLMarker": "asset-catalog",
                        "serviceDescription": "Search and understand your assets.",
                        "serviceWiki": "https://egeria-project.org/services/omvs/asset-catalog/overview/"
                    }
                ]
            }
            ```
The values returned for each registered view service are:

| Property                       | Use                                                                                                       |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| `serviceId`                    | Unique identifier of the service.                                                                         |
| `serviceName`                  | Name of the service, used in messages and documentation.                                                  |
| `serviceDevelopmentStatus`     | Describes the relative maturity of the view service.                                                      |
| `serviceURLMarker`             | Returns the unique name for the view service used in REST API URLs to identify a particular view service. |
| `serviceDescription`           | Returns a short description of the view service to help you choose which ones you want.                   |
| `serviceWiki`                  | Link to the documentation for the view service.                                                           |

To activate a specific view service in a view server, add an entry for the view service to the view server's configuration document.
View services can be configured into a view server either altogether or individually.

=== "Configure a single view service"

    A specific view service can be individually configured with the following command.  Listing the registered view services is a good way to discover the `serviceURLMarker` values used when configuring individual view services.

    !!! post "POST - configure a specific view service"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```

        The request body must contain a `ViewServiceRequestBody` object, while the `serviceURLMarker` can
        be found by [listing the registered view services](#list-configured-view-services).

=== "configure all view services"

    It is also possible to configurate a set of view services at the same time, using the following command:

    !!! post "POST - configure multiple view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
        ```

        Again the request body must contain a `ViewServiceRequestBody` object.  This object is used to configure each of the registered view services.

The `ViewServiceRequestBody` used on either of these requests contains 4 pieces of information:

* `omagServerName` - the name of the metadata access server that is to provide the metadata services to the view service.
* `omagServerPlatformRootURL` - platform URL root where the metadata access server is running.
* `viewServiceOptions` - optional list of specific options used to configure the behaviour of the view service.
* `resourceEndpoints` - a list of `ResourceEndpointConfig` objects.  These objects are used to configure dropdowns on calling user interfaces used to select a specific OMAG Server Platform or OMAG Server that the UI is to connect to.  The aim is to control which platforms and servers can be selected.

A resource endpoint describing a platform contains the following properties:

| Property           | Use                                                                   |
|--------------------|-----------------------------------------------------------------------|
| `resourceCategory` | required property, set to "Platform".                                 |
| `platformName`     | required property, a unique name given to a "Platform" resource.      |
| `platformURLRoot`  | required property, the URL root used to call the "Platform" resource. |
| `description`      | optional property that is displayed by some view services.            |

A resource endpoint describing an OMAG Server has the following properties:

| Property             | Use                                                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|
| `resourceCategory`   | required property, set to "Server"                                                                                        |
| `platformName`       | required property, a reference to a named "Platform" resource endpoint describing where the "Server" resource is located. |
| `serverName`         | required property, set to the name of the OMAG Server.                                                                    |
| `serverInstanceName` | required property, a unique name for the combination of server and platform.                                              | 
| `description`        | optional property describing the server.                                                                                  |


??? example "Example ViewServiceRequestBody"

    ```json
    {
        "class":"ViewServiceRequestBody",
        "omagserverName":"active-metadata-store",
        "omagserverPlatformRootURL":"https://localhost:9443",
        "resourceEndpoints" : [
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Platform",
                "platformName"       : "Platform:9443",
                "platformRootURL"    : "http://localhost:9443",
                "description"        : "This is the default OMAG Server Platform."
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "platformName"       : "Platform:9443",
                "serverInstanceName" : "Active Metadata Access Store",
                "serverName"         : "active-metadata-store",
                "description"        : "Metadata server with XTDB repository and supporting Apache Kafka notifications."
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "platformName"       : "Platform:9443",
                "serverInstanceName" : "Simple Metadata Access Store",
                "serverName"         : "simple-metadata-store",
                "description"        : "Metadata server with in-memory repository and no event notifications."
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "platformName"       : "Platform:9443",
                "serverInstanceName" : "Integration Daemon",
                "serverName"         : "integration-daemon",
                "description"        : "Integration daemon supporting the synchronization of metadata with thrid party platfrms and tools."
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "platformName"       : "Platform:9443",
                "serverInstanceName" : "Engine Host",
                "serverName"         : "engine-host",
                "description"        : "Engine host server running the AssetSurvey and Asset Governance governance engines."
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "platformName"       : "Platform:9443",
                "serverInstanceName" : "View Server",
                "serverName"         : "view-server",
                "description"        : "View server providing REST API support to user interfaces and non-Java environments."
            }
        ]
    }
    ```

It is possible to list the configured view services for a view Server using the following command:

!!! get "GET - list configured view services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
    ```

??? success "Response from listing configured view services"
    The response will be a `RegisteredOMAGServicesResponse` which contains a list of `RegisteredOMAGService` objects, that will look something like the following:

    ```json
    {
        "class": "RegisteredOMAGServicesResponse",
        "relatedHTTPCode": 200,
        "services": [
            {
                "serviceId": 800,
                "serviceName": "Glossary Author OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "glossary-author",
                "serviceDescription": "View Service for glossary authoring.",
                "serviceWiki": "https://egeria-project.org/services/omvs/glossary-author/overview"
            },
            {
                "serviceId": 803,
                "serviceName": "Dynamic Infrastructure and Operations OMVS",
                "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                "serviceURLMarker": "dino",
                "serviceDescription": "Explore and operate an open metadata ecosystem.",
                "serviceWiki": "https://egeria-project.org/services/omvs/dino/overview"
            },
            {
                "serviceId": 801,
                "serviceName": "Repository Explorer OMVS",
                "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                "serviceURLMarker": "rex",
                "serviceDescription": "Explore open metadata instances.",
                "serviceWiki": "https://egeria-project.org/services/omvs/rex/overview"
            },
            {
                "serviceId": 806,
                "serviceName": "Glossary Workflow OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "glossary-workflow",
                "serviceDescription": "Create glossary terms and organize them into categories as part of a controlled workflow process. It supports the editing glossary and multiple states.",
                "serviceWiki": "https://egeria-project.org/services/omvs/glossary-workflow/overview/"
            },
            {
                "serviceId": 807,
                "serviceName": "My Profile OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "my-profile",
                "serviceDescription": "Manage information about the logged on user as well as their preferences.",
                "serviceWiki": "https://egeria-project.org/services/omvs/my-profile/overview/"
            },
            {
                "serviceId": 802,
                "serviceName": "Type Explorer OMVS",
                "serviceDevelopmentStatus": "TECHNICAL_PREVIEW",
                "serviceURLMarker": "tex",
                "serviceDescription": "Explore the open metadata types in a repository or cohort.",
                "serviceWiki": "https://egeria-project.org/services/omvs/tex/overview"
            },
            {
                "serviceId": 804,
                "serviceName": "Server Author OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "server-author",
                "serviceDescription": "Author server configuration.",
                "serviceWiki": "https://egeria-project.org/services/omvs/server-author/overview/"
            },
            {
                "serviceId": 805,
                "serviceName": "Glossary Browser OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "glossary-browser",
                "serviceDescription": "View glossary terms and categories within a glossary.",
                "serviceWiki": "https://egeria-project.org/services/omvs/glossary-browser/overview/"
            },
            {
                "serviceId": 808,
                "serviceName": "Asset Catalog OMVS",
                "serviceDevelopmentStatus": "IN_DEVELOPMENT",
                "serviceURLMarker": "asset-catalog",
                "serviceDescription": "Search and understand your assets.",
                "serviceWiki": "https://egeria-project.org/services/omvs/asset-catalog/overview/"
            }
        ]
    }
    ```
It is also possible to retrieve the full configuration for the view services.  This contains the additional information provided by the platform.

=== "Retrieving a specific view service's configuration"

    !!! get "GET - retrieve a specific view service's configuration"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```
    
        The response will be a `ViewServiceConfigResponse` containing a `ViewServiceConfig` object.

=== "Retrieving all configured view services' configuration"

    !!! get "GET - retrieve current configuration for all configured view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
        ```

    This will return a `ViewServicesResponse` which will contain a list of `ViewServiceConfig` objects.

The structure of the `ViewServiceConfig` object is illustrated below:

![Configuration document contents for a view service](/concepts/view-service-config.svg)

Finally, view service configuration can easily be removed from a server configuration document.

=== "Removing configuration for a single view service"

    A specific view service can be individually cleared with the following command. This will remove the view service's
    configuration from the server.

    !!! delete "DELETE - remove configuration for a specific view service"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```

        The `serviceURLMarker` can be found by [listing the registered view services](#list-configured-view-services).

=== "Removing configuration for all view services"

    All the view services configured on a server can be cleared with the following command:

    !!! delete "DELETE - remove configured view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
        ```
