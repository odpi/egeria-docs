---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# File Type

A *file type* is similar to [*deployed implementation type*](/concepts/deployed-implementation-type).  It is a reference data value that that describes a type of file.  It links to reference data about the file extensions for the type of file to allow matching of a file's extension to a specific asset type.  Again the file type may link to templates and resources for processing files of this type.

The file type's *preferredValue* can be used to consistently populate the *fileType* attribute of [*DataFile*](/types/2/0220-Files-and-Folders) assets.  This acts as a logical file type.

## Examples of File Types

--8<-- "snippets/content-packs/file-types.md"

--8<-- "snippets/abbr.md"
