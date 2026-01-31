---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Anchor

An *anchor* is a metadata element that is the root of a group of linked elements that should be processed as if they were logically a part of the same "object". 

For example, an [asset](/concepts/asset) may be linked to its [schema](/concepts/schema), a [connection](/concepts/connection) and a [glossary term](/practices/common-data-definitions/anatomy-of-a-glossary).  The schema and connection would typically be anchored to the asset since they only have meaning in the context of the asset.  The glossary term is independent of the asset, since it can be used in many other contexts.  Therefore the glossary term would not be part of the asset's anchor grouping.

The value of establishing this *anchor grouping* is to ensure that elements that have little meaning without their anchor are managed consistently. There are four main use cases for the anchor grouping:

* *Security* - when elements within the anchor group are created, updated, deleted or accessed, the security check is whether the user has access to the anchor element.
* *Deleting* - when the anchor element is deleted, all of the other elements in the anchor grouping are deleted as well. This ensures anchored elements are cleaned up properly and are not left to uselessly clutter the repository.
* *Templated cataloguing* - when a new element is created from a [template](/concepts/template), all the linked elements anchored to the template are copied.  Other elements linked to the template are also linked to the equivalent newly created element(s).
* *Searching and retrieval* - the [Asset Catalog OMVS](/services/omvs/asset-catalog/overview) uses the anchor information in its search API to enable searches to include all elements anchored to assets.

!!! education "Further information"

    - [Anchor Management](/features/anchor-management/overview) provide support for the Anchors  classification.
    - [Anchor Classification](/types/0/0010-Base-Model) is used to implement the anchor grouping.

--8<-- "snippets/abbr.md"
