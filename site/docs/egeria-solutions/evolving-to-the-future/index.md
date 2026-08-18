<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Evolving to the future

[Leveraging your estate](/egeria-solutions/leveraging-your-estate) is about understanding the digital resources you already have and making better use of them.  Once that picture is emerging, attention turns to what comes next: the transformation projects that build the new capability your organization needs.

The solutions under *Evolving to the future* accelerate that work.  What holds a transformation project up is rarely the technology.  It is not being able to say precisely what data is needed; expertise that lives in people's heads and is never written down; designs that drift away from what actually got built; boundaries between the different kinds of data an organization keeps; and the awkward handovers between automated processes and the people who have to make the decisions.  Egeria has something to offer in each case.

## Building data specifications

At the start of a project, the need is to articulate *what data is required* - before anyone knows which system it will come from, or whether it exists at all.

A [data specification](/concepts/data-specification) captures exactly that.  It is built from [data structures](/concepts/data-structure), each an ordered list of [data fields](/concepts/data-field) describing the logical type of every data item needed, and each field can be linked to a [data class](/concepts/data-class) and a [glossary term](/practices/common-data-definitions/anatomy-of-a-glossary) so that its meaning is unambiguous.  A [data dictionary](/concepts/data-dictionary) holds pre-defined, reusable fields, so later projects specify their requirements by selecting from definitions the organization has already agreed rather than inventing new ones.  As the project progresses, the specification is matched against - and used to manufacture - the schemas of the concrete data assets that satisfy it.

The same artefact does more than start projects.  A [data sharing request](/patterns/harvest-and-publish/overview) uses a data specification to say what data is being asked for, and a [digital product](/concepts/digital-product) uses one to describe what it delivers.  Requirement, request and offer are all expressed in the same vocabulary, which is what allows them to be matched to each other.

* Solution page: [Building data specifications](/egeria-solutions/building-data-specifications/overview)
* Open metadata types: [0580 Data Dictionaries](/types/5/0580-Data-Dictionaries) - maintained through the [Data Designer](/services/omvs/data-designer/overview) API.

## Capturing expertise

Most of what an organization knows about its data is not written down anywhere.  It is held by the people who have worked with it for years, and it is lost when they move on.

Capturing that expertise means building [glossaries](/practices/common-data-definitions/anatomy-of-a-glossary) that define what terms actually mean, organizing them into [subject areas](/concepts/subject-area), describing repeatable procedures as [governance action processes](/concepts/governance-action-process), and adding the valid values, reference data and quality rules that go with them.  Together these form the *common data definitions* that let different systems and teams share data with a shared understanding - the full picture is described under [common data definitions](/practices/common-data-definitions/overview).

The practical difficulty is never the type system; it is getting busy experts to contribute.  This is why [Dr.Egeria](/user-interfaces/dr-egeria/overview) matters here: definitions are authored as ordinary Markdown documents that can be drafted, circulated for review and corrected in whatever editor the author already uses, then loaded into open metadata.  The goal is for capture to become a natural part of doing the work, rather than a documentation project that competes with it.

The Coco Pharmaceuticals scenarios show how this starts:

* [Defining the subject areas for data](/practices/coco-pharmaceuticals/scenarios/defining-subject-areas/overview) - Erin Overview and Peter Profile discover that their existing enterprise information model simply mirrored the org chart, and that focusing on the business transformation produces a very different, and far more useful, set of subject areas.
* [Defining a glossary](/practices/coco-pharmaceuticals/scenarios/defining-a-glossary/overview) - building the semantic definitions that give those subject areas their meaning.

Solution page: [Capturing expertise](/egeria-solutions/capturing-knowledge/overview)

## Blueprints to delivery

A [solution blueprint](/concepts/solution-blueprint) captures the design of a solution or process: its key [components](/concepts/solution-component), the roles involved, and how data flows between them.  It deliberately stops short of the detail found in a UML or E-R model - its purpose is to support a conversation with stakeholders, so it models only what those people need to discuss and agree on.

Its value grows as the project delivers.  Components are linked to the digital resources that implement them using the [ImplementedBy](/types/7/0737-Solution-Implementation) relationship as those resources appear, so the design and the implementation stay connected instead of drifting apart, and progress becomes visible against the design everyone agreed to.  Once the solution is running, the blueprint becomes the natural aggregation point for the operational picture - the metrics, statistics and [lineage](/concepts/information-supply-chain) that show whether the thing that was built is behaving as designed.

Solution page: [Blueprints to delivery](/egeria-solutions/solution-blueprints/overview)

## Crossing data boundaries

Organizations divide their data into categories and then manage each in its own tool, with its own team and its own vocabulary: master data about the key entities of the business; reference data and code sets; metadata describing where everything is; the transactional data the business runs on; and the analytics derived from it.  Each boundary is a place where value leaks away, because a question that spans two categories cannot be answered without a project.

Egeria's contribution is to link them.  The master data - [assets](/concepts/asset), people and organizations, [digital products](/concepts/digital-product), locations - sits in the same knowledge graph as the reference data that codes it, the metadata that describes where it is implemented and how it flows, and the insight derived from analysing it.  Once those links exist, a question such as which products depend on data from a given location, or which analytics are built on a data set that has just been reclassified, becomes a query rather than an investigation.

Solution page: [Crossing data boundaries](/egeria-solutions/crossing-data-boundaries/overview)

## Human in the loop

Transformation projects run on a partnership between people and automation, and the handover in each direction has to work.

In one direction, people need to see what is going on.  Egeria's [user interfaces](/user-interfaces) show both the structural picture - what exists, how it is defined, how it connects - and the operational status of the ecosystem, with [Egeria Operations](/user-interfaces/egeria-operations/overview) covering the servers, connectors, governance engines and engine actions, and [Egeria Audit](/user-interfaces/egeria-audit/overview) covering exceptions, certifications, licenses and users.

In the other direction, automation needs to reach people.  Egeria's own [governance actions](/concepts/governance-action) - and any other automation connected to the ecosystem, including AI applications - can raise anything from an informational [notification](/concepts/notification) that simply asks to be read, through to a [to-do](/concepts/to-do): a work item assigned to a role, with a priority and a status, that the automation waits on before it continues.  Because an individual has no REST API to call, this is how a process that hits a decision only a person can make gets that decision and carries on.  Who is notified, about what, and how, is managed through the [Notification Manager](/services/omvs/notification-manager/overview) API.

Solution page: [Human in the loop](/egeria-solutions/human-in-the-loop/overview)

---

As the new capability is delivered and begins to operate, the open metadata ecosystem that supported its development becomes a source of insight in its own right.  That is the subject of [Accelerating insight](/egeria-solutions/accelerating-insight).

--8<-- "snippets/abbr.md"
