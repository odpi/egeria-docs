---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Event Action Engines

An *event action engine* describes a set of related [event action services](/guides/developer/event-action-services/overview). Each event action service implements a specific type of event management.  This event management is built around [context events](/concepts/context-event) and actions.

An event action engine is hosted in the [Event Action Open Metadata Engine Service (OMES)](/services/omes/event-action/overview) running on one or more [Engine Host OMAG Servers](/concepts/engine-host).

![Event Action Engine](/connectors/event-action/event-action-service.svg)

When an event action engine is called, it is passed a governance request type and request parameters. This is mapped to a call to an [event action service](/concepts/event-action-service) through the [event action engine definition](/concepts/governance-engine-definition).

![Event Action Engine Definition Structure](/guides/developer/open-metadata-archives/event-action-engine-definition.svg)
> Logical structure of an event action engine definition showing how the governance request types map to the event action service definitions

!!! education "Further information"

    The Open Metadata Types used to define the event action engines are located in [model 0461 Governance Engines](/types/4/0461-Governance-Engines).


---8<-- "snippets/abbr.md"