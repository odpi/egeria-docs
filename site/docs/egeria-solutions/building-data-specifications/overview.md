<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Building data specifications

Every data project begins with the same conversation, and it is rarely a smooth one.  The people who need the data describe it in business language.  The people who have to supply it need column names, types and units.  In between, requirements are written into documents and spreadsheets that no tool can act on, and that quietly go stale the moment the project starts building.

A *data specification* replaces that document with metadata.  It records what data a project or new capability needs, in a form that can be reviewed by the business, matched against the data you actually hold, and used to generate what is missing.

## What a data specification contains

A [data specification](/concepts/data-specification) is a [collection](/concepts/collection) whose members are [data structures](/concepts/data-structure).  Each data structure is an ordered list of [data fields](/concepts/data-field), and each data field describes one type of data item that is required.

The ordering matters: it identifies the order in which the fields should be implemented in the resulting data source.  A field can also be marked as optional, or as something that may occur several times.

Data fields carry the detail that makes a requirement testable rather than aspirational:

| Property | Purpose |
|----------|---------|
| `dataType`, `length`, `minimumLength`, `precision` | The logical type and size of the value. |
| `units`, `absoluteUncertainty`, `relativeUncertainty` | What the value is measured in, and the accuracy of the instrument that produced it - essential for scientific and manufacturing data. |
| `isNullable`, `defaultValue` | Whether the value may be absent, and what to use when it is. |
| `orderedValues`, `sortOrder` | Whether the values are sorted, and in which direction. |
| `aliases`, `namePatterns` | Alternative names and match patterns, used when comparing the specification against a real schema. |
| `namespacePath` | Optional namespace used to build a qualified name for the field. |
| `isDeprecated` | Marks a field that should no longer be used. |

The *ObjectIdentifier* classification marks a field that is used as a unique identifier, which is what lets tooling recognize the key of a data set without being told.

The example below is the data structure behind one of Egeria's own digital products.  It shows the data specification it belongs to, and the ordered data fields that make it up.

--8<-- "snippets/data-structures/data-structure-for-digital-product-list-mermaid-graph.md"

## Reusing definitions through a data dictionary

Specifying every project's data from scratch produces subtly different definitions of the same thing, which is how an organization ends up with five incompatible versions of *customer name*.

A [data dictionary](/concepts/data-dictionary) is an organized, curated collection of pre-defined data fields that acts as the reference set for data professionals.  A new specification is assembled by selecting from it, and only genuinely new requirements are defined from first principles.  A dictionary might describe the fields found in a particular data store, or the typical fields of a [subject area](/concepts/subject-area), or serve as a set of templates for building new specifications.

The graph below shows a single data field - *Display Name* - held in a data dictionary and reused by many data structures.  That reuse is the whole point: consumers of any of those structures know they are looking at the same thing.

--8<-- "snippets/data-fields/display-name-mermaid-graph.md"

## Adding meaning

A data field on its own says what shape the data is.  Two further links say what it *means*:

* A [glossary term](/practices/common-data-definitions/anatomy-of-a-glossary) attached to the field states the business concept it holds, using the definitions your subject-matter experts have agreed.
* A [data class](/concepts/data-class) attached to the field states the kind of value it is - a postcode, an email address, a patient identifier - which is what allows values to be recognized and validated automatically.

This is the join between the work described in [Capturing expertise](/egeria-solutions/capturing-knowledge/overview) and the concrete data that a project delivers.

## From specification to implementation

As a project progresses, the specification stops being a wish list and starts being a template and a test:

* The `aliases` and `namePatterns` on each field are used to **match** the specification against the [schemas](/concepts/schema) of data assets you already hold, to find out what part of the requirement is already met.
* The data structures can be used to **manufacture** schemas for the data assets that have to be built, so that the implementation starts from the agreed definitions rather than a fresh interpretation of them.
* The *DataStructureDefinition* relationship links a data structure to a certification type, so that a data source can be **certified** as conforming to the structure and its associated glossary terms and data classes.

Because the same data fields are referenced throughout, the trail from a project requirement to the column that satisfies it stays intact, and a change to the definition is visible everywhere it is used.

## Where else data specifications are used

The same artefact appears at both ends of a data exchange, which is what allows the two ends to be matched:

* A **data sharing request** in a [data sharing hub](/patterns/harvest-and-publish/overview) uses a data specification to state what the requester needs.  The hub's data dictionary is the menu the requester selects from.
* A **[digital product](/concepts/digital-product)** uses one, through the *DataDescription* relationship, to describe the data it delivers to its subscribers.

Requirement, request and offer are then expressed in one vocabulary, so a consumer can be pointed at the product that already satisfies what they were about to ask for.

## Tools

* The [Data Designer](/services/omvs/data-designer/overview) API creates and maintains data specifications, data dictionaries, data structures and data fields.
* [Dr.Egeria](/user-interfaces/dr-egeria/overview) allows a specification to be authored as a Markdown document, so it can be drafted and reviewed by the business before it is loaded.
* [Egeria Explorer](/user-interfaces/egeria-explorer/overview) displays the specification and its mermaid graphs, and navigates from a field to everywhere it is used.

!!! info "Related information"

    * [Model 0580 Data Dictionaries](/types/5/0580-Data-Dictionaries) - the open metadata types for data specifications, data dictionaries, data structures and data fields.
    * [Data specification](/concepts/data-specification), [data dictionary](/concepts/data-dictionary), [data structure](/concepts/data-structure) and [data field](/concepts/data-field) concepts.
    * [Harvest and Publish](/patterns/harvest-and-publish/overview) - data sharing hubs and digital products, both of which build on data specifications.

--8<-- "snippets/abbr.md"
