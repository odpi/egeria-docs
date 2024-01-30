---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Survey Action Open Metadata Engine Service (OMES)

The Survey Action OMES provides support for [survey action engines](/concepts/survey-action-engine) that are part of the [Survey Action Framework (SAF)](/frameworks/saf/overview).

![Survey Action OMES](/services/omes/engine-services-survey-action-server-side.svg)

## Survey action engines

A survey action engine hosts specialized governance services called [survey action services](/concepts/survey-action-service).

The Survey Action OMES is capable of hosting one or more [survey action engines](/concepts/survey-action-engine).

The survey action engine services call the [Asset Owner Open Metadata Access Service (OMAS)](/services/omas/asset-owner/overview) running in a [metadata access server](/concepts/metadata-access-server) to retrieve information about assets and to store the results of the survey action services' work.

--8<-- "snippets/abbr.md"
