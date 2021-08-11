<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Data folder monitor integration connector

???+ info "Connector details"
    An [integration connector](/egeria-docs/connectors/integration-connector),
    hosted by the [Files Integrator OMIS](/egeria-docs/services/omis/file-integrator),
    running on an [integration daemon](/egeria-docs/concepts/integration-daemon).

    - Source: [files-integration-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/integration-connectors/files-integration-connectors){ target=gh }
    - Connector archive: `files-integration-connectors.jar`

## Overview

The data folder monitor integration connector monitor changes in a file directory (folder) and maintains a 
[DataFolder](/egeria-docs/types/2/0220-files-and-folders)
asset for the folder.
The files and directories
underneath it are assumed to be elements/records in the `DataFolder` asset and so each time there is a change to the
files and directories under the monitored directory, it results in an update to the `lastModified` property
of the corresponding `DataFolder` asset.

!!! attention "Assumes the DataFolder asset already exists"
    This connector assumes that the `DataFolder` asset is already defined. If it cannot retrieve the
    `DataFolder` asset, it ignores file changes.

## Configuration

![Operation of the data folder monitor integration connector](data-folder-monitor-integration-connector.png)

This connector uses the [Files Integrator OMIS](/egeria-docs/services/omis/files-integrator)
running in the [integration daemon](/egeria-docs/concepts/integration-daemon).

Following is its connection definition to use on the
[administration commands that configure the Files Integrator OMIS](/egeria-docs/guides/admin/configuring-an-integration-daemon/#configure-the-integration-services):

!!! example "Connection configuration"
    ```json linenums="1" hl_lines="10"
    {
      "connection": {
        "class": "Connection",
        "connectorType": {
          "class": "ConnectorType",
          "connectorProviderClassName": "org.odpi.openmetadata.adapters.connectors.integration.basicfiles.DataFolderMonitorIntegrationProvider"
        },
        "endpoint": {
          "class": "Endpoint",
          "address": "{{folderName}}"
        }
      }
    }
    ```

    Replace `{{folderName}}` with the path name of the folder to monitor.

!!! education "Further information"
    This connector is configured in the `exchangeDL01` integration daemon server in the
    [open metadata labs](/egeria-docs/getting-started/hands-on-labs)

--8<-- "snippets/abbr.md"
