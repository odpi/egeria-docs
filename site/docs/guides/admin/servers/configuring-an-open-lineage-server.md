<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an [open lineage server](/concepts/open-lineage-servery)

## Overview

Each [type of OMAG Server](/concepts/omag-server/#types-of-omag-server) is configured by creating
a [configuration document](/concepts/configuration-document).

For open lineage server following can be configured:

![Configuration for an open lineage server](open-lineage-server-configuration.svg)

??? question "What are the required configuration elements for this server type?"
    - Event Bus Config
    - Audit Log Destination
    - Open Lineage Config

--8<-- "docs/guides/admin/servers/configuring-local-server-url.md"

--8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

--8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

<!-- --8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md" -->

--8<-- "docs/guides/admin/servers/configuring-event-bus.md"


## Configuring the Open Lineage Services

!!! post "POST - Configure Open Lineage Services"
    ```
    {{serverURLRoot}}/open-metadata/admin-services/users/{{userId}}/servers/{{serverName}}/open-lineage/configuration
    ```

    ```json
    {
        "class": "OpenLineageConfig",
        "openLineageDescription": "Open Lineage Service is used for the storage and querying of lineage",
        "lineageGraphConnection": {
            "class": "Connection",
            "displayName": "Lineage Graph Connection",
            "description": "Used for storing lineage in the Open Metadata format",
            "connectorType": {
                "class": "ConnectorType",
                "connectorProviderClassName": "org.odpi.openmetadata.openconnectors.governancedaemonconnectors.openlineageconnectors.janusconnector.graph.LineageGraphConnectorProvider"
            },
            "configurationProperties": {
                "gremlin.graph": "org.janusgraph.core.JanusGraphFactory",
                "storage.backend": "berkeleyje",
                "storage.directory": "data/servers/{{ols-server-name}}/repository/berkeley",
                "index.search.backend": "lucene",
                "index.search.directory": "data/servers/{{ols-server-name}}/repository/searchindex"
            }
        },
        "accessServiceConfig": {
            "serverName": "{{server-name}}",
            "serverPlatformUrlRoot": "{{server-platform-url}}",
            "user": "admin",
            "password": "secret"
        },
        "backgroundJobs": [
            {
                "jobName": "LineageGraphJob",
                "jobInterval": 120,
                "jobEnabled": "false"
            },
            {
                "jobName": "AssetLineageUpdateJob",
                "jobInterval": 120,
                "jobEnabled": "false",
                "jobDefaultValue": "2021-01-01T00:00:00"
            }
        ]
    }
    ```

#### Configuration reference

| Property | Description | Is mandatory |
|---|---|---|
`lineageGraphConnection` | OCF configuration object that defines the Graph store connector type used. See [open-lineage-janus-connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-daemon-connectors/open-lineage-connectors/open-lineage-janus-connector) for more details. | Yes |
`accessServiceConfig.serverName` | the name of the metadata server where paired Asset Lineage OMAS is running. | Yes
`accessServiceConfig.serverPlatformUrlRoot` | The URL of the OMAG server platform running the metadata server where paired Asset Lineage OMAS is running. Also see [start-up information](#start-up-information) section. | Yes |
`accessServiceConfig.user` | The username to access the server running Asset Lineage OMAS. | Yes |
`accessServiceConfig.password` | The user password to access the server running Asset Lineage OMAS. Can be left out for non-secured access. | No |
`backgroundJobs[n].jobName` | Key used to match the job name pre-defined in the open lineage server. Supported values `LineageGraphJob` and `AssetLineageUpdateJob` | No |
`backgroundJobs[n].jobInterval` | Interval (**seconds**) to execute the repetitive task defined by the named job above | No |
`backgroundJobs[n].jobEnabled` | Controls if the job will be running (enabled) or not (disabled). Omitting the item in the `backgroundJobs` list had the same effect as setting the job to disable. | No
`backgroundJobs[n].jobDefaultValue` | Setting initial value for the task, only used in case of `AssetLineageUpdateJob`. When configured and not present in the store this value becomes the starting point in time to poll for updates. After successful update initial value is no longer used and last known value form the store. The value should be always specified in standard internet data-time format `YYYY-MM-DDThh:mm:ss`. See [ISO-8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.8) for more info and examples. | No |
 

#### Removing the Open Lineage Services from the server configuration

!!! delete "DELETE - Remove Open Lineage Configuration from the server"
    ```
    {{serverURLRoot}}/open-metadata/admin-services/users/{{userId]}}/servers/{{serverName}}/open-lineage/configuration
    ```
### Start up information

!!! info "Runtime consideration"
    It is important to consider that, to operate, open lineage server depends on the availability of metadata access server and asset lineage being up and running. This is the case because open lineage server discovers the event bus connectivity and the topic address from asset lineage during start-up. Consequently, it will always wait and retry until this condition is met, and it starts up successfully.

--8<-- "snippets/abbr.md"
