---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0422 Governance Action Classifications

Governance Action Classifications describe the common (ie typical) types of classifications
that are used in the governance controls.

* **Impact** describes the impact of a situation on a particular resource.
* **Criticality** describes how critical a resource is to the operations of the organization.
* **Confidentiality** typically is used with a data resource and indicates how confidential its content is.
* **Confidence** indicates how confident the organization in the use of this resource in terms of its quality.
* **Retention** defines how long a resource (typically a data resource) needs to be kept.

![UML](0422-Governance-Action-Classifications.svg)

The values used in **levelIdentifier**, **severityIdentifier** and **basisIdentifier** are define using
[GovernanceClassificationLevels](0421-Governance-Classification-Levels.md).

The values used in **statusIdentifier** are defined using
[GovernanceStatusLevels](0421-Governance-Classification-Levels.md).

--8<-- "snippets/abbr.md"