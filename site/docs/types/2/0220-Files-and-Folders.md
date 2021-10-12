---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0220 Files and Folders

A metadata catalog typically contains information about the data files
that can be processed and their location.  

Files and folders describe physical files and how they are organized on the file system.

![UML](0220-Files-and-Folders.svg)

The file system is a [Software Server Capability](/egeria-docs/types/0/0042-Software-Server-Capabilities).
The root folders (**FileFolders**) are connected to it using the
[ServerAssetUse](0045-Servers-and-Assets.md) relationship.
Beneath that are **FileFolders** with **DataFiles**
nested beneath them.  Data files can also have a symbolic link (**LinkedFile**) to
a element to show that it logically belongs to the other content in the
element.

There is also a special case of a
**DataFolder** which is a element that is the container of a collection of
data.
The files and nested folders within it collectively make up the data content.
They are not individually catalogued.

The diagram below illustrates the structure.

![File system structure](0220-Files-and-Folders-Example.png)

--8<-- "snippets/abbr.md"