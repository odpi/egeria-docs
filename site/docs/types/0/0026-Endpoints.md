<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0026 Endpoints

![UML](0026-Endpoints.svg)

## Endpoint

*`Endpoint`s* capture the network information needed to connect to a service. There is a wide variety of approaches to identifying the endpoint and so its properties will depend on how it is being used.

Endpoints are part of a [Connection](/types/2/0201-Connectors-and-Connections). The connection provides the information to create an instance of a connector that is accessing a remote asset. In this situation the *networkAddress* attribute is set up to the URL needed to connect to the specific asset.

## ITInfrastructure entity

*ITInfrastructure* entity is a type of [Asset](/types/0/0010-Base-Model) that supports the running of software systems.  It includes the *userId* attribute to indicate the user that the software runs with.  This userId can help identify the source of digital resources.

> Note: ITInfrastructure entities that represent systems that are connected to the Open Metadata ecosystem should link to an [ITProfile](/types/1/0117-IT-Profiles) and [UserIdentity](/types/1/0110-Actors) entities to describe the software's userId.

## ServerEndpoint

Endpoints can also be linked to infrastructure elements using the *ServerEndpoint* relationship to document their network address(s). These are often the values needed in the connection objects configured for [integration connectors](/connectors/integration-connector) running in an [integration daemon](/concepts/integration-daemon) and so the endpoint can be looked up either as the integration connector is being configured, or dynamically when the integration connector is running.

!!! example "Endpoint examples"
    The following picture illustrates the different uses of *Endpoint* entities. The top of the diagram shows the endpoint as part of a connection object used to create a connector to the real resource described by the *Asset* entities shown in green.

    In the middle is an *Endpoint* entity tied to a [SoftwareServerPlatform](/types/0/0037-Software-Server-Platforms) that is hosting assets. This endpoint can be queried when configuring integration connectors that are to connect to the platform and catalog the resources (assets) it is hosting.

    Finally, the [VisibleEndpoint](/types/0/0070-Networks-and-Gateways) and [NetworkEndpoint](/types/0/0070-Networks-and-Gateways) relationships shown at the bottom of the diagram help to document the visibility of an endpoint to a particular network and the host behind it.

    ![Endpoint examples](0026-Endpoints-Illustration.svg)

--8<-- "snippets/abbr.md"
