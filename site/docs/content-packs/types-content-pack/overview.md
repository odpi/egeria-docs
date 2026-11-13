---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Types Content Pack

The *Open Metadata Types* content pack contains all of the [open metadata type definitions](/types) provided by Egeria: 370 entity types, 208 relationship types and 93 classification types, along with 51 attribute type definitions (such as the primitive types and enumerations) and 76 patches to earlier type definitions.  It contains no metadata instances.

The content pack is found in the `OpenMetadataTypes.omarchive` file in the `content-packs` directory of the distribution.  You do not normally need to load it, since each [OMAG server](/concepts/omag-server) capable of being a [cohort member](/concepts/cohort-member) loads these types automatically on start up.  It is supplied for external utilities, and for servers that do not use the standard Egeria libraries, that need the type definitions in JSON format.  The other content packs supplied with Egeria declare it as a dependency.

This content pack is built by the [open-metadata-types-utility :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-metadata-types-utility){ target=gh } module using the definitions in the [open-metadata-types :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/open-metadata-types){ target=gh } module.

--8<-- "snippets/abbr.md"
