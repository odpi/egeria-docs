<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0310 Glossary Model

A [glossary](/practices/common-data-definitions/anatomy-of-a-glossary) is a collection of related semantic definitions. A semantic definition describes the meaning of something.  This may be, for example, a concept, object or activity.

A metadata repository may contain many glossaries, particularly when it is part of a bigger enterprise.  Each glossary may come from a specific team or external organization. Or it may be focused on a particular topic or set of use cases.

![UML](0310-Glossary.svg)

## Glossary entity

The anchor for each glossary is the *Glossary* entity. 

The [EditingGlossary](/types/3/0385-Controlled-Glossary-Development), *Taxonomy* and *CanonicalVocabulary* classifications associated with the glossary entity are used to document the type of vocabulary it contains and its purpose.
These classifications are independent of one another so a Glossary object may have none, one or all of these classifications attached.

## Taxonomy classification

The *Taxonomy* classification means the glossary includes a formal hierarchy of [Glossary Categories](/types/3/0320-Category-Hierarchy) and that a glossary term many only be linked into one of these categories. 

Such a taxonomy can be used to organize a complete collection of formal terms.  It can also be exported onto 
a content management system an be used to categorize and organize documents and other media in content repositories.

## CanonicalVocabulary classification

The *CanonicalVocabulary* classification means that all the terms in the glossary have a unique name. Typically such a glossary is used to link entities representing data fields with glossary terms via the [SemanticAssignment](/types/3/0370-Semantic-Assignment) relationship to indicate that the glossary term describes the meaning of the data stored in the data field.

## ExternallySourcedGlossary relationship

The *ExternallySourcedGlossary* relationship and *ExternalGlossaryLink* indicates that the content of this glossary comes from an external source. It may be, for example an industry-specific glossary, or from a standards body, or from an open data site, or from a commercial organization.

## ExternalGlossaryLink entity

The *ExternalGlossaryLink* entity is a type of [*ExternalReference*](0015-Linked-Media-Types) element that provides a detailed description of the location and provenance of the external glossary.

!!! info "Further information"
    * [Anatomy of a glossary](/practices/common-data-definitions/anatomy-of-a-glossary) describes how to structure your glossary.

--8<-- "snippets/abbr.md"