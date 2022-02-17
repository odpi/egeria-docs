<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Add ` extends IntegrationConnectorProvider` after `public class TopicCataloguingProvider`.

Paste this code between the curly braces of the `TopicCataloguingProvider` class.

```java linenums="1"
    /*
     * Unique identifier of the connector for the audit log.
     */
    private static final int    connectorComponentId   = 1095;

    /*
     * Unique identifier for the connector type.
     */
    private static final String connectorTypeGUID      = "6c31378e-66b5-48ac-a555-436c5722cd89";

    /*
     * Descriptive information about the connector for the connector type and audit log.
     */
    private static final String connectorQualifiedName = "EgeriaDojo:IntegrationConnector:Topics:TopicCataloguingConnector";
    private static final String connectorDisplayName   = "Topic Cataloging Integration Connector";
    private static final String connectorDescription   = "Connector maintains a list of KafkaTopic assets associated with an Apache Kafka event broker.";
    private static final String connectorWikiPage      = "https://odpi.github.io/egeria-docs/connectors/integration/integration-connector/";

    /*
     * Class of the connector.
     */
    private static final Class<?> connectorClass       = TopicCataloguingConnector.class;


    static final String TEMPLATE_QUALIFIED_NAME_CONFIGURATION_PROPERTY = "templateQualifiedName";

    /**
     * Constructor used to initialize the ConnectorProvider with the Java class name of the specific
     * store implementation.
     */
    public TopicCataloguingProvider()
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
```
