---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Discovery Analysis Report

The *discovery analysis report* lists the [discovery annotations](/guides/developer/open-discovery-services/overview/#discovery-annotations) that were created during the execution of an [open discovery service](/guides/developer/open-discovery-services/overview).  It is attached to the [asset](/concepts/asset) for the [digital resource](/concepts/resource) that was analysed.  Overtime, the discovery analysis reports show how the digital resource's contents are changing.

![Asset with discovery analysis reports](/guides/developer/open-discovery-services/asset-to-discovery-analysis-reports.svg)

The discovery analysis report is created in the open metadata repository by the [discovery engine](/concepts/open-discovery-engine) when it creates a discovery service instance. The discovery service can retrieve information about the discovery analysis report through the [discovery analysis report store](/guides/developer/open-discovery-services/overview/#discovery-analysis-report-store) client.

This client is accessed through the [discovery annotation store](/guides/developer/open-discovery-services/overview/#discovery-annotation-store).

The discovery analysis report store also enables a long-running discovery service (typically a [discovery pipeline](/guides/developer/open-discovery-services/overview/#discovery-pipelines)) to record its current analysis step.


## Discovery annotations

[Annotations](/guides/developer/open-discovery-services/overview/#discovery-annotations) are metadata elements that each describe a particular finding from the execution of an open discovery service.

![Structure of discovery analysis reports](/guides/developer/open-discovery-services/discovery-analysis-report-structure.svg)

!!! education "Further information"
    [Metadata Discovery and Stewardship](/features/discovery-andstewardship/overview)

--8<-- "snippets/abbr.md"
