---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Apache Atlas estate

--8<-- "snippets/work-in-progress.md"

[Apache Atlas](https://atlas.apache.org) is a metadata catalog originally designed for the Hadoop ecosystem.  It offers integration services called Hooks and Bridges to capture the schemas and data sets of data platforms such as [Apache Hive](https://hive.apache.org/), [Apache HBase](https://hbase.apache.org/) and [Apache Hadoop Distributed File System (HDFS)](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html) along with the processes for creating and maintaining data sets on these platforms.  The metadata descriptions of these data sets and processes are linked together using lineage relationships, allowing an understanding of how data is flowing through a Hadoop deployment.  Apache Atlas also supports glossaries and a tagging system that can be used both in searches and to control access to data through Apache Ranger (using the TagSync integration).

In recent years, Apache Atlas has been embedded in popular data catalogs such as [Microsoft Purview](https://azure.microsoft.com/en-gb/products/purview/) and [Atlan](https://atlan.com/) increasing the interest in being able to integrate with this metadata catalog.



???+ info "Further information"

    - [Apache Atlas](https://atlas.apache.org/)
    - [Comparison between Apache Atlas and Egeria](apache-atlas-vs-egeria.md)
    - [Apache Atlas Connectors from Egeria](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors) - The Apache Atlas connectors provide a suite of function that integrates an Apache Atlas server into the open metadata ecosystem.

       * *Apache Atlas REST Connector* provides a Java interface to the Apache Atlas REST APIs.
       * *Apache Atlas Survey Service* builds a discovery analysis report on the contents of an Apache Atlas metadata repository.
       * *Apache Atlas Integration Connector* synchronizes metadata between Apache Atlas and the open metadata ecosystem.


--8<-- "snippets/abbr.md"