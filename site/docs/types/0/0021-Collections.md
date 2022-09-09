<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0021 Collections

![UML](0021-Collections.svg)

## Collection

*Collection*s provide a general mechanism for grouping entities together.  They are [*Referenceable*](/types/0/0010-Base-Model) so collections can be nested inside one another.

## Classifications

The classifications associated with *Collection* allow it to be specialized for particular uses.

* *Folder* means the collection can be treated as if it where a folder on the file system.
* *Set* means the collection is a set of related items.
* [*GovernanceStatusSet*](/types/4/0421-Governance-Classification-Levels) for a collection of governance statuses.
* [*GovernanceClassificationSet*](/types/4/0421-Governance-Classification-Levels) for a collection of governance classification for a particular governance classification.
* [*EventSet*](/types/5/0421-Governance-Classification-Levels) for a collection of related event schemas.


--8<-- "snippets/abbr.md"
