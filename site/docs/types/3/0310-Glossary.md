<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0310 Glossary Model

A [glossary](/practices/common-data-definitions/anatomy-of-a-glossary) is a collection of related semantic definitions. A semantic definition describes the meaning of something.  This may be, for example, a concept, object or activity.  These are defined as [Glossary Terms](/types/0330-Terms).  The *Glossary* is a collection of glossary terms and other related definitions.  These can be organized into [folders](/types/0021-Collections).

A metadata repository may contain many glossaries, particularly when it is part of a bigger enterprise.  Each glossary may come from a specific team or external organization. Or it may be focused on a particular topic or set of use cases.

![UML](0310-Glossary.svg)

## Glossary entity

The anchor for each glossary is the *Glossary* entity. 

The *Taxonomy* and *CanonicalVocabulary* classifications associated with the glossary entity are used to document the type of vocabulary it contains and its purpose.
These classifications are independent of one another so a Glossary object may have none, one or all of these classifications attached.

## Taxonomy classification

The *Taxonomy* classification means the glossary includes a formal hierarchy of [Folders](/types/1/0021-Collections) and that a glossary term many only be linked into one of these folders. 

Such a taxonomy can be used to organize a complete collection of formal terms.  It can also be exported onto a content management system and be used to categorize and organize documents and other media in content repositories.

## CanonicalVocabulary classification

The *CanonicalVocabulary* classification means that all the terms in the glossary have a unique name. Typically such a glossary is used to link entities representing data fields with glossary terms via the [SemanticAssignment](/types/3/0370-Semantic-Assignment) relationship to indicate that the glossary term describes the meaning of the data stored in the data field.


--8<-- "snippets/abbr.md"