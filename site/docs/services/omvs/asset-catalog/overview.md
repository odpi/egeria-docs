<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Asset Catalog API

The Asset Catalog API provides a REST API to search for digital resources
(assets) that are catalogued in open metadata. It also enables the caller to retrieve asset
properties, schema, lineage and other related information.

## Key Features

The Asset Catalog API supports the following key features:

* **Asset Search**: Locate assets using a search string or regular expression across the asset domain.
* **Asset Graphs**: Retrieve all elements anchored to an asset, including their relationships, to
  visualize the asset's structure and context.
* **Lineage Graphs**: Explore the lineage of an asset to understand how data flows in and out of it,
  including relationships from the asset itself and its anchored schema elements.
* **Supported Types**: Query the subtypes of assets supported by the ecosystem.

## API Operations

The Asset Catalog API provides services to search for [data resources](/concepts/resource) including:

* data stores
* event feeds
* APIs
* data sets

The search locates data resources based on the content of the [asset](/concepts/asset) metadata itself and the metadata that links to it. This includes:

* glossary terms
* schema elements
* assets
* lineage


The Asset Catalog REST API supports:

* the retrieval of assets based on unique identifiers
* the retrieval of asset's relationships and classifications
* the query for related assets and lineage
* the retrieval of assets based on their type
* the retrieval of glossaries and their content

## Retrieving the lineage graph of an asset

The lineage graph of an asset is retrieved with:

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-catalog/assets/{{assetGUID}}/as-lineage-graph
```

The service walks the [lineage](/features/lineage-management/overview/) relationships of the asset upstream and downstream, together with those of its anchored schema elements if *allAnchors* is set.  Each element it reaches is returned once in *linkedAssets*, and the relationships between them in *lineageRelationships*, along with mermaid graphs of the whole lineage (*fullLineageMermaidGraph*) and of its ultimate sources and destinations (*edgeMermaidGraph*).  The starting asset is returned in full; the linked elements are returned without their own relationships, which keeps the response small.

On a large estate, lineage can reach a long way, because the elements that many flows pass through, such as a system's schema, join up flows that are otherwise unrelated.  The request body, *AssetLineageGraphRequestBody*, controls how much of the graph is returned:

| Field | Default | Meaning |
|---|---|---|
| *maxHops* | `8` | The maximum number of lineage relationships followed away from the asset, counted separately upstream and downstream.  `0` means no limit, which can take minutes on a large estate. |
| *includeOnlyRelationships* | the lineage relationships listed below | The relationship types to follow.  The list replaces the defaults.  A supertype name includes all of its subtypes, so `["LineageRelationship"]` follows every lineage relationship and `["DataLineageRelationship"]` follows *DataFlow*, *ProcessCall*, *LineageMapping* and the other data lineage relationships. |
| *skipRelationships* | none | Relationship types, with their subtypes, to remove from the default or requested list.  This trims the defaults without restating them. |
| *limitToISCQualifiedName* | none | Only follow relationships that belong to this [information supply chain](/concepts/information-supply-chain).  This is usually the quickest way to a focused graph. |
| *highlightISCQualifiedName* | none | In the mermaid graph, draw the relationships that belong to other information supply chains as thin lines, so this supply chain stands out. |
| *allAnchors* | `false` | Also follow the lineage of the schema elements anchored to each asset, such as the tables and columns of a database schema, as well as the asset's own lineage. |

The request body also accepts the usual query options, such as *effectiveTime* and *asOfTime*.  If there is no request body, the defaults apply, including the limit of 8 hops.

By default the walk follows *DataFlow*, *ControlFlow*, *LineageMapping*, *ProcessCall*, *DerivedSchemaTypeQueryTarget*, *DataSetContent*, *DataMapping* and *ActionRequester*.  All of them are subtypes of [*LineageRelationship*](/types/0/0010-Base-Model/#lineagerelationship-relationship), so each element's lineage is retrieved with a single query.

Each element in the graph has two fields that describe where it sits in the walk:

* *hopsFromStart* - the number of lineage relationships between the starting asset and the element, by the shortest route.  The starting asset is `0`.
* *hopLimitReached* - `true` when the lineage carries on past the element but the walk stopped there because of *maxHops*.  Such an element is not shown as an ultimate source or destination in the edge graph.  To follow the lineage further, request the lineage graph again starting from that element.

For example, this request returns the lineage within three hops of the asset, following every lineage relationship except *DataSetContent*:

```json
{
  "class" : "AssetLineageGraphRequestBody",
  "maxHops" : 3,
  "includeOnlyRelationships" : ["LineageRelationship"],
  "skipRelationships" : ["DataSetContent"]
}
```

## Further information

* [Asset Concept](/concepts/asset/)
* [Lineage Management](/features/lineage-management/overview/)

Sample requests for the REST API can be found in [Egeria-api-asset-catalog.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/asset-catalog/Egeria-api-asset-catalog.http).


--8<-- "snippets/abbr.md"
