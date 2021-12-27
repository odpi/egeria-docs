<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Defining new types

Egeria supports a [wide variety of open metadata types](/egeria-docs/types) that cover a broad range of metadata.  These types can be extended through the normal contribution process of the Egeria project.   It is also possible to create your own type definitions that can be exchanged across the [open metadata repository cohort](/egeria-docs/concepts/cohort-member) and may also be maintained through Egeria's APIs using [extended properties](/egeria-docs/concepts/extended-properties).

Type definitions need to be governed because they must be consistent across a cohort - during the whole time that one or more instances of the type are stored in the repositories.

## Dynamic definitions of types not recommended

Egeria does have an API for dynamically defining types but it is recommended that you only use it went experimenting with types and instances.  Instead, you should manage your types in an [open metadata archive](/egeria-docs/concepts/open-metadata-archive) that is loaded in the [metadata access servers](/egeria-docs/concepts/metadata-access-servers) during [each server start up](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-store/#configure-metadata-to-load-on-startup).

## Creating your own type archive

A type archive is created using a Java program that uses the [repository services archive utilities](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-archive-utilities) to add your new type definitions to an open metadata archive file.



Begin by setting up your build file - this is an example using Maven.

```xml

<?xml version="1.0" encoding="UTF-8"?>

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <name>My Types Utility</name>
    <description>
        This package builds the open metadata type archive for my extended types.
    </description>

    <artifactId>my-types-utility</artifactId>

    <dependencies>
        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>repository-services-apis</artifactId>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>repository-services-archive-utilities</artifactId>
        </dependency>

        <dependency>
            <groupId>org.odpi.egeria</groupId>
            <artifactId>open-metadata-types</artifactId>
        </dependency>
    
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <executions>
                    <execution>
                        <id>assemble-all</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                        <configuration>
                            <descriptorRefs>
                                <descriptorRef>jar-with-dependencies</descriptorRef>
                            </descriptorRefs>
                            <archive>
                                <manifest>
                                    <mainClass>cocopharma.openmetadata.types.CocoTypesArchiveUtility</mainClass>
                                </manifest>
                            </archive>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

```java
/* SPDX-License-Identifier: Apache-2.0 */
/* Copyright Contributors to the ODPi Egeria project. */
package cocopharma.openmetadata.types;

import org.odpi.openmetadata.opentypes.OpenMetadataTypesArchiveWriter;



/**
 * OpenMetadataTypesArchiveWriter create a physical open metadata archive file for the supplied open metadata archives
 * encoded using Open Metadata Repository Services (OMRS) formats.
 */
public class CocoTypesArchiveUtility
{
    private static final String defaultTypeArchiveFileName = "CocoMetadataTypes.json";

    /**
     * Main program to control the archive writer.
     * Note: See issue #3392 if logging is needed
     *
     * @param args ignored arguments
     */
    public static void main(String[] args)
    {
        OpenMetadataTypesArchiveWriter archiveWriter = new OpenMetadataTypesArchiveWriter();

        archiveWriter.writeOpenMetadataTypesArchive();
    }
}
```

--8<-- "snippets/abbr.md"
