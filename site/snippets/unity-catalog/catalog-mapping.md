<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property          | Egeria Type and Attribute                               | Supported in OSS Version |
|---------------------------------|---------------------------------------------------------|--------------------------|
| id                              | ExternalIdentifier.identifier                           | Yes                      |
| name                            | Catalog.name                                            | Yes                      |
| comment                         | Catalog.description                                     | Yes                      |
| owner                           | Ownership.owner                                         | No                       |
| name                            | ExternalIdentifier.mappingProperties.ucCatalogName      | Yes                      |
| created_at                      | ExternalIdentifier.externalInstanceCreationTime         | Yes                      |
| created_by                      | ExternalIdentifier.externalInstanceCreatedBy            | No                       |
| updated_at                      | ExternalIdentifier.externalInstanceLastUpdateTime       | Yes                      |
| updated_by                      | ExternalIdentifier.externalInstanceLastUpdatedBy        | No                       |
| catalog_type                    | PropertyFacet.properties.ucCatalogType                  | No                       |
| metastore_id                    | PropertyFacet.properties.ucMetastoreId                  | No                       |
| isolation_mode                  | PropertyFacet.properties.ucIsolationMode                | No                       |
| accessible_in_current_workspace | PropertyFacet.properties.ucAccessibleInCurrentWorkspace | No                       |
| browse_only                     | PropertyFacet.properties.ucBrowseOnly                   | No                       |
| securable_type                  | PropertyFacet.properties.ucSecurableType                | No                       |
| securable_kind                  | PropertyFacet.properties.ucSecurableKind                | No                       |



| Additional Values                             | Egeria Type and Attribute                                 | Supported in OSS Version |
|-----------------------------------------------|-----------------------------------------------------------|--------------------------|
| Unity Catalog Catalog: Server URL : full_name | Catalog.qualifiedName                                     | Yes                      |
| Unity Catalog Catalog                         | Catalog.deployedImplementationType                        | Yes                      |
| Databricks Unity Catalog Catalog: Server URL  | Catalog.qualifiedName                                     | No                       |
| Databricks Unity Catalog Catalog              | Catalog.deployedImplementationType                        | No                       |
| Server URL                                    | ExternalIdentifier.mappingProperties.serverNetworkAddress | Yes                      |
