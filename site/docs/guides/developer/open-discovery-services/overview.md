<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing an Open Discovery Service

---8<-- "docs/connectors/discovery/discovery-service-intro.md"
---8<-- "docs/connectors/discovery/discovery-pipeline-intro.md"

## Implementing open discovery services

An open discovery service is implemented as a specialized [Open Connector Framework (OCF)](/frameworks/ocf/overview) connector. This means it has two parts to it: a *connector provider* that is responsible for creating a new instance of the open discovery service and the *open discovery service implementation* (that is the *connector implementation* in the OCF terminology.)  

### Dependencies

The interfaces and base classes of the connector provider and open discovery service implementation are provided by the [Open Discovery Framework (ODF)](/frameworks/odf/overview).  This means you need to include the following Egeria modules in your build script:

* Open Connector Framework
* Open Discovery Framework
* Audit Log Framework and Repository Services APIs for audit logging and exceptions.
* The digital resource connector(s) used to gain access to the digital resource being analysed.

=== "Maven dependencies"
    ```xml
    
        <dependencies>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>audit-log-framework</artifactId>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-connector-framework</artifactId>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>open-discovery-framework</artifactId>
            </dependency>
    
            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>repository-services-apis</artifactId>
            </dependency>
    
            <dependency>
                  :
               Digital resource connectors need to be included
                  :
            </dependency>
    
        </dependencies>
    
    ```
=== "Gradle dependencies"
    ```
    dependencies {
        implementation project(':open-metadata-implementation:frameworks:audit-log-framework')
        implementation project(':open-metadata-implementation:frameworks:open-connector-framework')
        implementation project(':open-metadata-implementation:frameworks:open-discovery-framework')
        implementation project(':open-metadata-implementation:repository-services:repository-services-apis')
        implementation project('...data store connector...')  
    }
    ```
    

### Connector provider for an open discovery service

Each connector provider for an open discovery service extends the following base class:

```
org.odpi.openmetadata.frameworks.discovery.DiscoveryServiceProvider
```
This assumes:

- The open discovery service implementation class is instantiated with the default constructor. This means all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method.

If your open discovery service implementation matches these requirements, its connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs using:
               
- a GUID for the [connector type](/concepts/connector-type)
- a name for the connector type.
- a description of what the connector is for and how to configure it.
- the connector class it instantiates.
- a list of the additional properties, configuration properties and secured properties needed to configure instances of the connector.
- a description of the connector for its audit log (if the connector implements `AuditLoggingComponent`).

```java
/**
 * XXXDiscoveryProvider is the OCF connector provider for the XXX open discovery service.
 */
public class XXXDiscoveryProvider extends IntegrationConnectorProviderBase
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
    private static final String connectorQualifiedName = "MyOrg:XXXDiscoveryService";
    private static final String connectorDisplayName   = "XXX Discovery Service";
    private static final String connectorDescription   = "Open discovery service that supports ... add details here.";
    private static final String connectorWikiPage      = "Add url to documentation here";


    /*
     * Define the name of the connector implementation.
     */
    private static final Class<?> connectorClass = XXXDiscoveryService.class;
    
    /*
     * Define the name of configuration properties (optional).
     */
    public static final String REQUIRED_ANNOTATION_TYPES_CONFIGURATION_PROPERTY = "requiredAnnotationTypes";

    /**
     * Constructor used to initialize the ConnectorProviderBase class.
     */
    public XXXDiscoveryProvider()
    {
        super();

        /*
         * Set up the class name of the open discovery service that this provider creates.
         */
        super.setConnectorClassName(connectorClass.getName());

        /*
         * Set up the connector type that should be included in a connection used to configure this open discovery service.
         */
        ConnectorType connectorType = new ConnectorType();
        connectorType.setType(ConnectorType.getConnectorTypeType());
        connectorType.setGUID(connectorTypeGUID);
        connectorType.setQualifiedName(connectorQualifiedName);
        connectorType.setDisplayName(connectorDisplayName);
        connectorType.setDescription(connectorDescription);
        connectorType.setConnectorProviderClassName(this.getClass().getName());

        List<String> recognizedConfigurationProperties = new ArrayList<>();
        recognizedConfigurationProperties.add(REQUIRED_ANNOTATION_TYPES_CONFIGURATION_PROPERTY);
        connectorType.setRecognizedConfigurationProperties(recognizedConfigurationProperties);
 
        super.connectorTypeBean = connectorType;
 
        /*
         * Set up the component description used in the open discovery service's audit log messages.
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

### Open discovery service implementation

The open discovery service implementation inherits from:

```
org.odpi.openmetadata.frameworks.discovery.DiscoveryService
```
This base class handles the discovery context, any nested connectors and the audit log.  The following variables are set up:

* `discoveryServiceName` - the qualified name of the discovery service from the open metadata definition.

* `discoveryContext` - the discovery context that provides methods for querying and storing discovery metadata.

* `auditLog` - audit logging destination.

* `embeddedConnectors` - connectors created from connections nested in the discovery service connection.  These connectors are typically open discovery services that are embedded because this discovery service is an [open discovery pipeline](#open-discovery-pipelines).


There are two methods that you need to implement:

* `start()` - this method is where all the work takes place. It retrieves any configuration properties from the connection, uses the discovery context to access the asset and its [connector to the digital resource](/concepts/digital-resource-connector).  As it analyses the content of the digital resource, it adds its results to the annotation store retrieved from the discovery context.  The annotations are immediately stored in one of the open metadata repositories.

* `disconnect()` - this method is called either because the discovery service has completed running, or because its server is shutting down.  The open discovery service implementation should release any resources it is using - for example by calling the disconnect method on the digital resource connector it is using.

### Discovery Context

The discovery context provides the *open discovery service* with access to information about the discovery request along with the open metadata repository interfaces.

![Structure of the discovery context](/frameworks/odf/discovery-context.svg)

#### Discovery Asset Catalog Store

The discovery asset catalog store provides a search interface that enables an open discovery service to locate assets that are described in the open metadata repository.

#### Discovery Annotation Store

The discovery annotation store provides an open discovery service with access to the [annotations](/concepts/discovery-analysis-report/#discovery-annotations) created about a specific asset both from past invocations of open discovery services and those created during the current execution.

#### Discovery Asset Store

The discovery asset catalog store provides an open discovery service with access to all the known metadata about the digital resource it is to analyse.  It is able to create a connector to the digital resource based on the connection(s) attached to the asset.

#### Discovery Analysis Report Store

The discovery analysis report store is a client to an open metadata server that enables an open discovery service to query the properties of its discovery analysis report and update the analysis step that is currently executing and the status of its processing.

The discovery analysis report store is accessed from the [discovery annotation store](#discovery-annotation-store).

## Example implementations

The definition of the connector interfaces for discovery services is defined in the [open-discovery-services :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/open-discovery-framework/src/main/java/org/odpi/openmetadata/frameworks/discovery){ target=gh } module.

There are implementations of discovery services in the [discovery-service-connectors](/connectors/#open-discovery-services).

---8<-- "snippets/abbr.md"
