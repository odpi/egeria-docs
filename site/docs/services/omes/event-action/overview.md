---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Event Action Open Metadata Engine Service (OMES)

The Event Action OMES provides support for [event action engines](/concepts/event-action-engine) that are part of the [Event Action Framework (EAF)](/frameworks/eaf/overview).

![Event Action OMES](/services/omes/engine-services-event-action-server-side.svg)

## Event action engines

An event action engine hosts specialized governance services called [event action services](/concepts/event-action-services).

The Event Action OMES is capable of hosting one or more [event action engines](/concepts/event-action-engine).

The event action engine services call the [Governance Engine Open Metadata Access Service (OMAS)](/services/omas/governance-engine/overview) running in an open metadata server to retrieve information about events and to store the results of the event action services' work.

--8<-- "snippets/abbr.md"
