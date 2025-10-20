<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Tabular Data Set

A *Tabular Data Set* is logical collection of data that is organized in a tabular format.  It is typically a view over a tabular data store such as an Apache Parquet file, CSV File, or relational database table.
Similarly, a *Tabular Data Set Collection* is a collection of related tabular data sets.

Egeria's [Open Connector Framework (OCF)](/frameworks/ocf/overview) defines a standard connector interface for accessing different implementations of a tabular data set and tabular data set collection.  This means that [governance action services](/concepts/governance-action-services) and [integration connectors](/concepts/integration-connector) can operate on tabular data stored in many types of technologies without needing to know the specifics of the underlying technology.

Typically, the tabular data set connectors for a particular technology type are implemented as a pair: one for the tabular data set itself, and one for a collection of tabular data sets.  For example, the connector for a CSV file-based tabular data set has a companion connector that supports a file directory (folder) of CSV Files.  Similarly, the connector for a PostgreSQL table-based tabular data set has a companion connector for a PostgreSQL Schema that manages a collection of PostgreSQL tables.



???+ info "Additional information"
    * The open metadata types for tabular data sets are found in [Model 0211 Tabular Data Sets](/types/2/0211-Tabular-Data-Sets/).
    * The Javadoc for the tabular data set connector interfaces are found in Java package [org.odpi.openmetadata.frameworks.connectors.tabulardatasets](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/connectors/tabulardatasets/package-summary.html).


--8<-- "snippets/abbr.md"
