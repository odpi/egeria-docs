---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Asset Analysis Open Metadata Engine Service (OMES)

The Asset Analysis OMES provides support for [open discovery engines](/concepts/open-discovery-engine) that are part of the [Open Discovery Framework (ODF)](/frameworks/odf/overview).

![Governance Action OMES](/services/omes/engine-services-asset-analysis-server-side.svg)

## Open discovery engines

An open discovery engine hosts [automated metadata discovery](/features/discovery-and-stewardship/overview).

The Asset Analysis OMES is capable of hosting one or more [open discovery engines](/concepts/open-discovery-engine) and supports a REST API to request that an open discovery engine runs an [open discovery service](/guides/developer/open-discovery-services/overview) to analyse a [digital resource](/concepts/digital-resource). The results of this analysis is a [discovery analysis report](/concepts/discovery-analysis-report) that is attached to the resource's [asset](/concepts/asset).

The REST API also supports a request to a discovery engine to run a specific open discovery service against each asset it has access to.

The discovery engine services call the [Discovery Engine Open Metadata Access Service (OMAS)](/services/omas/discovery-engine/overview) running in an open metadata server to retrieve information about assets and to store the discovery analysis reports.

--8<-- "snippets/abbr.md"
