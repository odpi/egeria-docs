---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connector provider

A **connector provider** is the factory for a particular type of [connector](connector.md), and is part of the
[Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf). It is typically
called from the [connector broker](connector-broker.md), although it may be called directly.

Each connector provider implements the [`ConnectorProvider` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorProvider.java){ target=gh }
interface.

It has two types of methods:

- Return the [ConnectorType](connector-type.md) object that is added to a [connection](connection.md) object used to
  hold the properties needed to create an instance of the [connector](connector.md).
- Return a new instance of the [connector](connector.md) based on the properties in a [connection](connection.md) object.
  The connection object that has all the properties needed to create and configure the instance of the connector.

The [`ConnectorProviderBase` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/ConnectorProviderBase.java){ target=gh }
class provides much of the implementation for a connector provider.

??? example "Example implementation of the connector provider for a simple connector"
    If you have a simple connector implementation then your connector provider follows the following
    template. It assumes the connector is for the `XXXStore` and is called `XXXStoreConnector`.

    With this base implementation, a specific connector provider implementation need only implement a constructor to
    configure the base class's function with details of itself and the Java class of the connector it needs.

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

--8<-- "snippets/abbr.md"
