<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Search

Returns the list with supported types for search, including the sub-types supported

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json)

```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/supportedTypes
```
Path and request parameters:
* `serverName` - unique identifier for requested server
* `userId` - the unique identifier for the user
* `searchCriteria` - a string expression of the characteristics of the required assets 
* `searchParameters` - constrains to make the assets' search results more precise

Response:
* `AssetListResponse` - list of found assets

---8<-- "snippets/abbr.md"







