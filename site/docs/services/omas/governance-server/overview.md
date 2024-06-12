<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Governance Server Open Metadata Access Service (OMAS)

The *Governance Server OMAS* supports the implementation of a [governance server](/concepts/governance-server) by providing the metadata services for defining and running [governance engines](#governance-engines) as well as setting up [integration groups](#integration-groups).

## Governance Engines

A governance engine is a collection of related *[governance services](/concepts/governance-service)* that provide pluggable governance functions.  The governance services are implemented as 
specialist [connectors](/frameworks/ocf/overview) that are defined by:

* [Survey Action Framework (SAF)](/frameworks/saf/overview) for Survey Action Services that analyse the content of resources in the digital landscape.
* [Governance Action Framework (GAF)](/frameworks/gaf/overview) of Governance Action Services that monitor, assess and maintain metadata.

The governance services run in the [Engine Host OMAG Server](/concepts/engine-host) supported by the [Open Metadata Engine Services (OMES)](/services/omes).  They are triggered via [governance actions](/concepts/governane-action).

The Governance Engine OMAS has the following capabilities to support governance engines:

| Java Interface                                                                                                                                                    | Description                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [GovernanceEngineConfiguration](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceEngineConfiguration.html)       | Creating the definitions for [governance engines](/concepts/governance-engine) and their [governance services](/concepts/governance-service).                                                                    |
| [GovernanceEngineEventInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceEngineEventInterface.html)     | Providing the events that enable the Engine Host OMAG Server to be notified of any changes to governance actions, governance engines and governance services.  It also provides support for the watchdog events. |
| [GovernanceProcessingInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceProcessingInterface.html)       | Providing the APIs that enable the Engine Host OMAG Server to retrieve the definitions of the governance engines and services.                                                                                   |
| [GovernanceActionProcessInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceActionProcessInterface.html) | Creating the definitions for [governance action processes](/concepts/governance-action-process) that control the sequencing of [engine actions](/concepts/engine-action.                                         |
| [GovernanceProcessingInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceProcessingInterface.html)       | Providing APIs to initiate [engine actions](/concepts/engine-action) and [governance action processes](/concepts/governance-action-process) explicitly.                                                          |
| [GovernanceEngineEventListener](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceEngineEventListener.html)       | Notification of new [engine actions](/concepts/engine-action) to the Engine Host OMAG Servers that then invoke the appropriate governance services to action them.                                               |
| [MetadataElementInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/commonservices/gaf/api/MetadataElementInterface.html)                              | Supporting the metadata requirements for many of the [engine services](/services/omes).                                                                                                                          |
| [GovernanceEngineConfiguration](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/GovernanceEngineConfiguration.html)       | Providing APIs to query the status of the governance capabilities implemented through the governance engines.                                                                                                    |
| [SpecialGovernanceActionInterface](https://odpi.github.io/egeria/org/odpi/openmetadata/accessservices/governanceengine/api/SpecialGovernanceActionInterface.html) | Providing specialized governance remediation APIs such as linking duplicates.                                                                                                                                    |

Behind the scenes, Governance Engine OMAS handles the choreography of governance actions based on the process definition provided by a [governance action process](/concepts/governance-action-process).

!!! info "Further documentation"
    The documentation for writing governance services is located in the developer guide:

    - [Survey Action Services](/guides/developer/survey-action-services) for metadata discovery.
    - [Governance Action Services](/guides/developer/governance-action-services) for the Governance Action Services: Watchdog Governance Services, Triage Governance Services, Verification Governance Services, Remediation Governance Services and Provisioning Governance Services.
    - [Context Event Services](/guides/developer/context-event-services) for the time-based services.
    - [Repository Governance Services](/guides/developer/repository-governance-services) for the management of open metadata repositories.


## Integration Groups

An [integration group](/concepts/integration-group) is a collection of [integration connector](/concepts/integration-connector) definitions intended to run in one or more [integration daemons](/concepts/integration-daemon).  The Governance Engine OMAS provides the API to maintain the integration group and integration connector definitions.  The integration daemon then loads the definitions from the integration group and runs the requested integration connectors.  This is an alternative method to configure the integration daemon from adding the integration connectors directly into the integration daemon's configuration document.  The advantage of this approach is that new integration connectors can be added without restarting the integration daemon.

![integration group operation](integration-group-use.svg)

The Governance Server OMAS supports the creation and maintenance of the metadata that makes up an integration pack.  At the root is the [IntegrationGroup](/types/4/0464-Dynamic-Integration-Group).  Linked to it are the *IntegrationConnector* entities - one for each integration connector that is to run.  Each have a [connection](/concepts/connection) attached that is used to initialize the integration connector.  Optionally, the integration connector can be linked to existing metadata elements via the *CatalogTarget* relationship.  This guides the integration connector on which elements to update - rather than creating new elements.  For example, if the integration connector is cataloguing a specific database and its *Database* entity has already been created, it would be linked to the *IntegrationConnector* entity via the *CatalogTarget* relationship.  The integration connector is able to retrieve the catalog target via its context.

![integration group example](integration-group-example.svg)



--8<-- "snippets/abbr.md"
