<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring a [repository proxy](/concepts/repository-proxy)

A *Repository Proxy* is configured by creating a [configuration document](/concepts/configuration-document).  Below is the outline structure of the server's configuration document.

![Configuration for a repository proxy](repository-proxy-configuration.svg)

--8<-- "docs/guides/admin/servers/configuring-event-bus.md"

--8<-- "docs/guides/admin/servers/configuring-local-server-url.md"

--8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

--8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

--8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md"

--8<-- "docs/guides/admin/servers/configuring-registration-to-a-cohort.md"

--8<-- "docs/guides/admin/servers/configuring-the-startup-archives.md"

--8<-- "docs/guides/admin/servers/configuring-the-repository-proxy-connector.md"

## Configure the connectors to the third party metadata repository

The mapping between a third party metadata repository and the open metadata protocols in a [repository proxy](/concepts/repository-proxy) is implemented by two connectors:

- A [repository connector](/concepts/repository-connector)
- A [event mapper connector](/concepts/event-mapper-connector)

They are configured as follows.

### Configure the repository connector

The repository proxy can act as a proxy to a third party metadata repository. This is done by adding the connection for the [repository connector](/concepts/repository-connector) as follows.

!!! post "POST - configure the repository connector"
```
{{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/mode/repository-proxy/connection
```

!!! post "POST - configure an embedded local repository"
```
{{baseURL}}/open-metadata/admin-services/users/{{user}}/servers/{{server}}/local-repository/mode/repository-proxy/connection
```

with the body defining a VirtualConnection, 

for example , using an in memory local repository
```
{
    "class": "VirtualConnection",
    "headerVersion": 0,
    "displayName": "OMRS Hive Metastore Repository Connector",
    "connectorType": {
        "class": "ConnectorType",
        "headerVersion": 0,
        "type": {
            "class": "ElementType",
            "headerVersion": 0,
            "elementOrigin": "LOCAL_COHORT",
            "elementVersion": 0,
            "elementTypeId": "954421eb-33a6-462d-a8ca-b5709a1bd0d4",
            "elementTypeName": "ConnectorType",
            "elementTypeVersion": 1,
            "elementTypeDescription": "A set of properties describing a type of connector."
        },
        "guid": "bcdb3e04-b545-4001-b9e7-0305a4c21c1c",
        "qualifiedName": "OMRS Hive Metastore Repository Connector",
        "displayName": "OMRS Hive Metastore Repository Connector",
        "description": "OMRS Hive Metastore Repository Connector that issues calls to Hive Metastore",
        "connectorProviderClassName":"org.odpi.egeria.connectors.hms.repositoryconnector.CachingOMRSRepositoryProxyConnectorProvider"
   },
   "embeddedConnections":[
      {
         "class":"EmbeddedConnection",
         "headerVersion":0,
         "position":0,
         "displayName":"embedded in memory",
         "embeddedConnection":{
            "class":"Connection",
            "headerVersion":0,
            "connectorType":{
               "class":"ConnectorType",
               "headerVersion":0,
               "type":{
                  "class":"ElementType",
                  "headerVersion":0,
                  "elementOrigin":"LOCAL_COHORT",
                  "elementVersion":0,
                  "elementTypeId":"954421eb-33a6-462d-a8ca-b5709a1bd0d4",
                  "elementTypeName":"ConnectorType",
                  "elementTypeVersion":1,
                  "elementTypeDescription":"A set of properties describing a type of connector."
               },
               "guid":"65cc9091-757f-4bcd-b937-426160be8bc2",
               "qualifiedName":"Egeria:OMRSRepositoryConnector:InMemory",
               "displayName":"In Memory OMRS Repository Connector",
               "description":"Native open metadata repository connector that maps open metadata calls to a set of in memory hash maps - demo use only.",
               "connectorProviderClassName":"org.odpi.openmetadata.adapters.repositoryservices.inmemory.repositoryconnector.InMemoryOMRSRepositoryConnectorProvider"
            }
         }
      }
   ]
}

```


The request body should be the connection option to use for configuring the connector,
which can include any connector-specific options as well as general details like the 
endpoint and credentials for the third party repository.


### Configure the event mapper connector

Any open metadata repository that supports its own API **must** also implement an event mapper to ensure the [Open Metadata Repository Services (OMRS)](/services/omrs) is notified when metadata is added to the repository without going through the open metadata APIs.

The [event mapper is a connector](/concepts/event-mapper-connector) that listens for proprietary events from the repository and converts them into calls to the OMRS. The OMRS then distributes this new metadata.

!!! post "POST - configure event mapper"
```
{{platformURLRoot}}/open-metadata/admin-services/users/{{adminUserId}}/servers/{{serverName}}/local-repository/event-mapper-details?connectorProvider={{fullyQualifiedJavaClassName}}&eventSource={{resourceName}}
```

    The `connectorProvider` should be set to the fully-qualified Java class name for the [connector provider](/concepts/connector-provider), and the `eventSource` should give the details for how to access the events (for example, the hostname and port number of an Apache Kafka bootstrap server).







--8<-- "snippets/abbr.md"
