<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0016 Cited Documents

Cited documents support open metadata elements to link to a precise citation to remote documents in other types of repositories.

![UML](0016-Cited-Documents.svg)

## CitedDocument entity

*CitedDocument* entity is an [ExternalReference](/types/0/0014-External-References) that describes a specific document in an external repository.

## CitedDocumentLink

*CitedDocumentLink* connects a [Referenceable](/types/0/0010-Basic-Model) to a CitedDocument entity.  It allows a *referenceId* and a precise page range (*pages* attribute) to be specified along with a short description of the relevance of the citation.  This relationship is a multi-link relationship so the same referenceable can link to the same cited document multiple times, with different referenceIds.

--8<-- "snippets/abbr.md"
