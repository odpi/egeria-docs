<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Open Metadata Archive Store Connectors

---8<-- "snippets/connectors/open-metadata-archive-store-connector-intro.md"

## Interface and Base Classes


The definition of the open metadata archive connector interface is defined in the *repository-services-api* module in the [org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore){ target=gh } Java package.

Its interface is called [`OpenMetadataArchiveStore` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/OpenMetadataArchiveStore.java){ target=gh }

```java
public interface OpenMetadataArchiveStore
{
    /**
     * Return the contents of the archive.
     *
     * @return OpenMetadataArchive object
     */
    OpenMetadataArchive getArchiveContents();


    /**
     * Set new contents into the archive.  This overrides any content previously stored.
     *
     * @param archiveContents  OpenMetadataArchive object
     */
    void setArchiveContents(OpenMetadataArchive archiveContents);
}
```


The open metadata archive structure is defined by [`OpenMetadataArchive` :material-github](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/properties/OpenMetadataArchive.java){ target=gh }.

There are 3 sections:

| Section | Description
|---|---|
| `archiveProperties` | provides details of the source and contents of the archive |
| `archiveTypeStore` | a list of new AttributeTypeDefs, new TypeDefs and patches to existing TypeDefs |
| `archiveInstanceStore` | a list of new metadata instances (Entities, Relationships and Classifications) |

The definition of the connector interface for these connectors is
defined in the `repository-services-api` module
in the [org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore) Java package.

## Example Implementations

Implementations of this type of connector is located in the
[adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh } module.

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

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

## Writing the Connector



--8<-- "snippets/abbr.md"
