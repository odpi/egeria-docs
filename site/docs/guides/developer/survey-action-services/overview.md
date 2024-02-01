<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Writing a Survey Action Service

---8<-- "docs/connectors/survey-action/survey-action-service-intro.md"
---8<-- "docs/frameworks/saf/survey-action-pipeline-intro.md"


## Implementing survey action services

A survey action service is implemented as a specialized [Open Connector Framework (OCF)](/frameworks/ocf/overview) connector. This means it has two parts to it: a *connector provider* that is responsible for creating a new instance of the survey action service and the *survey action service implementation* (that is the *connector implementation* in the OCF terminology.)  

### Dependencies

The interfaces and base classes of the connector provider and survey action service implementation are provided by the [Survey Action Framework (ODF)](/frameworks/odf/overview).  This means you need to include the following Egeria modules in your build script:

* Open Connector Framework
* Survey Action Framework
* Governance Action Framework for access to open metadata definitions.
* Audit Log Framework for audit logging and exceptions.
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
                <artifactId>survey-action-framework</artifactId>
            </dependency>

            <dependency>
                <groupId>org.odpi.egeria</groupId>
                <artifactId>governance-action-framework</artifactId>
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
        implementation project(':open-metadata-implementation:frameworks:survey-action-framework')
        implementation project(':open-metadata-implementation:frameworks:governance-action-framework')
        implementation project('...data store connector...')  
    }
    ```
    

### Connector provider for a survey action service

Each connector provider for a survey action service extends the following base class:

```
org.odpi.openmetadata.frameworks.surveyaction.SurveyActionServiceProvider
```
This assumes:

- The survey action service implementation class is instantiated with the default constructor. This means all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method.

If your survey action service implementation matches these requirements, its connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs using:
               
- a GUID for the [connector type](/concepts/connector-type)
- a name for the connector type.
- a description of what the connector is for and how to configure it.
- the connector class it instantiates.
- a list of the additional properties, configuration properties and secured properties needed to configure instances of the connector.
- a description of the connector for its audit log (if the connector implements `AuditLoggingComponent`).

```java
/**
 * XXXSurveyActionProvider is the OCF connector provider for the XXX survey action service.
 */
public class XXXSurveyActionProvider extends SurveyActionProviderBase
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
    private static final String connectorQualifiedName = "MyOrg:XXXSurveyActionService";
    private static final String connectorDisplayName   = "XXX Survey Action Service";
    private static final String connectorDescription   = "A survey action service that supports ... add details here.";
    private static final String connectorWikiPage      = "Add url to documentation here";


    /*
     * Define the name of the connector implementation.
     */
    private static final String connectorClassName = "packagename.XXXSurveyActionService";
    
    /*
     * Define the name of configuration properties (optional).
     */
    public static final String REQUIRED_ANNOTATION_TYPES_CONFIGURATION_PROPERTY = "requiredAnnotationTypes";

    /**
     * Constructor used to initialize the ConnectorProviderBase class.
     */
    public XXXSurveyActionProvider()
    {
        super();

        /*
         * Set up the class name of the survey action service that this provider creates.
         */
        super.setConnectorClassName(connectorClassName);

        /*
         * Set up the connector type that should be included in a connection used to configure this survey action service.
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
         * Set up the component description used in the survey action service's audit log messages.
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

### Survey action service implementation

The survey action service implementation inherits from:

```
org.odpi.openmetadata.frameworks.surveyaction.SurveyActionServiceConnector
```
This base class handles the survey context, any nested connectors and the audit log.  The following variables are set up:

* `surveyServiceName` - the qualified name of the survey action service from the open metadata definition.

* `surveyContext` - the survey context that provides methods for querying and storing survey metadata.

* `auditLog` - audit logging destination.

* `embeddedConnectors` - connectors created from connections nested in the survey action service connection.  These connectors are typically survey action services that are embedded because this survey action service is an [survey action pipeline](#survey-action-pipelines).


There are two methods that you need to implement:

* `start()` - this method is where all the work takes place. It retrieves any configuration properties from the connection, uses the survey context to access the asset and its [connector to the digital resource](/concepts/digital-resource-connector).  As it analyses the content of the digital resource, it adds its results to the annotation store retrieved from the survey context.  The annotations are immediately stored in one of the open metadata repositories.

* `disconnect()` - this method is called either because the survey action service has completed running, or because its server is shutting down.  The survey action service implementation should release any resources it is using - for example by calling the disconnect method on the digital resource connector it is using.

### Survey Context

The survey context provides the *survey action service* with access to information about the survey request along with the open metadata repository interfaces.

![Structure of the survey context](/frameworks/saf/survey-context.svg)

#### Survey Asset Catalog Store

The survey asset catalog store provides a search interface that enables a survey action service to locate assets that are described in the open metadata repository.

#### Annotation Store

The survey annotation store provides a survey action service with access to the [annotations](/concepts/survey-report/#annotations) created about a specific asset both from past invocations of survey action services and those created during the current execution.

#### Open Metadata Store

Provides access to all types of open metadata through the Governance Action Framework (GAF).

## Example implementations

The definition of the connector interfaces for survey action services is defined in the [survey-action-services :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/frameworks/survey-action-framework/src/main/java/org/odpi/openmetadata/frameworks/survey){ target=gh } module.

There are implementations of survey action services in the [survey-service-connectors](/connectors/#survey-action-services).

---8<-- "snippets/abbr.md"
