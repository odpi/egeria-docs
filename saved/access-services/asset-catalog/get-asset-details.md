<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Details

Fetches asset's properties, relationships and classifications.

## Java client

AssetCatalog.java, method (more details in javadoc): [AssetCatalogResponse getAssetDetails(String userId, String assetGUID, String assetType) throws InvalidParameterException, PropertyServerException;](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetcatalog/AssetCatalog.html#getAssetDetails(java.lang.String,java.lang.String,java.lang.String))

## REST endpoint

```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/asset-details/{{asset-guid}}
```
Path and request parameters:
* `serverName` - unique identifier for requested server.
* `userId` - the unique identifier for the user
* `assetGUID` - the global unique identifier of the asset
* `assetType` - the type of the asset

Response:
* `AssetCatalogResponse` - list of properties used to narrow the search

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json).

---8<-- "snippets/abbr.md"







