<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


??? example "Example of the header from the [Core Content Pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh }"
    This is the start of `content-packs/CoreContentPack.omarchive`.  The `dependsOnArchives` property lists the GUID of the open metadata types archive (`OpenMetadataTypesArchive`), whose types the content pack's instances use.  The content pack defines no new types, so it has no `archiveTypeStore`; its `archiveInstanceStore` holds lists of `entities`, `relationships` and `classifications` (shown empty here).

    ```json
    {
      "class":"OpenMetadataArchive",
      "archiveProperties":
          {
              "class":"OpenMetadataArchiveProperties",
              "archiveGUID":"09450b83-20ff-4a8b-a8fb-f9b527bbcba6",
              "archiveName":"CoreContentPack",
              "archiveDescription":"Base Connector Types and Categories for connectors from the Egeria project along with metadata valid values, templates, and connectors for the basic types of technology supported by these connectors.",
              "archiveType":"CONTENT_PACK",
              "originatorName":"Egeria Project",
              "originatorLicense":"Apache 2.0",
              "creationDate":1775025949989,
              "dependsOnArchives":["bce3b0a0-662a-4f87-b8dc-844078a11a6e"]
          },
       "archiveInstanceStore":
          {
              "class":"OpenMetadataArchiveInstanceStore",
              "entities":[],
              "relationships":[],
              "classifications":[]
          }
    }
    ```
