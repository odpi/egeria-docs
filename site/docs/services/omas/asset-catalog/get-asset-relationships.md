<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Get Asset Relationships

Fetches the relationships for a specific asset

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
* `relationshipType` - the type of the relationship
* `from` - offset
* `pageSize` - limit the number of the assets returned

Response:
* `RelationshipListResponse` - list of relationships for the given asset

---8<-- "snippets/abbr.md"







