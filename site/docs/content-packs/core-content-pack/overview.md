<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Core Content Pack

The *CoreContentPack* is the foundation that every other Egeria content pack builds on.  It describes the connectors supplied with Egeria, the technologies they work with and the valid values used to describe them, and it configures the integration connectors and governance engines that look after the open metadata ecosystem itself.  It also supplies generic templates for cataloguing common technologies, a design library describing how Egeria is put together, and a small set of widely used security definitions.

This content pack is designed to provide a good starting point for a new Egeria deployment.  It is loaded automatically in the *active-metadata-store* sample server used by the quickstart.  As it loads, the integration connectors defined in its content start up in the *integration-daemon* server, and the governance engines it defines start up in the *engine-host*.

The content pack is found in the `CoreContentPack.omarchive` file in the `content-packs` directory of the distribution.  It has no dependencies on other content packs - the technology content packs, such as the [Files](/content-packs/files-content-pack/overview), [Egeria](/content-packs/egeria-content-pack/overview) and [Open Lineage](/content-packs/open-lineage-content-pack/overview) content packs, depend on it.  It is built by the [core-content-pack :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/core-content-pack){ target=gh } module.

## How the pieces fit together

The content falls into three layers:

* **Descriptions of the technology** - the [connector types](/concepts/connector-type) for Egeria's connectors, the [technology types](/concepts/deployed-implementation-type) that describe the kinds of resources they work with, and the valid metadata values for the properties used in open metadata.  Every other content pack refers to these elements rather than defining its own.
* **Active services** - the [integration groups](/concepts/integration-group) that run the *nanny connectors* in the [integration daemon](/concepts/integration-daemon), and the [governance engines](/concepts/governance-engine) that run in the [engine host](/concepts/engine-host).  The engines defined here are also reused by the technology content packs, which add their own request types to them.
* **Design information** - the generic [templates](/concepts/template) for cataloguing resources, the [solution blueprints](/concepts/solution-blueprint) and [information supply chains](/concepts/information-supply-chain) that describe Egeria's own deployment, and the collection folders of the *Egeria Design Library* that organize it all.

## Technology types and valid metadata values

The pack defines 166 technology types.  They form a hierarchy rooted at *Root Technology Type*, and cover:

| Family | Examples |
|---|---|
| Egeria's own runtime | *OMAG Server Platform*, *OMAG Server*, *Metadata Access Store*, *View Server*, *Integration Daemon*, *Engine Host*, the governance engine and service types, *Integration Connector*, *Dynamic Integration Group* |
| Connector categories | *Audit Log Destination*, *Cohort Registry Store*, *Secrets Store Connector*, *OMRS Repository Connector*, *Open Metadata Topic Connector*, *Resource Connector* |
| Files and folders | *File System*, *UNIX File System*, *File System Directory*, *Data Folder*, *Data File*, *CSV Data File* and the other file formats (JSON, Avro, Parquet, XML, spreadsheet, audio, video, raster, vector, 3D image, source code, script, properties, YAML, keystore, archive) |
| Cloud storage and tables | Amazon S3, Google Cloud Storage, Azure Blob Storage, Azure Data Lake Storage, Apache Hadoop HDFS and Databricks File System objects and folders; tables in Amazon Athena, AWS Glue, Amazon Redshift, Google BigQuery, Google Cloud Spanner, Snowflake, Teradata, Trino, Apache Hive, Apache Cassandra, MySQL, CrateDB, OceanBase, Azure Synapse Analytics, Azure Data Explorer, Azure Cosmos DB, Microsoft Fabric Warehouse and Milvus |
| Data sets | *Tabular Data Set*, *Tabular Data Set Collection*, *CSV Tabular Data Set*, *Data File Collection*, *In-Memory Data Set* |
| Events and APIs | *Apache Kafka Topic*, *Google Cloud Pub/Sub Topic* and *Subscription*, *REST API*, *REST API Endpoint*, *JDBC Endpoint*, *Event Broker* |
| Databases | *Database Server*, *JDBC Relational Database*, *JDBC Relational Database Schema*, *Relational database manager (RDBMS)* |
| Processing | *Apache Airflow Server*, *Apache Airflow DAG* and *Task*, *Apache Spark Job*, *SQL Job*, *Debezium Connector Task*, *Marquez Server*, *Apache Superset* |
| Documents | *Document File*, *Markdown Document File*, *Webpage File*, *Jupyter Notebook File*, Box, IBM FileNet and Microsoft SharePoint documents, Bitol ODCS and ODPS files |
| Infrastructure | *Bare Metal Computer*, *Laptop Computer*, *Apple MacBook Pro*, phones and tablets, *Virtual Machine*, *Docker Container*, *Kubernetes Cluster*, *Hadoop Cluster* |

The technology content packs add the types for their own technologies (for example *PostgreSQL Server* or *Apache Kafka Server*) beneath these.

The pack also holds just over 2000 *ValidMetadataValue* elements.  About 670 of them list the names of the open metadata types and about 760 list the names of the open metadata properties, so that tools can validate and offer them.  The rest are the valid values for some 70 properties, such as `activityStatus`, `annotationType`, `confidentialityLevel`, `criticalityLevel`, `deploymentStatus`, `incidentStatus`, `projectStatus`, `qualityDimension`, `resourceUse`, `retentionBasis` and `actorRoleGroups`.  They are retrieved through the [Valid Metadata OMVS](/services/omvs/valid-metadata/overview).

## Connector types

The pack defines 187 [connector types](/concepts/connector-type), one for each connector supplied with Egeria.  Most of them (165) are filed in the *Open Connectors* collection folder of the design library.  Grouped by kind, there are:

* around 44 integration connectors, including the nanny connectors, the file, database, Apache Kafka, Apache Atlas, Unity Catalog, Open Lineage, Bitol and DCAT connectors, and the OMAG Server Platform cataloguer;
* around 51 [tabular data set connectors](/concepts/tabular-data-set-connector), which present open metadata (valid values, survey measurements, people, locations, digital products and so on) and database tables as tables;
* around 20 survey action services, around 22 governance action services, 6 Lovelace analysis services and 3 watchdog action services;
* the resource connectors used by these services - file and folder stores, JDBC, REST API clients, Apache Atlas, Apache Kafka administration, Unity Catalog and WSO2 Micro Integrator - and the connectors that call Egeria's own platform and servers;
* the runtime connectors: audit log destinations, cohort registry store, repository connectors, open metadata topic connectors, open metadata archive stores, secrets stores and the configuration document store.

The connector types for technologies that have their own content pack, such as the PostgreSQL or Unity Catalog connectors, are defined here so that the connector catalog is complete whichever content packs are loaded.

## Templates

The pack's generic [templates](/concepts/template) let you catalog a resource of a common technology without a specialist connector.  Each one is linked to its technology type, so it can be found from the technology type in the [Automated Curation OMVS](/services/omvs/automated-curation/overview) and used with the template name placeholders shown.

| Group | Technology types with a template | Asset type | Qualified name pattern |
|---|---|---|---|
| Endpoints | JDBC Endpoint, REST API Endpoint | *Endpoint* | `JDBC Endpoint::~{serverName}~` |
| Cloud and warehouse tables | Amazon Athena, AWS Glue, Amazon Redshift, Google BigQuery, Google Cloud Spanner, Snowflake, Teradata, Trino, Apache Hive, Apache Cassandra, MySQL, CrateDB, OceanBase, Azure Synapse Analytics, Azure Data Explorer and Microsoft Fabric Warehouse tables; Azure Cosmos DB and Milvus collections; In-Memory Data Set | *DataSet* | `{technology type}::~{namespacePath}~::~{resourceName}~` |
| Object stores and distributed file systems | Objects and folders in Amazon S3, Google Cloud Storage, Azure Blob Storage, Azure Data Lake Storage, Apache Hadoop HDFS and Databricks File System, plus generic Data File and Data Folder | *DataFile*, *DataFolder* | `{technology type}::~{namespacePath}~::~{resourceName}~` |
| Documents | Box File, IBM FileNet Document, Microsoft SharePoint Document | *Document* | `{technology type}::~{namespacePath}~::~{resourceName}~` |
| Events | Apache Kafka Topic; Google Cloud Pub/Sub Topic and Subscription | *Topic*, *DataFeed* | `Topic::~{serverName}~.~{fullTopicName}~::inOut` for Kafka |
| Pipelines and jobs | Apache Airflow DAG, Apache Airflow Task, Apache Spark Job, SQL Job, Debezium Connector Task | *DeployedSoftwareComponent* | `{technology type}::~{namespacePath}~::~{resourceName}~` |
| Tabular data | Data File Collection, CSV Tabular Data Set, CSV Tabular Data Set Collection | *DataFileCollection*, *TabularDataSet*, *TabularDataSetCollection* | `CSV Tabular Data Set::~{directoryPathName}~::~{tableName}~::~{versionIdentifier}~` |
| File systems and hosts | File System, UNIX File System, Apple MacBook Pro | *FileSystem*, *BareMetalComputer* | `FileSystem::UNIX File System::null::~{fileSystemName}~` |

The `namespacePath` and `resourceName` placeholders follow the OpenLineage naming conventions, so assets created from these templates can be matched to the datasets named in [OpenLineage](/content-packs/open-lineage-content-pack/overview) events.  The [Files Content Pack](/content-packs/files-content-pack/overview) adds a second set of templates for files and folders on a local file system, keyed by path name.  All of the templates are described further in the [Template Catalog](/catalog-templates).

## Integration connectors

The pack defines nine dynamic [integration groups](/concepts/integration-group).  Eight of them each run one integration connector; the *DefaultIntegrationGroup* (`Egeria:IntegrationGroup:Default`) has no connectors and is there to use with your own integration daemon configuration.  Apart from the JDBC cataloguer, these are Egeria's [nanny connectors](/connectors/#nanny-connectors).

| Integration group | Connector | Runs as | Purpose |
|---|---|---|---|
| *DatabaseIntegrationGroup* | JDBCIntegrationConnector | `JDBCDatabaseCataloguer` (user `dbcatnpa`, every 60 minutes) | Catalogs the schemas, tables and columns of the JDBC databases attached as catalog targets.  The database content packs use it to catalog the databases they find. |
| *OpenMetadataObservabilityIntegrationGroup* | PepysActivityObserverIntegrationConnector | `PepysActivityObserver` (user `pepysnpa`, every 20 minutes) | Maintains the *UsageActivity* classification of each anchor element from the activity reported in the OMAG Servers' audit logs.  See [metadata observability](/features/metadata-observability/overview). |
| | SimonContributionRecorderIntegrationConnector | `SimonContributionRecorder` (user `simonnpa`, every 12 minutes) | Awards [karma points](/concepts/karma-point) to the users who change open metadata. |
| *BabbageIntegrationGroup* | BabbageAnalyticalEngineIntegrationConnector | `BabbageAnalyticalEngine` (user `babbagenpa`, every 1440 minutes) | Runs the analytical governance action types attached to it as catalog targets.  This pack attaches *Build Member Popularity Profile*; other packs attach more.  See [metadata insight](/patterns/metadata-insight/overview). |
| *MendelIntegrationGroup* | MendelAutomatedDuplicateManagerIntegrationConnector | `MendelAutomatedDuplicateManager` (user `mendelnpa`, every 1440 minutes) | Manages the duplicate links and classifications between elements detected as [duplicates](/features/duplicate-management/overview). |
| *DarwinIntegrationGroup* | DarwinProductDependencyManagerIntegrationConnector | `DarwinProductDependencyManager` (user `darwinnpa`, every 60 minutes) | Maintains the coarse-grained [lineage](/features/lineage-management/overview) implied by the finer-grained lineage beneath it, up to the dependencies between digital products. |
| *PasteurIntegrationGroup* | PasteurActionHistoryCleanupIntegrationConnector | `PasteurActionHistoryCleanup` (user `pasteurnpa`, every 1440 minutes) | Deletes finished actions once the configured number of days has passed since they completed. |
| *LiskovIntegrationGroup* | LiskovDataSharingHubManagerIntegrationConnector | `DataSharingHubManager` (user `liskovnpa`, every 1440 minutes) | Maintains the data dictionary of each [data sharing hub](/concepts/data-sharing-hub). |
| *SmartCollectionsIntegrationGroup* | SmartCollectionsIntegrationConnector | `SmartCollectionsMembershipManager` (user `smartcnpa`, every 30 minutes) | Maintains the membership of [smart collections](/egeria-solutions/smart-collections/overview) by running their saved queries. |

## Governance engines

The pack defines four governance engines.  The technology content packs add their own request types to them - for example the Egeria Content Pack adds the OMAG Server Platform services to *EgeriaGovernance*, the Open Lineage Content Pack adds its Lovelace services to *EgeriaGovernance* and `harvest-open-lineage-topic` to *AssetOnboarding*, and the Files Content Pack adds `watch-for-new-files-in-folder` to *EgeriaWatchdog*.

???+ info "AssetOnboarding - Asset Onboarding Engine"
    Monitors, validates and enriches metadata relating to assets as they are catalogued.

    | Request type | Governance service | Purpose |
    |---|---|---|
    | `seek-origin-of-asset` | Locate and Set Origin Governance Action Service | Follows the lineage of an asset back to its origin. |
    | `set-origin` | Set Origin Governance Action Service | Sets the *DigitalResourceOrigin* classification. |
    | `set-owner` | Set Owner Governance Action Service | Sets the *Ownership* classification. |
    | `set-zone-membership` | Update Asset's Zone Membership Governance Action Service | Assigns the configured governance zones. |
    | `set-retention-period` | Add a Retention classification to an Asset Governance Action Service | Assigns the configured retention classification. |
    | `verify-asset` | Verify an Asset Governance Action Service | Checks that an asset has its zones, owner and origin set up. |
    | `create-software-server`, `create-kafka-topic` | Create Asset Governance Service | Creates an asset from a template. |
    | `delete-software-server` | Delete Asset Governance Service | Deletes an asset that was created from a template. |
    | `delete-kafka-topic` | Create Asset Governance Service | Intended to delete an Apache Kafka topic asset, but the shipped content links it to the *Create* service (see the note below). |
    | `catalog-software-server` | Add Catalog Target to Asset Governance Service | Attaches an asset to an integration connector as a catalog target. |

???+ info "Stewardship - Stewardship Engine"
    Liaises with stewards to make corrections to open metadata.

    | Request type | Governance service | Purpose |
    |---|---|---|
    | `evaluate-annotations` | Verify annotations in a Survey Report | Raises a [to do](/concepts/to-do) for each *Request for Action* annotation in a survey report. |
    | `print-survey-report` | Print a Survey Report as a markdown document | Writes a survey report out as a file. |
    | `inform-steward` | Inform a Steward Governance Action Service | Creates a to do for a steward from a template. |
    | `report-incident` | Report an Incident Governance Action Service | Creates an [incident report](/concepts/incident-report) from a template. |
    | `write-to-audit-log` | Write an Audit Log Message | Writes a requested message to the audit log. |
    | `get-day-of-week` | Detect the day of the week | Outputs the day of the week as a [guard](/concepts/guard). |
    | `qualified-name-dedup` | Qualified Name De-duplicator Governance Action Service | Links elements with the same qualified name as duplicates. |
    | `detect-element-type` | Detect the Type of an Element Governance Action Service | Checks the type of each action target and outputs the result as a guard. |

???+ info "EgeriaGovernance - Egeria Governance Engine"
    Provides specialist governance services to Egeria's OMAG Server Platform and Servers.

    | Request type | Governance service | Purpose |
    |---|---|---|
    | `build-member-popularity-profile` | Lovelace Popularity Profiler Governance Action Service | Totals the usage activity of the members of each collection.  Run by the Babbage Analytical Engine. |
    | `provision-tabular-data-set` | Tabular Data Provisioning Pipeline Governance Action Service | Copies data from one tabular data set to another. |
    | `resynchronize-anchors-zones` | Anchors Zone Resynchronizer Governance Action Service | Corrects the governance zones held in *Anchors* classifications. |

???+ info "EgeriaWatchdog - Egeria Watchdog Engine"
    Provides standard watchdog services to Egeria's OMAG Server Platform and Servers.

    | Request type | Governance service | Purpose |
    |---|---|---|
    | `watch-for-element-change` | Generic Element Watchdog Action Service (`process-single-event`) | Waits for a single change to the requested elements and starts the configured governance action process. |
    | `watch-for-element-changes` | Generic Element Watchdog Action Service (`process-multiple-events`) | Continuously monitors the requested elements and starts the configured process for each change. |
    | `wait-for-steward` | Wait For Steward Watchdog Action Service | Waits for stewards to finish the to dos supplied as action targets. |

The pack also defines governance services that are only used by other content packs' engines: the CSV file, data file and folder [survey action services](/concepts/survey-action-service) used by the Files Content Pack, the file move/copy/delete service, and the *New Files Watchdog Action Service*.  The governance engines run in an [engine host](/concepts/engine-host).

!!! warning "delete-kafka-topic runs the wrong service"
    In this release the `delete-kafka-topic` request type (and so the *ApacheKafkaTopic:DeleteAsset* process that uses it) is linked to the *Create Asset Governance Service* rather than the *Delete Asset Governance Service*.

## Governance action processes

| Process | What it does |
|---|---|
| *Daily Governance Action Process* (`Egeria::DailyGovernanceActionProcess`) | Determines which day of the week it is with `get-day-of-week`, and writes the task assigned to that day to the audit log.  It is a simple illustration of guards. |
| *ApacheKafkaTopic:DeleteAsset* | Deletes the asset for an Apache Kafka topic using the template properties that were used to create it. |

??? info "Daily Governance Action Process"
    --8<-- "snippets/governance-action-processes/daily-governance-action-process-mermaid-graph.md"

The processes for creating, cataloguing and surveying specific technologies are in the technology content packs.

## Design library, solution blueprints and information supply chains

The *Egeria Design Library* root collection organizes the descriptions of how Egeria is designed and configured into collection folders: *Egeria Solutions* (with *Egeria Supply Chains* beneath it), *Content Pack Contents*, *Integration Groups*, *Governance Engines*, *Open Connectors*, *Analytical Services* and *Governance Actions*.  *Governance Actions* is divided further into *Catalog*, *Survey*, *Stewardship*, *Communication*, *Watchdog*, *File Management*, *Provision*, *Analytical* and *Digital Product Catalog Actions*.  Each content pack files its own elements in these folders, so the library grows as more packs are loaded.  A separate *Digital Product Catalogs* root collection links the digital product catalogs together.

The pack defines five [solution blueprints](/concepts/solution-blueprint):

* *Core Content Pack* - the components configured by this pack (shown below);
* *Egeria Default Runtime Solution Blueprint* - the services configured by Egeria's build to create a simple deployment environment;
* *Egeria Workspaces Runtimes* and *Egeria Workspaces Servers Solution Blueprints* - the technology runtimes and servers set up by Egeria Workspaces;
* *Open Metadata Archive Solution Blueprint* - how the content packs shipped with Egeria are built.

They are supported by six [solution roles](/concepts/solution-role) (Digital Product Manager, Egeria Open Source Community, Open Metadata User, Python Programmer, Runtime Manager and Security Manager) and 116 [solution components](/concepts/solution-component).

Five [information supply chains](/concepts/information-supply-chain) describe how open metadata flows through Egeria: *Open Metadata Highway*, *Open Lineage Highway*, *Open Metadata Observability*, *Dynamic Configuration* and *Security Access*.  There is also a template for new information supply chains, and a *SAMPLE Information Supply Chain - Deployment Status Demonstration*, with a set of elements whose names begin `SAMPLE`, that exists only to show how the different areas of an information supply chain and the deployment status of its components are displayed.

## Security definitions

The pack contains standard security definitions that are small and widely used: the six [STRIDE](/egeria-solutions/threat-modelling/overview#threat-elicitation) *Threat* definitions (`Threat::STRIDE::Spoofing`, `Threat::STRIDE::Tampering`, `Threat::STRIDE::Repudiation`, `Threat::STRIDE::InformationDisclosure`, `Threat::STRIDE::DenialOfService` and `Threat::STRIDE::ElevationOfPrivilege`), and the *CertificationType* for ISO/IEC 27001:2022 (`CertificationType::ISO/IEC 27001:2022`).  Larger security control catalogs are in the separate [Security Content Pack](/content-packs/security-content-pack/overview).

## Other reference content

* Twelve [perspectives](/concepts/perspective) - Administration, App/AI Builder, Architecture, Community, Consumer, Data Expert, Financial, Governance, Owner, Privacy, Security and Steward.
* Four *ExceptionType* definitions raised by the OMAG Server Platform cataloguer: clear text password, missing user account, missing user identity and missing zone access control.

## Solution blueprint

--8<-- "snippets/blueprints/content-packs/core-content-pack-solution-blueprint-mermaid-graph.md"

!!! summary "Usage"
    The Core Content Pack is loaded automatically into the *active-metadata-store* of Egeria's quickstart and default runtime.  For your own deployment, load it first - before any other content pack - into a [metadata access store](/concepts/metadata-access-store) with the [Runtime Manager](/services/omvs/runtime-manager/overview), or add it to the server's start-up archives.  The nanny connectors start in any integration daemon that runs the integration groups above, and the governance engines start in any engine host configured with their names.

--8<-- "snippets/abbr.md"
