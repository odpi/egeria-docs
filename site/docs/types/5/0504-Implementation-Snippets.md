
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0504 Implementation Snippets

Developers can be aided in their work by having snippets of schema implementation that follow approved structures and naming conventions that they can include in their APIs and data structures.

![UML](0504-Implementation-Snippets.svg)

## ImplementationSnippet entity

The *ImplementationSnippet* entity is for the storage of an implementation snippet, along with details of its language and version.  It inherits from [Referenceable](/types/0/0010-Base-Model) which means it can have a link to an [external reference](/types/0/0015-Linked-Media-Types) which could be, say, a physical schema implementation in a source code repository).


## AssociatedSnippet relationship

The *AssociatedSnippet* relationship links a [Referenceable](/types/0/0010-Base-Model) entity such as a [*SchemaType*]() or data class to an implementation snippet to guide developers on how to implement the schema type.  There is also [DataClassSnippet](/types/5/0540-Data-Classes) that links a data class to a snippet.

## SchemaTypeImplementation relationship

This relationship links a concrete implementation to a schema type.  This is for data values that are derived (calculated).

??? deprecated "Deprecated types"
    The *SchemaTypeSnippet* has been replaced by *AssociatedSnippet*.

--8<-- "snippets/abbr.md"