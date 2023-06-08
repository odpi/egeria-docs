<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Universe

Fetches asset's header, classification, properties and relationships

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json)

```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/asset-relationships/{{asset-guid}}?assetType={{asset-type}}&relationshipType={{relationship-type}}
```
Path and request parameters:
* `serverName` - unique identifier for requested server
* `userId` - the unique identifier for the user
* `assetGUID` - the unique identifier for the asset
* `assetType` - the type of the asset

Response:
* `AssetCatalogResponse` - the asset with its header and the list of associated classifications and relationship

---8<-- "snippets/abbr.md"







