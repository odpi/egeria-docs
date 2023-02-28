<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0464 Integration Groups

The types in this model are used to create [integration group](/concepts/integration-group) definitions.

![UML](0464-Dynamic-Integration-Groups.svg)

## IntegrationGroup entity

An [integration group](/concepts/integration-group) is a [software capability](/types/0/0042-Software-Capabilities) that is able to run specific [integration connectors](/concepts/integration-connector) on demand.

## RegisteredIntegrationConnector relationship

The integration connectors to run in an *integration group* are specified via the *RegisteredIntegrationConnector* relationships.

## IntegrationConnector entity

*[Integration connectors](/concepts/integration-connector)* are specialist [connectors](/concepts/connector).  They are represented in open metadata using the *IntegrationConnector* entity which is a specialization of *[DeployedConnector](/types/2/0215-Software-Components)*.  This entity is linked to a *[Connection](/types/2/0201-Connectors-and-Connections)* entity via a *[ConnectionToAsset](/types/2/0205-Connection-Linkage)* relationship.

An integration connector can be linked to multiple integration groups via the *RegisteredIntegrationConnector* relationship.  It can only be linked to a specific integration group once.  If multiple instances of the same integration connector implementation is to be specified in a group. each one is represented by an *IntegrationConnector* entity linked to its own *Connection* entity that describes its required behaviour.

## CatalogTarget

The *CatalogTarget* relationship links an *IntegrationConnector* entity to another entity that the integration connector is to update.  For example, if an integration connector is configured to catalog a database and its [*Database*](/types/2/0224-Databases) entity is already created, the *CatalogTarget* would link the *IntegrationConnector* entity with the *Database* entity.  This prevents the integration connector from recreating the Database entity when it runs.

--8<-- "snippets/abbr.md"