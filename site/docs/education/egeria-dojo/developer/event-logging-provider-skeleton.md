<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Add ` extends OMRSAuditLogStoreProviderBase` after `public class EventLoggingProvider`.  This base class provides most of the code needed to implement the connector provider.  All you need to add is some descriptive information about your connector.

Paste this code between the curly braces of the `EventLoggingProvider` class.

```java linenums="1"
    /*
     * Unique identifier for the connector type.
     */
    private static final String connectorTypeGUID      = "deb61a6d-08c8-4656-8340-6e6197e6df3e";

    /*
     * Descriptive information about the connector for the connector type and audit log.
     */
    private static final String connectorQualifiedName = "Egeria:AuditLogDestinationConnector:EventDisplay";
    private static final String connectorDisplayName   = "Event Display Audit Log Destination Connector";
    private static final String connectorDescription   = "Connector supports logging of EVENT audit log messages to stdout along with the event payload from the log record's additional information.";

    /*
     * Class of the connector.
     */
    private static final Class<?> connectorClass       = EventLoggingConnector.class;

    /**
     * Constructor used to initialize the ConnectorProviderBase with the Java class name of the specific
     * audit log store implementation.
     */
    public EventLoggingProvider()
    {
        super();

        /*
         * Set up the class name of the connector that this provider creates.
         */
        super.setConnectorClassName(connectorClass.getName());

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
        connectorType.setRecognizedConfigurationProperties(super.getRecognizedConfigurationProperties());

        super.connectorTypeBean = connectorType;
    }
```
