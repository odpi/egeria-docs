<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The `forLineage` flag is set by callers that are working with lineage.  Most callers will set this value to `false`.  It is used when retrieving elements to determine whether to return elements with the [*Memento*](/concepts/memento) classification.  The Memento classification indicates that the corresponding [digital resource](/concepts/resource) has been removed, and the metadata element has only been retained to support the linkage in a lineage graph.

When `forLineage=false` elements with the Memento classification are not returned; when `forLineage=true` they are returned.


