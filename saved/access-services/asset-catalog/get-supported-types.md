<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Supported Types

Returns the list with supported types for search, including the sub-types supported.

## Java client

AssetCatalog.java, method (more details in javadoc): [AssetCatalogSupportedTypes getSupportedTypes(String userId, String type) throws InvalidParameterException, PropertyServerException;](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/assetcatalog/AssetCatalog.html#getSupportedTypes(java.lang.String,java.lang.String))

## REST endpoint

```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/supportedTypes
```
Path and request parameters:
* `serverName` - unique identifier for requested server
* `userId` - the unique identifier for the user
* `type` - the type

Response:
* `AssetCatalogSupportedTypes` - list of types and sub-types supported for search

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json).

---8<-- "snippets/abbr.md"







