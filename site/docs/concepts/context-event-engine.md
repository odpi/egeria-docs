---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Context Event Engines

An *context event engine* describes a set of related [context event services](/guides/developer/context-event-services/overview). Each context event service implements a specific type of event management.  This event management is built around [context events](/concepts/context-event) and actions.

An context event engine is hosted in the [Context Event Open Metadata Engine Service (OMES)](/services/omes/context-event/overview) running on one or more [Engine Host OMAG Servers](/concepts/engine-host).

![Context Event Engine](/connectors/context-event/context-event-service.svg)

When an context event engine is called, it is passed a governance request type and request parameters. This is mapped to a call to an [context event service](/concepts/context-event-service) through the [context event engine definition](/concepts/governance-engine-definition).

![Context Event Engine Definition Structure](/guides/developer/open-metadata-archives/context-event-engine-definition.svg)
> Logical structure of an context event engine definition showing how the governance request types map to the context event service definitions

!!! education "Further information"

    The Open Metadata Types used to define the context event engines are located in [model 0461 Governance Engines](/types/4/0461-Governance-Engines).


---8<-- "snippets/abbr.md"