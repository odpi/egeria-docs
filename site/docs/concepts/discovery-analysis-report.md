---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Discovery Analysis Report

The *discovery analysis report* lists the [discovery annotations](/egeria-docs/guides/developer/open-discovery-services/discovery-annotations) that were created during the execution of an [open discovery service](/egeria-docs/guides/developer/open-discovery-services/overview).

The discovery analysis report is created in the open metadata repository by the [discovery engine](/egeria-docs/concepts/open-discovery-engine) when it creates the discovery service instance. The discovery service can retrieve information about the discovery analysis report through the [discovery analysis report store](/egeria-docs/guides/developer/open-discovery-services/discovery-analysis-report-store) client.

This client is accessed through the [discovery annotation store](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation-store).

The discovery analysis report store also enables a long running discovery service (typically a [discovery pipeline](/egeria-docs/guides/developer/open-discovery-services/discovery-pipeline)) to record its current analysis step.

## Discovery annotations

[Annotations](/egeria-docs/guides/developer/open-discovery-services/discovery-annotation) are metadata elements that describe a particular finding from the execution of an open discovery service.

--8<-- "snippets/abbr.md"
