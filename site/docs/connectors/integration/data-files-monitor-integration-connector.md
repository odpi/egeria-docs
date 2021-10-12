---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Data Files Monitor Integration Connector

??? info "Connector details"
    An [integration connector](/egeria-docs/connectors/integration-connector), hosted by the [Files Integrator OMIS](/egeria-docs/services/omis/file-integrator/overview), running on an [integration daemon](/egeria-docs/concepts/integration-daemon).

    - Source: [files-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors){ target=gh }
    - Connector archive: `files-integration-connectors.jar`

The data files monitor integration connector monitors changes in a file directory (folder) and updates the open metadata repository/repositories to reflect the changes to both the files and folders underneath it.

Specifically:

- A [`DataFile`](/egeria-docs/types/2/0220-files-and-folders/#datafile) asset is created and then maintained for each file in the folder (or any sub-folder).
- When a new file is created, a new `DataFile` asset is created.
- If a file is modified, the `lastModified` property of the corresponding `DataFile` asset is updated.
- When a file is deleted, its corresponding `DataFile` asset is either:
    - Archived: this means the asset is no longer returned on standard asset catalog searches, but it is still visible in [lineage graphs](/egeria-docs/concepts/lineage). This is the default behavior.
    - Deleted: this means that all metadata associated with the data file is removed. Only use this option if lineage is not important for these file.
- A [`FileFolder`](/egeria-docs/types/2/0220-files-and-folders) metadata asset for the monitored folder is created when the first file is catalogued, if it does not already exist.

## Configuration

![Operation of the data files monitor integration connector](data-files-monitor-integration-connector.svg)

This connector uses the [Files Integrator OMIS](/egeria-docs/services/omis/files-integrator/overview) running in the [integration daemon](/egeria-docs/concepts/integration-daemon).

Following is its connection definition to use on the [administration commands that configure the Files Integrator OMIS](/egeria-docs/guides/admin/servers/configuring-an-integration-daemon/#configure-the-integration-services):

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="10 12-15"
    {
      "connection": {
        "class": "Connection",
        "connectorType": {
          "class": "ConnectorType",
          "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFilesMonitorIntegrationProvider"
        },
        "endpoint": {
          "class": "Endpoint",
          "address": "{{folderName}}"
        },
        "configurationProperties": {
          "templateQualifiedName": "{{templateQualifiedName}}",
          "allowCatalogDelete": ""         
        }
      }
    }
    ```

    - Replace `{{folderName}}` with the path name of the folder where the files will be located.
    - The `configurationProperties` are optional and are used to override the connector's default behavior:
        - If `templateQualifiedName` is present in the configuration properties then `{{templateQualifiedName}}` must be set to the qualified name of a [`DataFile`](/egeria-docs/types/2/0220-Files-and-Folders/#datafile) metadata element that should be used as a template for the catalog entry for new files discovered by this connector. The base properties, schema, connection, classifications and any other attachments connected to the template are copied to the new metadata element for the file. (See [templated cataloging](../cataloging-assets/templated-cataloging.md) for more information on the use of templates.)
        - If `allowCatalogDelete` is present in the configuration properties then the metadata element for a file is deleted when the file is deleted. If this property is not in the configuration properties, then the metadata element is archived (by adding the [Memento](/egeria-docs/types/0/0010-Base-Model/#memento) classification to its entry). The archived element is no longer returned in standard catalog queries, but it is still visible in [lineage](/egeria-docs/concepts/lineage). Do not set `allowCatalogDelete` if lineage of these files is important.

??? education "Further information"
    This connector is configured in the `exchangeDL01` integration daemon server in the
    [open metadata labs](/egeria-docs/education/open-metadata-labs)

--8<-- "snippets/abbr.md"
