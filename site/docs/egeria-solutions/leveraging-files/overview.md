
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

The file survey connectors contain the implementation of three [survey action services](/concepts/survey-action-service) that extract and report on files and folders.  The connectors are provided by the Egeria community.

* **Folder Survey Service** - analyses the files nested in a folder.  The depth of the survey is controlled by the `analysisLevel` request parameter:

    * `TOP_LEVEL_ONLY` (the default) produces summary statistics for the top-level directory only.
    * `ALL_FOLDERS` produces statistics for the top-level directory and all subdirectories.
    * `TOP_LEVEL_AND_FILES` produces statistics for the top-level directory and classifies all the files found directly within it.
    * `ALL_FOLDERS_AND_FILES` produces statistics for all directories and classifies all files, at every level.

* **File Survey Service** - extracts properties about a single file and classifies it using Egeria's file reference data, as described above.

* **CSV Survey Service** - analyses the internals of a CSV file to determine the schema (column structure) and to profile the data in each column.


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


## Related information

* [File Type](/concepts/file-type) - the full list of file names and extensions recognized by Egeria's reference data.
* [Deployed Implementation Type](/concepts/deployed-implementation-type) - the broader technology categories that file types map to.
* [Open Survey Framework](/frameworks/osf/overview) - background on survey reports and annotations generally.

--8<-- "snippets/abbr.md"
