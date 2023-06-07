<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Data Engine Open Metadata Access Service (OMAS)

The Data Engine OMAS provides APIs and events for data movement/processing engines to record the changes made to the data landscape. 

It provides the ability to register the data engine itself along with the lineage details of the ETL transformations. 
Data Engine OMAS APIs offer support for creating the corresponding open metadata types for assets and jobs.
  
## Using the Data Engine OMAS

Below is the list of tasks supported by Data Engine OMAS.

#### External Tool registration

Typically, the first action to take for an external tool is to [register](register-data-engine-tool.md) as a 
[software-capability](../../../concepts/software-capability).

#### External Tool lookup

An external tool can [look up](lookup-registration.md) for the registered external tool.

#### [Create Schema Type](create-schema-type.md)

#### [Create Port Implementation with schema type](create-port-implementation.md)

#### [Create Process, with corresponding Port Implementations and Schema Types](create-process.md)

#### [Add data flows to processes](add-data-flows.md)

#### [Create Database](create-database.md) 

#### [Create Relational Tables](create-relational-table.md) 

#### [Create Data Files](create-data-file.md)

#### [Delete Database](delete-database.md)

#### [Delete Relational Tables](delete-relational-table.md)

#### [Delete Data Files](delete-data-file.md)

#### [Delete Connections](delete-connection.md)

#### [Delete Endpoint](delete-endpoint.md)


# Sample use case

[Initial load](initial-load-igc-data-stage.md) use case illustrates the integration between 
Data Engine OMAS and IBM's DataStage ETL tool.

--8<-- "snippets/abbr.md"
