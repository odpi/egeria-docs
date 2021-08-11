---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open metadata archive store connector

The open archive store connector provides a common interface
for managing stores of [open metadata archives](/egeria-docs/concepts/open-metadata-archive).

Its interface is defined in [`OpenMetadataArchiveStore` :material-github:](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/OpenMetadataArchiveStore.java){ target=gh }

The open metadata archive structure is defined by [`OpenMetadataArchive` :material-github](https://github.com/odpi/egeria/blob/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/archivestore/properties/OpenMetadataArchive.java){ target=gh }.

There are 3 sections:

| Section | Description
|---|---|
| `archiveProperties` | provides details of the source and contents of the archive |
| `archiveTypeStore` | a list of new AttributeTypeDefs, new TypeDefs and patches to existing TypeDefs |
| `archiveInstanceStore` | a list of new metadata instances (Entities, Relationships and Classifications) |

An implementations of this type of connector is located in the
[adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-archive-connectors){ target=gh }
module.

!!! education "Further information"
* [Open Metadata Archive Store Connectors in the Connector Catalog](../../../../../open-metadata-publication/website/connector-catalog/runtime-connectors.md)

--8<-- "snippets/abbr.md"
