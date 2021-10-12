<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0019 More Information

![UML](0019-More-Information.svg)

## MoreInformation

The *`MoreInformation`* relationship enables [`Referenceable`s](/egeria-docs/types/0/0010-Base-Model/#referenceable) of different subtypes to be associated in a way that indicates that one provides more detail about another. It can be used to show linkage between a glossary and the primary top level category, between a glossary term and its implementation. It is a looser association that a relationship such as [`SemanticAssignment`](/egeria-docs/types/3/0370-semantic-assignment/#semanticassignment).

The [Asset Manager OMAS](/egeria-docs/services/omas/asset-manager/overview) makes use of this relationship to link an asset to a glossary term that is providing supplementary properties to the asset.

--8<-- "snippets/abbr.md"
