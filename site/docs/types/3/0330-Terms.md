<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0330 Terms

The vocabulary for the glossary is documented using glossary terms. Each term represents a concept or short phrase in the vocabulary.  Just like a category, a term is owned by a glossary but can be linked into a category from any glossary.

Model 0330 shows the glossary term.

![UML](0330-Terms.svg)

## GlossaryTerm entity

*GlossaryTerm* represents a term in a glossary. 

## TermAnchor relationship

*TermAnchor* links each term to exactly one Glossary entity. This means that this is its anchor glossary.  If the Glossary object is deleted then so are all the terms linked to it.

## TermCategorization relationship

*TermCategorization* is a relationship used to organize terms into categories (like organizing files into folders on your disk).  A term may be linked with many categories and a category may have many terms linked to it.  This relationship may connect terms and categories both in the same glossary and in different glossaries.

## 
## LibraryTermReference relationship

*LibraryTermReference* provides reference information for how this term corresponds to a term in an external glossary.

--8<-- "snippets/abbr.md"