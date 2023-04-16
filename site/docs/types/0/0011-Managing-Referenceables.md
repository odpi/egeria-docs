<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0011 Managing Referenceables

[Referenceable](/types/0/0010-Basic-Model) entities can have chains of related feedback and additional knowledge attached to them. The following types help a metadata manager to process these collections of elements more efficiently.

![UML](0011-Managing-Referenceables.svg)

## LatestChange

The *LatestChange* classification is a convenience mechanism to indicate where the last change occurred. Components that are monitoring [Referenceable](/types/0/0010-Base-Model/#referenceable) entities can use the open metadata events related to classifications to maintain a complete picture of the entity.

## Template

The *Template* classification indicates that a [*Referenceable*](/types/0/0010-Base-Model/#referenceable) entity is a good element be used as a template when creating a new element of the same type. There is no restriction on using *Referenceable* entities without this classification as templates. The *Template* classification is simply a useful marker to enable templates to be found.  

## SourcedFrom

When one *Referenceable* entity is created by using another *Referencable* entity as a template, the *qualifiedName* must be changed in the new entity to give it a unique name - often the *displayName* value changes, too. This makes it hard to identify the source of a *Referenceable* entity's values.

The *SourcedFrom* relationship is used to show the provenance of the information from the template. This is useful to help trace where information has come from and to help understand any potential impact cause by a change to the template if this change also needs to be made to the elements that were copied from it.

The *sourceVersionNumber* identifies the version number of the template used when the new entity was created.

??? deprecated "Deprecated types"
    - `LastAttachment` - use `LatestChange` instead
    - `LastAttachmentLink` - use `LatestChange` instead

??? education "Further information"
    - [Anchor Management](/features/anchor-management/overview)
    - [Using templates](/features/templated-cataloguing/overview)

--8<-- "snippets/abbr.md"
