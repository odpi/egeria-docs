<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

The `forLineage` flag is set by callers that are working with lineage.  Most callers will set this value to `false`.  It is used when retrieving elements to determine whether to return elements with the [*Promise*](/concepts/promise) or [*Memento*](/concepts/memento) classification.  The Promise classification indicates that the corresponding [digital resource](/concepts/digital-resource) has not yet been delivered, and the metadata element has been created ahead of it to build out the lineage graph.  The Memento classification indicates that the corresponding digital resource has been removed, and the metadata element has only been retained to support the linkage in a lineage graph.

When `forLineage=false` elements with the Promise or Memento classification are not returned; when `forLineage=true` they are returned.


