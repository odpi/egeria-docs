<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0385 Controlled Glossary Development

Many organization that use glossary terms to drive the operation of the data landscape, need to use a controlled process to introduce and amend glossary terms, because the consequences of any change need to be carefully considered.  

This model covers the extensions needed to support a controlled development process for glossary terms.  Typically, the organization has its (approved) live glossary locked read-only to normal users.  When updates need to be made, copies of the affected glossary terms and related elements are made and linked to their original element via the [SourcedFrom](/types/0/0011-Managing-Referenceables) relationship.

In addition, the following associations are made:

* If the copied element is a glossary term it is also linked to the editing glossary via the [TermAnchor](/types/3/0330-Terms) relationship.
* If the copied element is a glossary category it is also linked to the editing glossary via the [CategoryAnchor](/types/3/0320-Category-Hierarchy) relationship.
* All copies of elements made to support an editing glossary will have their [*Anchors* classification](/types/0/0010-Base-Model) set to the editing glossary's unique identifier so if the editing glossary is deleted, all the copies are deleted too.


![editing glossary](editing-glossary.svg)
> An example of an editing glossary with its glossary terms linked to the appropriate terms in the live glossary.

Once the updates are complete, they go through a review and approval process.

Once approved, the changes identified in the editing glossary are made to the terms in the live glossary.  The [Glossary Manager OMVS](/services/omvs/glossary-manager/overview) supports a simple model that updates a glossary term based on the values from another glossary term and this can be used to perform a simple *merging* process. Alternatively, a [Governance Action Process](/concepts/governance-action-process) can perform the merging process.  This would run asynchronously to the end user request, which is useful if the editing glossary is large, and it can manage conflicts and organize the subsequent correction and resubmission of the changes through its stewardship support.  

![UML](0385-Controlled-Glossary-Development.svg)

## EditingGlossary classification

The *EditingGlossary* classification identifies that a glossary contains copies of live glossary terms that are being updated as part of a controlled glossary development process.

The contents of the editing glossary may represent a single change, changes associated with a particular project/community or may represent a new release of the whole glossary.

## StagingGlossary classification

The *StagingGlossary* classification identifies that a glossary contains copies of live glossary terms that are being published from a source glossary into a new glossary as part of a controlled glossary development process.


--8<-- "snippets/abbr.md"