<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# JanusGraph Repository

!!! info "Connector summary"

    - Connector Category: [Native Repository Connector](/concepts/repository-connector)
    - Hosting Service: [Open Metadata Repository Services (OMRS)](/services/omrs)
    - Hosting Server: [Metadata Access Store](/concepts/metdata-access-store)
    - Source Module: [graph-repository-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/graph-repository-connector){ target=gh }
    - Jar File Name: `graph-repository-connector.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector/GraphOMRSRepositoryConnectorProvider.java`

The Graph Repository provides a local repository for a [Metadata Access Store](/concepts/metadata-access-store) that uses JanusGraph as its persistence store.

## Configuration

To configure a Metadata Access Store to use the Graph Repository, set the repository-mode to 'local-graph-repository'. For example:

```
POST {platformURLRoot}/open-metadata/admin-services/users/{userName}/servers/{serverName}/local-repository/mode/local-graph-repository
```

Replace the *{serverURLRoot}*, *{userName}* and *{serverName}* with the values appropriate for the server you are configuring.

The request body is optional and set to a map of property names to property values that specify the storage properties that JanusGraph is to use.  If the storage properties are null, the following properties are used:

| Property name          | Property value                                           |
|------------------------|----------------------------------------------------------|
| storage.backend        | berkeleyje                                               |
| storage.directory      | ./data/servers/{serverName}/repository/graph/berkeley    |
| index.search.backend   | lucene                                                   |
| index.search.directory | ./data/servers/{serverName}/repository/graph/searchindex |

This stores the graph store in a file called `./data/servers/{serverName}/repository/graph/berkeley` where the server name is inserted into *{serverName}*.  The search index is stored in [Apache Lucene](https://lucene.apache.org/).

Details of the other supported storage backends and how to specify them are found in the [JanusGraph documentation](https://docs.janusgraph.org/storage-backend/).



--8<-- "snippets/abbr.md"

