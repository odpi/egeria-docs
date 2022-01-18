<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Audit Log Destination Connectors

---8<-- "docs/connectors/runtime/audit-log-destination-connector-intro.md"

## Interface and Base Classes

The [audit log](/egeria-docs/concepts/audit-log) running in an [OMAG Server](/egeria-docs/concepts/omag-server) is implemented by the [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs).  It is called `OMRSAuditLog` and is an extension to the `AuditLog` interface defined in the [Audit Log Framework (ALF)](/egeria-docs/frameworks/alf/overview).  The ALF supports an audit log with a single destination.  The OMRS extends this capability by implementing the ALF destination as an audit log record distributor that passes audit log records to each of the audit log destination connectors configured in the OMAG Server, depending on the severity of the audit log record and the connector's supported severities.

The OMRS also defines the list of severities used by Egeria and extends the audit log record to include details of the originating server.  It adds these values to each audit log record before it is passed to any of the audit log destination connectors.

The audit log destination connector interface is defined in the [repository-services-api :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis){ target=gh } module in the [org.odpi.openmetadata.repositoryservices.connectors.stores.auditlogstore :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/auditlogstore){ target=gh } Java package.



## Example Implementations

Implementations of this type of connector are located in the [adapters/open-connectors/repository-services-connectors/audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } module.

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


## Writing the Connector


--8<-- "snippets/abbr.md"
