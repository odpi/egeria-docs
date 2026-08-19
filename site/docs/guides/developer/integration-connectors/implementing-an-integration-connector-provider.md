<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


Each connector provider for an integration connector extends the [`IntegrationConnectorProvider` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/connectors/IntegrationConnectorProvider.java){ target=gh } base class, which in turn extends `OpenConnectorProviderBase` and `ConnectorProviderBase`.

This assumes the integration connector's implementation class is instantiated via the default constructor and all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method, plus the [catalog targets](/concepts/catalog-target) attached to it at runtime.

The descriptive information about the connector is supplied through an implementation of the [`OpenConnectorDefinition` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-connector-framework/src/main/java/org/odpi/openmetadata/frameworks/connectors/OpenConnectorDefinition.java){ target=gh } interface.  Defining it as an enum keeps the descriptions of all the connectors in your library together, and makes it easy to generate an open metadata archive that describes them.  Egeria's own connectors use the `EgeriaOpenConnectorDefinition` enum for this.

The definition supplies:

- a GUID for the [connector type](/concepts/connector-type), and its qualified name, display name and description.
- a unique component identifier and wiki page used in the connector's audit log messages (Egeria uses numbers under 1000 for its own connectors, so choose a number above that).
- the class name of the connector provider, and the development status of the connector.
- the open metadata type and [deployed implementation type](/concepts/deployed-implementation-type) of the asset that a connection for this connector should be linked to.

The connector provider's constructor then adds the information that is specific to integration connectors:

- the connector class it instantiates.
- the names of the configuration properties it recognizes, and their full descriptions.
- the types of element it accepts as a [catalog target](/concepts/catalog-target).
- the technology types it supports, and any templates it uses.
- optionally, the default refresh interval and whether the connector issues blocking calls.

```java
/**
 * XXXStoreProvider is the connector provider for the XXX integration connector.
 */
public class XXXStoreProvider extends IntegrationConnectorProvider
{
    /*
     * Class of the connector implementation.
     */
    private static final String connectorClassName = "packagename.XXXStoreConnector";


    /**
     * Constructor used to initialize the base class with details of this connector.
     */
    public XXXStoreProvider()
    {
        super(MyOpenConnectorDefinition.XXX_STORE_INTEGRATION_CONNECTOR,
              connectorClassName,
              XXXConfigurationProperty.getRecognizedConfigurationProperties());

        /*
         * The technology that this connector works with.
         */
        super.supportedTechnologyTypes = SupportedTechnologyType.getSupportedTechnologyTypes(
                new DeployedImplementationTypeDefinition[]{XXXDeployedImplementationType.XXX_SERVER});

        /*
         * The types of element that can be attached to this connector as a catalog target.
         */
        super.catalogTargets = XXXTarget.getCatalogTargetTypes();

        /*
         * Full descriptions of the configuration properties, for the person deploying the connector.
         */
        super.supportedConfigurationProperties = XXXConfigurationProperty.getConfigurationPropertyTypes();

        /*
         * Optional: how often refresh() should be called, in minutes.  Zero means only at start up
         * and when explicitly requested.  The default is 60.
         */
        super.setRefreshTimeInterval(30L);
    }
}
```

### Catalog target types

The `catalogTargets` list tells the people (and the tools) that deploy this connector which elements it can work with.  Each [`CatalogTargetType` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/frameworks/open-integration-framework/src/main/java/org/odpi/openmetadata/frameworks/integration/controls/CatalogTargetType.java){ target=gh } has:

* **name** - the *catalogTargetName* used on the *CatalogTarget* relationship.  A connector that accepts more than one kind of target uses this name to tell them apart.
* **typeName** - the [open metadata type](/types) of the element, such as `SoftwareServer` or `DataFolder`.
* **deployedImplementationType** - a more precise description of the technology, such as `PostgreSQL Server`.
* **otherPropertyValues** - additional property values that a compatible catalog target should have.

These are typically defined as an enum alongside the connector.  From the PostgreSQL connectors:

```java
public enum PostgresTarget
{
    SERVER("postgreSQLServer",
           PostgresDeployedImplementationType.POSTGRESQL_SERVER.getDescription(),
           PostgresDeployedImplementationType.POSTGRESQL_SERVER.getAssociatedTypeName(),
           PostgresDeployedImplementationType.POSTGRESQL_SERVER.getDeployedImplementationType(),
           null),

    DATABASE("postgresDatabase",
             PostgresDeployedImplementationType.POSTGRESQL_DATABASE.getDescription(),
             PostgresDeployedImplementationType.POSTGRESQL_DATABASE.getAssociatedTypeName(),
             PostgresDeployedImplementationType.POSTGRESQL_DATABASE.getDeployedImplementationType(),
             null),
    ;
}
```

The catalog target processor should still validate the element it is given, since the relationship can be created by anyone - see [writing the catalog target processor](/guides/developer/integration-connectors/catalog-targets/#writing-the-catalog-target-processor).

### Refresh interval and blocking calls

- `setRefreshTimeInterval(minutes)` sets the default number of minutes between calls to `refresh()`.  Zero means `refresh()` is only called at start up and when an operator explicitly requests it.  The value can be overridden in the connector's configuration.
- `setUsesBlockingCalls(true)` tells the integration daemon to run the connector on its own thread and to call `engage()` rather than `refresh()`.

