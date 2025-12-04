<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Integration Group

An *integration group* describes a collection of [integration connectors](/concepts/integration-connector) that are to run together in one or more [integration daemons](/concepts/integration-daemon).  

## Specification

Each integration connector is represented by an entity of type [*IntegrationConnector*](/types/4/0464-Dynamic-Integration-Groups) linked to a [*Connection*](/types/2/0201-Connectors-and-Connections) via the [*ConnectionToAsset*](/types/2/0205-Connection-Linkage) relationship.  This [connection](/concepts/connection) is used to instantiate the integration connector.  It is also passed to the integration connector as it initializes, so it is used to pass configuration properties that describes its desired behaviour.   The connection's optional endpoint describes the [catalog target](/concepts/catalog-target).  Alternatively, the integration connector's catalog target(s) can be supplied via the [*CatalogTarget*](/types/4/0464-Dynamic-Integration-Groups) relationship.  

![integration group structure](/services/omvs/asset-maker/integration-group-example.svg)

## Examples of integration connector definitions

The exact specification of an integration connector depends on how the integration connector is implemented.  Details of the integration connectors supplied with Egeria, and how to configure them are available in the [connector catalog](/connectors/#integration-connectors).

Some integration connectors use a simple connection structure. The [*ConnectorType*](/concepts/connector-type) linked to the connection identifies the implementation of the integration connector.  The endpoint describes how to connect to the third party technology.

![integration connector with a simple connection](/services/omvs/asset-maker/integration-connector-simple.svg)

Some connectors need a virtual connection with embedded connectors that describe different resources.

![Integration connector with a virtual connection](/services/omvs/asset-maker/integration-connector-virtual-connection.svg)

For example, this integration connector has a virtual connection with an embedded secrets store for managing passwords ans certificates.

![Example of integration connector with a virtual connection](/services/omvs/asset-maker/integration-connector-virtual-connection-example.svg)

Alternatively, using [catalog targets](/concepts/catalog-target) provides a more efficient way to supply information about the technology that the integration connector is to work with.

The connection for the integration connector just needs the connector type to describe its implementation.
The *CatalogTarget* relationship links to an asset that describes the technology that the integration connector is to work with.

![Example of integration connector with a virtual connection](/services/omvs/asset-maker/integration-connector-catalog-target.svg)

The integration connector can have multiple catalog log targets that can change over time.

## Configuring integration groups

An [integration daemon is configured](/guides/admin/servers/by-server-type/configuring-an-integration-daemon) with a list of qualified names for various integration groups.  It retrieves the list of integration connectors in each of these groups from the open metadata ecosystem and starts to run them.  It continues to monitor for changes to the integration groups and their linked integration connectors, changing the connectors it is running as needed.  

![integration group operation](/services/omvs/asset-maker/integration-group-use.svg)

???+ education "Further information"

    Each integration group has a unique name.  An *IntegrationGroup* entity with a qualifiedName set to this unique name is created through the [Asset Maker](/services/omvs/asset-maker/overview) API.  This API is also used to create and link the integration connector definitions into the integration group.

    The [integration group's qualifiedName is configured](/guides/admin/servers/by-section/integration-daemon-services-section) in the [integration daemon](/concepts/integration-daemon).

    The open metadata types for this definition are in model [0464 - Dynamic Integration Groups](/types/4/0464-Dynamic-Integration-Groups) - specifically notice that *IntegrationGroup* and *IntegrationConnector* are linked by the *RegisteredIntegrationConnector* relationship.


--8<-- "snippets/abbr.md"