<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Open Metadata Archive Store Connectors


The definition of the [open metadata archive store connector](/concepts/open-metadata-archive-store-connector) interface is defined in the *repository-services-apis* module in the [org.odpi.openmetadata.repositoryservices.connectors.stores.archivestore :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore){ target=gh } Java package.

Its interface is called [`OpenMetadataArchiveStore` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/OpenMetadataArchiveStore.java){ target=gh }

```java
public interface OpenMetadataArchiveStore
{
    /**
     * Return the contents of the archive.
     *
     * @return OpenMetadataArchive object
     * @throws RepositoryErrorException a problem accessing the archive
     */
    OpenMetadataArchive getArchiveContents() throws RepositoryErrorException;


    /**
     * Set new contents into the archive.  This overrides any content previously stored.
     *
     * @param archiveContents  OpenMetadataArchive object
     */
    void setArchiveContents(OpenMetadataArchive archiveContents);
}
```


The [open metadata archive](/concepts/open-metadata-archive) structure is defined by [`OpenMetadataArchive` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/properties/OpenMetadataArchive.java){ target=gh } in the `properties` sub-package.

There are 3 sections:

| Section | Description |
|---|---|
| `archiveProperties` | an `OpenMetadataArchiveProperties` object that provides details of the source and contents of the archive |
| `archiveTypeStore` | an `OpenMetadataArchiveTypeStore` object with a list of new AttributeTypeDefs (`attributeTypeDefs`), new TypeDefs (`newTypeDefs`) and patches to existing TypeDefs (`typeDefPatches`) |
| `archiveInstanceStore` | an `OpenMetadataArchiveInstanceStore` object with a list of new metadata instances: entities (`entities`), relationships (`relationships`) and classifications (`classifications`) |

The package also contains the following classes that help with writing a connector:

* `OpenMetadataArchiveStoreConnector` - the abstract base class for the connector.  It extends `ConnectorBase` and implements `OpenMetadataArchiveStore` and `AuditLoggingComponent`, so the connector receives an audit log for its messages.
* `OpenMetadataArchiveStoreProviderBase` - the abstract base class for the connector provider.  It extends `OpenConnectorProviderBase`.
* `OpenMetadataArchiveBuilder` - an optional interface for a connector that is able to manage the individual elements of an archive (for example `setArchiveProperties`, `addPrimitiveDef`, `addEntityDef`, `addEntity` and `addRelationship`) rather than receiving the whole archive as a single structure.  Where a connector does not implement this interface, the `OMRSArchiveBuilder` utility in the *repository-services-archive-utilities* module builds the archive in memory and passes it to the connector with `setArchiveContents`.
* `OpenMetadataArchiveCache` - an optional interface for a builder that accumulates the archive contents in memory.

## Example Implementations

Implementations of this type of connector are located in the
[adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh } module:

* `FileBasedOpenMetadataArchiveStoreConnector` in *open-metadata-archive-file-connector* stores an open metadata archive as a single JSON file.  The file name is taken from the network address of the endpoint in its connection, or defaults to `open.metadata.omarchive`.  Properties are written in alphabetical order, and map entries in key order, so writing the same archive contents always produces the same file.
* `DirectoryBasedOpenMetadataArchiveStoreConnector` in *open-metadata-archive-directory-connector* stores an open metadata archive as an organized collection of JSON files within a single directory.  It also implements `OpenMetadataArchiveBuilder`.

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

    ```
    dependencies {
        compileOnly project(':open-metadata-implementation:frameworks:open-connector-framework')
        compileOnly project(':open-metadata-implementation:repository-services:repository-services-apis')
    }
    ```

## Writing the Connector Provider

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

The connector provider for an open metadata archive store connector extends `OpenMetadataArchiveStoreProviderBase`.  For example, `FileBasedOpenMetadataArchiveStoreProvider` passes `EgeriaOpenConnectorDefinition.JSON_FILE_OPEN_METADATA_ARCHIVE_CONNECTOR` and the class name of its connector to the base class.

## Writing the Connector

The connector extends `OpenMetadataArchiveStoreConnector` and implements `getArchiveContents` and `setArchiveContents`.  It typically uses `initialize` to extract the location of the archive from the endpoint in its connection, and the `logRecord` and `logExceptionRecord` methods inherited from `ConnectorBase` to report progress and problems to the audit log.  `getArchiveContents` throws a `RepositoryErrorException` if the archive cannot be read.

--8<-- "snippets/abbr.md"
