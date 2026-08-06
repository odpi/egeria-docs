---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Watchdog Action Engines

A *watchdog action engine* is a type of [governance engine](/concepts/governance-engine) that describes a set of related [watchdog action services](/concepts/watchdog-action-service).  Each watchdog action service monitors for a specific situation or event in the open metadata ecosystem and notifies its subscribers when it occurs.

A watchdog action engine is hosted in the [Watchdog Action Open Metadata Engine Service (OMES)](/services/omes/watchdog-action/overview) running on one or more [Engine Host OMAG Servers](/concepts/engine-host).

![Watchdog Action Service](/concepts/watchdog-action-service.svg)

When a watchdog action engine is called, it is passed a governance request type and request parameters.  This is mapped, through the watchdog action engine's [governance engine definition](/concepts/governance-engine-definition), to a call to a specific watchdog action service.

Watchdog action engines are deliberately different from [governance action engines](/concepts/governance-action-engine) and [survey action engines](/concepts/survey-action-engine) in one important respect: the services they host are expected to keep running for as long as the situation being watched for might occur, rather than completing quickly.  This is why watching for change was given its own engine, and its own [framework](/frameworks/owf/overview), separate from the rest of governance action processing - see [Open Watchdog Framework (OWF)](/frameworks/owf/overview) for the full explanation.

!!! education "Further information"

    The Open Metadata Types used to define the watchdog action engines are located in [model 0461 Governance Engines](/types/4/0461-Governance-Engines).


--8<-- "snippets/abbr.md"
