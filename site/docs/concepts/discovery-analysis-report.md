---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Discovery Analysis Report

The discovery analysis report lists the [discovery annotations](#discovery-annotations)
that were created during the execution of
a [discovery service](open-discovery-service.md).

The discovery analysis report is created in the open metadata repository
by the [discovery engine](open-discovery-engine.md) when it creates the
discovery service instance.
The discovery service can retrieve information about the discovery analysis report
through the [discovery analysis report store](discovery-analysis-report-store.md) client.

This client is accessed
through the [discovery annotation store](discovery-annotation-store.md).

The discovery analysis report store also enables a long running discovery service
(typically a [discovery pipeline](open-discovery-service.md#discovery-pipeline)) to record its current
analysis step.

## Discovery annotations


--8<-- "snippets/abbr.md"
