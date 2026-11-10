<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


Each connector provider extends the following abstract class:

```
org.odpi.openmetadata.frameworks.connectors.ConnectorProvider
```

There is a base class that provides much of the implementation for a connector provider:

```
org.odpi.openmetadata.frameworks.connectors.ConnectorProviderBase
```

and a subclass of it that sets up the connector provider from a single description of the connector:

```
org.odpi.openmetadata.frameworks.connectors.OpenConnectorProviderBase
```

These base classes assume:

- There is a single connector implementation class for the connector.
- The connector is instantiated with the default constructor. This means all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method.

If your connector implementation matches these requirements, its connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs using:

- a GUID for the [connector type](/concepts/connector-type)
- a qualified name and display name for the connector type.
- a description of what the connector is for and how to configure it.
- the connector class it instantiates.
- a list of the additional properties, configuration properties and secured properties needed to configure instances of the connector.
- a description of the connector for its audit log (if the connector implements `AuditLoggingComponent`).

!!! tip "Use the base class for your type of connector"
    Many types of connector have their own connector provider base class that extends `OpenConnectorProviderBase`, for example `IntegrationConnectorProvider` for [integration connectors](/concepts/integration-connector) and `OMRSRepositoryConnectorProviderBase` for [repository connectors](/concepts/repository-connector).  Extend the base class for the type of connector you are writing.

### Using OpenConnectorProviderBase

The descriptive information about the connector is supplied through an implementation of the `OpenConnectorDefinition` interface.  This is typically an enum that describes all the connectors in a module.  Egeria's own connectors are described in the `EgeriaOpenConnectorDefinition` enum in the `org.odpi.openmetadata.adapters.connectors` package.  An `OpenConnectorDefinition` returns:

- `getConnectorComponentId()` - unique identifier of the connector for the audit log.
- `getConnectorTypeGUID()` - unique identifier of the connector type.
- `getConnectorQualifiedName()`, `getConnectorDisplayName()`, `getConnectorDescription()` and `getConnectorWikiPage()` - descriptive information for the connector type and audit log.
- `getConnectorProviderClassName()` - the class name of the connector provider.  `OpenConnectorProviderBase` checks that this matches the class of the connector provider being constructed.
- `getConnectorDevelopmentStatus()` - the `ComponentDevelopmentStatus` of the connector.
- `getSupportedAssetTypeName()` and `getSupportedDeployedImplementationType()` - the type of asset and the deployed implementation type that the connector works with.
- `getComponentDescription()` - the `AuditLogReportingComponent` for the connector's audit log messages.

The connector provider then passes this definition to the `OpenConnectorProviderBase` constructor, along with the connector class name and the names of its recognized configuration properties.  The constructor builds the connector type and audit log component description from these values.

```java
/**
 * XXXStoreProvider is the OCF connector provider for the XXX connector.
 */
public class XXXStoreProvider extends OpenConnectorProviderBase
{
    /*
     * Define the name of the connector implementation.
     */
    private static final String connectorClassName = "packagename.XXXStoreConnector";

    /*
     * Define the name of configuration properties.
     */
    public static final String TEMPLATE_QUALIFIED_NAME_CONFIGURATION_PROPERTY = "templateQualifiedName";

    /**
     * Constructor used to initialize the ConnectorProviderBase class.
     */
    public XXXStoreProvider()
    {
        super(MyOrgConnectorDefinition.XXX_STORE_CONNECTOR,
              connectorClassName,
              List.of(TEMPLATE_QUALIFIED_NAME_CONFIGURATION_PROPERTY));
    }
}
```

There is also a constructor that takes the list of interfaces that the connector supports and a description of the data format that it expects.  After calling `super(...)`, the constructor may set up the `supportedTechnologyTypes`, `supportedConfigurationProperties` and `supportedTemplateTypes` variables inherited from `ConnectorProvider`.

??? example "Example: BasicFileStoreProvider"
    The [`BasicFileStoreProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector/src/main/java/org/odpi/openmetadata/adapters/connectors/datastore/basicfile/BasicFileStoreProvider.java){ target=gh } passes `EgeriaOpenConnectorDefinition.BASIC_FILE_STORE_CONNECTOR`, its connector class name and the `BasicFileStore` interface to `OpenConnectorProviderBase`, and then sets `supportedTechnologyTypes` to show that it works with files.

### Using ConnectorProviderBase directly

Alternatively, the connector provider can extend `ConnectorProviderBase` and set up the connector type and component description itself.

```java
/**
 * XXXStoreProvider is the OCF connector provider for the XXX connector.
 */
public class XXXStoreProvider extends ConnectorProviderBase
{
    /*
     * Unique identifier of the connector for the audit log.
     */
    private static final int    connectorComponentId   = 10001; /* Add unique number here */

    /*
     * Unique identifier for the connector type.
     */
    private static final String connectorTypeGUID      = "Add unique GUID here";

    /*
     * Descriptive information about the connector for the connector type and audit log.
     */
    private static final String connectorQualifiedName = "MyOrg:XXXStoreConnector";
    private static final String connectorDisplayName   = "XXX Store Connector";
    private static final String connectorDescription   = "Connector supports ... add details here.";
    private static final String connectorWikiPage      = "Add url to documentation here";


    /*
     * Define the name of the connector implementation.
     */
    private static final String connectorClassName = "packagename.XXXStoreConnector";
    
    /*
     * Define the name of configuration properties.
     */
    public static final String TEMPLATE_QUALIFIED_NAME_CONFIGURATION_PROPERTY = "templateQualifiedName";

    /**
     * Constructor used to initialize the ConnectorProviderBase class.
     */
    public XXXStoreProvider()
    {
        super();

        /*
         * Set up the class name of the connector that this provider creates.
         */
        super.setConnectorClassName(connectorClassName);

        /*
         * Set up the connector type that should be included in a connection used to configure this connector.
         */
        ConnectorType connectorType = new ConnectorType();
        connectorType.setGUID(connectorTypeGUID);
        connectorType.setQualifiedName(connectorQualifiedName);
        connectorType.setDisplayName(connectorDisplayName);
        connectorType.setDescription(connectorDescription);
        connectorType.setConnectorProviderClassName(this.getClass().getName());

        List<String> recognizedConfigurationProperties = new ArrayList<>();
        recognizedConfigurationProperties.add(TEMPLATE_QUALIFIED_NAME_CONFIGURATION_PROPERTY);
        connectorType.setRecognizedConfigurationProperties(recognizedConfigurationProperties);
 
        super.connectorTypeBean = connectorType;
 
        /*
         * Set up the component description used in the connector's audit log messages.
         */
        AuditLogReportingComponent componentDescription = new AuditLogReportingComponent();
 
        componentDescription.setComponentId(connectorComponentId);
        componentDescription.setComponentName(connectorQualifiedName);
        componentDescription.setComponentDescription(connectorDescription);
        componentDescription.setComponentWikiURL(connectorWikiPage);
 
        super.setConnectorComponentDescription(componentDescription);
    }
}
```

