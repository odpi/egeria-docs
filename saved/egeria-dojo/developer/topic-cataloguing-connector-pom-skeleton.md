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

    <name>Topic Cataloguing Integration Connector</name>
    <description>
        Monitors the topics in a Kafka Broker and creates a list of KafkaTopic assets for each topic.
    </description>

    <groupId>egeria.dojo</groupId>
    <artifactId>topic-cataloguing-connector</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
    
         <!-- Level of Java  -->
         <maven.compiler.source>11</maven.compiler.source>
         <maven.compiler.target>11</maven.compiler.target>
    
         <!-- Platform encoding  -->
         <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
         <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    
         <!-- Versions of Egeria libraries -->
         <open-metadata.version>4.2</open-metadata.version>
    
         <!-- Versions of other dependent libraries -->
         <kafka.version>3.1.0</kafka.version>

    </properties>

    <dependencies>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>audit-log-framework</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>open-connector-framework</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>topic-integrator-api</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>data-manager-api</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>repository-services-apis</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>
        
        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>integration-daemon-services-api</artifactId>
            <scope>provided</scope>
            <version>${open-metadata.version}</version>
        </dependency>

        <dependency>
            <groupId>org.apache.kafka</groupId>
            <artifactId>kafka-clients</artifactId>
            <version>${kafka.version}</version>
        </dependency>

    </dependencies>

</project>

```





