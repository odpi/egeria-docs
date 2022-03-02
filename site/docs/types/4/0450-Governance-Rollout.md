---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0450 Governance Rollout

As important aspect of the governance program is the
ability to measure its effectiveness and identify the
assets that are delivering the highest value, or operating with the greatest efficiency etc.

A value that should be captured to demonstrate the effectiveness of the governance program
is documented using the **GovernanceMetric** entity.  It is linked to the appropriate
[GovernanceDefinition](/types/4/0401-Governance-Definitions)
and can be linked to a [DataSet](/types/0/0010-Base-Model) where the specific measurements are
being gathered.

The calculation of governance metrics is often a summary of many other measurements
associated with specific resources (such as data sources and processes) operating under the
scope of the governance program.
These resources are catalogued as [Assets](/types/0/0010-Base-Model).
The definition of their expected behavior or content can be captured using the
**GovernanceExpectations** classification attached to the Asset.
The measurements that support the assessment of a particular resource
can be gathered and stored in a **GovernanceMeasurements** classification attached to its Asset.


![UML](0450-Governance-Rollout.svg)

--8<-- "snippets/abbr.md"