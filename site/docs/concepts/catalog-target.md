<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Catalog Target

A *catalog target* describes the third party technology ([resource](/concepts/resource)) that a specific [integration connector](/concept/integration-connector) is exchanging metadata with.  

## Catalog Target Types

The developer of an integration connector is able to specify one or more types of technology supported by the connector.  These are called *Catalog Target Types* and they are specified in the implementation of the integration connector's [connector provider](/concepts/connector-provider). Catalog Target Types include the following properties:

* **typeName** - the [open metadata type name](/types) of the element that describes a specific catalog type.
* **deployedImplementationType** - the [deployed implementation type](/concepts/deployed-implementation-type) of the element that describes a specific catalog type.  This allows a more fine-grained specification of the type of technology supported by the integration connector.
* **otherPropertyNames** - as the name suggests, this allows other properties that are useful to a person deploying the connector.

The catalog target type is given a name called the **catalogTargetName**.  Here is a code snippet from the [Data Files Monitor Integration Connector's](/connectors/integration/data-files-monitor-integration-connector) connector provider showing how the catalog target types are set up.  This connector is configured with the name of a directory (folder) on a filesystem and it catalogues the files underneath this folder.  Therefore, the catalog target type describes a directory.

```java

    static public final String CATALOG_TARGET_NAME  = "directoryToMonitor";

    CatalogTargetType catalogTargetType = new CatalogTargetType();

    catalogTargetType.setTypeName(OpenMetadataTypesMapper.DATA_FOLDER_TYPE_NAME);
    catalogTargetType.setDeployedImplementationType(DeployedImplementationType.DATA_FOLDER.getDeployedImplementationType());

    super.catalogTargetTypes.put(CATALOG_TARGET_NAME, catalogTargetType);
```

This information is then available to the person choosing the appropriate integration connector and setting it up to run. 

At runtime, the specific catalog target can be supplied to an integration connector via its [endpoint](/concepts/endpoint) which is connected to its entity's [connection](/concepts/connection), or via one or more *CatalogTarget* relationships. 

## CatalogTarget relationship

The [*CatalogTarget*](/types/4/0464-Dynamic-Integration-Groups) relationship links an integration connector's entity to an entity that describes the specific third party technology that the integration connector should exchange metadata with. It is used when configuring an [integration daemon](/concepts/integration-daemon) using [integration groups](/concepts/integration-group).  With this style of configuration, details of the integration connectors to run are described in the open metadata repositories that the integration daemon is connected to.  The catalog target relationship is part of this open metadata description.

The diagram below shows the open metadata elements describing an integration group.  This integration group has two integration connectors.  Each integration connector is linked to a [connection](/concepts/connection) that describes how to create a running instance of the integration connector.  This connection may optionally include the endpoint information of the third party technology that the integration connector is to exchange metadata with. The *CatalogTarget* relationship provides an alternative way to supply details of one, or more third party technologies that it should connect to.  These technologies are described, typically by an [asset](/concepts/asset) open metadata element (shown in yellow) and are linked to the integration connector's element using the *CatalogTarget* relationship.

![Integration group](/services/omas/governance-engine/integration-group-example)

The [connection](/concepts/connection) information associated with the third party technology can be used by the integration connector to create a [resource connector](/concepts/digital-resource-connector) that acts as a client to call the third party technology.

The diagram below shows an example of a metadata description for an integration connector that catalogs files found in a directory (folder).  The catalog target is the asset that describes the directory where the files are located.  Linked to the asset is a connection for the data folder connector that will provide access to the files in the directory.

![Data file cataloguing integration connector](/services/omas/governance-engine/integration-connector-catalog-target-data-folder-example)

This style of configuration means that the connection to a specific third party technology only needs to be specified once and can be used for multiple purposes.  This is important for technologies that need a complex connection structure that may need to be updated from time to time.  For example, the next diagram shows an integration connector that is linked to a database asset.  This database's connection is complex and includes an embedded secret store connector.  If details of the secrets used to connect to the database need to be changed, it only needs to be changed in one connection.

![Database cataloguing integration connector](/services/omas/governance-engine/integration-connector-catalog-target-database-example)

The *CatalogTarget* relationship is similar to the [*TargetForAction*](/types/4/0463-Engine-Actions) relationships that links [engine actions](/concepts/engine-action) to the elements describing the technology that the associated [governance service](/concepts/governance-service) is to work on.

From the perspective of the database element, these relationships make it possible to see the automated processing (agents) working with the database, as well as the metadata they are gathering/validating/updating.  This is useful for either the owner or the consumer of the resource to know how the technology and its metadata are being maintained.

![Database's agents and information](/services/omas/governance-engine/database-agents-and-information)



--8<-- "snippets/abbr.md"
