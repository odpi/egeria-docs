<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Open Connector Framework (OCF)

The *open connector framework* (OCF), as the name suggests, is an open framework for supporting [connectors](#connector). Connector provide client-side access to remote digital resources such as data sets, APIs and software components. OCF connectors also provide access to metadata about the resource ([assets](/concepts/asset)) and may call the [Audit Log Framework](/frameworks/alf/overview) to log audit messages.

## Benefits

Applications and tools benefit from using OCF connectors because:

- Network and security parameters for accessing the data resources are managed in the metadata repository as part of a named connection. The application need only supply the identifier of the connection and provided they have the appropriate security credentials then a connector is returned to them for use.
    - There is no need to hard-code user ids and passwords in the application code - nor manage key stores for this sensitive information since the metadata repository handles this.
    - If the location of the data changes, then the named connection configuration is changed in the metadata repository and the application will be connected to the new location the next time they request a connector.
- The OCF connector provides two sets of APIs. The first set provides access to the resource contents and the second set provides access to the properties of the resource stored in the open metadata repositories. This provides applications and tools with a simple mechanism to make use of metadata as they process the resource. It is particularly useful for data science tools where these properties can help guide the end user in the use of the resource.
- OCF connectors are not limited to representing resources as they are physically implemented. An OCF connector can represent a simplified logical (virtual) data resource that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources.

Organizations benefit from advocating the use of OCF connectors for their systems because the OCF connectors provide a consistent approach to resource access and audit logging. This is particularly important in data-rich environments where individuals are able to combine data from different resources creating new, potentially sensitive insight. The common approach to auditing, and the linkage between the data accessed and the metadata that describes its characteristics help to detect and prevent such actions.

## Design rationale

The following factors influenced the design of the OCF.

- There are many existing connectors and connector frameworks in the industry today. It is important that these existing connectors can be incorporated into the OCF. Thus, the OCF includes placeholders for adapters to external connector providers and connectors.
- Application developers will only adopt a connector framework if it is easy to use. Thus, the connector interfaces allow for the use of native data APIs to minimize the effort an application developer has to take in order to use the OCF connectors.
- Access to the all properties known about an asset should be available to the consumers of the corresponding resource.  Therefore, the OCF provides a standard interface for accessing these properties. Different providers of these properties can plug into the OCF. Egeria provides an implementation of this interface to supply asset properties stored in open metadata repositories in the [OCF metadata management common service](/services/common/ocf-metadata-management).

## Terminology

There are a number of key components within the OCF:

### Connector

A *connector* is a Java client object that provides applications with access to a data source or service (known as an resource) along with its related metadata.

An OCF connector provides four APIs:

| API | Description |
|---|---|
| Connector lifecycle | Manages the lifecycle state of the connector and includes `initialize()`, `start()` and `disconnect()`. |
| Metadata store initialization | If the connector is created by a metadata service then it adds a client to the metadata server called [`ConnectedAssetProperties`](connected-asset-properties.md) to the connector between `initialize()` and `start()`. The `ConnectedAssetProperties` client can be retrieved from the connector instance and used to retrieve metadata about the asset that is stored in the metadata server. |
| Specific initialization for the type of connector | Some types of connectors need additional initialization. These methods are called by the component creating the connector before the `start()` method is called. |
| Asset content | This API is crafted to provide the most natural interface to the asset's contents. Therefore, the asset content API is typically different for each type of connector. |

OCF connectors are not limited to representing assets as they are physically implemented. An OCF connector can represent a simplified logical (virtual) asset, such as a data set, that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources. It is called a *virtual connector*.

!!! education "Further information"
    See the [developer guide](/guides/developer/guide) for information on writing connectors.

### Connection

The *connection* provides the set of properties needed to create and initialize an instance of a [connector](#connector).

A connection contains properties about the specific use of the connector, such as user Id and password, or parameters that control the scope or resources that should be made available to the connector.

It links to an optional:

- [Connector type](#connector-type) that describes the type of the connector that needs to be created in order to access the asset.
- [Endpoint](#endpoint) that describes the server endpoint where the asset is accessed from.

Connector types and endpoints can be reused in multiple connections.

![Connection structure](connection.png)

Connections are typically managed in a metadata repository, but they can also be manually populated.

#### Connection implementations

The OCF offers two implementations of the connection:

- [`Connection` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/beans/Connection.java){ target=gh } is a bean implementation of the connection used in REST API requests and events. It allows properties to be set up and retrieved.
- [`ConnectionProperties` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/properties/ConnectionProperties.java){ target=gh } is a read-only wrapper for the connection properties that is used in client interfaces that do not allow the properties to be updated.

#### Connection properties

The properties for a connection are defined in [model 0201](/types/2/0201-connectors-and-connections) and include:

| Property | Description |
|---|---|
| `guid` | GUID for the connection. |
| `url` | URL of the connection definition in the metadata repository. |
| `qualifiedName` | The official (unique) name for the connection. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. (Sourced from the `qualifiedName` attribute in `Referenceable` - [model 0010](/types/0/0010-Base-Model))
| `displayName` | A consumable name for the connection. Often a shortened form of the qualifiedName for use on user interfaces and messages. The displayName should be only be used for audit logs and error messages if the qualifiedName is not set. |
| `type` | Information about the TypeDef for the connection. |
| `description` | A full description of the connection covering details of the assets it connects to along with usage and version information. |
| `additionalProperties` | Any additional properties associated with the connection. |
| `configurationProperties` | Properties for configuring the connector. |
| `securedProperties` | Protected properties for secure log on by connector to back end server. These are protected properties that can only be retrieved by privileged connector code. |
| `userId` | Name or URI of connecting user. |
| `encryptedPassword` | Password for the userId - needs decrypting by connector before use. |
| `clearPassword` | Password for userId - ready to use. |
| [`connectorType`](#connector-type) | Properties that describe the connector type for the connector. |
| [`endpoint`](#endpoint) | Properties that describe the server endpoint where the connector will retrieve the assets. |

#### Using Connections from open metadata repositories

Each connection stored in a metadata repository has a unique identifier. An application can request a connector instance through selected Egeria OMAS interfaces, such as the [Asset Consumer OMAS](/services/omas/asset-consumer), with just the unique identifier or name of a connection.

The OMAS retrieves the connection object from the open metadata repositories and passes it to the [connector broker](#connector-broker) factory object. The connector broker (and underlying [connector provider](#connector-provider)) uses the information from the connection object to create an instance of the connector.

The advantage of retrieving the connection information from a metadata repository is that the connection properties do not need to be hard-coded in the consuming applications and the metadata associated with the linked asset can be retrieved via the connector's [connected asset properties](#connected-asset-properties) interface.

Connections can be created in the open metadata repositories through the following interfaces:

- [Asset Owner OMAS](/services/omas/asset-owner/overview)
- [Asset Manager OMAS](/services/omas/asset-manager/overview)
- [Data Manager OMAS](/services/omas/data-manager/overview)
- [Database Integrator OMIS](/services/omis/database-integrator/overview)
- [Files Integrator OMIS](/services/omis/files-integrator/overview)
- [Governance Action OMES](/services/omes/governance-action/overview)

#### Configuring connections

The [administration guide](/guides/admin/guide) describes how to configure Egeria's OMAG Server Platforms and servers. Both the platform and the servers use connectors for access to the external resources to support their basic operation and to coordinate metadata and governance with third party technologies. This means that the configuration includes connection definitions for these connectors.

All of these interfaces have Java clients that enable you to set up the connection using the OCF connection bean. However, if you want to use the REST API directly, then you need to specify the connection in JSON.

!!! example "Example connection definition in JSON"
    Egeria's JSON structures map one-to-ene with the properties in the equivalent Java beans and also include
    a `class` property that gives the name of the class that it maps to. So a simple connection object
    would look something like this in JSON:

    ```json linenums="1"
    {
      "connection" : 
      {
        "class" : "Connection",
        "connectorType" : 
        {
          "class" : "ConnectorType",
          "connectorProviderClassName" : "...fully qualified class name..."
        },
        "endpoint" : 
        {
          "class" : "Endpoint",
          "address" : "... network address of resource ..."
        }
      }
    }
    ```

### Connector broker

The *connector broker* is a generic factory class for all open connectors. Given a valid [connection](#connection) object, the connector broker is able to create a new instance of a [connector](#connector). This means the caller does not need to know the implementation details of the connector - just its interface.

It is implemented in the [`ConnectorBroker` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorBroker.java){ target=gh } class, and is used as follows:

!!! example "Example usage of a connector broker"
    ```java linenums="1"
    import org.odpi.openmetadata.frameworks.connectors.Connector;
    import org.odpi.openmetadata.frameworks.connectors.ConnectorBroker;

    // ...

    ConnectorBroker   connectorBroker     = new ConnectorBroker();
    Connector         connector           = connectorBroker.getConnector(connection);
    ```

When the connector instance is requested, the connector broker uses the [*connector type*](#connector-type) properties from the supplied [connection](#connection) to identify the appropriate [connector provider](#connector-provider). The connector broker delegates the connector instance request to the connector provider and returns the result to its caller.

The connector broker is used in the client code of the [Open Metadata Access Services (OMAS)](/services/omas) that provide connector instances to their consumers, for example:

- [Asset Consumer OMAS](/services/omas/asset-consumer/overview)
- [Asset Owner OMAS](/services/omas/asset-owner/overview)

### Connector type

The *connector type* is a set of properties that defines the supported capabilities and the identity of the [connector provider](#connector-provider) for a [connector](#connector). Its properties are:

| Property | Description |
|---|---|
| `guid` | GUID for the connector type. |
| `url` | External link address for the connector type properties in the metadata repository. |
| `qualifiedName` | The official (unique) name for the connector type. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. |
| `displayName` | A consumable name for the connector type. Often a shortened form of the qualifiedName for use on user interfaces and messages.  The displayName should be only be used for audit logs and error messages if the qualifiedName is not set. |
| `description` | A full description of the connector type covering details of the assets it connects to along with usage and versioning information. |
| `connectorProviderClassName` | The [connector provider](#connector-provider) is the factory for a particular type of [connector](#connector). This property defines the class name for the connector provider that the [connector broker](#connector-broker) should use to request new connector instances.
| `recognizedAdditionalProperties` | These are the [connection](#connection)'s additional properties recognized by the connector implementation. |
| `recognizedConfigurationProperties` | These are the [connection](#connection)'s configuration properties recognized by the connector implementation. |
| `recognizedSecuredProperties` | These are the [connection](#connection)'s secured properties recognized by the connector implementation. |
| `additionalProperties` | Any additional properties that the [connector provider](#connector-provider) needs to know in order to create [connector](#connector) instances. |

The connector type is linked to the [connection](#connection) objects that request this type of connector.

![Connection Structure](connection.png)

!!! education "Further information"
    - The open metadata type for a connector type is defined in [model 0201](/types/2/0201-Connectors-and-Connections).
    - The [open connector archives :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-archives/open-connector-archives){ target=gh } module provides an open metadata archive that contains connector types for connectors supported by Egeria.

### Connector provider

A *connector provider* is the factory for a particular type of [connector](#connector). It is typically
called from the [connector broker](#connector-broker), although it may be called directly.

Each connector provider implements the [`ConnectorProvider` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorProvider.java){ target=gh } interface.

It has two types of methods:

- Return the [connector type](#connector-type) object that is added to a [connection](#connection) object used to hold the properties needed to create an instance of the [connector](#connector).
- Return a new instance of the [connector](#connector) based on the properties in a [connection](#connection) object. The connection object that has all the properties needed to create and configure the instance of the connector.

The [`ConnectorProviderBase` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorProviderBase.java){ target=gh } class provides much of the implementation for a connector provider.

??? example "Example implementation of the connector provider for a simple connector"
    If you have a simple connector implementation then your connector provider follows the following template. It assumes the connector is for the `XXXStore` and is called `XXXStoreConnector`.

    With this base implementation, a specific connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs.

    ```java linenums="1"
    /**
     * XXXStoreProvider is the OCF connector provider for the XXX store connector.
     */
    public class XXXStoreProvider extends ConnectorProviderBase
    {
        static final String  connectorTypeGUID = "Add unique GUID here";
        static final String  connectorTypeName = "XXX Store Connector";
        static final String  connectorTypeDescription = "Connector supports ... add details here";

        /**
         * Constructor used to initialize the ConnectorProviderBase with the Java class name of the specific
         * store implementation.
         */
        public BasicFileStoreProvider()
        {
            Class<?> connectorClass = XXXStoreConnector.class;

            super.setConnectorClassName(connectorClass.getName());

            ConnectorType connectorType = new ConnectorType();
            connectorType.setType(ConnectorType.getConnectorTypeType());
            connectorType.setGUID(connectorTypeGUID);
            connectorType.setQualifiedName(connectorTypeName);
            connectorType.setDisplayName(connectorTypeName);
            connectorType.setDescription(connectorTypeDescription);
            connectorType.setConnectorProviderClassName(this.getClass().getName());

            super.connectorTypeBean = connectorType;
        }
    }
    ```

??? example "Actual implementation of the connector provider for the [basic file connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector){ target=gh }"
    ```java linenums="1"
    /* SPDX-License-Identifier: Apache-2.0 */
    /* Copyright Contributors to the Egeria project. */

    package org.odpi.openmetadata.adapters.connectors.datastore.basicfile;

    import org.odpi.openmetadata.frameworks.connectors.ConnectorProviderBase;
    import org.odpi.openmetadata.frameworks.connectors.properties.beans.ConnectorType;

    /**
     * BasicFileStoreProvider is the OCF connector provider for the basic file store connector.
     */
    public class BasicFileStoreProvider extends ConnectorProviderBase
    {
        static final String  connectorTypeGUID = "ba213761-f5f5-4cf5-a95f-6150aef09e0b";
        static final String  connectorTypeName = "Basic File Store Connector";
        static final String  connectorTypeDescription = "Connector supports reading of Files.";

        /**
         * Constructor used to initialize the ConnectorProviderBase with the Java class name of the specific
         * store implementation.
         */
        public BasicFileStoreProvider()
        {
            Class<?>    connectorClass = BasicFileStoreConnector.class;

            super.setConnectorClassName(connectorClass.getName());

            ConnectorType connectorType = new ConnectorType();
            connectorType.setType(ConnectorType.getConnectorTypeType());
            connectorType.setGUID(connectorTypeGUID);
            connectorType.setQualifiedName(connectorTypeName);
            connectorType.setDisplayName(connectorTypeName);
            connectorType.setDescription(connectorTypeDescription);
            connectorType.setConnectorProviderClassName(this.getClass().getName());

            super.connectorTypeBean = connectorType;
        }
    }
    ```

### Connected asset properties

*Connected asset properties* are the properties known about an asset accessed through a connector, hosted by a [metadata access server](/concepts/metadata-access-server). These properties are presented at three levels:

#### Asset summary

`AssetSummary` holds asset properties that are used for displaying details of an asset in summary lists or hover text:

| Property | Description |
|---|---|
| `type` | metadata type information for the asset |
| `guid` | GUID for the asset |
| `url` | external link for the asset |
| `qualifiedName` | The official (unique) name for the asset. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. (Sourced from the `qualifiedName` attribute in `Referenceable` - [model 0010](/types/0/0010-Base-Model)) |
| `displayName` | A consumable name for the asset. Often a shortened form of the asset's qualifiedName for use on user interfaces and messages. The asset's displayName should be only be used for audit logs and error messages if the qualifiedName is not set. (Sourced from `displayName` attribute within `Asset` - [model 0010](/types/0/0010-Base-Model)))
| `shortDescription` | Short description about the asset. (Sourced from `assetSummary` within `ConnectionsToAsset` - [model 0205](/types/2/0205-Connection-Linkage)) |
| `description` | Full description of the asset. (Sourced from `description` attribute within `Asset` - [model 0010](/types/0/0010-Base-Model)) |
| `owner` | Name of the person or organization that owns the asset. (Sourced from the `AssetOwnership` classification - [model 0445](/types/4/0445-Governance-Roles)) |
| `zoneMembership` | List of governance zones assigned to the asset. (Sourced from the `AssetZoneMembership` classification - [model 0445](/types/4/0424-Governance-Zones)) |
| `classifications` | Full list of the classifications assigned to the asset along with their properties. |

#### Asset detail

`AssetDetail` extends `AssetSummary` to provide all the properties directly related to this asset:

| Property | Description |
|---|---|
| `ExternalIdentifiers` | List of identifiers for this asset that are used in other systems. |
| `RelatedMediaReferences` | List of links to external media (images, audio, video) about this asset. |
| `NoteLogs` | List of NoteLogs for this asset, often providing more detail on how to use the asset and its current status. |
| `ExternalReferences` | List of links to additional information about this asset. |
| `Connections` | List of connections defined to access this asset. |
| `Licenses` | List of licenses associated with the asset. |
| `Certifications` | List of certifications that have been awarded to this asset. |

#### Asset universe

`AssetUniverse` extends `AssetDetail`, and adds information about the
common open metadata entities related to this asset:

| Property | Description |
|---|---|
| `meanings` | Glossary term(s) assigned to this asset. |
| `schema` | Details of the schema type associated with the asset. |
| `feedback` | Details of the likes, reviews and comments, that are connected to the asset. |
| `knownLocations` | Details of the known locations of the asset. |
| `lineage` | Details of the lineage for the asset. |
| `relatedAssets` | Details of the assets linked to this asset. |

#### Implementation details

The [connector broker](#connector-broker) does not have access to a metadata repository because the OCF is metadata repository neutral. When it creates a connector, the connected asset properties are null.

[Egeria Open Metadata Access Services (OMAS)](/services/omas) such as [Asset Consumer OMAS](/services/omas/asset-consumer/overview), [Asset Owner OMAS](/services/omas/asset-owner/overview) and
[Discovery Engine OMAS](/services/omas/discovery-engine/overview), include the connector broker in their clients and support APIs for managing connections and creating connectors.

Connectors created by the Egeria access services will include the connected asset properties object configured to retrieve metadata from the same open metadata repository where the OMAS is running.

The connected asset properties are retrieved from the open metadata repositories by [OCF Metadata Management common services](/services/common/ocf-metadata-management). It will use the same user id that was used to create the connector.

### Endpoint

The *endpoint* is a set of properties that defines the network address and how to connect to it for a resource deployed in the digital landscape. Its properties are:

| Property | Description |
|---|---|
| `guid` | GUID for the endpoint. |
| `url` | External link address for the endpoint properties in the metadata repository. This URL can be stored as a property in another entity to create an explicit link to this endpoint. |
| `qualifiedName` | The official (unique) name for the endpoint. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. |
| `displayName` | A consumable name for the endpoint. Often a shortened form of the qualifiedName for use on user interfaces and messages. The displayName should be only be used for audit logs and error messages if the qualifiedName is not set. |
| `description` | A description for the endpoint. |
| `address` | The location of the asset. For network connected resources, this is typically the URL and port number (if needed) for the server where the asset is located (or at least accessible by the connector). For file-based resources, this is typically the name of the file. |
| `protocol` | The communication protocol that the connection should use to connect to the server. |
| `encryptionMethod` | Describes the encryption method to use (if any). This is an open value allowing information needed by the connector user to retrieve all of the information they need to work with the endpoint. |
| `additionalProperties` | Any additional properties that the connector need to know in order to access the resource. |

## Types

Open metadata repositories are able to store information needed to use OCF connectors. Details of the types involved are as follows:

- [Model 0040](/types/0/0040-Software-Servers) defines the structure of an `Endpoint`.
- [Model 0201](/types/2/0201-Connectors-and-Connections) defines the structures for `Connection`s and `ConnectorType`s.
- [Model 0205](/types/2/0205-Connection-Linkage) defines the linkage between the connection and the connected asset.

!!! education "Further information"
    - The [OCF Metadata Management](/services/ocf-metadata-management) supports the retrieval of connection and connected asset properties from the open metadata repository/repositories.
    - The [Asset Consumer OMAS](/services/omas/asset-consumer/overview) embeds the OCF to provide client-side support for connectors.
    - The [Open Metadata Repository Services (OMRS)](/services/omrs) make extensive use of OCF connectors for accessing open metadata repository servers and other resources. These connectors are collectively called the [OMRS connectors](#connector).
    - Many of the [Open Metadata Governance Servers](/concepts/governance-server) make use of OCF connectors to loosely-couple integration with a variety of underlying technologies.
    - The [developer guide](/guides/developer/guide) provides more information on writing connectors for Egeria.
    - The [connector catalog](/connectors) lists the pre-built connectors supplied by Egeria.

--8<-- "snippets/abbr.md"
