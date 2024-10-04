<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property | Egeria Type and Attribute                                                                  | Supported in OSS Version |
|------------------------|--------------------------------------------------------------------------------------------|--------------------------|
| volume_id              | ExternalIdentifier.identifier                                                              | Yes                      |
| name                   | FileFolder.name                                                                            | Yes                      |
| full_name              | FileFolder.resourceName                                                                    | Yes                      |
| comment                | FileFolder.description                                                                     | Yes                      |
| storage_location       | FileFolder.pathName + Endpoint.networkAddress + PropertyFacet.properties.ucStorageLocation | Yes                      |
| owner                  | Ownership.owner                                                                            | No                       |
| created_at             | ExternalIdentifier.externalInstanceCreationTime                                            | Yes                      |
| created_by             | ExternalIdentifier.externalInstanceCreatedBy                                               | No                       |
| updated_at             | ExternalIdentifier.externalInstanceLastUpdateTime                                          | Yes                      |
| updated_by             | ExternalIdentifier.externalInstanceLastUpdatedBy                                           | No                       |
| catalog_name           | ExternalIdentifier.mappingProperties.ucCatalogName                                         | Yes                      |
| schema_name            | ExternalIdentifier.mappingProperties.ucSchemaName                                          | Yes                      |
| volume_type            | PropertyFacet.properties.ucVolumeType                                                      | Yes                      |
| metastore_id           | PropertyFacet.properties.ucMetastoreId                                                     | No                       |
| browse_only            | PropertyFacet.properties.ucBrowseOnly                                                      | No                       |
| securable_type         | PropertyFacet.properties.ucSecurableType                                                   | No                       |
| securable_kind         | PropertyFacet.properties.ucSecurableKind                                                   | No                       |
| resource_name          | PropertyFacet.properties.ucResourceName                                                    | No                       |



| Additional Values                                       | Egeria Type and Attribute                                 | Supported in OSS Version |
|---------------------------------------------------------|-----------------------------------------------------------|--------------------------|
| Unity Catalog Volume: Server URL : full_name            | FileFolder.qualifiedName                                  | Yes                      |
| Unity Catalog Volume                                    | FileFolder.deployedImplementationType                     | Yes                      |
| Databricks Unity Catalog Volume: Server URL : full_name | FileFolder.qualifiedName                                  | No                       |
| Databricks Unity Catalog Volume                         | FileFolder.deployedImplementationType                     | No                       |
| Server URL                                              | ExternalIdentifier.mappingProperties.serverNetworkAddress | Yes                      |
