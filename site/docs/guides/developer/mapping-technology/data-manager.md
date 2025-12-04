<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


# Data Manager

## Basic metadata model

Figure 1 shows the types of metadata captured by the Data Manager.

![Figure 1](basic-model.svg)
> **Figure 1:** Basic metadata capture by the Data Manager

These are:

* **Asset** - Asset describes the digital resource such as the data set, database schema, topic, API etc.
* **Connection**, **Connector Type** and **Endpoint** are used to create a [connector](/concepts/connector)
to access the data in the data asset.
* **Schema Element(s)** describe the structure of the data managed by the data asset.

To make it possible to search for particular types of asset, there are many specialized asset types defined in Egeria.
The full list is shown [here](/concepts/asset), however Data Manager OMAS supports
the following subtypes of Asset (and any additional subtypes of these types that you wish to define yourself).

* **DeployedAPI** for API descriptions.
* **Topic** for topics supported by an event manager.
* **DataFile** for a file with sub types of:
   * **CSVFile** for CSV files.
   * **AvroFile** for files using the Avro format.
   * **JSONFile** for files using the JSON format.
* **Database** for databases.
* **DeployedDatabaseSchema** for schemas within a database.
* **DeployedReport** for reports.
* **Form** for interactive forms.
* **InformationView** for queries.


The Data Manager OMAS APIs needs to accommodate slight variations between different vendor
implementations of data managers, along with information relating to local deployment standards.
As such there is provision in these interfaces to support:

* `VendorProperties` for properties unique to a specific vendor implementation, and
* `AdditionalProperties` for properties that the metadata team wish to add to the metadata.

## Data Managers

The Data Manager OMAS Supports the following types of data managers:

| Icon                                   | Name     | Provenance | Description |
| :----------------------------------:   | :---------- | :------------------------------------------------------: | :---------- |
| ![File System](files/file-system.svg)   | File System | Local Cohort | Create metadata elements for files and folders along with their data connections and any known schema information. Catalogued files and folders are members of the local cohort because many different types of processes may work with them. |
| ![File Manager](files/file-manager.svg) | File Manager | External  | Create metadata elements for files and folders along with their data connections and any known schema information. Catalogued files and folders are members of the data manager's metadata collection because it is responsible for their maintenance.|
| ![Database System](databases/database-server.svg) | Database Manager | External | Create metadata elements for databases, database schemas, tables, views, columns, primary keys and foreign keys. Catalogued elements are members of the data manager's metadata collection because it is responsible for their maintenance.|
| ![Event Manager](topics/event-broker.svg) | Event Broker | Local Cohort or External | Create metadata elements for topics and the event payloads they support. Catalogued elements are members of the data manager's metadata collection (ie External provenance) if it is responsible for their maintenance.|
| ![API Gateways](api-gateway.svg) | API Manager | Local Cohort or External | Create metadata elements for APIs and their supported headers and payloads. Catalogued elements are members of the data manager's metadata collection (ie External provenance) if it is responsible for their maintenance.|
| ![Display Tools](displays/display-tools.svg) | Display Tools | Local Cohort or External | Create metadata elements for reporting tools, forms and associated queries. Catalogued elements are members of the data manager's metadata collection (ie External provenance) if it is responsible for their maintenance.|


## More information

* [What is an Asset?](/concepts/asset)
* [Building an asset catalog](/concepts/basic-concepts/#metadata-manager)
* [Modeling schema structures](/concepts/schema)


--8<-- "snippets/abbr.md"
