---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Context Event Open Metadata Engine Service (OMES)

The Context Event OMES provides support for [context event engines](/concepts/context-event-engine) that are part of the [Context Event Framework (CEF)](/frameworks/eaf/overview).

![Context Event OMES](/services/omes/engine-services-context-event-server-side.svg)

## Context event engines

An context event engine hosts specialized governance services called [context event services](/concepts/context-event-services).

The Context Event OMES is capable of hosting one or more [context event engines](/concepts/context-event-engine).

The context event engine services call the [Stewardship Action Open Metadata Access Service (OMAS)](/services/omas/stewardship-action/overview) running in an open metadata server to retrieve information about events and to store the results of the context event services' work.

--8<-- "snippets/abbr.md"
