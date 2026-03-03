<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Configure integration groups

An [integration group](/concepts/integration-group) identifies a list of [integration connectors](/concepts/integration-connector) that an integration daemon should run.  These integration connectors are defined and maintained as open metadata elements stored in the open metadata repositories.  Changes can be made to these integration connectors at any time using the [Governance Server OMAS](/services/omas/governance-server/overview).  The integration daemon is monitoring for changes and updates the integration connectors it is running in line with the changes it discovers.  This approach allows changes to be made to the integration daemon's configuration without needing access to the administration commands, nor a restart of the integration daemon. 

#### Configure an integration group

Each integration group is configured with the network location of a [metadata access server](/concepts/metadata-access-server) running the appropriate [Open Metadata Access Services (OMASs)](/services/omas) along with the qualified name of the [IntegrationGroup](/types/4/0464-Dynamic-Integration-Groups) open metadata entity that represents the integration group. 

!!! post "POST - configure an integration group"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/integration-groups/configuration
    ```

    With a request body like the following:

    ```json
    {
      "class": "IntegrationGroupConfig",
      "omagserverPlatformRootURL": "{MDServerURLRoot}",
      "omagserverName": "{MDServerName}",
      "integrationGroupQualifiedName": {qualifiedName}
    }
    ```

#### Configure all integration groups in one command

!!! post "POST - configure all integration groups"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/integration-groups/configuration/all
    ```

    With a request body like the following:

    ```json
    [
      {
        "class": "IntegrationGroupConfig",
        "omagserverPlatformRootURL": "{MDServerURLRoot}",
        "omagserverName": "{MDServerName}",
        "integrationGroupQualifiedName": {qualifiedName}
      },
      {
        "class": "IntegrationGroupConfig",
        "omagserverPlatformRootURL": "{MDServerURLRoot}",
        "omagserverName": "{MDServerName}",
        "integrationGroupQualifiedName": {qualifiedName}
      },
    ]
    ```

#### Retrieve configured integration groups

!!! get "GET - all configured integration groups"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/integration-groups/configuration
    ```

#### Remove all configured integration groups

!!! delete "DELETE - all configured integration groups"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/integration-groups
    ```

#### Remove a specific configured integration group

!!! delete "DELETE - a configured integration group"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/servers/{{serverName}}/integration-groups/{{qualifiedName}}
    ```




