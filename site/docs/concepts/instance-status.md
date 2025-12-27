---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Element/Instance status

Most types of metadata element (instances) may be in one of two status:

- ACTIVE - this means it is visible in the repositories.
- DELETED - this means it has been soft-deleted and can only be retrieved via a special query.  For repositories that support history, it is possible to move the element back to the status it was before it was deleted using the `restore()` method.

This status is maintained by the open metadata repositories.

When a query is made to retrieve open metadata elements, only elements in ACTIVE status are returned.  However, it is possible to request that elements that have been soft-deleted are returned using the `limitResultsByStatus` option.  This is a list of status values, so if set to `[DELETED]`, only soft-deleted elements matching the query request are returned.  Returning all known elements that match the query request is achieved by setting the `limitResultsByStatus` option to `[ACTIVE, DELETED]`.

The ability to retrieve soft-deleted elements is particularly useful for connectors trying to ascertain if a remote system has a new element, or one that we have seen before, but was deleted from the open metadata ecosystem.  Depending on the ownership of the element, the element may be deleted from the remote system, or the catalog entry in open metadata is recreated.

--8<-- "snippets/abbr.md"
