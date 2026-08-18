<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Capturing knowledge from your subject-matter experts

Most of what an organization knows about its data is not written down.  It is held by the people who have worked with it for years: which system is authoritative, why that column is always null before 2019, what the difference is between a *customer* and an *account holder*, and which steps have to happen before a data set can be released.  That knowledge walks out of the door when they change jobs, and it is re-learned - expensively - by whoever comes next.

The obstacle is never the will to write it down.  It is that capturing knowledge is usually organized as a documentation project running alongside the real work, in a tool the experts do not otherwise use, producing an artefact that no system can act on.  Egeria's approach is to make the capture part of the work, and to make what is captured immediately useful.

## What is worth capturing

### Meaning

A [glossary](/practices/common-data-definitions/anatomy-of-a-glossary) is a collection of semantic definitions, focused on the meaning of data.  Each [glossary term](/concepts/glossary-term) describes a single concept, starting with a name and a short description that distinguishes it from every other term.  Where a term matters enough, it can be built out with a detailed description, usage notes, examples, images and links to further information.

Terms are organized with categories, related to each other with [term relationships](/types/3/0350-Related-Terms) that pin down *how* two concepts are connected, and classified to show how they are intended to be used.  An organization typically has several glossaries, each with a defined scope and an owner responsible for the quality of what it contains.

### Scope

[Subject areas](/concepts/subject-area) group the definitions into the topics of knowledge that matter to the organization - typically the data that is widely shared, where consistency between copies has business value.  Deciding the subject areas is a strategic act rather than a modelling exercise: it determines where the effort goes.

### Values

Meaning is only half the story.  The [valid values](/guides/planning/valid-values/overview) and [reference data](/features/reference-data-management/overview) that define which values are permitted, and the quality rules that check them, turn a definition into something that can be enforced.  A [data class](/concepts/data-class) captures the shape of a particular kind of value, so that data of that kind can be recognized automatically wherever it appears.

### Procedures

Expertise is not only vocabulary; much of it is procedure - the sequence of steps an experienced person follows to onboard a supplier, release a data set or retire a system.  A [governance action process](/concepts/governance-action-process) captures that sequence as metadata: the steps, the order, and the conditions under which each one runs.  Written this way, the procedure is documentation *and* an executable process, so what the expert described is what actually runs - and the description carries the explanation of what each step is for:

--8<-- "snippets/governance-action-processes/onboard-landing-area-files-for-clinical-trial-project-mermaid-graph.md"

### Context for people and AI

Newer types capture the knowledge that helps someone - or something - work effectively in a domain: [perspectives](/types/1/0145-Perspectives) describe a point of view on the metadata, [questions](/types/3/0340-Dictionary) record the things people actually need answered, and skills and skill sets describe the capabilities a role requires.  This material is what gives an AI application useful context about your organization, rather than generic knowledge about the world.

## Making capture part of the work

[Dr.Egeria](/user-interfaces/dr-egeria/overview) is the route in for people who will never use a metadata tool.  Definitions are authored as ordinary Markdown documents that mix explanation with the commands that create the metadata - the approach described under [literate governance](/concepts/literate-governance).

This matters practically:

* The expert works in whatever editor they already use - including [Obsidian](/user-interfaces/dr-egeria/overview) or a notebook environment - not in a system they have to be trained on.
* The document can be circulated for peer review, argued over and corrected, because it reads as prose.
* It can be validated and reprocessed as many times as it takes, and the command language includes report requests so the author can check that what they meant is what got loaded.
* The artefact people collaborate on and the artefact that configures the ecosystem are the same artefact, so they cannot drift apart.

A particularly effective pattern is the **form and report round trip**: Egeria generates a Markdown form containing everything that is known so far - for example, every field in a newly derived data dictionary - the expert and their colleagues fill in the gaps, and the completed document is loaded back.  This is how [Robbie Records](/practices/coco-pharmaceuticals/scenarios/patient-data-sharing-hub/overview) documents his patient data dictionary, and the document itself sparks enough interest that colleagues ask for copies.

Not all contributions need to be that formal.  The [Feedback Manager](/services/omvs/feedback-manager/overview) API supports comments, informal tags, reviews and ratings, which is how knowledge gets crowd-sourced from the people using a resource day to day - see [user feedback](/features/user-feedback/overview).  Note logs let an owner post the status and events that consumers need to know about.

## Putting the knowledge to work

Captured definitions earn their keep by being attached to things:

* Glossary terms and data classes attach to [data fields](/concepts/data-field) in a [data specification](/egeria-solutions/building-data-specifications/overview), so a project's requirements are stated in agreed language.
* They attach to the schema attributes of catalogued assets, so a consumer reading a column definition sees what the data means, not just its type.
* [Governed data classifications](/types/4/0422-Governed-Data-Classifications) link definitions to governance requirements, so classifying data also determines how it must be handled.

The [common data definitions](/practices/common-data-definitions/overview) practice describes the full lifecycle around this - harvesting existing definitions, managing them with subject-matter experts, consuming them in the tools that build new capability, and delivering value in production - and [semantic to implementation](/practices/common-data-definitions/semantic-to-implementation) shows how the semantic layer connects to the physical one.

## Seeing it in practice

* [Defining the subject areas for data](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview) - Erin Overview and Peter Profile start from Coco Pharmaceuticals' existing enterprise information model and discover that it mirrors the org chart and challenges nothing.  Talking to manufacturing and sales about where the business is going produces a very different set of subject areas, centred on patient, clinician and treatment.
* [Defining a glossary](/practices/coco-pharmaceuticals/scenarios/defining-a-glossary/overview) - building the semantic definitions that give those subject areas their meaning.
* [Planning for common data definitions](/practices/coco-pharmaceuticals/scenarios/planning-for-common-data-definitions/overview) - how the work is organized and who does it.

!!! info "Related information"

    * [Anatomy of a glossary](/practices/common-data-definitions/anatomy-of-a-glossary) - glossaries, terms, categories, relationships and classifications.
    * [Glossary Manager](/services/omvs/glossary-manager/overview) and [Subject Area](/services/omvs/subject-area/overview) APIs - maintaining glossaries, terms and subject area definitions.
    * [Literate governance](/concepts/literate-governance) - the philosophy behind Dr.Egeria's Markdown documents.
    * [Organization Engagement](/patterns/organization-engagement/overview) - the wider pattern of engaging people across the organization.

--8<-- "snippets/abbr.md"
