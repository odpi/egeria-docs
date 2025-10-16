<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0014 External References

Linked media types describe the simple structures that are used repeatedly in open metadata to connect it to documents and entities in other types of repositories.

![UML](0014-External-References.svg)

## ExternalReference entity

*ExternalReference* entity ia a [Referenceable](/types/0/0010-Basic-Model) that describes an external source of information.

## ExternalReferenceLink relationship

*ExternalReferenceLink* connects another [Referenceable](/types/0/0010-Basic-Model) to an ExternalReference entity.  It allows a *label* to be specified along with a short description of the relevance of the external reference.  This relationship is a multi-link relationship so the same referenceable can link to the same external reference entity multiple times, typically with different labels.

## ExternalSourceCode entity

*ExternalSourceCode* is a special type of external reference that refers to software source code source. If the component created from this sourcecode is catalogued, it is linked to the ExternalSourceCode using the *ExternalReferenceLink* relationship.

## ExternalDataSource entity

*ExternalDataSource* is a special type of external reference that refers to an external data source. It is possible that the data from this data source has been extracted and is available internally.  The internal version is typically catalogued as a [DigitalProduct](/types/7/0710-Digital-Products) or a simple [Asset](/types/0/0010/Base-Model).  These elements are then linked to the ExternalDataSource using the *ExternalReferenceLink* relationship.

## ExternalModelSource entity

*ExternalModelSource* is a special type of external reference that refers to an external model (analytical, AI, ...) source. It is possible that the code for this model has been extracted and is available internally.  The internal version is typically catalogued as a [DigitalProduct](/types/7/0710-Digital-Products) or a simple [Asset](/types/0/0010/Base-Model).  These elements are then linked to the ExternalModelSource using the *ExternalReferenceLink* relationship.




--8<-- "snippets/abbr.md"
