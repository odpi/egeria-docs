<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# JanusGraph Repository

!!! info "Connector summary"

    - Connector Category: [Native Repository Connector](/concepts/repository-connector)
    - Hosting Service: [Open Metadata Reposiotry Services (OMRS)](/services/omrs)
    - Hosting Server: [Metadata Access Store](/concepts/metdata-access-store)
    - Source Module: [graph-repository-connector :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/graph-repository-connector){ target=gh }
    - Jar File Name: `graph-repository-connector.jar`
    - ConnectorProviderClassName: `org.odpi.openmetadata.adapters.repositoryservices.graphrepository.repositoryconnector/GraphOMRSRepositoryConnectorProvider.java`

The Graph Repository provides a local repository that uses a graph store as its persistence store.

## Configuration
To configure a [Metadata Access Store](/concepts/metadata-access-store) to use the Graph Repository, set the repository-mode to 'local-graph-repository'. For example:

```
POST <serverURLRoot>/open-metadata/admin-services/users/<userName>/servers/<serverName>/local-repository/mode/local-graph-repository
```

Replace the <serverURLRoot>, <userName> and <serverName> with the values appropriate for the server you are configuring.

## Using the Graph Repository
The interface to the graph repository is the OMRS MetadataCollection API. The graph repository supports almost all of the MetadataCollection API apart from historical queries and undo.

## Using the find methods
The find methods (listed below) use regular expression (regexp) syntax. They are intended for retrieval of specific entities or relationships and the regexp is always matched to the whole of the property value or classification name.
* findEntitiesByProperty()
* findRelationshipsByProperty()
* findEntitiesByPropertyValue()
* findRelationshipsByPropertyValue()
* findEntitiesByClassification()

The first two methods accept a map of property names and values that acts as a filter.
The next pair of methods accept a string that is matched against the values of any string properties.
The last method accepts a string that is matched against the names of classifications associated with an entity.

In all cases the string value(s) provided are treated as a regular expression that is matched against the whole property value or classification name.

To find entities with property values of "coco-asset-123", "coco-asset-456", "coco-asset-789" you could specify a regexp e.g. "coco-asset-.*"

To find an entity or relationship with a property value of "coco-asset-123" you need to specify a regexp that will match the whole string value, e.g. "coco-asset-.*", a substring is not sufficient. If you were to only specify a regexp of "coco-asset", it would not match the entity or relationship.

Similarly, to find an entity with a classification with name "coco-classification-abc" you would need to to specify a regexp that will match the whole string value, e.g. "coco-classification-.*"


## Under the hood
Internally, the Graph Repository uses JanusGraph to create a graph database. The JanusGraph graph database and graph are automatically created and the graph schema and search indexes are automatically configured.

The Graph Repository configures JanusGraph to use the berkeley embedded database and Lucene search indexes.

The supported interface for using the Graph Repository is the MetadataCollection API, and access should only be performed through this interface. In contrast, the schema and indexing used internally by the Graph Repository are subject to change as a result of future improvements to Egeria and should not be relied upon directly.

The repository uses the repository helper for parameter and type validation.


--8<-- "snippets/abbr.md"

