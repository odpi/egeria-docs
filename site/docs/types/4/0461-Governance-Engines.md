---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0461 Governance Engines

A [governance engine](/concepts/governance-engine) is a [software capability](/types/0/0042-Software-Capabilities) that is able to run specific services on demand.  These services, called [governance services](/concepts/governance-service), typically implement specific logic that is needed to govern an organization's resources or the metadata associated with them.

Open metadata recognizes three types of governance engine:

* [Governance action engines and services](/guides/developer/governance-action-services/overview) support the active governance of metadata and the resources they represent.  There are different types of governance action engines/services that are defined by the [Governance Action Framework (GAF)](/frameworks/gaf/overview).

* [Discovery engines and services](/guides/developer/open-discovery-services/overview) support the analysis of [real world resources](/concepts/resource).  The results of this analysis are stored in a [discovery analysis report](/types/6/0605-Open-Discovery-Analysis-Reports) chained off of the corresponding [Asset](/types/0/0010-Base-Model#asset) metadata element. The interfaces for discovery are found in the  [Open Discovery Framework (ODF)](/frameworks/odf/overview).

* [Repository governance engines and services](/guides/developer/repository-governance-services/overview) support the maintenance of [open metadata archives](/concepts/open-metadata-archive) that are defined in the [Open Metadata Repository Services (OMRS)](/services/omrs).

The capability of a *governance engine* is specified in a [governance engine definition](/concepts/governance-engine-definition).  This is a collection of open metadata elements starting with an entity of the appropriate `GovernanceEngine` subtype.  This is linked to `GovernanceService` entities via the `SupportedGovernanceService` relationship.  The `requestType` property in this relationship is used to map an incoming [governance request type](/concepts/governance-request-type) passed to the running governance engine into a governance service to invoke.  The `requestParameters` provide initial values of the request parameters passed to the governance services when it is called.  These are overlaid by any request parameters supplied by the caller.

*Governance services* are specialist [connectors](/concepts/connector).  They are represented in open metadata using the `GovernanceService` entity which is a specialization of [`DeployedConnector`](/types/2/0215-Software-Components).  This entity is linked to a [`Connection`](/types/2/0201-Connectors-and-Connections) entity via a [`ConnectionToAsset`](/types/2/0205-Connection-Linkage) relationship.

![UML](0461-Governance-Engines.svg)

??? education "Further information"

    The [Open Metadata Engine Services (OMES)](/services/omes) support the implementation of each type of governance engine. They run in an [Engine Host](/concepts/engine-host) OMAG Server and draw their configuration from the  `GovernanceEngine` and the linked `GovernanceService` elements in the associated metadata server.
    
    The type definitions for discovery engines and services are shown in [model 0601](/types/6/0601-Open-Discovery-Engine).

--8<-- "snippets/abbr.md"