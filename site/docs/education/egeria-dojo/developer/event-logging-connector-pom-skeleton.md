<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

Paste this structure into your `pom.xml` class.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <name>Event Logging Connector</name>
    <description>
        Outputs the event payloads on the audit log.
    </description>

    <groupId>egeria.dojo</groupId>
    <artifactId>event-logging-connector</artifactId>
    <version>3.12-SNAPSHOT</version>

    <properties>
    
         <!-- Level of Java  -->
         <maven.compiler.source>11</maven.compiler.source>
         <maven.compiler.target>11</maven.compiler.target>
    
         <!-- Platform encoding  -->
         <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
         <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    
         <!-- Versions of Egeria libraries -->
         <open-metadata.version>3.12-SNAPSHOT</open-metadata.version>
    
    </properties>

    <dependencies>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>open-connector-framework</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>repository-services-apis</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

    </dependencies>

</project>

```
Notice the `<scope>provided</scope>` setting.  This prevents the Egeria libraries from being included in your connector jar file.  By using the provided scope, your connector can run with any level of Egeria that supports this type of connector.  Without it, duplicate Egeria classes would be loaded into your OMAG Server Platform and if the platform was running at a different level it is not certain which version of the classes would run. (It "may" be ok but experience, as we know, teaches us that "if it can go wrong it will go wrong" so avoiding problems is always preferable :).   




