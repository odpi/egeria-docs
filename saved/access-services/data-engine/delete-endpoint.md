<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Delete endpoint

Delete an endpoint

More examples can be found in the
[sample collection](samples/collections/DataEngine-asset_endpoints.postman_collection.json)

```
DELETE {serverURLRoot}/servers/{serverName}/open-metadata/access-services/data-engine/users/{userId}/endpoints/

{
    "guid": "endpointGUID",
    "qualifiedName": "Endpoint::ftp::localhost",
    "externalSourceName": "(organization)=Company::(project)=ExternalDataPlatform"
}
```
`externalSourceName` - qualifiedName of the external data engine tool.<br>
`guid` - optional property describing the unique identifier of the endpoint to be deleted
`qualifiedName` - optional property describing the qualifiedName of the endpoint to be deleted<br>
Note that you must provide either the qualifiedName, or the guid of the endpoint <br>
`VoidRespone` - void response with status and error message if failing


---8<-- "snippets/abbr.md"







