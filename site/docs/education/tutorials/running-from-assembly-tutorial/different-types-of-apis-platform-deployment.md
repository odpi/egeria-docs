<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Types of APIs and Platform Deployment

Once your [OMAG Server Platform](/concepts/omag-server-platform) is running, you can query it to find out how it is deployed and which services it offers.  This uses the [Platform Services](/services/platform-services/overview), which are one of the platform APIs.  Egeria's APIs fall into two groups:

* **Platform APIs** - configure and operate the platform and the [OMAG Servers](/concepts/omag-server) it hosts.  Their REST paths begin `{{platformURLRoot}}/open-metadata/platform-services/...` or `{{platformURLRoot}}/open-metadata/admin-services/...`.
* **Server APIs** - offered by the [registered services](/services) running inside a server.  For example, the [view services](/services/omvs) in a [view server](/concepts/view-server) have REST paths that begin `{{platformURLRoot}}/servers/{{viewServer}}/api/open-metadata/{{serviceURLMarker}}/...`.

The requests below are in the `Egeria-platform-services.http` collection, which is in the assembly's `opt/http-client-collections` directory.  Every request except the first needs a bearer token in its `Authorization` header - see [REST APIs](/guides/developer/rest-apis) for how to obtain one.

??? beginner "Check the platform is running"
    The platform origin is the simplest request, and needs no token:

    ```
    GET {{platformURLRoot}}/open-metadata/platform-services/server-platform/origin
    ```

    It returns the name and version of the platform:

    ```text
    Egeria OMAG Server Platform (version 6.3-SNAPSHOT)
    ```

    The equivalent Java call uses the `PlatformServicesClient`:

    ```java linenums="1"
    PlatformServicesClient platformServicesClient = new PlatformServicesClient("MyPlatform",
                                                                               platformURLRoot,
                                                                               secretStoreProvider,
                                                                               secretStoreLocation,
                                                                               secretStoreCollection,
                                                                               delegatingUserId,
                                                                               auditLog);

    String platformOrigin = platformServicesClient.getPlatformOrigin();
    ```

??? beginner "List the registered services"
    *Registered services* are optional services that are plugged into the platform and provide the services to retrieve, maintain and govern open metadata.  They are listed by type:

    ```
    GET {{platformURLRoot}}/open-metadata/platform-services/server-platform/registered-services/access-services
    GET {{platformURLRoot}}/open-metadata/platform-services/server-platform/registered-services/engine-services
    GET {{platformURLRoot}}/open-metadata/platform-services/server-platform/registered-services/view-services
    ```

    The default platform has three access services, which run in a [metadata access server](/concepts/metadata-access-server):

    | Service                            | Description                                                                                                                          |
    |------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
    | Connected Asset Services           | Common metadata services for the Open Connector Framework (OCF).                                                                     |
    | Open Metadata Store Services       | Provides generic open metadata retrieval and management services for the Open Frameworks and Open Metadata Access Services (OMASs). |
    | Open Governance Framework Services | Support open governance services.                                                                                                    |

    It has four engine services, which run in an [engine host](/concepts/engine-host):

    | Service                    | Description                                                                                                                                                   |
    |----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Governance Action OMES     | Executes requested governance action services to monitor, assess and maintain metadata and its real-world counterparts.                                       |
    | Repository Governance OMES | Dynamically govern open metadata repositories in the connected cohorts.                                                                                       |
    | Survey Action OMES         | Analyses the content of an asset's real world counterpart (resource), generates annotations in a survey report that is attached to the asset in the open metadata repositories. |
    | Watchdog Action OMES       | Monitors for particular situations/events and notifies registered subscribers.                                                                                |

    It also has around forty view services, which run in a view server and provide the APIs used by the [Python clients](/guides/developer/python-clients/overview) and user interfaces.  Each entry in the response describes one service.  For example:

    ```json
    {
        "serviceId": 233,
        "serviceName": "Community Matters API",
        "serviceDevelopmentStatus": "STABLE",
        "serviceURLMarker": "community-matters",
        "serviceDescription": "Manages the definitions of communities, their leaders and membership.",
        "serviceWiki": "https://egeria-project.org/services/omvs/community-matters/overview/",
        "serverType": "View Server",
        "partnerServiceName": "Open Metadata Store Services",
        "partnerServerType": "Metadata Access Server"
    }
    ```

    The `partnerServiceName` shows which access service the view service calls to retrieve and maintain metadata.

    In Java, the same lists come from `getAccessServices()`, `getEngineServices()` and `getViewServices()` on the `PlatformServicesClient`.

??? beginner "List the servers on the platform"
    The platform can also list the servers that are running on it:

    ```
    GET {{platformURLRoot}}/open-metadata/platform-services/server-platform/servers/active
    ```

    On a newly installed platform with no servers configured, the list is empty.  Once servers are configured and started, they appear in the list.  For example, the quickstart environment returns:

    ```json
    {
        "class": "ServerListResponse",
        "relatedHTTPCode": 200,
        "serverList": ["qs-engine-host", "qs-integration-daemon", "qs-metadata-store", "qs-view-server", "qs-nanny-daemon"]
    }
    ```

    `GET .../servers` lists every server that has run on the platform since it started, and `GET .../servers/{serverName}/status` returns the start and stop history of a server.

!!! tip "Reports on platforms and servers"
    Once a view server is running, the [Runtime Manager](/services/omvs/runtime-manager/overview) view service can produce a report on a platform (`GET .../runtime-manager/platforms/{platformGUID}/report`) or a running server (`GET .../runtime-manager/omag-servers/{serverGUID}/instance/report`) that combines these details.


--8<-- "snippets/abbr.md"
