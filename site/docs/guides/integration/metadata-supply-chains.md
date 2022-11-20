<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

## Metadata supply chains

The open metadata ecosystem collects, links and disseminates metadata from many sources.  However, it is designed in an iterative, agile manner, adding new use cases and capabilities over time.

Each stage of development considers a particular source of metadata and where it needs to be distributed to.  Consider this scenario...  

!!! example "Database schema capture and distribution"
    There is a database server (*Database Server 1*) that is used to store application data that is of interest to other teams.  An initiative is started to automatically capture the schemas of the databases on this database server.  This schema information will be replicated to two destinations:

    * Another database server (*Database Server 2*) is used by a data science team as a source of data for their work.  An ETL job runs every day to refresh the data in this second database with data from the first database.  The data is anonymized by the ETL job, but the schema and data profile remains consistent.  If the schema in the first database changes, the ETL job is updated at the same time.  However, the schema in the second database is not updated because the team making the change do not have access to it.  Nevertheless it must be updated consistently before the ETL job runs; otherwise it will fail.
    * The analytics tool that is also used by the data science team has a catalog of data sources to show the data science team what data is available.  This needs to be kept consistent with the structure of the databases.  The tool does provide a feature to refresh any data source schema in its catalog, but the team are often unaware of changes to their data sources, or simply forget to do it, and only discover the inconsistency when their models fail to run properly.

    ![metadata supply chain scenario](/guides/integration/metadata-supply-chains-scenario.svg)

The integration of these third party technologies with the open metadata ecosystem can be thought of as having four parts to it.

1. Any changes to the database schema are extracted from *Database Server 1* and published to the open metadata ecosystem.
2. The new schema information from *Database Server 1* is detected in the open metadata ecosystem and deployed to *Database Server 2*.
3. The changes to *Database Server 2*'s schema are detected and published to the open metadata ecosystem.
4. The new schema information from *Database Server 2* is detected in the open metadata ecosystem and distributed to the *Analytics Workbench*.

![metadata supply chain integration points](/guides/integration/integration-points.svg)
> Four integration steps to capture and distribute the database schema metadata from *Database Server 1*.

Here is another view of the process, but shown as a flow from left to right.

![Metadata supply chain integration points](/guides/integration/metadata-supply-chain.svg)

At each stage, there is a trigger (typically detecting something has changed), metadata is assembled, updated and when it is read, made visible through the open metadata ecosystem.

![Metadata Update Specification Pattern](/patterns/metadata-governance/metadata-update-specification-pattern.svg)
> A three-step specification pattern of *Trigger*, *Maintain Metadata* and *Make Visible*.


The implementation of the three-step pattern for each part of the integration is located in an [integration connector](/concepts/integration-connector).  Integration connectors are configurable components that are designed to work with a specific third party technology.  There would be 4 configured integration connectors to support the scenario above.  However, the implementation of the integration connectors for parts 1 and 3 would be the same implementation, just 2 instances, each configured to work with a different database server.

The integration connectors supplied with Egeria are described in the [connector catalog](/connectors/#integration-connectors).  It is also possible to write your own integration connectors if the ones supplied by Egeria do not meet your needs.

Integration connectors run in the [Integration Daemon](/concepts/integration-daemon).  It is possible to have all 4 integration connectors running in the same integration daemon.  Alternatively, they each may run in a different integration daemon - or any combination in between.  The choice is determined by the organization of the teams that will operate the service.  For example, if this metadata synchronization process was run by a centralized team, then all 4 integration connectors would probably run in the same integration daemon.  If the work is decentralized, the integration connector for part 1 may be in an integration daemon operated by the same team that operates *Database Server 1*.  The other integration connectors may run together in an integration daemon operated by the team that operates *Database Server 2* and the *Analytics Workbench*.

The diagram below shows the decentralized option.

![Decentralized deployment](/guides/integration/decentralized-integration-daemons.svg)

This type of deployment choice keeps control of the metadata integration with the teams that own the third party technology, and so upgrades, back-ups and outages can be coordinated.

The implementation of the open metadata ecosystem that connects the integration daemons can also be centralized or decentralized.  This next diagram shows two integration daemons connecting into a centralized [metadata access store](/concepts/metadata-access-store) that provides the open metadata repository.

![Centralized metadata store](/guides/integration/centralized-metadata-store.svg)

Alternatively, each team could have their own metadata access store, giving them complete control over their metadata.  The two metadata access stores are connected via an [Open Metadata Repository Cohort](/features/cohort-operation/overview) (or just "cohort" for short.)  The cohort enables the two metadata access stores to operate as one logical metadata store.

![Decentralized metadata stores with cohort](/guides/integration/decentralized-metadata-stores.svg)

The behaviour of the integration daemons is unaffected by the deployment choice made for the metadata access stores.

### Adding lineage

In the scenario above, data from *Database Server 1* is extracted, anonymized and stored in *Database Server 2* by an ETL job running in an ETL engine.

![Role of the ETL engine](/guides/integration/etl-engine.svg)

The data scientist team want to know the source of each of the databases they are working with.  The metadata that describes the source of data is called [lineage](/concepts/lineage).  Ideally it is captured by the ETL engine to ensure it is accurate.

ETL engines have a long history of capturing lineage, since it is a common requirement in regulated industries.  The diagram below shows three choices on how an ETL engine may handle its lineage metadata.

* In the first box on the left, the ETL engine has its own metadata repository and so it is integrated into the open metadata ecosystems via the integration daemon (in the same way as the database and analytics workbench).
* In the middle box, the ETL engine is producing lineage events that follow the [OpenLineage Standard](/features/lineage-management/overview/#the-openlineage-standard).  The integration daemon has native support for this standard and so the ETL Engine can send these events directly to the integration daemon which will pass them to any integration connector that is configured to receive them.
* The final box on the right-hand side shows an ETL engine that is part of a suite of tools that share a metadata repository.  These types of third party metadata repositories often have a wide variety of metadata that is good for many use cases. So, although it is possible to integrate them through the integration connectors running in the integration daemon, it is also possible to connect them directly into the cohort via a [Repository Proxy](/concepts/repository-proxy).  This is a more complex integration to perform.  However, it has the benefit that the metadata stored in the third party metadata repository is logically part of the open metadata ecosystem and available through any of the open metadata and governance APIs without needing to copy its metadata into a metadata access store.

![Choices when integrating lineage](/guides/integration/integrating-lineage.svg)

!!! summary "Summary"

    In this guide your have seen that integration with the open metadata ecosystem is built up iteratively using *integration connectors* running in an *integration daemon*.  Open metadata is stored in *metadata access stores* and shared across the open metadata ecosystem using a *cohort*.  It is also possible to plug in a third party metadata repository using a *repository proxy*.

    ![Complete integration solution](/guides/integration/integrated-solution.svg)

!!! education "Related information"
    - [Choosing the integration style for metadata repositories/catalogs](/guides/integration/types-of-metadata-repository)
    - [Building an integration connector](/guides/developer/integration-connectors/overview)
    - [Building a repository connector](/guides/developer/repository-connectors/overview)

--8<-- "snippets/abbr.md"