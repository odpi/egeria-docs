<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0042 Software Server Capabilities

![UML](0042-software-server-capabilities.svg)

## SoftwareServerCapability

Within a software server are many capabilities.

Different organizations and tools can choose the granularity in which the capabilities are captured in order to provide appropriate context to data assets and the decisions made around them.

These are the software server capabilities defined in the open types:

- [`APIManager`](/egeria-docs/types/0/0050-applications-and-processes/#apimanager) - A capability that manages callable APIs that typically delegate onto Software Services.
- [`Application`](/egeria-docs/types/0/0050-applications-and-processes/#application) - A capability supporting a specific business function.
- [`Catalog`](/egeria-docs/types/0/0050-applications-and-processes/#catalog) - A capability that manages collections of descriptions about people, places, digital assets, things, ...
- [`DataManager`](/egeria-docs/types/0/0050-applications-and-processes/#datamanager) - A capability that manages collections of data.
- [`Engine`](/egeria-docs/types/0/0055-data-processing-engines/#engine) - A programmable engine for running automated processes.
    - [`WorkflowEngine`](/egeria-docs/types/0/0055-data-processing-engines/#workflowengine) - An engine capable of running a mixture of human and automated tasks as part of a workflow process.
    - [`ReportingEngine`](/egeria-docs/types/0/0055-data-processing-engines/#reportingengine) - An engine capable of creating reports by combining information from multiple data sets.
    - [`AnalyticsEngine`](/egeria-docs/types/0/0055-data-processing-engines/#analyticsengine) - An engine capable of running analytics models using data from one or more data sets.
    - [`DataMovementEngine`](/egeria-docs/types/0/0055-data-processing-engines/#datamovementengine) - An engine capable of copying data from one data store to another.
    - [`DataVirtualizationEngine`](/egeria-docs/types/0/0055-data-processing-engines/#datavirtualizationengine) - An engine capable of creating new data sets by dynamically combining data from one or more data stores or data sets.
- [`EventBroker`](/egeria-docs/types/0/0050-applications-and-processes/#eventbroker) - A capability that supports event-based services, typically around topics.
- [`SoftwareService`s](/egeria-docs/types/0/0057-software-services/#softwareservice) - A capability that provides externally callable functions to other services.
    - [`ApplicationService`](/egeria-docs/types/0/0057-software-services/#applicationservice) - A software service that supports a reusable business function.
    - [`MetadataIntegrationService`](/egeria-docs/types/0/0057-software-services/#metadataintegrationservice) - A software service that exchanges metadata between servers.
    - [`MetadataAccessService`](/egeria-docs/types/0/0057-software-services/#metadataaccessservice) - A software service that provides access to stored metadata.
    - [`EngineHostingService`](/egeria-docs/types/0/0057-software-services/#enginehostingservice) - A software service that provides services that delegate to a hosted engine.
    - [`UserViewService`](/egeria-docs/types/0/0057-software-services/#userviewservice) - A software service that provides user interfaces access to digital resources.
- [`NetworkGateway`](/egeria-docs/types/0/0070-networks-and-gateways/#networkgateway) - A connection point enabling network traffic to pass between two networks.
- [`DatabaseManager`](/egeria-docs/types/2/0224-databases/#databasemanager) - A capability that manages data organized as relational schemas.
- [`EnterpriseAccessLayer`](/egeria-docs/types/2/0225-metadata-repositories/#enterpriseaccesslayer) - Repository services for the Open Metadata Access Services (OMAS) supporting federated queries and aggregated events from the connected cohorts.
- [`CohortMember`](/egeria-docs/types/2/0225-metadata-repositories/#cohortmember) - A capability enabling a server to access an open metadata repository cohort.
- [`GovernanceEngine`](/egeria-docs/types/4/0461-governance-engines/#governanceengine) - A collection of related governance services of the same type.
    - [`GovernanceActionEngine`](/egeria-docs/types/4/0461-governance-engines/#governanceactionengine) - A collection of related governance services supporting the Governance Action Framework (GAF).
    - [`OpenDiscoveryEngine`](/egeria-docs/types/6/0601-open-discovery-engine/#opendiscoveryengine) - A collection of related governance services supporting the Open Discovery Framework (ODF).

In addition, it is possible to augment software server capabilities with the following classifications:

- [`CloudService`](/egeria-docs/types/0/0090-cloud-platforms-and-services/#cloudservice) - A capability enabled for a tenant on a cloud platform.
- [`ContentCollectionManager`](/egeria-docs/types/2/0221-document-stores/#contentcollectionmanager) - A manager of controlled documents and related media.
- [`FileSystem`](/egeria-docs/types/2/0220-files-and-folders/#filesystem) - A capability that supports a store of files organized into a hierarchy of file folders for general use.
- [`FileManager`](/egeria-docs/types/2/0220-files-and-folders/#filemanager) - A manager of a collection of files and folders.
- [`NotificationManager`](/egeria-docs/types/2/0223-events-and-logs/#notificationmanager) - A server capability that is distributing events from a topic to its subscriber list.

--8<-- "snippets/abbr.md"
