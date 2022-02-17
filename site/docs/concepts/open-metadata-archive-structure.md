<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

The logical structure of an open metadata archive is as follows:

![Logical structure of an open metadata archive](/guides/developer/open-metadata-archives/open-metadata-archive-structure.svg)

--8<-- "docs/guides/developer/open-metadata-archives/open-metadata-archive-header-example.md"

Instances are linked together as follows:

- Entities are stored as `EntityDetail` structures.
- Relationships are stored as `Relationship` structures and link to their entities through the embedded `EntityProxy` structure.
- The entities will include their classifications; however, for classifications that are attached to entities that are not included in the archive, they are stored in an `ClassificationEntityExtension` structure.

![Instance structures in an open metadata archive](/guides/developer/open-metadata-archives/open-metadata-archive-instances.svg)

Typically, open metadata archives are encoded in JSON format and stored in a file; however, both the format and storage method can be changed by changing the [open metadata archive connector](/concepts/open-metadata-archive-store-connector).

--8<-- "snippets/abbr.md"
