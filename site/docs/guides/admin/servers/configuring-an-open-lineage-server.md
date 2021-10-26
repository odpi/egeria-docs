<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an [open lineage server](/egeria-docs/concepts/open-lineage-servery)

Each [type of OMAG Server](/egeria-docs/concepts/omag-server/#types-of-omag-server) is configured by creating
a [configuration document](/egeria-docs/concepts/configuration-document).

![Configuration for an open lineage server](open-lineage-server-configuration.svg)

--8<-- "snippets/tasks/configuring-local-server-url.md"

--8<-- "snippets/tasks/configuring-omag-server-basic-properties.md"

--8<-- "snippets/tasks/configuring-the-audit-log.md"

--8<-- "snippets/tasks/configuring-the-server-security-connector.md"


Configure the Open Lineage Service, by POSTing a payload like the following
 
```json
    {
      "class": "OpenLineageConfig",
      "inTopicName": "server.omas.omas.assetlineage.outTopic",
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
          "storage.directory": "./egeria-lineage-repositories/lineageGraph/berkeley",
          "index.search.backend": "lucene",
          "index.search.directory": "./egeria-lineage-repositories/lineageGraph/searchindex"
        }
      },
      "accessServiceConfig": {
        "serverName": "cocoMDS1",
        "serverPlatformUrlRoot": "https://localhost:9443",
        "user": "admin",
        "password": "admin"
      },
      "backgroundJobs": [
        {
          "jobName": "LineageGraphJob",
          "jobInterval": 120,
          "jobEnabled": false
        }, 
        {
          "jobName": "AssetLineageUpdateJob",
          "jobInterval": 120,
          "jobEnabled": true,
          "jobDefaultValue": "2021-12-03T10:15:30"
        }
      ]
   }
```
to the following address

```
    POST {{serverURLRoot}}/open-metadata/admin-services/users/{{userId}}/servers/{{serverName}}/open-lineage/configuration
 ```

Update the payload with specific configuration values:
- `inTopicName` - the topic name of Asset Lineage OMAS Out Topic
- `lineageGraphConnection` - contains the information needed for configuring the 
[open-lineage-janus-connector](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/governance-daemon-connectors/open-lineage-connectors/open-lineage-janus-connector)
- `accessServiceConfig.serverName` - the name of the server where Asset Lineage is running (mandatory value - exception will be thrown during configuration if null)
- `accessServiceConfig.serverPlatformUrlRoot` - the base URL where the Asset Lineage is running (mandatory value - exception will be thrown during configuration if null)
- `accessServiceConfig.user` - the user needed for authentication in Asset Lineage (not used at the moment)
- `accessServiceConfig.password` - the password needed for authentication in Asset Lineage (not user at the moment)
- `backgroundJobs.jobName` - should be the name of the job class name
- `backgroundJobs.jobInterval` - interval for Open Lineage Services background processing job. The default is 120 if not specified
- `backgroundJobs.jobEnabled` - enables or disables the job. The default is true if not specified
- `backgroundJobs.jobDefaultValue` - value used to specify a particular value for the job. It's used in OLS only for the AssetLineageUpdateJob. It should have the ISO-8601 format, example: '2021-04-06T10:32:22.235'. It offers the chance to avoid the initial load and start publishing entities only starting from the given date and time. It is used only if there is no value saved in the graph to indicate the last update time. If a parsing error occurs, the job and the triggers will be shut down.  

Note that you can configure the connector to run embedded or on a standalone JanusGraph server, by setting the `connectorProviderClassName` parameter to `org.odpi.openmetadata.openconnectors.governancedaemonconnectors.openlineageconnectors.janusconnector.graph.LineageGraphConnectorProvider` (embedded) or `org.odpi.openmetadata.openconnectors.governancedaemonconnectors.openlineageconnectors.janusconnector.graph.LineageGraphRemoteConnectorProvider` (standalone server). 
 

### Removing the Open Lineage Services from the server configuration

Remove the Open Lineage Services from the server configuration by issuing the following HTTP request:
    
```
DELETE {{serverURLRoot}}/open-metadata/admin-services/users/{{userId]}}/servers/{{serverName}}/open-lineage/configuration
```

--8<-- "snippets/abbr.md"
