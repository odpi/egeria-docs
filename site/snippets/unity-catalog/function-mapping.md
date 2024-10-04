<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


| Unity Catalog Property                          | Egeria Type and Attribute                                                                               | Supported in OSS Version |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------|
| function_id                                     | ExternalIdentifier.identifier                                                                           | Yes                      |
| name                                            | DeployedAPI.name + DeployedSoftwareComponent.name + ExternalIdentifier.mappingProperties.ucFunctionName | Yes                      |
| full_name                                       | DeployedAPI.resourceName                                                                                | Yes                      |
| comment                                         | DeployedAPI.description                                                                                 | Yes                      |
| owner                                           | Ownership.owner                                                                                         | No                       |
| input_parameters.parameters.name                | APIParameter.displayName                                                                                | Yes                      |
| input_parameters.parameters.comment             | APIParameter.description                                                                                | Yes                      |
| input_parameters.parameters.position            | APIParameter.position                                                                                   | Yes                      |
| input_parameters.parameters.nullable            | APIParameter.isNullable                                                                                 | Yes                      |
| input_parameters.parameters.type_precision      | APIParameter.precision                                                                                  | Yes                      |
| input_parameters.parameters.type_scale          | APIParameter.significantDigits                                                                          | Yes                      |
| input_parameters.parameters.type_text           | TypeEmbeddedAttribute.displayName                                                                       | Yes                      |
| input_parameters.parameters.type_name           | TypeEmbeddedAttribute.dataType                                                                          | Yes                      |
| input_parameters.parameters.parameter_default   | TypeEmbeddedAttribute.defultValue                                                                       | Yes                      |
| input_parameters.parameters.type_interval_type  | TypeEmbeddedAttribute.additionalProperties.ucTypeIntervalType                                           | Yes                      |
| input_parameters.parameters.type_json           | TypeEmbeddedAttribute.additionalProperties.ucTypeJSON                                                   | Yes                      |
| input_parameters.parameters.parameter_mode      | APIParameter.additionalProperties.ucParameterMode                                                       | Yes                      |
| input_parameters.parameters.parameter_type      | APIParameter.parameterType                                                                              | Yes                      |
| return_parameters                               | DataAssetEncoding.encoding                                                                              | Yes                      |
| return_parameters.parameters.name               | APIParameter.displayName                                                                                | Yes                      |
| return_parameters.parameters.comment            | APIParameter.description                                                                                | Yes                      |
| return_parameters.parameters.position           | APIParameter.position                                                                                   | Yes                      |
| return_parameters.parameters.nullable           | APIParameter.isNullable                                                                                 | Yes                      |
| return_parameters.parameters.type_precision     | APIParameter.precision                                                                                  | Yes                      |
| return_parameters.parameters.type_scale         | APIParameter.significantDigits                                                                          | Yes                      |
| return_parameters.parameters.type_text          | TypeEmbeddedAttribute.displayName                                                                       | Yes                      |
| return_parameters.parameters.type_name          | TypeEmbeddedAttribute.dataType                                                                          | Yes                      |
| return_parameters.parameters.parameter_default  | TypeEmbeddedAttribute.defultValue                                                                       | Yes                      |
| return_parameters.parameters.type_interval_type | TypeEmbeddedAttribute.additionalProperties.ucTypeIntervalType                                           | Yes                      |
| return_parameters.parameters.type_json          | TypeEmbeddedAttribute.additionalProperties.ucTypeJSON                                                   | Yes                      |
| return_parameters.parameters.parameter_mode     | APIParameter.additionalProperties.ucParameterMode                                                       | Yes                      |
| return_parameters.parameters.parameter_type     | APIParameter.parameterType                                                                              | Yes                      |
| created_at                                      | ExternalIdentifier.externalInstanceCreationTime                                                         | Yes                      |
| created_by                                      | ExternalIdentifier.externalInstanceCreatedBy                                                            | No                       |
| updated_at                                      | ExternalIdentifier.externalInstanceLastUpdateTime                                                       | Yes                      |
| updated_by                                      | ExternalIdentifier.externalInstanceLastUpdatedBy                                                        | No                       |
| catalog_name                                    | ExternalIdentifier.mappingProperties.ucCatalogName                                                      | Yes                      |
| schema_name                                     | ExternalIdentifier.mappingProperties.ucSchemaName                                                       | Yes                      |
| storage_location                                | PropertyFacet.properties.ucStorageLocation                                                              | Yes                      |
| data_type                                       | PropertyFacet.properties.ucFunctionDataType                                                             | Yes                      |
| full_data_type                                  | PropertyFacet.properties.ucFunctionFullDataType                                                         | Yes                      |
| routine_parameter_style                         | PropertyFacet.properties.ucRoutineParameterStyle                                                        | Yes                      |
| security_type                                   | PropertyFacet.properties.ucSecurityType                                                                 | Yes                      |
| specific_name                                   | PropertyFacet.properties.ucSpecificName                                                                 | Yes                      |
| metastore_id                                    | PropertyFacet.properties.ucMetastoreId                                                                  | No                       |
| browse_only                                     | PropertyFacet.properties.ucBrowseOnly                                                                   | No                       |
| securable_type                                  | PropertyFacet.properties.ucSecurableType                                                                | No                       |
| securable_kind                                  | PropertyFacet.properties.ucSecurableKind                                                                | No                       |
| resource_name                                   | PropertyFacet.properties.ucResourceName                                                                 | No                       |
| routine_dependencies                            | ProcessCall relationship                                                                                | Yes                      |
| routine_definition                              | DeployedSoftwareComponent.description                                                                   | Yes                      |
| external_language                               | DeployedSoftwareComponent.implementationLanguage                                                        | Yes                      |
| is_null_call                                    | DeployedSoftwareComponent.additionalProperties.ucIsNullCall                                             | Yes                      |
| sql_data_access                                 | DeployedSoftwareComponent.additionalProperties.ucSQLDataAccess                                          | Yes                      |
| is_deterministic                                | DeployedSoftwareComponent.additionalProperties.ucIsDeterministic                                        | Yes                      |
| routine_body                                    | DeployedSoftwareComponent.additionalProperties.ucRoutineBodyType                                        | Yes                      |



| Additional Values                                         | Egeria Type and Attribute                                                                     | Supported in OSS Version |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------|
| Unity Catalog Function: Server URL : full_name            | DeployedAPI.qualifiedName                                                                     | Yes                      |
| Unity Catalog Function                                    | DeployedAPI.deployedImplementationType + DeployedSoftwareComponent.deployedImplementationType | Yes                      |
| Databricks Unity Catalog Function: Server URL : full_name | DeployedAPI.qualifiedName                                                                     | No                       |
| Databricks Unity Catalog Function                         | DeployedAPI.deployedImplementationType + DeployedSoftwareComponent.deployedImplementationType | No                       |
| Server URL                                                | ExternalIdentifier.mappingProperties.serverNetworkAddress                                     | Yes                      |
