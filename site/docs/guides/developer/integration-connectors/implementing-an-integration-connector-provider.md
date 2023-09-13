<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


Each connector provider for an integration connector extends the [IntegrationConnectorProvider](https://odpi.github.io/egeria/org/odpi/openmetadata/governanceservers/integrationdaemonservices/connectors/IntegrationConnectorProvider.html) base class, which in turn extends the standard `ConnectorProviderBase`:

This assumes the integration connector's implementation class is instantiated via the default constructor and all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method.

If your connector implementation matches these requirements, its connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs using:
               
- a GUID for the [connector type](/concepts/connector-type)
- a name for the connector type.
- a description of what the connector is for and how to configure it.
- the connector class it instantiates.
- a list of the additional properties, configuration properties and secured properties needed to configure instances of the connector.
- a description of the connector for its audit log (if the connector implements `AuditLoggingComponent`).

```java
/**
 * XXXStoreProvider is the OCF connector provider for the XXX integration connector.
 */
public class XXXStoreProvider extends IntegrationConnectorProviderBase
{
    /*
     * Unique identifier of the connector for the audit log.
     */
    private static final int    connectorComponentId   = 10001; /* Add unique number here - Egeria uses numbers under 1000 */

    /*
     * Unique identifier for the connector type.
     */
    private static final String connectorTypeGUID      = "Add unique GUID here";

    /*
     * Descriptive information about the connector for the connector type and audit log.
     */
    private static final String connectorQualifiedName = "MyOrg:Integration:XXXStoreConnector";
    private static final String connectorDisplayName   = "XXX Store Connector";
    private static final String connectorDescription   = "Connector supports ... add details here.";
    private static final String connectorWikiPage      = "Add url to documentation here";


    /*
     * Define the name of the connector implementation.
     */
    private static final String connectorClassName = "packagename.XXXStoreConnector";
    
    /*
     * Define the name of configuration properties (optional).
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
        connectorType.setType(ConnectorType.getConnectorTypeType());
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


