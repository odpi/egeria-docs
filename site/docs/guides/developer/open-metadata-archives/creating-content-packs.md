<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Creating content packs

A *content pack* is a packaging of one or more metadata elements into an [open metadata archive](/concepts/open-metadata-archive) so that they can be loaded and reused in different organizations.  The archive has an `archiveType` of `CONTENT_PACK` and, by convention, a file name ending in `.omarchive`.

A content pack is built using a Java program called an *archive writer*.  The structure of an archive writer is described in [building open metadata archives](/guides/developer/#building-open-metadata-archives).

## Egeria's content packs

Egeria's own content packs are listed in the [content pack catalog](/content-packs).  They are built by the archive writers in the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module and written to the `content-packs` directory at the top of `egeria.git`, where they are committed and included in the distribution.

* `ContentPackDefinition` is an enum with an entry for each content pack.  It provides the archive's GUID, name, description and file name (for example `CORE_CONTENT_PACK` and `DUCKDB_CONTENT_PACK`).
* Further enums, such as `IntegrationGroupDefinition`, `IntegrationConnectorDefinition`, `GovernanceEngineDefinition`, `GovernanceServiceDefinition`, `RequestTypeDefinition` and the template definitions, describe the elements to add.  Each entry names the `ContentPackDefinition` it belongs to.
* `ContentPackBaseArchiveWriter` (in the `base` package) extends `EgeriaBaseArchiveWriter` from [content-pack-helpers :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/content-pack-helpers){ target=gh }.  It has methods such as `addIntegrationGroups()`, `addIntegrationConnectors()`, `createGovernanceEngines()`, `createGovernanceServices()` and `createRequestTypes()` that add the entries of these enums that belong to the requested content pack.
* There is one archive writer per content pack, for example `CorePackArchiveWriter`, `PostgresPackArchiveWriter` and `DuckDBPackArchiveWriter`.  Each passes the `ContentPackDefinition` values to its superclass constructor, along with the archives it depends on (typically the archive produced by `CorePackArchiveWriter`), and implements `getArchiveContent()`.
* `CorePacksArchivesWriter` has the `main()` method that runs each of the archive writers in turn, writing to the `content-packs` folder.

Running the writers requires the GUID map files (`EgeriaContentPacksGUIDMap.json` and `UsedEgeriaContentPacksGUIDMap.json`) from the top of `egeria.git` to be in the working directory, so that existing elements keep their GUIDs.

## Writing your own content pack

The simplest way to write your own content pack is to extend `EgeriaBaseArchiveWriter`.  Its constructor creates an `OMRSArchiveBuilder` that depends on the open metadata types (plus any additional archives you pass) and a `GovernanceArchiveHelper` (available as `archiveHelper`) for creating the elements.  You implement `getArchiveContent()` and call `writeOpenMetadataArchive()` to build and write the archive.

```java linenums="1"
public class MyContentPackArchiveWriter extends EgeriaBaseArchiveWriter
{
    private static final String archiveGUID        = "...";   // fixed GUID for this archive
    private static final String archiveName        = "MyContentPack";
    private static final String archiveDescription = "Reference data and templates for my organization.";
    private static final String archiveFileName    = "MyContentPack.omarchive";
    private static final Date   creationDate       = new Date(1700000000000L);   // fixed - it becomes the createTime of each element

    public MyContentPackArchiveWriter()
    {
        super(archiveGUID, archiveName, archiveDescription, creationDate, archiveFileName);
    }

    @Override
    public void getArchiveContent()
    {
        // use archiveHelper (GovernanceArchiveHelper) to add elements, for example
        // archiveHelper.addGovernanceZone(...), archiveHelper.addConnectorType(...), archiveHelper.addGlossary(...)
    }

    public static void main(String[] args)
    {
        new MyContentPackArchiveWriter().writeOpenMetadataArchive();
    }
}
```

The `creationDate` must not change between builds because it becomes the `createTime` of every element in the archive, and repositories use it to match an incoming element with the one they already store before comparing version numbers.  The version number of the elements is set by `EgeriaBaseArchiveWriter`, and the `ArchiveVersionStabilizer` keeps the previous version of elements that have not changed since the last time the archive was written.  `writeOpenMetadataArchive()` saves the GUID map after writing the archive.

!!! warning "Fixed values in EgeriaBaseArchiveWriter"
    `EgeriaBaseArchiveWriter` sets the originator (`Egeria Project`), the license (`Apache 2.0`), the version name used in the elements and the GUID map file name (`EgeriaContentPacksGUIDMap.json`) to fixed values.  If you need different values, build your writer directly on `OMRSArchiveWriter`, `OMRSArchiveBuilder` and `SimpleCatalogArchiveHelper` (or `GovernanceArchiveHelper`), whose constructors take these values as parameters.

The [Coco Pharmaceuticals sample archives :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-samples/sample-metadata/coco-metadata-archives){ target=gh } are further examples of archive writers built on `EgeriaBaseArchiveWriter`.

## Loading a content pack

A content pack is loaded into a [metadata access store](/concepts/metadata-access-store) either by adding it to the server's configuration so it is loaded each time the server starts (see [configuring the open metadata archives to load on server startup](/guides/admin/servers/by-section/repository-services-section)), or by [adding it to a running server](/guides/operations/adding-archive-to-running-server).  Loading the same content pack more than once does not create duplicates.

--8<-- "snippets/abbr.md"
