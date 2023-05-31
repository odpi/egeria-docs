<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/tech-preview.md"

# Data Engine Open Metadata Access Service (OMAS)

The Data Engine OMAS provides APIs and events for data movement/processing engines to record the changes made to the data landscape. 

It provides the ability to register the data engine itself along with the lineage details of the ETL transformations. 
Data Engine OMAS APIs offer support for creating the corresponding open metadata types for assets and jobs.
  
## Using the Data Engine OMAS
Below is the list of tasks supported by Data Engine OMAS.

#### [External Tool registration](register-data-engine-tool.md)
Typically, the first action to take for an external tool is to register as an
[engine](https://egeria-project.org/concepts/software-capability/#engine).

#### [External Tool lookup](lookup-registration.md)

#### [Create Schema Type](create-schema-type.md)

#### [Create Port Implementation with schema type](create-port-implementation.md)

#### [Create Process, with corresponding Port Implementations and Schema Types](create-process.md)

#### [Add data flows to processes](add-data-flows.md)

#### [Delete Schema Type](delete-schema-type.md)

#### [Delete Port Implementation](delete-port-implementation.md)

#### [Delete Process](delete-process.md)

#### [Create Database](create-database.md)

#### [Create Database Schema](create-database-schema.md)

#### [Create Relational Tables](create-relational-table.md)

#### [Create Data Files](create-data-file.md)

#### [Delete Database](delete-database.md)

#### [Delete Database Schema](delete-database-schema.md)

#### [Delete Relational Tables](delete-relational-table.md)

#### [Delete Data Files](delete-data-file.md)

#### [Delete Connections](delete-connection.md)

#### [Delete Endpoint](delete-endpoint.md)

#### [Create Topic](create-topic.md)

#### [Create EventType](create-event-type.md)

#### [Delete Topic](delete-topic.md)

#### [Delete EventType](delete-event-type.md)

#### [Find an entity](find-entity.md)

# Sample use case

[Initial load](initial-load-igc-data-stage.md) use case illustrates the integration between
Data Engine OMAS and IBM's DataStage ETL tool.

--8<-- "snippets/abbr.md"
