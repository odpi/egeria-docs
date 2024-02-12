<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0011 Managing Referenceables

[Referenceable](/types/0/0010-Basic-Model) entities can have chains of related feedback and additional knowledge attached to them. The following types help a metadata manager to process these collections of elements more efficiently.

![UML](0011-Managing-Referenceables.svg)

## LatestChange classification

The *LatestChange* classification is a convenience mechanism to indicate where the last change occurred. Components that are monitoring [Referenceable](/types/0/0010-Base-Model/#referenceable) entities can use the open metadata events related to classifications to monitor changes to the entity.

## Template classification

Templates are used when creating new elements that are similar.  For example, consider the case when multiple resources need to be catalogued as assets with the same classifications.  One of the assets can be set up to act as a template.  The other resources can be catalogued using the first asset as a template.

![Example of the use of a template](template-use-case-1.svg)

The *Template* classification indicates that a [*Referenceable*](/types/0/0010-Base-Model/#referenceable) entity is a good element be used as a template when creating a new element of the same type. There is no restriction on using *Referenceable* entities without this classification as templates. The *Template* classification is simply a useful marker to indicate that the referenceable does not represent a real resource, since it is only a template.  

![Example of the use of a Template classification](template-use-case-2.svg)

The properties for the *Template* classification are:

* *name* - name of the template, designed to help the selection of the correct template.
* *description* - further information on the purpose of the template.
* *placeholderProperties* - provides the names of the [placeholder properties](/concepts/placeholder) mapped to a description/guidance of the value to supply when the template is used.
* *replacementProperties* - provides the names of the attributes in the top-level entity created from the template that should be replaced.   Again each attribute name is mapped to a description of the value to supply and its use.  replacement properties can be used for attributes of type string, boolean, int and long.
* *additionalProperties* - allows additional information about the template to be supplied

Templates can include relationships.  If the relationship links to an entity that has the same anchor as the starting entity, the entity and the relationship is replicated.  If the linked entity is part of a different anchor, only the relationship is created.  In the example above, the glossary term has a different anchor to the asset.  Therefore any assets created with *tAsset* as a template will be linked to the same glossary term.

## TemplateSubstitute classification

If a query requests all assets linked to the glossary term, *GlossaryTerm*, the *tAsset* entity will be returned with the other assets.  This could be confusing.  Therefore it is possible to create a copy of the glossary term that is linked to *tAsset*.  This copy has the *TemplateSubstitute* classification to show that the real glossary term to link a new asset to is identified by the *SourcedFrom* relationship.

![Example of the use of a TemplateSubstitute classification](template-use-case-3.svg)

With this set up, when *Asset2* is created with the template *tAsset*, it is linked to the same glossary term as *Asset*.

![Example of the use of a template](template-use-case-4.svg)

## SourcedFrom relationship

When one *Referenceable* entity is created by using another *Referencable* entity as a template, the *qualifiedName* must be changed in the new entity to give it a unique name - often the *displayName* value changes, too. This makes it hard to identify the source of a *Referenceable* entity's values.

The *SourcedFrom* relationship is used to show the provenance of the information from the template. This is useful to help trace where information has come from and to help understand any potential impact cause by a change to the template if this change also needs to be made to the elements that were copied from it.

The *sourceVersionNumber* identifies the version number of the template used when the new entity was created.

## CatalogTemplate relationship

The *CatalogTemplate* relationship links an *OpenMetadataRoot* entity that describes a class of technology with a [template](/features/templated-cataloguing/overview) for creating a catalog entry for a resource of this class.

??? deprecated "Deprecated types"
    - *LastAttachment* - use *LatestChange* instead
    - *LastAttachmentLink* - use *LatestChange* instead

??? education "Further information"
    - [Anchor Management](/features/anchor-management/overview)
    - [Using templates](/features/templated-cataloguing/overview)
    - [Automated Curation OMVS](/services/omvs/automated-curation/overview)

--8<-- "snippets/abbr.md"
