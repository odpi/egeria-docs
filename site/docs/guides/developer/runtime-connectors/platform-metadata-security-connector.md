<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Platform Metadata Security Connectors

The *platform metadata security connector* provides authorization support for requests to the [OMAG Server Platform](/concepts/omag-server-platform).

![Figure 1](/connectors/runtime/platform-metadata-security-connector.svg)
> **Figure 1:** Platform Metadata Security Connector

## Interface and Base Classes

## Example Implementations

An example implementation of this type of connector is located in the [open-metadata-security-samples :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/open-metadata-security-samples){ target=gh } module.

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
            <artifactId>metadata-security-connectors</artifactId>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>metadata-security-apis</artifactId>
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
    implementation project(':open-metadata-implementation:common-services:metadata-security:metadata-security-connectors')
    implementation project(':open-metadata-implementation:repository-services:repository-services-apis')
    implementation project(':open-metadata-implementation:frameworks:open-connector-framework')
    implementation project(':open-metadata-implementation:frameworks:audit-log-framework')
    implementation project(':open-metadata-implementation:common-services:metadata-security:metadata-security-apis')

    }
    ```    

## Writing the Connector Provider

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

## Writing the Connector


--8<-- "snippets/abbr.md"
