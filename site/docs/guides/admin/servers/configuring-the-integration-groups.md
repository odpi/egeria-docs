<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Configure dynamic integration groups

Each integration group hosts one or more [integration connectors](/concepts/integration-connector). An integration connector is responsible for the exchange of metadata with a specific deployment of a third party technology. For example, the [database integrator](/services/omis/database-integrator) integration service supports integration connectors that work with relational databases (RDBMS). 

#### Configure an integration group

Each integration group is configured with the network location of the [metadata access point](/concepts/metadata-access-point) / [metadata access store](/concepts/metadata-access-store) running the appropriate [OMAS](/services/omas) along with the qualified name of the [IntegrationGroup](/types/4/0464-Dynamic-Integration-Groups) entity that represents the integration group. 

!!! post "POST - configure an integration group"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-groups/configuration
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
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-groups/configuration/all
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
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-groups/configuration
    ```

#### Remove all configured integration groups

!!! delete "DELETE - all configured integration groups"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-groups
    ```

#### Remove a specific configured integration group

!!! delete "DELETE - a configured integration group"
    ```
    {{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/integration-groups/{{qualifiedName}}
    ```




