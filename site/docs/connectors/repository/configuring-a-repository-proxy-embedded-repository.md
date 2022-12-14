<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring a [repository proxy](/concepts/repository-proxy)

Each [type of OMAG Server](/concepts/omag-server/#types-of-omag-server) is configured by creating
a [configuration document](/concepts/configuration-document).

![Configuration for a repository proxy](../../guides/admin/servers/repository-proxy-configuration.svg)

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

!!! post "POST - configure as a repository proxy"
```
{{baseURL}}/open-metadata/admin-services/users/{{user}}/servers/{{server}}/local-repository/mode/repository-proxy/connection
```

with the body defining a VirtualConnection, 

for example, using an XTDB local repository and the OMRS Caching Metastore Repository Connector.
```
{
    "class": "VirtualConnection",
    "headerVersion": 0,
    "displayName": "OMRS Caching Repository Connector",
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
        "guid": "41a30f1e-4dad-461b-a21c-eacabb4016cc",
        "qualifiedName": "Egeria:OMRSRepositoryConnector:Cached",
        "displayName": "OMRS Caching Repository Connector",
        "description": " The OMRS caching Repository Connector provides a simple repository implementation that caches metadata in an embedded repository connector.",
        "connectorProviderClassName":"org.odpi.openmetadata.adapters.repositoryservices.caching.repositoryconnector.CachingOMRSRepositoryProxyConnectorProvider"
   },
   "embeddedConnections":[
      {
         "class":"EmbeddedConnection",
         "headerVersion":0,
         "position":0,
         "displayName":"embedded XTDB store",
         "embeddedConnection":{  
           "class": "Connection",
               "connectorType": {
                  "class": "ConnectorType",
                  "connectorProviderClassName": "org.odpi.egeria.connectors.juxt.xtdb.repositoryconnector.XtdbOMRSRepositoryConnectorProvider"
               }
         }
      }
   ]
}


```


The request body contains an EmbeddedConnection, which should refer to the required repository connector that will act as the cache.
In the above example the cache is the XTDB connector.

--8<-- "snippets/abbr.md"
