<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Governance Officer API

The Governance Officer API provides the ability to define and maintain
governance definitions, regulations, metrics, and manage licenses and certifications for metadata elements.
It also supports the tracking of implementation resources back to their design elements, exploring
governance action processes, and recording the decisions that are made, what was assessed to make them and what resulted from them.

## Key features

* **Governance Definition Management**: Support for creating, updating, and deleting governance definitions, including the ability to create definitions from templates.
* **Relationship Management**: Capabilities for linking and detaching peer and supporting governance definitions, and associating definitions with metadata elements using the *GovernedBy* relationship.
* **Regulatory Compliance**: Linking regulator organizations to regulation governance definitions.
* **Governance Results Tracking**: Associating governance metrics with the data stores where measurements are located.
* **Licenses and Certifications**: Managing the lifecycle of licenses and certifications for metadata elements, including linking to license/certification types and updating properties.
* **Governance Action Process Exploration**: Visualizing and exploring the structure of governance action processes through process graphs.
* **Implementation and Design Tracking**: Linking design elements to implementation resources and implementation elements to track how governance requirements are realized.
* **Decisions**: Recording decisions, the assessments of the elements that contributed to them, and their outcomes.

??? info "Further information"

    * [Governance Definition Concept](/concepts/governance-definition/)
    * [Governance Action Concept](/concepts/governance-action/)
    * [0018 Decisions](/types/0/0018-Decisions) describes the open metadata types for decisions.
    * [Defining a governance program](/guides/planning/governance-program/overview)

----
Sample REST API requests can be found in [Egeria-api-governance-officer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/governance-officer/Egeria-api-governance-officer.http).

## Recording decisions

A [*Decision*](/types/0/0018-Decisions/#decision-entity) documents a decision that has been made: its summary, scope, usage, importance, disposition (status) and implications, notes on why it was made, and when it starts, was last reviewed, is next due for review and expires.

| Operation | URL (after the URL marker) | Request body |
|---|---|---|
| *createDecision* | `/decisions` | *NewElementRequestBody* |
| *createDecisionFromTemplate* | `/decisions/from-template` | *TemplateRequestBody* |
| *updateDecision* | `/decisions/{decisionGUID}/update` | *UpdateElementRequestBody* |
| *deleteDecision* | `/decisions/{decisionGUID}/delete` | *DeleteElementRequestBody* |
| *getDecisionsByName* | `/decisions/by-name` | *FilterRequestBody* |
| *findDecisions* | `/decisions/by-search-string` | *SearchStringRequestBody* |
| *getDecisionByGUID* | `/decisions/{decisionGUID}/retrieve` | *GetRequestBody* |

A decision is linked to the elements around it with two relationships:

* The [*Outcome*](/types/0/0018-Decisions/#outcome-relationship) relationship links a decision to an element that represents an outcome of the decision, with the importance and disposition of that outcome.  There is at most one *Outcome* relationship between a decision and an element, so it is attached and detached using the unique identifiers of the decision and the element (*linkDecisionOutcome* / *detachDecisionOutcome*).
* The [*Assessment*](/types/0/0018-Decisions/#assessment-relationship) relationship links an element that was assessed to the decision that the assessment contributed to.  It records who made the assessment, when it was made, when it expires and any notes.  It is a [multi-link](/concepts/uni-multi-link) relationship: the same element may be assessed many times for the same decision.  For this reason, *linkAssessment* always creates a new relationship and returns its unique identifier, and *updateAssessment* and *detachAssessment* use that identifier rather than the identifiers of the two elements.

| Operation | URL (after the URL marker) | Request body |
|---|---|---|
| *linkDecisionOutcome* | `/decisions/{decisionGUID}/outcomes/{outcomeGUID}/attach` | *NewRelationshipRequestBody* |
| *detachDecisionOutcome* | `/decisions/{decisionGUID}/outcomes/{outcomeGUID}/detach` | *DeleteRelationshipRequestBody* |
| *linkAssessment* | `/elements/{elementGUID}/assessments/{decisionGUID}/attach` | *NewRelationshipRequestBody* |
| *updateAssessment* | `/assessments/{assessmentGUID}/update` | *UpdateRelationshipRequestBody* |
| *detachAssessment* | `/assessments/{assessmentGUID}/detach` | *DeleteRelationshipRequestBody* |

When a decision is retrieved, the elements that were assessed are returned in *inputsToDecision* and its outcomes in *decisionOutcomes*.  An element that has been assessed shows the decisions in *assessmentDecisions*, and an element that is an outcome of a decision shows it in *associatedDecisions*.

## Defining a governance strategy

??? info "Further information"
    * [Defining the data strategy for Coco Pharmaceuticals](/practices/coco-pharmaceuticals/scenarios/defining-the-data-strategy/overview)




--8<-- "snippets/abbr.md"
