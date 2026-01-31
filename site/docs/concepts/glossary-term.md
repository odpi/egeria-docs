<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Glossary Term

A glossary term describes the meaning of a word or phrase.  The definition includes examples, abbreviations as well as a detailed description of the term's meaning.

It is possible that the same term has different meanings depending on the context.  For example, the term "client" can mean a customer or a piece of software used to make calls to a service.  This is captured using two glossary terms, one for each of the meanings.  The *displayName* contains the term.  Each glossary term has a different *qualifiedName*.
The *description* attribute captures the meaning of the term. Each of the terms may be linked to an element that describes the [context](/types/3/0360-Contexts) in which it is used.

Glossary terms are organized into special types of collections called [glossaries](/practices/common-data-definitions/anatomy-of-a-glossary).  The same glossary term may be linked to multiple glossaries.

???+ info "Further information"

    * [Anatomy of a Glossary](/practices/common-data-definitions/anatomy-of-a-glossary) describes how glossary terms are organized.
    * [Glossary Manager API](/services/omas/glossary-manager/overview) provides the operations to create your own glossary terms.
    * [Type definition for a glossary term](/types/3/0330-Terms)
    * [Type definition for a glossary](/types/3/0310-Glossary)


---8<-- "snippets/abbr.md"