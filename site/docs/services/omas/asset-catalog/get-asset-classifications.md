<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Classifications

This is the ability to retrieve all classifications that exist on a specific asset.

## Java client

AssetCatalog.java, method (more details in javadoc): [ClassificationListResponse getClassificationsForAsset(String userId, String assetGUID, String assetType, String classificationName) throws InvalidParameterException, PropertyServerException;](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetcatalog/AssetCatalog.html#getClassificationsForAsset(java.lang.String,java.lang.String,java.lang.String,java.lang.String))

## REST endpoint
```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/supportedTypes
```
Path and request parameters:
* `serverName` - unique identifier for requested server
* `userId` - the unique identifier for the user
* `assetGUID` - the unique identifier for the asset
* `assetType` - the type of the asset
* `classificationName` - the name of the classification

Response:
* `ClassificationsResponse` - the classification for the asset

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json).

---8<-- "snippets/abbr.md"







