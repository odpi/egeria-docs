<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0226 Archive Files

Archive files combine multiple files into a single file.

![UML](0226-Archive-Files.svg)

## ArchiveFile entity

The *ArchiveFIle* entity describes an archive file such as a ZIP file or Jar file.

## ArchiveContents relationship

The *ArchiveContents* relationship links an *ArchiveFile* to a [*Collection*](/types/0/0021-Collections) entity.  The *Collection* entity links to member entities that describe the archive's contents.

--8<-- "snippets/abbr.md"

