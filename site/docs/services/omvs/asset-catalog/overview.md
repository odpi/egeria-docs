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

## Further information

* [Asset Concept](/concepts/asset/)
* [Lineage Management](/features/lineage-management/overview/)

Sample requests for the REST API can be found in [Egeria-api-asset-catalog.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-services/asset-catalog/Egeria-api-asset-catalog.http).


--8<-- "snippets/abbr.md"
