
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your files

Files are everywhere in an organization's data landscape - extracts, exports, configuration, logs, source code, documents, images and more, spread across file systems, shared drives and cloud storage.  Unlike a database, a file system has no catalog of its own: a directory listing gives you names and sizes, but nothing about what a file actually contains or why it matters.

Egeria's *file connectors* close that gap.  They can:

* **Survey** a file, or a folder (and everything nested underneath it), to build a picture of what is there - counts and sizes of files, and increasingly, *what kind* of files they are - and capture that picture as a survey report.
* **Classify** each file against Egeria's file reference data, matching its name or extension to a file type, and from there to the kind of open metadata asset and technology it represents.  This is what turns "a file called `readme.md`" into "a `README File` - a `Document`, encoded in Markdown".
* **Catalog** files and folders as open metadata assets, keeping them synchronized as files are added, changed or removed.

Because Egeria already knows what several hundred common file names and extensions mean, it can tell you a great deal about a folder full of unfamiliar files before anyone opens a single one of them.


## Understanding file content through Egeria's file reference data

A file's name or extension is usually the best clue available to what it contains - `.csv` files hold tabular data, `pom.xml` is a Maven build file, `README.md` documents the directory it sits in.  Egeria packages this knowledge as [*file type*](/concepts/file-type) reference data: several hundred entries mapping a file name or extension to:

* A **file type** - a human-readable classification such as *CSV File*, *README File* or *Personal Information Exchange File* - together with its **encoding** (for example `CSV`, `XML`, `JSON`, `PDF`) where that is known.
* An **asset sub-type name** - the more specific open metadata type the file should be catalogued as, such as `CSVFile`, `Document`, `PropertiesFile`, `SpreadsheetFile` or `KeystoreFile`.
* A **deployed implementation type** - the broader category of technology the file represents, such as *Data File*, *Program File*, *Archive File* or *Log File*.

The reference data is looked up in two steps: first by exact **file name** (so special files like `pom.xml`, `Dockerfile`, `LICENSE` or `.gitignore` are recognized regardless of any extension), and only if that doesn't match, by **file extension**.  A handful of examples from the full table:

| File name / extension | File Type                            | Encoding | Deployed Implementation Type |
|------------------------|---------------------------------------|----------|-------------------------------|
| `pom.xml`              | Apache Maven Build File               | XML      | Program File                  |
| `README.md`            | README File                           | Markdown | Data File                     |
| `.csv`                 | CSV File                              | CSV      | Data File                     |
| `.pdf`                 | Portable Document Format (PDF) File   | PDF      | Data File                     |
| `.p12` / `.pfx`        | Personal Information Exchange File    | PKCS#12  | Data File                     |
| `.parquet`             | Parquet File                          | Parquet  | Data File                     |
| `.py`                  | Python Program File                   |          | Program File                  |

See [File Type](/concepts/file-type) for the complete list, covering documents, spreadsheets, images, audio, video, source code, scripts, archives, keystores, logs and Egeria's own configuration and archive files.  Because this reference data lives in the open metadata ecosystem itself (not hard-coded into a connector), it can be extended - if your organization has its own special file names or extensions that carry meaning, they can be added as further valid values.


### How the survey and cataloguing connectors use it

This reference data isn't just for browsing - it is applied automatically wherever Egeria looks at a file:

* When the **File Survey Service** examines a single file, it uses the file reference data (via the *FileClassifier*) to produce an *Extract File Properties* annotation.  Alongside the physical attributes visible through the file system (size, timestamps, read/write/execute permissions, whether it's a symbolic link or hidden), this annotation records the file's classified **File Type**, **Deployed Implementation Type** and **Asset Type Name**.
* When the **Folder Survey Service** examines a folder, it classifies every file it finds and rolls the results up into a set of profile annotations - so instead of reading through hundreds of file names yourself, you get a breakdown of what's actually in the folder:

    * *Profile File Extensions* - a count of occurrences of each file extension found.
    * *Profile File Types* - the same files, grouped by their classified file type.
    * *Profile Asset Types* - grouped by the open metadata asset type they would be catalogued as.
    * *Profile Deployed Implementation Types* - grouped by the broader technology category (Data File, Program File, Archive File, and so on).
    * *Missing File Reference Data* - a list of the files that **couldn't** be classified.  This doubles as a to-do list: if any of them turn out to be significant, the reference data can be extended to recognize them next time.

  These, together with basic counts (*Capture File Counts* - total files, subdirectories, readable/writable/executable/hidden/symbolic-link counts) are recorded as [annotations](/frameworks/osf/overview) on the survey report for the folder.
* The **Data Files Monitor** and **Data Folder Monitor** integration connectors use the same classification when they catalogue files: the file type, encoding, asset type and deployed implementation type it resolves to become properties of the resulting `DataFile` or `DataFolder` asset, so the classification is preserved in open metadata, not just in the survey report.

??? example "Example annotations from surveying a folder"
    ```json
    {
      "class": "ResourcePhysicalStatusAnnotation",
      "annotationType": "Extract File Properties",
      "summary": "Extract properties from the file.",
      "explanation": "Extract the properties that visible through the standard File interface and classify the file using reference data.",
      "analysisStep": "Measure Resource",
      "size": 4021,
      "resourceProperties": {
        "File Name": "README.md",
        "File Extension": "md",
        "Open metadata type name for asset": "Document",
        "File Type": "README File",
        "Deployed Implementation Type": "Data File",
        "Readable file?": "true",
        "Writeable file?": "true",
        "Executable file?": "false",
        "Hidden file?": "false"
      }
    }
    ```
    ```json
    {
      "class": "ResourceProfileAnnotation",
      "annotationType": "Profile Deployed Implementation Types",
      "summary": "Iterate through files under a directory (folder) and count each potential deployed implementation type if they were to be catalogued in open metadata.",
      "explanation": "The deployed implementation type reflects the technology employed within this resource.  The deployed implementation type is defined as reference data in Egeria.",
      "analysisStep": "Profiling Associated Resources",
      "valueCount": {
        "Data File": 128,
        "Program File": 34,
        "Archive File": 6,
        "Log File": 2
      }
    }
    ```

<!-- SCREENSHOT PLACEHOLDER: file-survey-report-annotations.png - the classification-based annotations produced by a Folder survey, as shown against the asset in the Egeria UI. -->
*(Screenshot to follow: the survey report and its file-classification annotations, as displayed against the surveyed folder in the Egeria UI.)*


## File Surveys

The file survey connectors contain the implementation of four [survey action services](/concepts/survey-action-service) that extract and report on files and folders.  The connectors are provided by the Egeria community.

* **Folder Survey Service** - analyses the files nested in a folder.  The depth of the survey is controlled by the `analysisLevel` request parameter:

    * `TOP_LEVEL_ONLY` (the default) produces summary statistics for the top-level directory only.
    * `ALL_FOLDERS` produces statistics for the top-level directory and all subdirectories.
    * `TOP_LEVEL_AND_FILES` produces statistics for the top-level directory and classifies all the files found directly within it.
    * `ALL_FOLDERS_AND_FILES` produces statistics for all directories and classifies all files, at every level.

* **File Survey Service** - extracts properties about a single file and classifies it using Egeria's file reference data, as described above.

* **CSV Survey Service** - analyses the internals of a CSV file to determine the schema (column structure) and to profile the data in each column.

* **Parquet Survey Service** - analyses the footer of an Apache Parquet file to determine the schema and to profile the data in each column.  See [Working with Apache Parquet files](#working-with-apache-parquet-files).


## Working with Apache Parquet files

[Apache Parquet](https://parquet.apache.org/) is a column-oriented file format that is widely used to store data for analytics.  A Parquet file describes itself: it ends with a *footer* where the software that wrote the file records the schema of the data, how the rows are divided into *row groups*, how the values are compressed and encoded, and statistics about the values in each column.

Egeria uses the footer to describe a Parquet file without reading the data in it.  This means that:

* describing a file takes the same time whatever its size;
* the description is available for files written to any version of the Parquet format, using any encoding and any compression algorithm; and
* no Parquet, Hadoop or compression libraries are needed.

### Cataloguing Parquet files

A file with a file extension of `.parquet` is recognized by the file reference data as a *Parquet File*.  The connectors that catalogue files create a [*ParquetFile*](/types/2/0220-Files-and-Folders/#parquetfile-entity) asset for it, with a deployed implementation type of *Parquet Data File*.  The asset is created from the *Parquet Data File* template in the [Core Content Pack](/content-packs/core-content-pack/overview), which gives it a connection to the Parquet File Store connector.

### Surveying Parquet files

The `survey-parquet-file` survey is the survey listed for the *Parquet Data File* technology type.  It has four analysis steps, and the `finalAnalysisStep` request parameter can be used to stop the survey early.

| Analysis step | Annotation | What is recorded |
|:--------------|:-----------|:-----------------|
| Check Asset | | Checks that the asset is a *ParquetFile* with a connection to the Parquet File Store connector. |
| Measure Resource | *Extract File Properties* | The properties of the file that are visible through the file system.  This is the annotation that the File Survey Service produces. |
| Measure Resource | *Extract Parquet File Properties* | The number of rows, row groups and columns; the compressed and uncompressed size of the data; the software that wrote the file; and the features of the Parquet format that the file uses.  These show what a reader needs to support in order to read the file. |
| Schema Extraction | *Extract Schema From Footer* | The number of columns and their names.  A *TabularColumn* is attached to the asset's schema type for each top-level column, with its name, position, data type and whether it is nullable.  If the asset already has a schema, matching columns are updated, new columns are added, and columns that are no longer in the file are archived. |
| Profile Data | *Profile Column From Statistics* | For each column that holds values: the smallest and largest values; the number of values, nulls and distinct values; its compressed and uncompressed size; and how the values are stored. |

The last step also counts how many times each value occurs in a top-level column, provided the column has no more than 100 different values.  This is intended for columns that hold codes or categories.  It is the only part of the survey that reads the data in the file.

!!! info "What to expect from the column profiles"
    * The smallest, largest and distinct values come from the statistics that the writer of the file chose to save.  They are left out if the writer did not save them, or saved them in a form that is known to be unreliable.
    * A column that contains nested data (an array, map or structure) is catalogued as one column, with a data type that describes its structure.  It has a profile for each of the nested columns that hold values.
    * Counting the values needs the DuckDB JDBC driver, which is included in the OMAG Server Platform.  Without it, the survey completes without the counts and logs message `SURVEY-ACTION-SERVICE-0007`.
    * Columns that are encrypted are identified, and have no statistics.  A file with an encrypted footer can not be described.

### Reading the data in Parquet files

The Parquet connectors read the rows in a file through the [DuckDB](https://duckdb.org/) JDBC driver, which has a complete implementation of the Parquet format.  The driver is included in the OMAG Server Platform.  In a runtime without the driver, the connectors still describe the file, but a request to read a row fails with the `PARQUET-FILE-CONNECTOR-400-005` exception.  The connectors do not write to Parquet files.

A Parquet file can also be catalogued as a [tabular data set](/concepts/tabular-data-set) rather than as a file.  This is for consumers that are interested in the table of data, and not in how it is stored.  The Core Content Pack has a template for each of these deployed implementation types:

* *Parquet Tabular Data Set* - a single Parquet file.  The `directoryPathName` and `tableName` configuration properties identify the file, which is called `<tableName>.parquet`.  The optional `tableDescription` configuration property describes the table.
* *Parquet Tabular Data Set Collection* - a directory of Parquet files, identified by the `directoryPathName` configuration property.  Each file in the directory is a table, named after the file.

These are the same configuration properties as are used by the equivalent connectors for CSV files.

### Parquet files in data sharing hubs

The [Liskov Data Sharing Hub Manager](/patterns/harvest-and-publish/overview/#the-liskov-data-sharing-hub-manager) keeps Parquet files catalogued and surveyed, and adds their columns to the data dictionary of a [data sharing hub](/concepts/data-sharing-hub).  This applies to a Parquet file that is a member of the hub, and to the Parquet files catalogued from a directory that is a member.  The files in a directory are matched to it using their path names - see [File System Normalization](/features/file-system-normalization/overview).


## Connectors for working with Files

Files provide storage for many types of data.  They are organized into folders (also known as directories on some operating systems).  Some connectors work with any type of file.  Other connectors are able to understand the content of specific types of file formats and so these connectors are organized by file type.

### Any type of File

* The [Basic File Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector/README.md#basic-file-connector){ target=gh } provides support to read and write to a file using the Java File object.
* The [Move Copy File Provisioning Governance Action Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors/docs/move-copy-file-provisioning-governance-action-service.md){ target=gh } moves or copies files from one location to another and maintains the lineage of the action.

### File Folders (Directories)

* The [Basic Folder Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/basic-file-connector/README.md#basic-folder-connector){ target=gh } is for accessing the files within a folder (directory).
* The [Data Files Monitor Integration Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors/README.md#data-files-monitor-integration-connector){ target=gh } maintains a `DataFile` asset for each file in the directory (or any subdirectory), classified using the file reference data described above.  When a new file is created, a new DataFile asset is created.  If a file is modified, the lastModified property of the corresponding DataFile asset is updated.  When a file is deleted, its corresponding DataFile asset is also deleted (or archived if it is still needed for lineage).
* The [Generic Folder Watchdog Governance Action Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/governance-action-connectors/docs/generic-folder-watchdog-governance-action-service.md){ target=gh } listens for changing `DataFile` assets linked to a specified `FileFolder` element and initiates governance actions when specific events occur. This may be for files directly linked to the folder or located in sub-folders.

### Data Folders

* The [Data Folder Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/data-folder-connector/README.md){ target=gh } is for accessing data that is stored as a number of files within a folder (directory).
* The [Data Folder Monitor Integration Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors/README.md#data-folder-monitor-integration-connector){ target=gh } maintains a `DataFolder` asset for the directory.  The files and directories underneath it are assumed to be elements/records in the DataFolder asset and so each time there is a change to the files and directories under the monitored directory, it results in an update to the lastModified property of the corresponding DataFolder asset.

### CSV Files

* The [CSV File Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/csv-file-connector/README.md){ target=gh } is able to retrieve data from a Comma Separated Values (CSV) file where the contents are stored in logical columns with a special character delimiter between the columns.

### Parquet Files

* The [Parquet File Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/parquet-file-connector/README.md){ target=gh } describes the contents of an Apache Parquet file from its footer, and reads the rows of data in it.
* The [Parquet Tabular Data Set Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/parquet-file-connector/README.md#parquet-tabular-data-set-connector){ target=gh } reads a Parquet file that is catalogued as a tabular data set.
* The [Parquet Tabular Data Set Collection Connector :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors/parquet-file-connector/README.md#parquet-tabular-data-set-collection-connector){ target=gh } reads a directory of Parquet files as a collection of tabular data sets.
* The [Parquet File Survey Service :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/file-survey-connectors/README.md#parquet-file-survey-service){ target=gh } catalogues the columns in a Parquet file and profiles the data in them.


## Related information

* [File System Normalization](/features/file-system-normalization/overview) - how directories and files are catalogued under a canonical path name.
* [File Type](/concepts/file-type) - the full list of file names and extensions recognized by Egeria's reference data.
* [Deployed Implementation Type](/concepts/deployed-implementation-type) - the broader technology categories that file types map to.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports and annotations generally.

--8<-- "snippets/abbr.md"
