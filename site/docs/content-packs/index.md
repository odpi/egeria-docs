<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Content Packs

The Egeria content packs provide a means to distribute standard metadata to different organizations. They are formatted as [Open Metadata Archives](/concepts/open-metadata-archive) and can be loaded using at server start up (see [Configuring the Start-up Archives](/guides/admin/servers/by-server-type/configuring-a-metadata-access-store)) or while the server is running (see [Runtime Manager OMVS](/services/omvs/runtime-manager/overview)).

The content packs are as follows:

* Technology Content Packs

    * [CoreContentPack](/content-packs/core-content-pack/overview) - contains the connector definitions for the Egeria and File System connectors and governance services supplied in the *omag-server-platform* distribution along with the valid metadata values for the technologies they support. This content pack is designed to provide a good starting point for a new Egeria deployment. It is loaded automatically in the active-metadata-store sample server.
  
    * [ApacheAtlasContentPack](/content-packs/apache-atlas-content-pack/overview) - contains the connector definitions for the Apache Atlas connectors and governance services supplied in the *omag-server-platform* distribution along with the valid metadata values for the technologies they support. This content pack is designed to provide a good starting point for connecting Egeria to Apache Atlas. 
  
    * [ApacheKafkaContentPack](/content-packs/apache-kafka-content-pack/overview) - contains the connector definitions for the Apache Kafka connectors and governance services supplied in the *omag-server-platform* distribution along with the valid metadata values for the technologies they support. This content pack is designed to provide a good starting point for connecting Egeria to Apache Kafka.

    * [APIsContentPack](/content-packs/apis-content-pack/overview) - contains the connector definitions for the connector the catalogs an open API through its swagger REST API.  This connector is supplied in the *omag-server-platform* distribution. This content pack is designed to provide a good starting point for connecting Egeria to applications supporting the open API specification in order to build an API catalog.
  
    * [ObservabilityContentPack](/content-packs/observability-content-pack/overview) - contains the connector definitions for the connectors that capture observations about the open metadata ecosystem.  These connectors are supplied in the *omag-server-platform* distribution. This content pack is designed to load a PostgreSQL database with key observations that can be used for building a dashboard.
  
    * [PostgreSQLContentPack](/content-packs/postgres-content-pack/overview) - contains the connector definitions for the PostgreSQL connectors and governance services supplied in the *omag-server-platform* distribution along with the valid metadata values for the technologies they support. This content pack is designed to provide a good starting point for connecting Egeria to PostgreSQL databases.
  
    * [UnityCatalogContentPack](/content-packs/unity-catalog-content-pack/overview) - contains the connector definitions for the Unity Catalog connectors and governance services supplied in the *omag-server-platform* distribution along with the valid metadata values for the technologies they support. This content pack is designed to provide a good starting point for connecting Egeria to Unity Catalog.
 
* [CloudInformationModel](/content-packs/cim-content-pack/overview) - glossary from the Cloud Information Model's JSONLD formatted model. The content covers basic commerce concepts such as Party, Product, Invoice and Shipping. The cloud information project has been archived. However, this is a useful starter set glossary,

* [OpenMetadataTypes](/content-packs/types-content-pack/overview) - Archive of the open metadata types defined by Egeria. This archive contains all the open metadata type definitions provided by Egeria. It is supplied for external utilities since each OMAG server capable of being a cohort member will load these types on start up.

* [CocoComboArchive](/content-packs/coco-content-pack/overview) - supplies metadata to support the Coco Pharmaceuticals scenarios. It is a useful content pack to load when experimenting with Egeria's capabilities since it provides examples of many types of open metadata. In addition, this metadata is also available in the following archives that are used in the Open Metadata Labs where different subsets of this metadata are loading into each of the servers.

    *  CocoBusinessSystemsArchive provides a catalog of the business systems and the lineage between them and the load of their data into the data lake. This archive simulates the type of metadata expected from an ETL tool suite. It is intended for cocoMDS5 in the open metadata labs but can be used in any server.

    *  CocoOrganizationArchive - provides the profiles, user identifies and team of the featured personas of Coco Pharmaceuticals.

    *  CocoClinicalTrialsTemplatesArchive - provides the template assets used for onboarding weekly patient measurements during a clinical trial.

    *  CocoGovernanceProgramArchive - provides the metadata to describe Coco Pharmaceuticals governance program.

    *  CocoGovernanceEngineDefinitionsArchive - provides the metadata to describe Coco Pharmaceuticals three governance engines: AssetGovernance, AssetDiscovery and AssetQuality.

    *  CocoSustainabilityArchive - provides the base definitions for Coco Pharmaceutical's sustainability initiative.

    *  CocoTypesArchive - provides additional types for Coco Pharmaceuticals. These are BiopsyScope Enum, BiopsyReport Entity, BiopsySupportingEvidence Relationship and ReviewedByClinicalTrials Classification.

* [SimpleCatalog](/content-packs/simple-content-pack/overview) - provides an example of a database, an API and an event structure linked to a glossary term. It is loaded automatically in the simple-metadata-store sample server. SimpleCatalog is also supplied as four archives for use in a demo showing 4 metadata access servers connected together in a single cohort. The archives are each loaded into a different server. It is then possible to show how the cohort integrates metadata from different catalogs. These archives are used in the Development labs which are part of the Open Metadata Labs.

    *  SimpleAPICatalog - API metadata typically found in an API catalog.

    *  SimpleDataCatalog - Database metadata typically found in an Data catalog.

    *  SimpleEventCatalog - Event metadata typically found in an API catalog.

    *  SimpleGovernanceCatalog - A glossary term linked to metadata elements in the API, Event, Data catalogs.


--8<-- "snippets/abbr.md"