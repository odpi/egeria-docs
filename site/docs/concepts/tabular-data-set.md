<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Tabular Data Set

A *Tabular Data Set* is a collection of data that is organized in a tabular format.  It is typically a view over a tabular data store such as an Apache Parquet file, CSV File, or relational database table.  Alternatively, it may represent a query that returns a tabular result. For example, the [Open Metadata Digital Product Catalog](/patterns/harvest-and-publish/overview) uses tabular data sets to support digital products based on open metadata.

A *Tabular Data Set Collection* is a collection of related tabular data sets.  For example, aa database schema is a collections of database tables and a file directory can hold a collection of CSV of Parquet files.


???+ info "Additional information"
    * The open metadata types for tabular data sets are found in [Model 0211 Tabular Data Sets](/types/2/0211-Tabular-Data-Sets/).
    * The Javadoc for the tabular data set connector interfaces are found in Java package [org.odpi.openmetadata.frameworks.connectors.tabulardatasets](https://odpi.github.io/egeria/org/odpi/openmetadata/frameworks/connectors/tabulardatasets/package-summary.html).
    * The [Data Engineer](/services/omvs/data-engineer/overview) API has an operation that supports the retrieval of data from a tabular data set.


--8<-- "snippets/abbr.md"
