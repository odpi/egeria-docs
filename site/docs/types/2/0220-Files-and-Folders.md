---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0220 Files and Folders

A metadata catalog typically contains information about the data files that can be processed and their location.   Files and folders describe physical files and how they are organized on the file system.

## DataFile

`DataFile` catalogs a physical file.  It inherits from [`DataStore`](/egeria-docs/types/2/0210-Data-Stores) to declare that it is a physical artifact.  There are subtypes for `DataFile` that identify the format of the file:

- `CSVFile` contains comma-separated values.
- `AvroFile` is organized according to the [Apache Avro](https://avro.apache.org) specification.
- `JSONFile` is encoded using [JavaScript Object Notation (JSON)](https://www.json.org/json-en.html).


## FileFolder

A `Filefolder` represents a folder or directory used to group related files together.`

![UML](0220-Files-and-Folders.svg)


## FolderHierarchy

`FolderHierarchy` links `FileFolder` elements together to show a hierarchical organization.

## NestedFile

`NestedFile` links a file to a folder.

## LinkedFile

Files can also have a symbolic link (`LinkedFile`) to a element to show that it logically belongs to the other content in the element.

## DataFolder

`DataFolder` is a special case of `Filefolder` for cataloguing directories that are contain a collection of data.  The files and nested folders within it collectively make up the data content.  They are not individually catalogued.

## Hierarchical file structures

The diagram below illustrates the structure of a file system.

The [`FileSystem`](/egeria-docs/types/0/0056-Resource-Managers) is typically a [Software Capability](/egeria-docs/types/0/0042-Software-Capabilities).
The root folders (of type `FileFolder`) are connected to it using the
[`ServerAssetUse`](/egeria-docs/types/0/0045-Servers-and-Assets) relationship.
Beneath that are `FileFolder`s with `DataFile`s nested beneath them.
 

![File system structure](0220-Files-and-Folders-Example.png)

--8<-- "snippets/abbr.md"