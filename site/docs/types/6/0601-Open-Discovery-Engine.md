---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0601 Open Discovery Engines and Services

An [open discovery engine](/egeria-docs/concepts/discovery-engine) executes [open discovery services](/egeria-docs/concepts/open-discovery-service) on request.

The `OpenDiscoveryEngine` entity creates a description of an instance of these types of engines. It is represented as a special type [`GovernanceEngine`](/egeria-docs/types/4/0461-Governance-Engines) when it is documented in metadata.

[Open discovery services](/egeria-docs/concepts/open-discovery-service) are pluggable components that analyse data sources and document the results.

A description of an open discovery engine is linked with a [`SupportedGovernanceService`](/egeria-docs/types/4/0461-Governance-Engines) relationship to the description of an `OpenDiscoveryService` to indicate that
the open discovery engine supports the open discovery service.

The `OpenDiscoveryService` entity describes an implementation of an open discovery service.  This implementation is an specialized [OCF Connector](/egeria-docs/concepts/connector). The `OpenDiscoveryService` entity is a subtype of [`Asset`](/egeria-docs/types/0/0010-Base-Model) and is linked with a [`ConnectionToAsset`](/egeria-docs/types/2/0205-Connection-Linkage) relationship to a [Connection](/egeria-docs/types/2/0201-Connectors-and-Connections) entity that defines how to create an instance of the open discovery service in the Egeria OMAG Server Platform.

[Open discovery pipelines](/egeria-docs/concepts/open-discovery-service/#discovery-pipeline) are specialized open discovery services that execute multiple open discovery services in a single run.

The `OpenDiscoveryPipeline` entity describes an open discovery pipeline.  It is typically linked to a [VirtualConnection](/egeria-docs/types/2/0205-Connection-Linkage) with the connections of the open discovery services embedded within it.

![UML](0601-Open-Discovery-Engine.svg)

??? deprecated "Deprecated types"
    - **SupportedDiscoveryService** - Use [SupportedGovernanceService](/egeria-docs/types/4/0461-Governance-Engines).

--8<-- "snippets/abbr.md"