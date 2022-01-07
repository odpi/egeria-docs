---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0461 Governance Engines

A governance engine is a software capability that is able to run specific services
on demand.  These services, called governance services, typically implement specific logic that
is needed to govern an organization's resources or the metadata associated with them.

Open metadata recognizes three types of governance engine:

* Governance action engines and services support the active governance of metadata and the resources they represent.  There are different types of governance action engines/services that are defined by the [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf/overview).

* [Discovery engines and services](/egeria-docs/types/6/0601-Open-Discovery-Engine.md) support the analysis of [real world resources](/egeria-docs/concepts/resource).  The results of this analysis are stored in a [discovery analysis report](/egeria-docs/types/6/0605-Open-Discovery-Analysis-Reports) chained off of the corresponding [Asset](/egeria-docs/types/0/0010-Base-Model#asset) metadata element. The interfaces for discovery are found in the  [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview).

* Archive engines and services support the maintenance of [open metadata archives](/egeria-docs/concepts/open-metadata-archive).

![UML](0461-Governance-Engines.svg)

The [Open Metadata Engine Services (OMES)](/egeria-docs/services/omes) support the implementation of each type of governance engine. They run in an [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server and draw their configuration from the  **GovernanceEngine** and the linked **GovernanceService** elements in the associated metadata server.

--8<-- "snippets/abbr.md"