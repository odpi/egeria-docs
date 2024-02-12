---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Survey Action Engines

A *survey action engine* is a type of [governance engine](/concepts/governance-engine) that describes a set of related [survey action services](/concepts/survey-action-service). Each survey action service implements a specific type of analysis.  This analysis is looking into the content of a [digital resource](/concepts/resource) and storing its findings in annotations within a [survey report](/concepts/survey-report) that is linked of the resource's [Asset](/concepts/asset) in the metadata repository.

A survey action is hosted in the [Survey Action Open Metadata Engine Service (OMES)](/services/omes/survey-action/overview) running on one or more [Engine Host OMAG Servers](/concepts/engine-host).

![Survey Action Engine](/connectors/survey-action/survey-action-service.svg)

When a survey action engine is called, it is passed a governance request type and request parameters. This is mapped to a call to an open discovery service through the [open discovery engine definition](/concepts/governance-engine-definition).

![Survey Action Engine Definition Structure](/guides/developer/open-metadata-archives/survey-action-engine-definition.svg)
> Logical structure of a survey action engine definition showing how the governance request types map to the survey action service definitions

!!! education "Further information"

    The Open Metadata Types used to define the survey action engines are located in [model 0461 Governance Engines](/types/4/0461-Governance-Engines).


---8<-- "snippets/abbr.md"