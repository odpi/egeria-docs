<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria Workspaces

[**Egeria Workspaces**](https://github.com/odpi/egeria-workspaces) offers a preconfigured, containerized Egeria environment that you can quickly download and run.  Once running, Egeria workspaces has an explorer web application, JupyterLab notebook environment, command line and a Markdown environment for activating Egeria's governance solutions and configuring them to work with your organization's digital resources.  There is also an MCP Server, Apache Web Server, Apache Kafka Event Bus, an Open Lineage Proxy and a PostgreSQL server to play with.

There are two choices of environment provided by Egeria Workspaces: **Quickstart** and **Freshstart**. You can select just one, or run them both together.

![Egeria Workspaces](egeria-workspaces-environments.svg)

If you are new to Egeria and want to find out what it does, you should start with the [Quickstart environment](/egeria-workspaces/quickstart).  If you are already familiar with Egeria and want to use it for your own projects, you should use the [Freshstart environment](/egeria-workspaces/freshstart).

## What is included?

The diagram below outlines what to expect in a Egeria Workspaces environment.  The components in blue are part of the basic Egeria environment that are started with either Quickstart and/or Freshstart.

![What is included](egeria-workspaces.svg)

There are also a number of containerized environments that you may wish to connect to Egeria.  These are the components in green.  They can be started with additional commands to expand the technologies working with the open metadata ecosystem.  For example:

* Apache Airflow and Marquez
* Apache Atlas,
* Apache Superset
* Unity Catalog
* Delta Lake, Apache Spark, Hive Metastore and Minio
* Milvus
* MLFlow
* Ollama

As you activate [Egeria's solutions](/egeria-solutions), the associate runtimes are connected to Egeria.

In addition, Egeria servers are automatically configured and started.  This gives you:

* A [View Server](/concepts/view-server) providing the [REST APIs](/services/omvs) for accessing Egeria's services.
* A [Metadata Access Store](/concepts/metadata-access-store) providing the metadata repository services backed by [PostgreSQL storage](/connectors/repository/postgres/overview).
* An [Integration Daemon](/concepts/integration-daemon) for running the integration connectors that synchronize metadata with different tools and runtimes.
* An [Engine Host](/concepts/engine-host) for running governance services both on the open metadata and the connected tools and runtimes.

![What is inside](egeria-workspaces-exposed.svg)

## Quickstart vs Freshstart

The table below summarizes the differences between the Quickstart and Freshstart environments.

| Content       | Quickstart                                | Freshstart                                |
|---------------|-------------------------------------------|-------------------------------------------|
| UserDirectory | coco-user-directory.omsecrets             | egeria-user-directory.omsecrets           |
|               |                                           |                                           |
| Port          | 9443                                      | 8443                                      |
|               |                                           |                                           |
| Content Packs | CoreContentPack.omarchive                 | CoreContentPack.omarchive                 |
| loaded at     | EgeriaContentPack.omarchive               | EgeriaContentPack.omarchive               |
| startup       | APIsContentPack.omarchive                 | APIsContentPack.omarchive                 |
|               | FilesContentPack.omarchive                | FilesContentPack.omarchive                |
|               | OpenLineageContentPack.omarchive          | OpenLineageContentPack.omarchive          |
|               | OpenMetadataDigitalProducts.omarchive     | OpenMetadataDigitalProducts.omarchive     |
|               | OrganizationInsightsContentPack.omarchive | OrganizationInsightsContentPack.omarchive |
|               | PostgresContentPack.omarchive             | PostgresContentPack.omarchive             |
|               | UnityCatalogContentPack.omarchive         |                                           |
|               | CocoComboArchive.omarchive                |                                           |
|               | CocoTypesArchive.omarchive                |                                           |
|               | SimpleCatalog.omarchive                   |                                           |

--8<-- "snippets/abbr.md"
