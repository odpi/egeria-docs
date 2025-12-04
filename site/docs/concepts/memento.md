<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Memento

A *Memento* is a classification that is typically applied to an asset or related elements such as schema elements. It indicates that the element is logically deleted because it is no longer describing all or part of a [real-world digital resource](/concepts/digital-resource) (typically because the resource has been deleted or changed).

This element has only been retained to support lineage graph queries.   It will not be returned to callers unless the caller specifies the *forLineage* parameter.  If it is set to `true`, the *Memento* classification is ignored and the element is returned.

!!! info "Open Metadata Types"
    The definition for the *Memento* classification is found in the [0010 Base Model](/types/0/0010-Base-Model)


--8<-- "snippets/abbr.md"
