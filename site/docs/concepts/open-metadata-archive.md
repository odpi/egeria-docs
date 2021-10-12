---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata Archive

An *open metadata archive* is a document containing open metadata [type definitions](/egeria-docs/introduction/key-concepts/#metadata-types) and [instances](/egeria-docs/introduction/key-concepts/#metadata-instances).

The open metadata archive has two types:

- A **content pack** containing reusable definitions that are generally useful. They may come from the Egeria community or third parties.
- A **metadata export** containing an export of metadata from a repository. They are used to transfer metadata between repositories that are not connected to the same [cohort](/egeria-docs/services/omrs/cohort).

## Structure

The logical structure of an open metadata archive is as follows:

![Logical structure of an open metadata archive](open-metadata-archive-structure.png)

Instances are linked together as follows:

- Entities are stored as `EntityDetail` structures.
- Relationships are stored as `Relationship` structures and link to their entities through the embedded `EntityProxy` structure.
- The entities will include their classifications; however, for classifications that are attached to entities that are not included in the archive, they are stored in an `ClassificationEntityExtension` structure.

![Instance structures in an open metadata archive](open-metadata-archive-instances.png)

Typically, open metadata archives are encoded in JSON format and stored in a file; however, both the format and storage method can be changed by changing the [open metadata archive connector](/egeria-docs/connectors/open-metadata-archive-store-connector).

!!! example "Example of the header from the [Cloud Information Model archive :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-archives/design-model-archives){ target=gh }"
    ```json
    {
      "class":"OpenMetadataArchive",
      "archiveProperties":
          {
              "class":"OpenMetadataArchiveProperties",
              "archiveGUID":"9dc75637-92a7-4926-b47b-a3d407546f89",
              "archiveName":"Cloud Information Model (CIM) glossary and concept model",
              "archiveDescription":"Data types for commerce focused cloud applications.",
              "archiveType":"CONTENT_PACK",
              "originatorName":"The Cloud Information Model",
              "originatorLicense":"Apache 2.0",
              "creationDate":1570383385107,
              "dependsOnArchives":["bce3b0a0-662a-4f87-b8dc-844078a11a6e"]
          }, 
       "archiveTypeStore":{},
       "archiveInstanceStore":{}
    }
    ```

## Processing

Open metadata archives are introduced into the server through the admin services either:

1. provided as part of the contents of the server's configuration document, or
2. through the operational command that added the archive directly into the running server's repository.

![Processing of an open metadata archive](open-metadata-archive-processing.png)

The archive is passed to the repository services' operational services, which in turn passes it on to the [archive manager](/egeria-docs/services/omrs/archive-manager). Type information is passed to the [repository content manager](../services/omrs/repository-content-manager.md).

Both the types and instances are passed to the local repository (if there is one).

The archive loads in the following order:

1. Attribute Type Definitions (`AttributeTypeDef`s) from the type store, through `verifyAttributeTypeDef()` and then `addAttributeTypeDef()`:
    1. PrimitiveDefs
    2. CollectionDefs
    3. EnumDefs
2. New Type Definitions (`TypeDef`s) from the type store, through `verifyTypeDef()` and `addTypeDef()`:
    1. EntityDefs
    2. RelationshipDefs
    3. ClassificationDefs
3. Updates to types (`TypeDefPatch`es)
4. Instances, as reference copies:
    1. Entities
    2. Relationships
    3. Classifications

!!! tip "Cohort propagation"
    If the server is connected to the cohort, the new content is sent as notifications to the rest of the cohort.

!!! education "Further information"
    More information about open metadata archives can be found in the [open-metadata-archives :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-archives){ target=gh } module.

    In addition, these articles may be of interest:

    - [Configuring an open metadata archive in an OMAG Server](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-store/#configure-metadata-to-load-on-startup)
    - [Adding an open metadata archive to a running OMAG Server](/egeria-docs/guides/admin/servers/configuring-a-metadata-access-store/#add-to-a-running-server)

--8<-- "snippets/abbr.md"
