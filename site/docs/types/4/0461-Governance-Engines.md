<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0461 Governance Engines

The governance engine types in this model are used to create a [governance engine definition](/concepts/governance-engine-definition).

![UML](0461-Governance-Engines.svg)

## GovernanceEngine entity

A [governance engine](/concepts/governance-engine) is a [software capability](/types/0/0042-Software-Capabilities) that is able to run specific services on demand.  These services, called [governance services](/concepts/governance-service), typically implement specific logic that is needed to govern an organization's resources or the metadata associated with them.

Open metadata recognizes three types of governance engine:

* *GovernanceActionEngine* - [Governance action engines and services](/concepts/governance-action-engine) support the active governance of metadata and the resources they represent.  There are different types of governance action engines/services that are defined by the [Governance Action Framework (GAF)](/frameworks/gaf/overview).
* *OpenSurveyEngine* - 
* *EventActionEngine* - event action engines and services support the automated management of [context events](/types/4/0475-Context-Events) and their associated [actions](/types/1/0137-Actions).  Note - this type of engine is still in development.
* *RepositoryGovernanceEngine* - [Repository governance engines and services](/concepts/repository-governance-engine) support the maintenance of repository level concerns, such as monitoring audit logs and maintaining [open metadata archives](/concepts/open-metadata-archive) that are defined in the [Open Metadata Repository Services (OMRS)](/services/omrs).
* *[OpenDiscoveryEngine](/types/6/0601-Open-Discovery-Engine)* - [Discovery engines and services](/concepts/open-discovery-engine) support the analysis of [digital resources](/concepts/resource).  The results of this analysis are stored in a [discovery analysis report](/types/6/0605-Open-Discovery-Analysis-Reports) chained off of the corresponding [Asset](/types/0/0010-Base-Model#asset) metadata element. The interfaces for discovery are found in the  [Open Discovery Framework (ODF)](/frameworks/odf/overview).  The types for the open discovery engines are shown on model .

## SupportedGovernanceService relationship

The capability of a *governance engine* is specified via the *SupportedGovernanceService* relationships.  

The `requestType` attribute in this relationship is the caller's request type (known as the [governance request type](/concepts/governance-request-type)).  The `serviceRequestType` attribute maps the *governance request type* to a request type supported by the associated [governance service](#governanceservice-entity).  If `serviceRequestType` is null, the governance request type is used when calling the governance service.

Each governance request type linked to a specific governance engine must be unique.

The `requestParameters` provide initial values of the request parameters passed to the governance services when it is called.  These are overridden by any request parameters supplied by the caller.

## GovernanceService entity

*[Governance services](/concepts/governance-service)* are specialist [connectors](/concepts/connector).  They are represented in open metadata using the *GovernanceService* entity which is a specialization of *[DeployedConnector`](/types/2/0215-Software-Components)*.  This entity is linked to a *[Connection](/types/2/0201-Connectors-and-Connections)* entity via a *[ConnectionToAsset](/types/2/0205-Connection-Linkage)* relationship.

A governance service can be linked to multiple governance engines via the *SupportedGovernanceService* relationship.  It can be linked to the same governance engine multiple times as long as each *SupportedGovernanceService* relationship has a different governance request type.

The subtype of the governance service linked via the *SupportedGovernanceService* relationship should be consistent with the subtype of the associated governance engine.  For example:

* A *GovernanceActionService* is linked to a *GovernanceActionEngine*.
* An *OpenSurveyService* is linked to an *OpenSurveyService*.
* A *RepositoryGovernanceService* is linked to a *RepositoryGovernanceEngine*.
* An *EventActionService* is linked to a *EventActionEngine*.
* An *OpenDiscoveryService* is linked to an *OpenDiscoveryService*.


??? education "Further information"

    The [Open Metadata Engine Services (OMES)](/services/omes) support the implementation of each type of governance engine. They run in an [Engine Host](/concepts/engine-host) OMAG Server and draw their configuration from the  *GovernanceEngine* and the linked *GovernanceService* elements in the associated metadata server.
    
    The type definitions for discovery engines and services are shown in [model 0601](/types/6/0601-Open-Discovery-Engine).

--8<-- "snippets/abbr.md"