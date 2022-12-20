<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

#  A Repository proxy with an embedded native repository 

This is a [repository proxy](/concepts/repository-proxy) that caches content into a native repository.
It simplifies the development of a repository proxy repository because:

- All the OMRS APIs are delegated down to the embedded native repository, so there is no need to write any special technology 
- the event mapper can poll the 3rd party technology and add in the content to the embedded repository.

This connector maybe useful in the following cases:

- a quick way to show Egeria connectivity with a repository proxy connector
- it is a way to migrate 3rd party content into an Egeria native repository
- for small deployments, it provides a cache so queries can be honoured. 

In most cases an integration or standard repository proxy pattern is likely to be more appropriate. 

## Configuration 
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


!!! post "POST - configure as a repository proxy"
```
{{baseURL}}/open-metadata/admin-services/users/{{user}}/servers/{{server}}/local-repository/mode/repository-proxy/connection
```

The request body is a [virtual connection](/concepts/connection/?h=embeddedconnection#virtual-connections), which contains an EmbeddedConnection, which should refer
to the required native repository connector that will act as the cache.
In the below example the cache uses the [XTDB connector](/connectors/repository/xtdb/).

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


--8<-- "snippets/abbr.md"
