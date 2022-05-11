---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Discovery Analysis Report

A *discovery analysis report* contains one or more sets of related properties that an [open discovery service](/concepts/open-discovery-service) has discovered about the resource, its metadata, structure and/or content. These are stored in a set of [discovery annotations](#discovery-annotations) linked off of the discovery analysis report.

It is attached to the [asset](/concepts/asset) for the [digital resource](/concepts/resource) that was analysed.  Overtime, the discovery analysis reports show how the digital resource's contents are changing.

![Asset with discovery analysis reports](/guides/developer/open-discovery-services/asset-to-discovery-analysis-reports.svg)

The discovery analysis report is created in the open metadata repository by the [Asset Analysis OMES](/services/omes/asset-analysis/overview) when it creates an new open discovery service instance. The open discovery service can retrieve information about the discovery analysis report through the [discovery analysis report store](/guides/developer/open-discovery-services/overview/#discovery-analysis-report-store) client. This client is accessed through the [discovery annotation store](/guides/developer/open-discovery-services/overview/#discovery-annotation-store).

The discovery analysis report store also enables a long-running discovery service (typically an [open discovery pipeline](/concepts/open-discovery-service/#open-discovery-pipeline) to record its current analysis step.


## Discovery annotations

---8<-- "docs/guides/developer/open-discovery-services/discovery-annotation-intro.md"


!!! education "Further information"
    [Metadata Discovery and Stewardship](/features/discovery-and-stewardship/overview)

--8<-- "snippets/abbr.md"
