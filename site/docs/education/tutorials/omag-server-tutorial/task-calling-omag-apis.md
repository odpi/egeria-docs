<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Calling Open Metadata and Governance Services

Now that the metadata server is started, it is possible to query the metadata.  

Egeria offers many different REST APIs to retrieve and maintain metadata.  In this exercise it is not possible to try them all out.  The aim is to show an example of how metadata is retrieved.  The command below finds [assets](/concepts/asset).  Assets represent resources such as data sets and servers used by the organization.

```text
POST https://localhost:9443/servers/myMetadataServer/open-metadata/access-services/asset-owner/users/peterprofile/assets/by-search-string?startFrom=0&pageSize=10
```
The request body contains the search parameters.
```json
{
    "class" : "SearchStringRequestBody",
    "searchString" : ".*."
}
```
The results show there are two assets in the metadata repository - a database and a database schema.
```json
{
  "class": "AssetElementsResponse",
  "relatedHTTPCode": 200,
  "startingFromElement": 0,
  "assets": [
    {
      "elementHeader": {
        "class": "ElementHeader",
        "headerVersion": 0,
        "status": "ACTIVE",
        "type": {
          "typeId": "eab811ec-556a-45f1-9091-bc7ac8face0f",
          "typeName": "DeployedDatabaseSchema",
          "superTypeNames": [
            "DataSet",
            "Asset",
            "Referenceable",
            "OpenMetadataRoot"
          ],
          "typeVersion": 1,
          "typeDescription": "A collection of database tables and views running in a database server."
        },
        "origin": {
          "sourceServer": "myMetadataServer",
          "originCategory": "DEREGISTERED_REPOSITORY",
          "homeMetadataCollectionId": "2216ab62-176a-46c0-b889-9aa081754b54",
          "homeMetadataCollectionName": "SimpleDataCatalog"
        },
        "versions": {
          "createdBy": "Egeria",
          "createTime": "2021-09-19T10:10:51.579+00:00",
          "version": 1
        },
        "guid": "4782e08b-043c-4017-9b2f-d63163f67fd8"
      },
      "assetProperties": {
        "class": "AssetProperties",
        "qualifiedName": "V37B8752.FH567.sys/BRANCH.RETAILSCHEMA",
        "typeName": "DeployedDatabaseSchema",
        "displayName": "RETAILSCHEMA",
        "name": "RETAILSCHEMA",
        "description": "Retail banking schema.",
        "ownerType": "OTHER"
      }
    },
    {
      "elementHeader": {
        "class": "ElementHeader",
        "headerVersion": 0,
        "status": "ACTIVE",
        "type": {
          "typeId": "0921c83f-b2db-4086-a52c-0d10e52ca078",
          "typeName": "Database",
          "superTypeNames": [
            "DataStore",
            "Asset",
            "Referenceable",
            "OpenMetadataRoot"
          ],
          "typeVersion": 2,
          "typeDescription": "A data store containing relational data."
        },
        "origin": {
          "sourceServer": "myMetadataServer",
          "originCategory": "DEREGISTERED_REPOSITORY",
          "homeMetadataCollectionId": "2216ab62-176a-46c0-b889-9aa081754b54",
          "homeMetadataCollectionName": "SimpleDataCatalog"
        },
        "versions": {
          "createdBy": "Egeria",
          "createTime": "2021-09-19T10:10:51.579+00:00",
          "version": 1
        },
        "guid": "076b4498-a099-4c6b-9243-73e816b28504"
      },
      "assetProperties": {
        "class": "AssetProperties",
        "qualifiedName": "V37B8752.FH567.sys/BRANCH",
        "typeName": "Database",
        "displayName": "BRANCH Database",
        "name": "BRANCH Database",
        "description": "Main branch system database.",
        "ownerType": "OTHER"
      }
    }
  ]
}
```

!!! education "Further APIs"
    * The [Open Metadata Access Services (OMASs)](/services/omas) show the range of APIs offered by Egeria.
    * [Finding Metadata](/guides/developer/finding-metadata/overview) explains how metadata retrieval requests work.


