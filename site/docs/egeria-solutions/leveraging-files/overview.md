---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your files

--8<-- "snippets/work-in-progress.md"


## File Surveys

The file survey connectors contain the implementation of three
[survey action services](https://egeria-project.org/concepts/survey-action-service) that extract and report on files and folders.
The connectors are provided by the Egeria community.

* Folder Survey Service -  *FolderSurveyService* is a survey action service implementation for analysing the files nested in a folder. The depth of the survey is controlled by the analysisLevel request parameter.

    * The default value is 'TOP_LEVEL_ONLY' which produces summary statistics for the top-level directory only.
    * If it is set to 'ALL_FOLDERS' then there are statistics created for the top level directory, and all subdirectories.
    * If it set to 'TOP_LEVEL_AND_FILES' then statistics are created for the top-level directory and all files that are encountered.
    * Finally, if it is set to 'ALL_FOLDERS_AND_FILES' then statistics are created for all directories and files encountered.", "string", "myFile.csv".

* File Survey Service - *File Survey Service* extracts properties about a file.  It then maps these properties to Egeria's file reference data to enable summary statistics to be calculated.

* CSV Survey Service - *CSV File Survey* analyses the internals of a CSV file to determine the schema (column structure) and to profile the data in each column.


### Connectors for working with Files

Files provide storage for many types of data.  They are organizes into folders (also known as directories on some operating systems).  Some connectors work with any type of file.  Other connectors are able to understand the content of specific types of file formats and so these connectors are organized by file type.

#### Any type of File

* The [Basic File Resource Connector](/connectors/resource/basic-file-resource-connector)  provides support to read and write to a file using the Java File object.
* The [Move/Copy File Provisioning Governance Action Service](/connectors/governance-action/move-copy-file-provisioning-governance-action-service)  moves or copies files from one location to another and maintains the lineage of the action.

#### File Folders (Directories)

* The [Basic Folder Resource Connector](/connectors/resource/basic-folder-resource-connector) is for accessing the files within a folder (directory).
* The [Data Files Monitor Integration Connector](/connectors/integration/data-files-monitor-integration-connector) maintains a `DataFile` asset for each file in the directory (or any subdirectory). When a new file is created, a new DataFile asset is created.  If a file is modified, the lastModified property of the corresponding DataFile asset is updated.  When a file is deleted, its corresponding DataFile asset is also deleted (or archived if it is still needed for lineage).
* The [Generic Folder Watchdog Governance Action Service](/connectors/governance-action/generic-folder-watchdog-governance-action-service) listens for changing `DataFile` assets linked to a specified `FileFolder` element and initiates governance actions when specific events occur. This may be for files directly linked to the folder or located in sub-folders.

#### Data Folders

* The [Data Folder Resource Connector](/connectors/resource/data-folder-resource-connector) is for accessing data that is stored as a number of files within a folder (directory).
* The [Data folder Monitor Integration Connector](/connectors/integration/data-folder-monitor-integration-connector) maintains a `DataFolder` asset for the directory.  The files and directories underneath it are assumed to be elements/records in the DataFolder asset and so each time there is a change to the files and directories under the monitored directory, it results in an update to the lastModified property of the corresponding DataFolder asset.

#### CSV Files

* The [CSV File Resource Connector](/connectors/resource/csv-file-resource-connector)  is able to retrieve data from a Comma Separated Values (CSV) file where the contents are stored in logical columns with a special character delimiter between the columns.


--8<-- "snippets/abbr.md"