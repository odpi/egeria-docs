---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/released.md"

# Platform Operation Services

The platform operation services provide the APIs for querying the [OMAG Server Platform](/concepts/omag-server-platform) and discovering information about the [OMAG Servers](/concepts/omag-server) that it is hosting.   Its client is called `PlatformServicesClient`and it is located in the `platform-services-client` module.

--8<-- "docs/guides/developer/java-clients/platform-constructor-parameters.md"

Below is an example of the code used to construct the `PlatformServicesClient`.

??? example "Example: Creating a platform services client"
    ```java linenums="1"
    PlatformServicesClient platformServicesClient = new PlatformServicesClient("MyPlatform", platformURLRoot);
    ```

## Platform origin

Once the client is created, use it to call the API it offers which is documented using [Javadoc](https://odpi.github.io/egeria/org/odpi/openmetadata/platformservices/client/PlatformServicesClient.html). For example, the code below queries the platform origin. This indicates the release of Egeria that is running in the platform.

??? example "Example: Retrieving the platform origin"
    ```java linenums="1"
    String platformOrigin = platformServicesClient.getPlatformOrigin(clientUserId);
    ```

## Registered services

It is also possible to list the [registered services](/services/#registered-services) that are available in the platform.

??? example "Example: Retrieving the registered services"
    ```java linenums="1"
    List<RegisteredOMAGService> registeredOMASs = platformServicesClient.getAccessServices(clientUserId);
    List<RegisteredOMAGService> registeredOMESs = platformServicesClient.getEngineServices(clientUserId);
    List<RegisteredOMAGService> registeredOMISs = platformServicesClient.getIntegrationServices(clientUserId);
    List<RegisteredOMAGService> registeredOMVSs = platformServicesClient.getViewServices(clientUserId);
    ```

## Known servers

The *known servers* are those servers that have run on the platform since it started.  The `getKnownServers` method returns a list of server names which is useful for stepping through each of the servers in a `for` loop.

??? example "Example: Retrieving the list of known servers"
    ```java linenums="1"
    List<String> serverList = platformServicesClient.getKnownServers(clientUserId);

    if (serverList != null)
    {
        for (String serverName : serverList)
        {
            if (serverName != null)
            {
               /*
                * Add code here
                */
           }
        }
    }

    ```

## Active servers

The *active servers* are those servers running on the platform. The `getActiveServers` returns a list of names of the servers running when the request was made.

??? example "Example: Retrieving the list of active servers"
    ```java linenums="1"
    List<String> serverList = platformServicesClient.getActiveServers(clientUserId);

    if (serverList != null)
    {
        for (String serverName : serverList)
        {
            if (serverName != null)
            {
                /*
                 * Add code here
                 */
            }
        }
    }

    ```

Once you have the `serverName`, you can query the status of an OMAG Server running on the platform:

??? example "Example: Retrieving a server's status"
    ```java linenums="1"
    ServerStatus platformServerStatus = platformServicesClient.getServerStatus(clientUserId, serverName);
    ```
The `platformServerStatus` returned includes:

- `serverName` - Name of the server.
- `isActive` - Boolean flag indicating whether it is active (running) on the server.
- `serverStartTime` - The most recent date/time that the server started.
- `serverEndTime` - The most recent date/time that the server stopped.
- `serverHistory` - The list of start and stop times for the previous restarts of the server.

This helps to ascertain when the server was available.



--8<-- "snippets/abbr.md"
