<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


### Configure integration groups

An [integration group](/concepts/integration-group) identifies a list of [integration connectors](/concepts/integration-connector) that an integration daemon should run.  These integration connectors are defined and maintained as open metadata elements stored in the open metadata repositories.  Changes can be made to these integration connectors at any time using the [Governance Engine OMAS](/services/omas/governance-engine/overview).  The integration daemon is monitoring for changes and updates the integration connectors it is running in line with the changes it discovers.  This approach allows changes to be made to the integration daemon's configuration without needing access to the administration commands, nor a restart of the integration daemon. 

#### Configure an integration group

Each integration group is configured with the network location of a [metadata access server](/concepts/metadata-access-server) running the appropriate [Open Metadata Access Services (OMASs)](/services/omas) along with the qualified name of the [IntegrationGroup](/types/4/0464-Dynamic-Integration-Groups) open metadata entity that represents the integration group. 

The OMASs needed in the metadata access server depend on the [Open Metadata Integration Services (OMISs)](/services/omis) in use by the integration connectors.  If you are unsure of which integration services will be used by your integration connectors, configure all of the listed OMASs in the metadata access store. 

| Open Metadata Integration Service (OMIS)                                       | OMIS Description                                                                                                                             | Open Metadata Access Service (OMAS) running in the metadata access server |
|:-------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| [API Integrator](/services/omis/api-integrator/overview)                       | provides cataloguing for APIs.                                                                                                               | [Data Manager OMAS](/services/omas/data-manager/overview)                 |
| [Catalog Integrator](/services/omis/catalog-integrator/overview)               | provides a two-way synchronization for data catalogs.                                                                                        | [Asset Manager OMAS](/services/omas/asset-manager/overview)               |
| [Database Integrator](/services/omis/database-integrator/overview)             | provides metadata extraction from relational databases.                                                                                      | [Data Manager OMAS](/services/omas/data-manager/overview)                 |
| [Display Integrator](/services/omis/display-integrator/overview)               | provides metadata extraction from systems that provide user displays and forms to capture new data values.                                   | [Data Manager OMAS](/services/omas/data-manager/overview)                 |
| [Files Integrator](/services/omis/files-integrator/overview)                   | collects metadata about files stored in a filesystem or file manager.                                                                        | [Data Manager OMAS](/services/omas/data-manager/overview)                 |
| [Infrastructure Integrator](/services/omis/infrastructure-integrator/overview) | supports the extraction of metadata from IT infrastructure artifacts as well as the use of metadata to maintain IT infrastructure artifacts. | [IT Infrastructure OMAS](/services/omas/it-infrastructure/overview)       |
| [Lineage Integrator](/services/omis/lineage-integrator/overview)               | collects metadata about processes, their internal logic and the data assets they work with.                                                  | [Asset Manager OMAS](/services/omas/asset-manager/overview)               |
| [Organization Integrator](/services/omis/organization-integrator/overview)     | imports details of an organization's structure - such as teams and departments.                                                              | [Community Profile OMAS](/services/omas/community-profile/overview)       |
| [Search Integrator](/services/omis/search-integrator/overview)                 | supports the building of search indexes based on open metadata events.                                                                       | [Asset Consumer OMAS](/services/omas/asset-consumer/overview)             |
| [Security Integrator](/services/omis/security-integrator/overview)             | distributes security properties to access control enforcement points.                                                                        | [Security Manager OMAS](/services/omas/security-manager/overview)         |
| [Stewardship Integrator](/services/omis/stewardship-integrator/overview)       | exchanges requests for stewardship action (and results) with a human task manager.                                                           | [Stewardship Action OMAS](/services/omas/stewardship-action/overview)     |
| [Topic Integrator](/services/omis/topic-integrator/overview)                   | provides cataloguing of topics and event schema for event brokers.                                                                           | [Data Manager OMAS](/services/omas/data-manager/overview)                 |

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




