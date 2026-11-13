<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Files Content Pack

The *FilesContentPack* contains the reference data, templates, connector definitions and governance services for working with files and directories (folders) on a file system.  It lets you catalog the files in a directory and keep that catalog up to date as files come and go, survey a directory or file to understand what it contains, and move, copy and delete files while keeping their catalog entries and lineage correct.  The connectors it configures are supplied in the *omag-server-platform* distribution.

The content pack is found in the `FilesContentPack.omarchive` file in the `content-packs` directory of the distribution.  It depends on the [Core Content Pack](/content-packs/core-content-pack/overview), which supplies the file technology types, the file survey services and the *EgeriaWatchdog* engine.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module, and the connectors are in the [files-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors){ target=gh } module.

## How the pieces fit together

A directory can be described in two ways.  A *File System Directory* is a *FileFolder* asset whose files are each catalogued as assets in their own right.  A *Data Folder* is a *DataFolder* asset whose files are treated as the records of a single data source, so only the folder is catalogued.

Running *FileDirectory::CreateAsCatalogTarget* creates a *FileFolder* asset from its template and attaches it as a [catalog target](/concepts/catalog-target) of the *FilesCataloguer* integration connector.  From then on, the cataloguer maintains an asset for each file in the directory and its subdirectories, using the [file type](/concepts/file-type) reference data in this pack to choose the asset type and properties from each file's name and extension.  For a data folder, the *MaintainLastUpdateDate* connector keeps the folder's last update time in step with the activity in the directory.

The survey engine gives a one-off, in-depth view of a directory or file, recorded as a [survey report](/concepts/survey-report) rather than as catalog entries.  The *Create and Survey* processes create the asset, run the survey and print out the report in one step.

Three further connectors are pre-configured to catalog the directories of Egeria's own runtime: the `content-packs` directory, the `secrets` directory and the `loading-bay/sample-data` directory.

## Reference data

The pack defines the reference data used to recognise files: 115 file types, 107 file extensions and 14 specific file names (such as `pom.xml`, `build.gradle` and `Dockerfile`), linked to each other and to the technology types defined in the Core Content Pack.  These are listed under [file type](/concepts/file-type).  It also defines 10 annotation types used in the file and folder survey reports.

## Technology types and templates

The technology types themselves are defined in the Core Content Pack.  This pack adds a template, keyed by file system name and path name, for each of them.

| Technology type | Template creates | Qualified name |
|---|---|---|
| File System Directory | A *FileFolder* asset | `FileFolder::~{fileSystemName}~:~{directoryPathName}~` |
| Data Folder | A *DataFolder* asset | `DataFolder::~{fileSystemName}~:~{directoryPathName}~` |
| Data File | A *DataFile* asset | `DataFile::~{fileSystemName}~:~{filePathName}~` |
| CSV Data File, Avro Data File, JSON Data File, Parquet Data File, Spreadsheet Data File, XML Data File | A *CSVFile*, *AvroFile*, *JSONFile*, *ParquetFile*, *SpreadsheetFile* or *XMLFile* asset | `CSVFile::~{fileSystemName}~:~{filePathName}~` and so on |
| Document File | A *Document* asset | `Document::~{fileSystemName}~:~{filePathName}~` |
| Audio Data File, Video Data File, 3D Image Data File, Raster Data File, Vector Data File | An *AudioFile*, *VideoFile*, *ThreeDImageFile*, *RasterFile* or *VectorFile* asset | `AudioFile::~{fileSystemName}~:~{filePathName}~` and so on |
| Archive File, Keystore File | An *ArchiveFile* or *KeyStoreFile* asset | `ArchiveFile::~{fileSystemName}~:~{filePathName}~` and so on |
| Source Code File, Build Instruction File, Executable File, Script File, Properties File, YAML File | A *SourceCodeFile*, *BuildInstructionFile*, *ExecutableFile*, *ScriptFile*, *PropertiesFile* or *YAMLFile* asset | `SourceCodeFile::~{fileSystemName}~:~{filePathName}~` and so on |

The Core Content Pack has a second set of templates for *Data File* and *Data Folder*, keyed by OpenLineage namespace and resource name, for files in object stores.  The templates are described further in the [Template Catalog](/catalog-templates).

## Governance action processes

| Process | Steps |
|---|---|
| `FileDirectory::CreateAsCatalogTarget` | `create-file-folder`, then `catalog-file-folder` to attach the *FileFolder* asset to the files cataloguer. |
| `FileDirectory:CreateAndSurvey` | `create-file-folder`, then `survey-all-folders-and-files`, then `print-survey-report`. |
| `FileDirectory:DeleteAsset` | `delete-file-folder`. |
| `DataDirectory::CreateAsCatalogTarget` | `create-data-folder`, then `catalog-data-folder` to attach the *DataFolder* asset to the cataloguer. |
| `DataDirectory:CreateAndSurvey` | `create-data-folder`, then `survey-folder-and-files`, then `print-survey-report`. |
| `DataDirectory:DeleteAsset` | `delete-data-folder`. |

The *DataDirectory::CreateAsCatalogTarget* process is registered against the *File System Directory* technology type rather than *Data Folder*, so its solution component is called *Create and catalog Governance Action Process for File System Directory* and its first step is labelled *Create the FileFolder entity*, even though it creates a *DataFolder*.

## Integration connectors

The pack defines the *FilesIntegrationGroup* (`Egeria:IntegrationGroup:Files`), a dynamic [integration group](/concepts/integration-group) that runs in an [integration daemon](/concepts/integration-daemon).

| Connector | Runs as | Purpose |
|---|---|---|
| GeneralFilesMonitorIntegrationConnector | `FilesCataloguer` (user `filescatnpa`, refreshes every 60 minutes) | Catalogs the files found under the directories attached as catalog targets. |
| MaintainDataFolderLastUpdateDateIntegrationConnector | `MaintainLastUpdateDate` (user `datafoldercatnpa`, every 60 minutes) | Maintains the last update time of a *DataFolder* asset from the file activity in its directory. |
| ContentPacksMonitorIntegrationConnector | `ContentPacksCataloguer` (user `contentpackcatnpa`, every 60 minutes) | Catalogs the open metadata archive files in the `content-packs` directory, and any other directory attached as a catalog target, using the information in each archive's header. |
| SecretsStoreMonitorIntegrationConnector | `SecretsStoreCataloguer` (user `secretsstorecatnpa`, every 60 minutes) | Catalogs the secrets stores in the `secrets` directory, and any other directory attached as a catalog target. |
| SampleDataFilesMonitorIntegrationConnector | `SampleDataCataloguer` (user `sampledatacatnpa`, every 840 minutes) | Catalogs the files in the `loading-bay/sample-data` directory, used for demonstrations. |

## Governance engines

| Governance engine | Request type | Governance service | Purpose |
|---|---|---|---|
| *FileSurvey* - Files and Directories Survey Engine | `survey-folder` | Folder (directory) Survey Service | Summarizes the files in a directory. |
| | `survey-folder-and-files` | Folder (directory) Survey Service | Characterises each file in a directory. |
| | `survey-all-folders` | Folder (directory) Survey Service | Summarizes the files in a directory and the nested directories beneath it. |
| | `survey-all-folders-and-files` | Folder (directory) Survey Service | Characterises each file in a directory and the nested directories beneath it. |
| | `survey-data-file` | Data File Survey Service | Describes the characteristics of a single file, without looking inside it. |
| | `survey-csv-file` | CSV File Survey Service | Describes a CSV file, extracting its schema and profiling its data. |
| *FileGovernance* - Files and Directories Governance Engine | `copy-file`, `move-file`, `delete-file` | File {move, copy, delete} Governance Action Service | Copies, moves or deletes a file and maintains its catalog entries and lineage. |
| | `create-file-folder`, `create-data-folder` | Create Asset Governance Service | Creates the directory's asset from its template. |
| | `catalog-file-folder`, `catalog-data-folder` | Add Catalog Target to Asset Governance Service | Attaches the asset to the appropriate integration connector as a catalog target. |
| | `delete-file-folder`, `delete-data-folder` | Delete Asset Governance Service | Deletes an asset that was created by a template. |
| | `watch-for-new-files-in-folder` | New Files Watchdog Action Service | Also registered with *EgeriaWatchdog* (see below). |
| *EgeriaWatchdog* - Egeria Watchdog Engine (from the Core Content Pack) | `watch-for-new-files-in-folder` (`watch-nested-in-folder`) | New Files Watchdog Action Service | Listens for new file assets in a directory and starts the appropriate governance actions. |

The survey services themselves are defined in the Core Content Pack.  The governance engines run in an [engine host](/concepts/engine-host).

## Graphs

The solution blueprint for the content pack shows its connectors, governance action types and processes, and the technologies they work with.

--8<-- "snippets/blueprints/content-packs/files-content-pack-solution-blueprint-mermaid-graph.md"

The technology type reports below, taken from Egeria's quickstart, show how the templates, governance action processes, integration connectors and governance action types are linked to each technology type.

??? info "Technology type report for File System Directory"
    --8<-- "snippets/technology-types/file-system-directory-technology-report-mermaid-graph.md"

??? info "Technology type report for CSV Data File"
    --8<-- "snippets/technology-types/csv-data-file-technology-report-mermaid-graph.md"

!!! summary "Usage"
    The Files Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart.  For other deployments, load it into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  Then run *FileDirectory::CreateAsCatalogTarget* with the file system name and directory path name to start cataloguing a directory, or *FileDirectory:CreateAndSurvey* to survey it.

    [Leveraging your files](/egeria-solutions/leveraging-files/overview) walks through surveying and cataloguing files step by step.

--8<-- "snippets/abbr.md"
