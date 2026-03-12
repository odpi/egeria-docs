---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your PostgreSQL estate

--8<-- "snippets/work-in-progress.md"



### PostgreSQL Connectors

* The [JDBC Resource Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) is for accessing a database via the JDBC DataSource interface.
* The [JDBC Integration Connector](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/jdbc-integration-connector) automatically maintains the open metadata instances on a database server via JDBC. This includes the database schemas, tables, columns, primary keys and foreign keys.
* The [PostgreSQL connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/postgres-server-connectors) extend the JDBC connector capability by using PostgreSQL specific APIs and queries to its catalog:


--8<-- "snippets/abbr.md"