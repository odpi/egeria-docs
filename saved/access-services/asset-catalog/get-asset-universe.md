<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Universe

Fetches asset's header, classification, properties and relationships.

## Java client

AssetCatalog.java, method (more details in javadoc): [AssetCatalogResponse getAssetUniverse(String userId, String assetGUID, String assetType) throws InvalidParameterException, PropertyServerException;](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetcatalog/AssetCatalog.html#getAssetUniverse(java.lang.String,java.lang.String,java.lang.String))

## REST endpoint

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

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json).

---8<-- "snippets/abbr.md"







