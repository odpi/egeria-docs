<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the view services

The [Open Metadata View Services (OMVS's)](/services/view) run in a [view server](/concepts/view-server).

View services provide task-oriented, domain-specific services for user interfaces that integrate with open metadata. View services are part of a multi-tier architecture for the provision of multi-tenant user interfaces. The front tier consists of web components that are rendered in a web browser and served by a web application called the [presentation server :material-dock-window:](https://github.com/odpi/egeria-react-ui){ target=react }. The presentation server in turn delegates requests to a set of _view services_ that form a second tier running in the view server. Each view service exposes a REST API that supports the domain-specific operations relevant to the service and issues queries and commands to other OMAG Servers.

To get a description of each of the registered view services, and each service's `viewServiceURLMarker`, see [list view services](#list-view-services) instructions below.

To activate a specific view service in a view server, it is necessary to add an entry for the view service to the view server's configuration document.

![Configuration document contents for a view service](/concepts/view-service-config.svg)

The descriptive information and operational status are filled out automatically by the administration services based on the `viewServiceURLMarker` value that you supply. The other values are supplied on the configuration call.

There are two types of view services, each with a different type of view service configuration object:

### Solution view services

A *solution view service* supports operations needed by a solution-oriented user interface. These are typically geared toward a specific [Open Metadata Access Service (OMAS)](/services/omas). For example, the Glossary Author view service supports a user interface for creation and management of glossaries using the Subject Area OMAS.

A solution view service is configured using a `SolutionViewServiceConfig` object which has the following properties:

| Property | Use |
|---|---|
| `viewServiceId` | required property, set to a unique numeric identifier |
| `viewServiceAdminClass` | required property, set to the admin class of the view service |
| `viewServiceName` | required property, set to the name of the view service being configured |
| `viewServiceFullName` | required property, set to the full name of view service |
| `viewServiceURLMarker` | required property, set to the serviceURL Marker of the service - this can be discovered by [listing the registered view services](#list-view-services) |
| `viewServiceDescription` | optional property that describes the view service |
| `viewServiceWiki` | optional property specifying the location of the view service documentation |
| `viewServiceOperationalStatus` | required property, set to ENABLED or DISABLED |
| `viewServiceOptions` | optional property that specifies options needed by a specific view service (refer to the documentation for the specific service for details) |
| `omagServerPlatformRootURL` | required property (see below) |
| `omagServerName` | required property (see below) |

A solution view service configuration must include `omagServerPlatformRootURL` and  `omagServerName` properties(defined in `OMAGServerClientConfig`). These properties specify the OMAG Server to which to send downstream REST calls to an OMAG Server that is running the OMAS needed by the view service.

!!! example "Example solution view service configuration"
    Below is an example of a configuration object for a solution view service. In this example, the view service is [Glossary Author View Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/view-services/glossary-author-view){ target=gh }. It would be similar for the other solution view services.
 
    The configuration contains the name and status of the view service and contains the name and rootURL of the OMAG Server to which 'downstream' requests will be sent. In this example the 'downstream' server is the server running the Subject Area OMAS, required by the Glossary Author view service.

    ```
    {
        "class":"SolutionViewServiceConfig",
        "viewServiceAdminClass":"org.odpi.openmetadata.viewservices.glossaryauthor.admin.GlossaryAuthorViewAdmin",
        "viewServiceFullName":"Glossary Author",
        "viewServiceOperationalStatus":"ENABLED",
        "omagserverName":"Subject_Area_Server",
        "omagserverPlatformRootURL":"https://localhost:8083"
    }
    ```

### Integration view services

An *integration view service* supports operations needed by an integration-oriented user interface. Examples 
include the [Repository Explorer View Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/view-services/rex-view){ target=gh }, [Type Explorer View Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/view-services/tex-view){ target=gh } or [Dino View Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/view-services/dino-view){ target=gh } for operational management.

It additionally has the following configuration properties:

| Property | Use |
|---|---|
| `viewServiceId` | required property, set to a unique numeric identifier |
| `viewServiceAdminClass` | required property, set to the admin class of the view service |
| `viewServiceName` | required property, set to the name of the view service being configured |
| `viewServiceFullName` | required property, set to the full name of view service |
| `viewServiceURLMarker` | required property, set to the serviceURL marker of the service - this can be discovered by [listing the registered view services](#list-view-services) |
| `viewServiceDescription` | optional property that describes the view service |
| `viewServiceWiki` | optional property specifying the location of the view service documentation |
| `viewServiceOperationalStatus` | required property, set to ENABLED or DISABLED |
| `viewServiceOptions` | optional property that specifies options needed by a specific view service (refer to the documentation for the specific service for details) |
| `resourceEndpoints` | required property that lists the platform and server endpoints of the OMAG Platforms or Servers to which to send downstream REST calls, for example to query metadata repositories (see below) |

An integration view service configuration does not need the `omagServerPlatformRootURL` and  `omagServerName` properties that are required for a solution view service configuration. This is because an integration view service will generally need to perform operations routed to a variety of open metadata servers, selected by the user at runtime. The set of platforms and servers that the user can select are configured by the `resourceEndpoints` configuration property.

The `resourceEndpoints` property is a list of `ResourceEndpointConfig` objects, which each have the following properties:

| Property | Use |
|---|---|
| `resourceCategory` | required property, set to either "Platform" or "Server" |
| `platformName` | required property, a unique name given to a "Platform" resource, or a reference to a named "Platform" resource endpoint from a "Server" resource |
| `serverName` | required property for a "Server" resource, set to the name of the OMAG Server. Not used for a "Platform" resource. |
| `serverInstanceName` | required property for a "Server" resource, a unique name for the combination of server and platform. | 
| `description` | optional property that is displayed by some integration view services |

In an Egeria deployment, a server may be deployed to multiple platforms; this is typically used for clustering. A "Server" `ResourceEndpointConfig` must possess a `serverInstanceName` property which contains a unique name that refers to the specific instance of the server identified by the `serverName` property hosted by the platform identified by the `platformName` property. For example, you could configure a pair of server resource endpoints called `Server1@PlatformA` and `Server1@PlatformB`: both are `Server1`, but hosted on different platforms (`PlatformA` and `PlatformB`). The `serverInstanceName` is used to display the resource in the user interface selector lists.

!!! example "Example integration view service configuration"
    Below is an example of a configuration object for an Integration View Service. In this example, the view service is [Dino View Service :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/view-services/dino-view){ target=gh }. It would be similar for the other integration view services.
 
    The configuration contains the name and status of the view service and contains a list of the resources that will appear in the platform and server selectors in the user interface. All requests to the view service REST API are based on these configured named resources. When a user selects a platform name or server name from the selector lists, the interface sends the resource name to the view service, which resolves the platform or server name to a resource endpoint to identify the URL needed to send a request to the platform or server.

    In the example configuration, the list of `ResourceEndpointConfig` objects represents two platforms and two servers. Every `ResourceEndpointConfig` has a `resourceCategory`, set to either `"Platform"` or `"Server"`. Each platform `ResourceEndpointConfig` has a unique `platformName` and `platformRootURL` and an optional `description` property. Each server `ResourceEndpointConfig` has a `serverInstanceName`, `serverName` and the `platformName` of one of the configured platform resource endpoints. Each server also has an optional `description` property.

    You would need to replace the `<hostname>` and `<port>` variables with your own values:

    ```json
    {
        "class":"IntegrationViewServiceConfig",
        "viewServiceAdminClass":"org.odpi.openmetadata.viewservices.rex.admin.RexViewAdmin",
        "viewServiceFullName":"RepositoryExplorer",
        "viewServiceOperationalStatus":"ENABLED",
        "resourceEndpoints" : [
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Platform",
                "platformName"       : "Platform1",
                "platformRootURL"    : "https://<hostname>:<port>",
                "description"        : "This platform is running in the development cloud"
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Platform",
                "platformName"       : "Platform2",
                "platformRootURL"    : "https://<hostname>:<port>",
                "description"        : "This platform is running in the departmental test cluster"               
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "serverInstanceName" : "Central Metadata Server",
                "serverName"         : "Metadata_Server1",
                "platformName"       : "Platform1",
                "description"        : "Metadata server with home reopsitory for schema artefacts"
            },
            {
                "class"              : "ResourceEndpointConfig",
                "resourceCategory"   : "Server",
                "serverInstanceName" : "Supplementary Metadata Server",
                "serverName"         : "Metadata_Server2",
                "platformName"       : "Platform2",
                "description"        : "Metadata server with home repository for review artefacts"
            }
        ]
    }
    ```

### Administrative operations

#### List view services

It is possible to list the registered view services for an [OMAG Server Platform](/concepts/omag-server-platform) using the following command:

!!! get "GET - list view services"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{adminUserId}}/server-platform/registered-services/view-services
    ```

??? success "Response from listing view services"
    ```json
    {
        "class": "RegisteredOMAGServicesResponse",
        "relatedHTTPCode": 200,
        "services": [
            {
                "serviceName": "Glossary Author",
                "serviceURLMarker": "glossary-author",
                "serviceDescription": "View Service for glossary authoring.",
                "serviceWiki": "https://egeria-project.org/services/omvs/glossary-author/overview/"
            },
            {
                "serviceName": "Repository Explorer",
                "serviceURLMarker": "rex",
                "serviceDescription": "Explore open metadata instances.",
                "serviceWiki": "https://egeria-project.org/services/omvs/rex/overview/"
            },
            {
                "serviceName": "Type Explorer",
                "serviceURLMarker": "tex",
                "serviceDescription": "Explore the open metadata types.",
                "serviceWiki": "https://egeria-project.org/services/omvs/tex/overview/"
            },
            {
                "serviceName": "Dino",
                "serviceURLMarker": "dino",
                "serviceDescription": "Operate an open metadata topology.",
                "serviceWiki": "https://egeria-project.org/services/omvs/dino/overview/"
            }
        ]
    }
    ```

These view services are available to configure either together or individually.

This operation is a good way to discover the `serviceURLMarker` property for each view service, which is needed for various operations described below.

#### List configured view services

It is possible to list the configured view services for an [OMAG Server](/concepts/omag-server) using the following command:

!!! get "GET - list configured view services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/configuration
    ```

??? success "Response from listing configured view services"
    The response will be a `RegisteredOMAGServicesResponse` which contains a list of `RegisteredOMAGService` objects, that will look something like the following:

    ```json
    {
        "class": "RegisteredOMAGServicesResponse",
        "relatedHTTPCode": 200,
        "services": [
            {
                "serviceName": "Glossary Author",
                "serviceURLMarker": "glossary-author",
                "serviceDescription": "View Service for glossary authoring.",
                "serviceWiki": "https://egeria-project.org/services/omvs/glossary-author/overview/"
            },
            {
                "serviceName": "Repository Explorer",
                "serviceURLMarker": "rex",
                "serviceDescription": "Explore open metadata instances.",
                "serviceWiki": "https://egeria-project.org/services/omvs/rex/overview/"
            },
            {
                "serviceName": "Type Explorer",
                "serviceURLMarker": "tex",
                "serviceDescription": "Explore the open metadata types.",
                "serviceWiki": "https://egeria-project.org/services/omvs/tex/overview/"
            }
        ]
    }
    ```

These view services are available to configure either together or individually.

#### Retrieve view service configuration

=== "individually"

    Retrieve a specific view service's configuration:

    !!! get "GET - retrieve a specific view service's configuration"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```
    
        The response will be a `ViewServiceConfigResponse` containing a `ViewServiceConfig` object.

=== "multiple"

    It is also possible to retrieve the current configuration for all configured view services:

    !!! get "GET - retrieve current configuration for all configured view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
        ```

    This will return a `ViewServicesResponse` which will contain a list of `ViewServiceConfig` objects.

#### Configure view services

=== "individually"

    A specific view service can be individually configured with the following command:

    !!! post "POST - configure a specific view service"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```

        The request body must contain a `ViewServiceConfig` object, while the `serviceURLMarker` can
        be found by [listing the configured view services](#list-configured-view-services).

=== "multiple"

    It is also possible to configurate a set of view services at the same time, using the following command:

    !!! post "POST - configure multiple view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/configuration
        ```

        The request body must contain a list of `ViewServiceConfig` objects.

#### Remove view services

=== "individually"

    A specific view service can be individually cleared with the following command. This will remove the view service's
    configuration from the server.

    !!! delete "DELETE - remove configuration for a specific view service"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services/{{serviceURLMarker}}
        ```

        The `serviceURLMarker` can be found by [listing the configured view services](#list-configured-view-services).

=== "multiple"

    All the view services configured on a server can be cleared with the following command:

    !!! delete "DELETE - remove configured view services"
        ```
        {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/view-services
        ```
