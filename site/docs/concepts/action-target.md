---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Action Target

An *action target* is a metadata element that is to be processed by a [governance action service](/concepts/governance-action-service) or [repository governance service](/concepts/repository-governance-service).

A list of action targets is passed to the governance service when it starts.  When it completes, it can supply a list of action targets for follow-on governance services to process.

For example, consider a governance action service responsible for verifying that all columns in a database asset are linked to a glossary term with a [semantic assignment](/types/3/0370-Semantic-Assignment) relationship.  It may be supplied with the unique identifier (guid) of the database asset to validate.  If it discovers any columns without a glossary term, it could return a [guard](/concepts/guard) of "incomplete-semantic-assignment" and a list of unique identifiers of the columns that need the semantic assignment as the action targets.  A follow-on governance service would receive this list of columns in its action targets when it starts and could assign a [ToDo](/concepts/to-do) to the appropriate steward for correction along with the list of columns to work on.

The action targets allow work to be passed between governance services.  These governance services are choreographed together using a [governance action process](/concepts/governance-action-process).

--8<-- "snippets/abbr.md"
