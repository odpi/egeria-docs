---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Survey Report

A *survey report* contains one or more sets of related properties that a [survey action service](/concepts/survey-action-service) has discovered about a resource, its metadata, structure and/or content. These are stored in a set of [annotations](#annotations) linked off of the survey report.

The survey report is attached to the [asset](/concepts/asset) for the [digital resource](/concepts/digital-resource) that was analysed.  Over time, the survey reports show how the digital resource's contents are changing.

The survey report is [anchored](/features/anchor-management/overview) to the asset, and each of its annotations is anchored to the survey report.  Deleting the asset therefore deletes its survey reports and their annotations, and deleting a survey report on its own deletes the annotations it reported.  (Before release 6.2, the annotations were anchored directly to the asset, so deleting a report on its own left its annotations behind.)

![Asset with survey reports](/frameworks/osf/asset-to-survey-reports.svg)

The survey report is created in the open metadata repository by the [Survey Action OMES](/services/omes/survey-action/overview) when it creates an new survey action service instance. The survey action service can retrieve information about the survey report through the [survey context](/guides/developer/survey-action-services/overview).

##  Annotations

---8<-- "snippets/concepts/annotation-intro.md"


!!! education "Further information"
    [Metadata Discovery and Stewardship](/features/metadata-discovery/overview)

--8<-- "snippets/abbr.md"
