---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Survey Report

A *survey report* contains one or more sets of related properties that a [survey action service](/concepts/survey-action-service) has discovered about a resource, its metadata, structure and/or content. These are stored in a set of [annotations](#annotations) linked off of the survey report.

The survey report is attached to the [asset](/concepts/asset) for the [digital resource](/concepts/resource) that was analysed.  Over time, the survey reports show how the digital resource's contents are changing.

![Asset with discovery analysis reports](/guides/developer/survey-action-services/asset-to-survey-reports.svg)

The survey report is created in the open metadata repository by the [Survey Action OMES](/services/omes/survey-action/overview) when it creates an new survey action service instance. The survey action service can retrieve information about the survey report through the [survey context](/guides/developer/open-discovery-services/overview/#discovery-analysis-report-store).

##  Annotations

---8<-- "docs/guides/developer/survey-action-services/annotation-intro.md"


!!! education "Further information"
    [Metadata Discovery and Stewardship](/features/discovery-and-stewardship/overview)

--8<-- "snippets/abbr.md"
