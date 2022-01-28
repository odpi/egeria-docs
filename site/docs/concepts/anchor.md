---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Anchor

An *anchor* is a [Referenceable](/concepts/referenceable) metadata entity that
groups other entities together as if they were logically a part of the anchor.
This means, for example, if the anchor entity is deleted then
the entities anchored to this entity are also deleted.

The value of establishing this grouping is to ensure that entities that have little meaning without their
anchor entity are cleaned up properly and are not left to uselessly clutter the repository.



!!! education "Further information"
    
    - [Anchor Management](/egeria-docs/features/anchor-management/overview) provide support for the Anchors and LatestChange classifications.

--8<-- "snippets/abbr.md"
