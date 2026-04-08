<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2019. -->

# Connector catalog

Egeria has a growing collection of *connectors* to third party technologies. These connectors help to accelerate the rollout of your open metadata ecosystem since they can be used to automate the extraction and distribution of metadata to the third party technologies.

A connector is a client to a third party technology. It supports a standard API that Egeria calls, and it then translates these calls into requests to the third party technology. Some connectors are also able to listen for notifications from the third party technology. When a notification is received, the connector converts its content into a call to Egeria to distribute the information to the open metadata ecosystem.

Connectors enable Egeria to operate in many environments and with many types of third party technologies, just by managing the configuration of the [OMAG servers](/concepts/omag-server). The Connector Catalog list the connector implementations supplied by the Egeria community. There are four broad categories of connectors and the connector catalog is organized accordingly:

* Connectors that support the [security of the open metadata ecosystem](#open-metadata-security-connectors).

* Connectors that support the [exchange and maintenance of metadata](#metadata-exchange-and-maintenance-connectors) with third party technology. This includes the resource connectors, survey action connectors, integration connectors and adapter repository connectors.  These connectors are organized by the type of third part technology type work with.

* Connectors that support the [governance of open metadata](#open-metadata-governance-connectors). This includes the watchdog action services and governance action services.  These connectors are organized by function.

* Connectors that support the integration of [Egeria's runtimes](#runtime-connectors) into the IT infrastructure where it is running. This includes the native repository connectors, event bus connectors, cohort registry stores, configuration stores, audit log destination connectors, open metadata archive stores, REST client connectors and the cohort member remote repository connectors.  These connectors are organized by connector type.

## Open Metadata Security Connectors

There are three types of connectors that support the security of the open metadata ecosystem:

* [Platform Metadata Security Connectors](/concepts/platform-metadata-security-connector) are used to authenticate and authorize access to the OMAG Server Platform services.
* [Server Metadata Security Connectors](/concepts/server-metadata-security-connector) are used to authorize access to the OMAG Server services.
* [Secrets Store Connectors](/concepts/secrets-store-connector) are used to send and receive events.

## Metadata exchange and maintenance connectors

The connectors that support the exchange and maintenance of metadata help to accelerate the rollout of your open metadata ecosystem, since they can be used to automate the extraction and distribution of metadata to the third party technologies.

* [File connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/file-connectors) work with different types of files.
* [JDBC Database connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-store-connectors/jdbc-resource-connector) make use of the JDBC standards to work with different types of relational databases.
* [Unity Catalog connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/data-manager-connectors/unity-catalog-connectors) work with the contents of the Unity Catalog server.
* [Apache Kafka connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-kafka-connectors) work with the topics and/or events passing through the Apache Kafka event broker.
* [Apache Atlas connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/system-connectors/apache-atlas-connectors) work with an Apache Atlas server.
* [Open API Specification connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openapi-integration-connector) extract metadata about APIs through the Open API interfaces provided through the Swagger API.
* [Open Lineage Event connectors](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/openlineage-integration-connectors) works with the open lineage event standard.


## Open Metadata Governance Connectors

* [Governance Action Services](/concepts/governance-action-service) are used to govern the open metadata ecosystem.
* [Survey Action Services](/concepts/survey-action-service) are used to gather information about the technology deployed within reach of the open metadata ecosystem.
* [Watchdog Action Services](/concepts/watchdog-action-service) monitors specific situations occurring in the open metadata ecosystem and initiate governance actions.
* [Repository Governance Services](/concepts/repository-governance-service) manages the activity in the [repository services](/services/omrs).


## Runtime connectors

*Runtime* connectors enable Egeria's [OMAG Server Platform](/concepts/omag-server-platform) and its hosted [OMAG Servers](/concepts/omag-server) to operate in many environments by providing plug-in points for the runtime services it needs to operate. Most of the runtime connectors relate to persistent storage, or connections to distributed services.  The connectors are organized by type to allow you to choose the options available from the Egeria community.

| Type                                                                                        | Description                                                                                                                                                            |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Repository and Event Mapper connectors](/concepts/repository-connector)                    | Integrate metadata repositories into the open metadata ecosystem so that they can interact with one or more [open metadata repository cohorts](/services/omrs/cohort). |
| [Configuration Document Store Connectors](/concepts/configuration-document-store-connector) | manage the persistence and retrieval of [configuration documents](/concepts/configuration-document).                                                                   |
| [Cohort Registry Store Connectors](/concepts/cohort-registry-store-connector)               | store the [open metadata repository cohort](/concepts/cohort-member) membership details in the [cohort registry store](/concepts/cohort-registry-store).               |
| [Open Metadata Archive Store Connectors](/concepts/open-metadata-archive-store-connector)   | read and write [open metadata archives](/concepts/open-metadata-archive).                                                                                              |
| [Audit Log Destination Connectors](/concepts/audit-log-destination-connector)               | support different destinations for audit log records.                                                                                                                  |
| [REST Client Connectors](/concepts/rest-client-connector)                                   | issue REST API calls to Egeria's deployed platforms and third party technologies.                                                                                      |
| [Cohort Member Client Connector](/concepts/cohort-member-client-connector)                  | supports repository service called to remote cohort members.                                                                                                           |
| [Open Metadata Topic Connectors](/concepts/open-metadata-topic-connector)                   | send and receive events.                                                                                                                                               |


--8<-- "snippets/abbr.md"
