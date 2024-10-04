<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property     | Egeria Type and Attribute                                                      | Supported in OSS Version |
|----------------------------|--------------------------------------------------------------------------------|--------------------------|
| table_id                   | ExternalIdentifier.identifier                                                  | Yes                      |
| name                       | VirtualRelationalTable.name + ExternalIdentifier.mappingProperties.ucTableName | Yes                      |
| full_name                  | VirtualRelationalTable.resourceName                                            | Yes                      |
| comment                    | VirtualRelationalTable.description                                             | Yes                      |
| owner                      | Ownership.owner                                                                | No                       |
| data_source_format         | DataAssetEncoding.encoding                                                     | Yes                      |
| columns.name               | RelationalColumn.displayName                                                   | Yes                      |
| columns.comment            | RelationalColumn.description                                                   | Yes                      |
| columns.position           | RelationalColumn.position                                                      | Yes                      |
| columns.nullable           | RelationalColumn.isNullable                                                    | Yes                      |
| columns.type_precision     | RelationalColumn.precision                                                     | Yes                      |
| columns.type_scale         | RelationalColumn.significantDigits                                             | Yes                      |
| columns.partition_index    | RelationalColumn.additionalProperties.ucPartitionIndex                         | Yes                      |
| columns.type_text          | TypeEmbeddedAttribute.displayName                                              | Yes                      |
| columns.type_name          | TypeEmbeddedAttribute.dataType                                                 | Yes                      |
| columns.type_interval_type | TypeEmbeddedAttribute.additionalProperties.ucTypeIntervalType                  | Yes                      |
| columns.type_json          | TypeEmbeddedAttribute.additionalProperties.ucTypeJSON                          | Yes                      |
| created_at                 | ExternalIdentifier.externalInstanceCreationTime                                | Yes                      |
| created_by                 | ExternalIdentifier.externalInstanceCreatedBy                                   | No                       |
| updated_at                 | ExternalIdentifier.externalInstanceLastUpdateTime                              | Yes                      |
| updated_by                 | ExternalIdentifier.externalInstanceLastUpdatedBy                               | No                       |
| catalog_name               | ExternalIdentifier.mappingProperties.ucCatalogName                             | Yes                      |
| schema_name                | ExternalIdentifier.mappingProperties.ucSchemaName                              | Yes                      |
| storage_location           | PropertyFacet.properties.ucStorageLocation                                     | Yes                      |
| table_type                 | PropertyFacet.properties.ucTableType                                           | Yes                      |
| metastore_id               | PropertyFacet.properties.ucMetastoreId                                         | No                       |
| browse_only                | PropertyFacet.properties.ucBrowseOnly                                          | No                       |
| securable_type             | PropertyFacet.properties.ucSecurableType                                       | No                       |
| securable_kind             | PropertyFacet.properties.ucSecurableKind                                       | No                       |
| resource_name              | PropertyFacet.properties.ucResourceName                                        | No                       |



| Additional Values                                      | Egeria Type and Attribute                                 | Supported in OSS Version |
|--------------------------------------------------------|-----------------------------------------------------------|--------------------------|
| Unity Catalog Table: Server URL : full_name            | VirtualRelationalTable.qualifiedName                      | Yes                      |
| Unity Catalog Table                                    | VirtualRelationalTable.deployedImplementationType         | Yes                      |
| Databricks Unity Catalog Table: Server URL : full_name | VirtualRelationalTable.qualifiedName                      | No                       |
| Databricks Unity Catalog Table                         | VirtualRelationalTable.deployedImplementationType         | No                       |
| Server URL                                             | ExternalIdentifier.mappingProperties.serverNetworkAddress | Yes                      |
