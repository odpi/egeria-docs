<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configure the engine host services

The engine host services provide the base implementation of the [engine host](/egeria-docs/concepts/engine-host) OMAG Server.

There are two parts to configuring the engine host services:

### Specify location of governance engine

The location of the [metadata access store](/egeria-docs/concepts/metadata-access-store) (or [metadata access point](/egeria-docs/concepts/metadata-access-point)) running the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine), which will supply the definitions of the governance engines that will run in the engine services, is configured using two properties:

- the [server url root](/egeria-docs/concepts/omag-server/#platform-url-root) of the metadata server's OMAG Server Platform, and
- the [name of the metadata server](/egeria-docs/concepts/omag-server/#server-name).

!!! post "POST - specify location of governance engine"
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

The [engine services](/egeria-docs/services/omes) (or Open Metadata Engine Services (OMES) to give them their full name) also run in the engine host.

Each engine service provides support for a particular type of governance engine:

- [Open Discovery Engines](/egeria-docs/frameworks/odf/overview)
- [Governance Action Engines](/egeria-docs/frameworks/gaf/overivew)

Each engine service hosts one or more governance engines. A governance engine is a collection of governance services of a specific type:

- [Asset analysis](/egeria-docs/services/omes/asset-analysis/overview) hosts [open discovery services](/egeria-docs/concepts/open-discovery-service) that analyze the content of an asset's real world counterpart, generates [annotations](/egeria-docs/frameworks/odf/discovery-annotation) in an [open discovery analysis report](/egeria-docs/frameworks/odf/discovery-analysis-report) that is attached to the asset in the open metadata repositories.
- [Governance action](/egeria-docs/services/omes/governance-action/overview) hosts [governance action services](/egeria-docs//governance-action-service) that monitor changes in the metadata and initiate updates and other actions as a result.

#### List engine services

It is possible to get a description of each of the registered engine services using the following command:

!!! get "GET - list engine services"
    ```
    {{platformURLRoot}}/open-metadata/platform-services/users/{{userId}}/server-platform/registered-services/engine-services
    ```

Note the `engineServiceURLMarker` for the engine service that you want to configure.

#### Configure engine service

![Configuration document contents for an integration service](engine-service-config.svg)

The descriptive information and operational status are filled out automatically by the administration services based on the `engineServiceURLMarker` value that you supply. The other values are supplied on the configuration call.

Each engine service is configured with the network location of the [metadata access point](/egeria-docs/concepts/metadata-access-point) / [metadata access store](/egeria-docs/concepts/metadata-access-store) running the appropriate [OMAS](/egeria-docs/services/omas). There are a set of options that the engine service supports along with the list of configuration properties for the governance engines that will be run in the engine service. The governance engine's configuration properties identify which governance engine to
run. The governance engine's definition, including the services it supports are retrieved from the metadata access point / metadata server when the engine service starts up.

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

    - `engineQualifiedName` - set up the qualified name of the governance engine stored in the metadata servers.
    - `connectorUserId` - set up the user id for the engine: if this is null, the engine host's userId is used on requests to the Open Metadata Access Service (OMAS).

#### Further Information

The definition of the governance services that are supported by these governance engines are retrieved from the open metadata server when the engine host server starts up.

Maintaining these definitions is described:

- For discovery engines and services see [Discovery Engine OMAS](/egeria-docs/services/omas/discovery-engine/overview)
- For governance action engines and services see [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview)

### Remove engine host services

The following command removes the configuration for the engine host services from an OMAG Server's configuration document. This may be used if the engine host services have been added in error.

!!! delete "DELETE - remove engine host services"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{engineHostServerName}}/engine-host-services
    ```

--8<-- "snippets/abbr.md"
