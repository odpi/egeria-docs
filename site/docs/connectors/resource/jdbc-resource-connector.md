<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->
  
--8<-- "snippets/content-status/tech-preview.md"

# JDBC Resource Connector

???+ info "Connector summary"
    - Connector Category: [Digital Resource Connector](/concepts/digital-resource-connector)
    - Source Module: [jdbc resource connector :material-github:](https://github.com/odpi/egeria-database-connectors/tree/main/jdbc-resource-connector){ target=gh }.
    - Jar File Name: `jdbc-resource-connector.jar`


The JDBC Resource Connector provides a DataSource, which in turn is used to get a connection to underlying database.  It provides access to both the schema metadata and the business data content.

![Figure 1](jdbc-resource-connector.svg)
> **Figure 1:** JDBC resource connector


## Usage

The connector is initialized using the connection information attached to the [Database](/types/2/0224-Databases) asset in open metadata.

![Figure 2](jdbc-resource-connector-use.svg)
> **Figure 2:** Connection information used to create an instance of the JDBC resource connector

