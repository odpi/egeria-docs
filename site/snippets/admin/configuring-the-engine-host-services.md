<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the engine host services

The [engine host services](/services/engine-host-services) provide the base implementation of the [engine host](/concepts/engine-host) OMAG Server.

There are two parts to configuring the engine host services:

### Specify location of governance engine definitions

The location of the [metadata access server](/concepts/metadata-access-server) running the [Governance Server OMAS](/services/omas/governance-server/overview) that will supply the definitions of the governance engines, is configured using two properties:

- the [server url root](/concepts/platform-url-root) of the metadata access server's OMAG Server Platform, and
- the [name of the metadata access server](/concepts/server-name).

!!! post "POST - specify location of governance engine definitions"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{engineHostServerName}}/engine-definitions/client-config
    ```

    With a request body like the following:

    ```json
    {
        "class": "OMAGServerClientConfig",
        "omagserverPlatformRootURL": {{MDServerURLRoot}},
        "omagserverName" : "{{MDServerName}}"
    }
    ```

### Configure the engines services

The [engine services](/services/omes) (or Open Metadata Engine Services (OMES) to give them their full name) also run in the engine host.  Each engine service provides support for a particular type of governance engine which is in turn, a collection of governance services.
The governance engine is described in a [Governance Engine Definition](/concepts/governance-engine-definition)

#### List engine services

It is possible to get a description of each of the registered engine services using the following command:

!!! get "GET - list engine services"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/engine-services
    ```

Note the `engineServiceURLMarker` for the engine service that you want to configure.

#### Configure engine service

![Configuration document contents for an integration service](/concepts/engine-service-config.svg)

The descriptive information and operational status are filled out automatically by the administration services based on the `engineServiceURLMarker` value that you supply. The other values are supplied on the configuration call.

Each engine service is configured with the network location of the [Metadata Access Server](/concepts/metadata-access-server) running the appropriate partner service. There are a set of options that the engine service supports along with the list of configuration properties for the governance engines that will be run in the engine service. The governance engine's configuration properties identify which governance engine to run. The governance engine's definition, including the services it supports are retrieved from the metadata access server when the engine service starts up.

!!! post "POST - configure engine service"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/engine-services/{{engineServiceURLMarker}}
    ```

    With a request body like the following:

    ```json
    {
        "class": "EngineServiceRequestBody",
        "omagserverPlatformRootURL": {{MDServerURLRoot}},
        "omagserverName" : "{{MDServerName}}",
        [ {
             "class": "EngineConfig",
             "engineQualifiedName" : " ... "             
             "engineUserId" : " ... "
        } ]
    }
    ```

    Where:

    - `engineQualifiedName` - set up the qualified name of the GovernanceEngine entity stored in the metadata servers.
    - `engineUserId` - set up the user id for the engine: if this is null, the engine host's userId is used on requests to the Open Metadata Access Service (OMAS).

### Remove engine host services

The following command removes the configuration for the engine host services from an OMAG Server's configuration document. This may be used if the engine host services have been added in error.

!!! delete "DELETE - remove engine host services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{engineHostServerName}}/engine-host-services
    ```


