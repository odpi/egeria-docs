<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property | Egeria Type and Attribute                          | Supported in OSS Version |
|------------------------|----------------------------------------------------|--------------------------|
| schema_id              | ExternalIdentifier.identifier                      | Yes                      |
| name                   | DeployedDatabaseSchema.name                        | Yes                      |
| full_name              | DeployedDatabaseSchema.resourceName                | Yes                      |
| comment                | DeployedDatabaseSchema.description                 | Yes                      |
| owner                  | Ownership.owner                                    | No                       |
| created_at             | ExternalIdentifier.externalInstanceCreationTime    | Yes                      |
| created_by             | ExternalIdentifier.externalInstanceCreatedBy       | No                       |
| updated_at             | ExternalIdentifier.externalInstanceLastUpdateTime  | Yes                      |
| updated_by             | ExternalIdentifier.externalInstanceLastUpdatedBy   | No                       |
| catalog_name           | ExternalIdentifier.mappingProperties.ucCatalogName | Yes                      |
| name                   | ExternalIdentifier.mappingProperties.ucSchemaName  | Yes                      |
| catalog_type           | PropertyFacet.properties.ucCatalogType             | No                       |
| metastore_id           | PropertyFacet.properties.ucMetastoreId             | No                       |
| browse_only            | PropertyFacet.properties.ucBrowseOnly              | No                       |
| securable_type         | PropertyFacet.properties.ucSecurableType           | No                       |
| securable_kind         | PropertyFacet.properties.ucSecurableKind           | No                       |
| properties             | PropertyFacet.properties                           | No                       |



| Additional Values                                       | Egeria Type and Attribute                                 | Supported in OSS Version |
|---------------------------------------------------------|-----------------------------------------------------------|--------------------------|
| Unity Catalog Schema: Server URL : full_name            | DeployedDatabaseSchema.qualifiedName                      | Yes                      |
| Unity Catalog Schema                                    | DeployedDatabaseSchema.deployedImplementationType         | Yes                      |
| Databricks Unity Catalog Schema: Server URL : full_name | DeployedDatabaseSchema.qualifiedName                      | No                       |
| Databricks Unity Catalog Schema                         | DeployedDatabaseSchema.deployedImplementationType         | No                       |
| Server URL                                              | ExternalIdentifier.mappingProperties.serverNetworkAddress | Yes                      |
