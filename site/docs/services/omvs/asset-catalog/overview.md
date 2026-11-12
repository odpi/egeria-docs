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
* **DCAT Exchange**: Catalog the datasets, data services and catalogs described in a W3C Data Catalog Vocabulary (DCAT) document, and retrieve the DCAT description of an asset.

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

## Exchanging DCAT descriptions of assets

The W3C [Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/) is the standard that governments and many other organizations use to describe the data assets that they make available.  The Asset Catalog API has three requests that [exchange asset descriptions](/features/asset-description-exchange/overview) in the JSON-LD serialization of DCAT version 3.  The mapping between DCAT and open metadata is described in the [feature overview](/features/asset-description-exchange/overview/#mapping-to-open-metadata).

### Cataloguing a DCAT document

A DCAT document is catalogued directly with:

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-catalog/assets/dcat/import-document
```

The request body is the JSON-LD document.  Each dataset it describes becomes a *DataSet* asset with an asset for each of its distributions, each data service becomes a *DeployedAPI* and each catalog becomes a *CollectionFolder*.  The unique identifiers (GUIDs) of these elements are returned.  Sending the same description again updates the elements rather than creating new ones.

For example, this document describes a dataset with two distributions: a CSV file to download, which is catalogued as a *DataFile*, and an API, which is catalogued as a *DataStore*.

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "vcard": "http://www.w3.org/2006/vcard/ns#"
  },
  "@id": "https://data.example.gov/dataset/air-quality-2025",
  "@type": "dcat:Dataset",
  "dct:title": "Air quality measurements 2025",
  "dct:description": "Hourly readings of nitrogen dioxide, ozone and particulates from the national monitoring network.",
  "dct:identifier": "air-quality-2025",
  "dct:publisher": { "@type": "foaf:Organization", "foaf:name": "Environment Agency" },
  "dcat:contactPoint": { "@type": "vcard:Organization", "vcard:fn": "Open Data Helpdesk", "vcard:hasEmail": { "@id": "mailto:opendata@environment.example.gov" } },
  "dcat:keyword": [ "air quality", "pollution" ],
  "dct:license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "dcat:landingPage": { "@id": "https://data.example.gov/air-quality" },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "Air quality 2025 (CSV)",
      "dcat:downloadURL": { "@id": "https://data.example.gov/files/air-quality-2025.csv" },
      "dct:format": "CSV"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "Air quality 2025 (API)",
      "dcat:accessURL": { "@id": "https://api.example.gov/air-quality/v1" }
    }
  ]
}
```

### Sending a DCAT document to an integration daemon

A DCAT document is sent to an [integration daemon](/concepts/integration-daemon) with:

```
POST {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-catalog/integration-daemons/{{integrationDaemonGUID}}/dcat/publish-document
```

The request body is the JSON-LD document, and *integrationDaemonGUID* is the unique identifier of the integration daemon's *SoftwareServer* asset in the catalog.  The integration daemon passes the document to the integration connectors that have registered a listener for DCAT documents, such as the DCAT Cataloguer from the [DCAT Content Pack](/content-packs/dcat-content-pack/overview), which catalogs the datasets, data services and catalogs that the document describes.  Nothing is returned, since the document is processed by the integration daemon.

### Retrieving the DCAT description of an asset

The DCAT description of an asset is retrieved with:

```
GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/asset-catalog/assets/{{assetGUID}}/dcat-document
```

A *DeployedAPI* is described as a `dcat:DataService`.  Any other type of asset is described as a `dcat:Dataset`; a data set's distributions are the assets that supply its data.  The *document* property of the response is a complete JSON-LD document, including its context.  The asset does not need to be a member of the [DCAT Publishing Catalog](/features/asset-description-exchange/overview/#publishing-descriptions) - that collection controls which assets the DCAT Publisher writes to the file system.

## Further information

* [Asset Concept](/concepts/asset/)
* [Lineage Management](/features/lineage-management/overview/)
* [Exchanging Asset Descriptions](/features/asset-description-exchange/overview/)

Sample requests for the REST API can be found in [Egeria-api-asset-catalog.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/asset-catalog/Egeria-api-asset-catalog.http).


--8<-- "snippets/abbr.md"
