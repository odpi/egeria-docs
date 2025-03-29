---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


# 0770 - Lineage Mapping

Lineage Mapping identifies elements that are [equivalent to each other in the lineage graph](/features/lineage-management/overview/#stitching). It is used to stitch the lineage graph together.

This is contrast with the [Data Passing](/types/7/0750-Data-Passing) relationships that represent implementation relationships between components.

![UML](0770-Lineage-Mapping.svg)

## LineageMapping relationship

The *LineageMapping* relationship identifies two elements that represent the same real-world object.  This occurs when different tools are integrated into the open metadata ecosystem and they either use different names or catalog at different levels of granularity.  The aim of this relationship is to link up disconnected parts of a lineage graph.

## DataMapping relationship

The *DataMapping* relationship maps, typically, a schema attribute from one asset to the equivalent schema attribute of another asset to indicate that the data is copied from one to another.  The attributes within this relationship describe any transformation/mapping used.  The relationship is shown between two referenceables so that mapping components can be included in this fine-grained lineage.

--8<-- "snippets/abbr.md"
