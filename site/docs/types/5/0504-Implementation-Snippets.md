
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0504 Implementation Snippets

Developers can be aided in their work by having snippets of schema implementation that follow approved structures and naming conventions that they can include in their APIs and data structures.

![UML](0504-Implementation-Snippets.svg)

## ImplementationSnippet entity

The *ImplementationSnippet* entity is for the storage of an implementation snippet, along with details of its language and version.  It inherits from [Referenceable](/types/0/0010-Base-Model) which means it can have a link to an [external reference](/types/0/0015-Linked-Media-Types) which could be, say, a physical schema implementation in a source code repository).

The additional attributes of an implementation snippet are:

* *snippet* - the implementation code.
* *implementationLanguage* - the programming/encoding language used for the snippet.  For example, JSON, XML, Java, ...
* *versionIdentifier* - identifier for this version of the data field that this snippet represents.
* *usage* - how should this snippet be used.

## AssociatedSnippet relationship

The *AssociatedSnippet* relationship links a [Referenceable](/types/0/0010-Base-Model) entity such as a [*SchemaType*](/types/5/0501-Schema-Elements) or [data class](/types/5/0540-Data-Classes) to an implementation snippet to guide developers or code generators on how to implement the schema type.

## SchemaTypeImplementation relationship

This relationship links a concrete implementation to a schema type.  This is for identifying the code for managing data values that are derived (calculated).

??? deprecated "Deprecated types"
    The *SchemaTypeSnippet* and *DataClassSnippet* have been replaced by *AssociatedSnippet*.

--8<-- "snippets/abbr.md"