<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property | Egeria Type and Attribute                          | Supported in OSS Version |
|------------------------|----------------------------------------------------|--------------------------|
| function_id            | ExternalIdentifier.identifier                      | Yes                      |
| name                   | DeployedAPI.name                                   | Yes                      |
| full_name              | DeployedAPI.resourceName                           | Yes                      |
| comment                | DeployedAPI.description                            | Yes                      |
| owner                  | Ownership.owner                                    | No                       |
| data_source_format     | DataAssetEncoding.encoding                         | Yes                      |
| created_at             | ExternalIdentifier.externalInstanceCreationTime    | Yes                      |
| created_by             | ExternalIdentifier.externalInstanceCreatedBy       | No                       |
| updated_at             | ExternalIdentifier.externalInstanceLastUpdateTime  | Yes                      |
| updated_by             | ExternalIdentifier.externalInstanceLastUpdatedBy   | No                       |
| catalog_name           | ExternalIdentifier.mappingProperties.ucCatalogName | Yes                      |
| schema_name            | ExternalIdentifier.mappingProperties.ucSchemaName  | Yes                      |
| storage_location       | PropertyFacet.properties.ucStorageLocation         | Yes                      |
| table_type             | PropertyFacet.properties.ucTableType               | Yes                      |
| metastore_id           | PropertyFacet.properties.ucMetastoreId             | No                       |
| browse_only            | PropertyFacet.properties.ucBrowseOnly              | No                       |
| securable_type         | PropertyFacet.properties.ucSecurableType           | No                       |
| securable_kind         | PropertyFacet.properties.ucSecurableKind           | No                       |
| resource_name          | PropertyFacet.properties.ucResourceName            | No                       |



| Additional Values                                         | Egeria Type and Attribute                                 | Supported in OSS Version |
|-----------------------------------------------------------|-----------------------------------------------------------|--------------------------|
| Unity Catalog Function: Server URL : full_name            | DeployedAPI.qualifiedName                      | Yes                      |
| Unity Catalog Function                                    | DeployedAPI.deployedImplementationType         | Yes                      |
| Databricks Unity Catalog Function: Server URL : full_name | DeployedAPI.qualifiedName                      | No                       |
| Databricks Unity Catalog Function                         | DeployedAPI.deployedImplementationType         | No                       |
| Server URL                                                | ExternalIdentifier.mappingProperties.serverNetworkAddress | Yes                      |
