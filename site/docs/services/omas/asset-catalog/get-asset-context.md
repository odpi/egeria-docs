<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Context

Return the full context of an asset/glossary term based on its identifier. 
The response contains the list of the connections assigned to the asset.

More examples can be found in the
[sample collection](samples/collections/Asset-Catalog-endpoints.postman_collection.json)

```
GET {{base-url}}/servers/{{server-id}}/open-metadata/access-services/asset-catalog/users/{{user-id}}/asset-context/{{asset-guid}}
```
Path and request parameters:
* `serverName` - unique identifier for requested server.
* `userId` - the unique identifier for the user
* `assetGUID` - the global unique identifier of the asset
* `assetType` - the type of the asset

Response:
* `AssetResponse` - list of properties used to narrow the search

---8<-- "snippets/abbr.md"







