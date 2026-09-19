<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Memento

A *Memento* is a classification that is typically applied to an asset or related elements such as schema elements. It indicates that the element is logically deleted because it is no longer describing all or part of a [real-world digital resource](/concepts/digital-resource) (typically because the resource has been deleted or changed).

This element has only been retained to support lineage graph queries.   It will not be returned to callers unless the caller specifies the *forLineage* parameter.  If it is set to `true`, the *Memento* classification is ignored and the element is returned.

*Memento* is the counterpart of the [*Promise*](/concepts/promise) classification.  A *Promise* element describes a resource that has not yet been delivered, and a *Memento* element describes a resource that no longer exists.  Together they allow a lineage graph to show the whole life of a resource.

A *Memento* element no longer reserves its *qualifiedName*, so a new element describing a replacement resource can be created with the same unique name.  A *Promise* element, by contrast, keeps its unique name reserved until the promise is cleared.

!!! info "Open Metadata Types"
    The definition for the *Memento* classification is found in the [0010 Base Model](/types/0/0010-Base-Model)


--8<-- "snippets/abbr.md"
