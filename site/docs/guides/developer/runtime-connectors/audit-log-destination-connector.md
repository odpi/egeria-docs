<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Audit Log Destination Connectors

---8<-- "docs/connectors/runtime/audit-log-destination-connector-intro.md"

## Interface and Base Classes

The [audit log](/concepts/audit-log) running in an [OMAG Server](/concepts/omag-server) is implemented by the [Open Metadata Repository Services (OMRS)](/services/omrs).  It is called `OMRSAuditLog` and is an extension to the `AuditLog` interface defined in the [Audit Log Framework (ALF)](/frameworks/alf/overview).  The ALF supports an audit log with a single destination.  The OMRS extends this capability by implementing the ALF destination as an audit log record distributor that passes audit log records to each of the audit log destination connectors configured in the OMAG Server, depending on the severity of the audit log record and the connector's supported severities.

The OMRS also defines the list of severities used by Egeria and extends the audit log record to include details of the originating server.  It adds these values to each audit log record before it is passed to any of the audit log destination connectors.

The audit log destination connector interface is defined in the *repository-services-api* module in the [org.odpi.openmetadata.repositoryservices.connectors.stores.auditlogstore :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/auditlogstore){ target=gh } Java package.

In that package you will see the following Java classes:

* `OMRSAuditLogRecord` - provides a carrier for details about a single log record in the OMRS audit log.  It extends the `AuditLogRecord` class from the ALF with deprecated fields from the original OMRS implementation to provide backward compatible support to original implementation of the audit log destination connectors.
* `OMRSAuditLogRecordOriginator` - describes the server that originated an audit log record.  This is useful if an organization is aggregating log records from different servers together into a single physical destination.
* `OMRSAuditLogReportingComponent` describes the component issuing the audit log record.  It implements the `ComponentDescription` interface from the ALF.
* `OMRSAuditLogStore` is the main interface of the audit log destination connector.  It includes the following methods:

   * `getDestinationName` - used by the OMRS in its logging.
   * `getSupportedSeverities` - returns the list of audit log record severities that have been configured for this destination instance.  These are passed to the connector in its [configuration properties](/concepts/configuration-properties) passed in its [connection](/concepts/connection) that is set up in the server's [configuration document](/concepts/configuration-document).  The name of the property is `supportedSeverities`.
   * `storeLogRecord` - called for each log record that has a severity from the supported severities.
   * `getAuditLogRecord` - optional method to retrieve a specific log record.
   * `getAuditLogRecordsByTimeStamp` - optional method to retrieve a list of log records written in a specified time period.  The offset and maximumRecords parameters support paging.
   * `getAuditLogRecordsBySeverity` - optional method to retrieve a list of log records that have a specific severity.  The offset and maximumRecords parameters support paging.
   * `getAuditLogRecordsByComponent` - optional method to retrieve a list of log records originating from a specific component.  The offset and maximumRecords parameters support paging.

* `OMRSAuditLogStoreConnectorBase` is the abstract base class for the audit log destination connector.  It implements `OMRSAuditLogStore` and provides default methods for all but `storeLogRecord`.  It also implements `initialize` to extract the `supportedSeverities` from the connection. In addition it includes the following protected methods to aid the writer of a connector.

  * `validateLogRecord` - validates that a new log record is properly filled out and throws an `InvalidParameterException` if not.
  * `isSupportedSeverity` - checks whether an incoming log record has a supported severity.
  * `getJSONLogRecord` - converts a log record to a JSON structure.
  
* `OMRSAuditLogStoreProviderBase` is an abstract base class for the audit log destination connector's connector provider.  It extends `ConnectorProviderBase` and a method called `getRecognizedConfigurationProperties` that is used to set the `recognizedConfigurationProperties` in the connector type.

## Example Implementations

Implementations of this type of connector are located in the [adapters/open-connectors/repository-services-connectors/audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } module.

## Build Dependencies

=== "Maven"

    ```xml
    <dependencies>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>open-connector-framework</artifactId>
        </dependency>
        
         <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>repository-services-apis</artifactId>
         </dependency>

    </dependencies>
    ```

=== "gradle"

    ```xml
    dependencies {
        implementation project(':open-metadata-implementation:frameworks:open-connector-framework')
        implementation project(':open-metadata-implementation:repository-services:repository-services-apis')
    }
    ```    

## Writing the Connector Provider

The connector provider for an audit log destination connector extends the `OMRSAuditLogStoreProvider` implements the following interface:

```
org.odpi.openmetadata.frameworks.connectors.ConnectorProvider
```

There is a base class that provides much of the implementation for a connector provider.

```
org.odpi.openmetadata.frameworks.connectors.ConnectorProviderBase
```

This assumes:

- There is a single connector implementation class for the connector.
- The connector is instantiated with the default constructor. This means all of its configuration information is contained in the [Connection](/concepts/connection) object supplied on the `initialize()` method.

If your connector implementation matches these requirements, its connector provider implementation need only implement a constructor to configure the base class's function with details of itself and the Java class of the connector it needs using:
               
- a GUID for the [connector type](/concepts/connector-type)
- a name for the connector type.
- a description of what the connector is for and how to configure it.
- the connector class it instantiates.
- a list of the additional properties, configuration properties and secured properties needed to configure instances of the connector.
- a description of the connector for its audit log (if the connector implements `AuditLoggingComponent`).

```java
/**
 * XXXAuditLogDestinationProvider is the OCF connector provider for the XXX audit log destination  connector.
 */
public class XXXAuditLogDestinationProvider extends OMRSAuditLogStoreProvider
{
    /*
     * Unique identifier for the connector type.
     */
    private static final String connectorTypeGUID      = "Add unique GUID here";

    /*
     * Descriptive information about the connector for the connector type and audit log.
     */
    private static final String connectorQualifiedName = "MyOrg:XXXAuditLogDestinationConnector";
    private static final String connectorDisplayName   = "XXX Audit Log Destination Connector";
    private static final String connectorDescription   = "Connector supports ... add details here.";

    /**
     * Constructor used to initialize the ConnectorProviderBase super class.
     */
    public XXXAuditLogDestinationProvider()
    {
        super();

        /*
         * Set up the class name of the connector that this provider creates.
         */
        String connectorClassName = "packagename.XXXStoreConnector";
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
        
        connectorType.setRecognizedConfigurationProperties(super.getRecognizedConfigurationProperties);
 
        super.connectorTypeBean = connectorType;
    }
}
```

## Writing the Connector

The audit log destination needs to implement the `storeLogRecord` method.  This needs to efficiently move the log record into the destination.  The code snippet below shows the use of the super class methods to determine which record to process.

```java
    /**
     * Store the audit log record in the audit log destination.
     *
     * @param logRecord  log record to store
     * @return unique identifier assigned to the log record
     * @throws InvalidParameterException indicates that the logRecord parameter is invalid.
     */
    @Override
    public String storeLogRecord(OMRSAuditLogRecord logRecord) throws InvalidParameterException
    {
        final String   methodName = "storeLogRecord";

        super.validateLogRecord(logRecord, methodName);

        if (super.isSupportedSeverity(logRecord))
        {
            // Put implementation here
        }

        return logRecord.getGUID();
    }
```

If the destination supports querying then you can also override the query methods: `getAuditLogRecord`, `getAuditLogRecordByTimeStamp`, `getAuditLogRecordBySeverity` and `getAuditLogRecordByComponent`.

Finally, the connector should use the `start` and `disconnect` methods to initialize and close down the access to the destination technology.

--8<-- "snippets/abbr.md"
