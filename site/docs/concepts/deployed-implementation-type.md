---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Deployed Implementation Type

A *deployed implementation type* is an entity that describes a type of technology that is deployed in an organization's IT landscape.  Its purpose is to describe how technology of this type should be governed and the resources available to do so.  For example:

* An instance of this technology is likely to be catalogued in the open metadata ecosystem using an [asset](/concepts/asset).  The deployed implementation type can define the subtype of the asset to use.  It is also possible to define a template for creating the asset and associate it with the deployed implementation type.
* The governance action processes, governance services and connectors that support this type of technology can be identified.


## File Type

A *file type* is a type of *deployed implementation type* that describes a type of file.  It includes the file extension for the type of file to allow matching of a file's full name to a specific file type.  Again the file type links to templates and resources for processing files of this type.



--8<-- "snippets/abbr.md"
