<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0385 Controlled Glossary Development

Many organization that use glossary terms to drive the operation of the data landscape, need to use a controlled process to introduce and amend glossary terms, because the consequences of any change need to be carefully considered.  

This model covers the extensions needed to support a controlled development process for human-authored elements such as glossary terms.  Typically, the organization has its (approved) live versions of these elements locked read-only to normal users.  When updates need to be made, copies of the affected elements (glossary terms in this example) and related elements are made and linked to their original element via the [SourcedFrom](/types/0/0011-Managing-Referenceables) relationship.

In addition, all copies of elements made are linked into an editing collection and their [*Anchors* classification](/types/0/0010-Base-Model) are set to the editing collection's unique identifier so if the editing collection is deleted, all the copies are deleted too.

![editing glossary](editing-glossary.svg)
> An example of an editing collection with its glossary terms linked to the appropriate terms in the live glossary.

Once the updates are complete, they go through a review and approval process.

Once approved, the changes identified in the editing collection are made to the terms in the live collection.  The [Open Metadata View Services](/services/omvs) supports a simple command (updateWithTemplate) that updates a elements based on the values from another element and this can be used to perform a simple *merging* process. Alternatively, a [Governance Action Process](/concepts/governance-action-process) can perform the merging process.  This would run asynchronously to the end user request, which is useful if the editing collection is large, and it can manage conflicts and organize the subsequent correction and resubmission of the changes through its stewardship support.  

![UML](0385-Controlled-Glossary-Development.svg)

## ScopingCollection classification

The *ScopingCollection* classification identifies that a collection contains copies of elements that are being selected for a project or other activity.  It is used to allow discussion and review for which elements are to be worked on.

## EditingCollection classification

The *EditingCollection* classification identifies that a collection contains copies of live elements that are being updated as part of a controlled development process.

The contents of the editing collection may represent a single change, changes associated with a particular project/community or may represent a new release of the whole collection.

## StagingCollection classification

The *StagingCollection* classification identifies that a collection contains copies of elements that are approved to be copied from one collection to another.  When the staging collection's elements are merged into the new collection, an elements that have been previously published this way are updated.


--8<-- "snippets/abbr.md"