<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Crossing Data Boundaries

Organizations sort their data into categories, and then manage each category separately - its own tool, its own team, its own vocabulary, often its own budget.  The categories are useful; the boundaries between them are where value quietly leaks away, because any question that spans two of them turns into a project.

| Category | What it is | Where it usually lives |
|----------|------------|------------------------|
| **Master data** | The key entities the business is described in terms of: customers, suppliers, products, people, organizations, locations, systems. | An MDM hub, or several systems of record that disagree. |
| **Reference data** | The agreed code sets and valid values that other data refers to: country codes, product categories, status values. | Spreadsheets, and a table in each application. |
| **Metadata** | What data exists, where it is implemented, how it is structured, where it came from and how it must be governed. | A catalog, if there is one. |
| **Transactional data** | The operational record of what the business did. | The applications and data stores that run the business. |
| **Analytics** | What has been derived from the rest: measurements, models, reports, insight. | Warehouses, lakes, notebooks and dashboards. |

Egeria's contribution is not to move this data into one place.  It is to hold the *descriptions* of all of it in one knowledge graph, and to link them, so that the relationships that cross the boundaries can be followed.

## What gets linked

**Master data** is described by the same open metadata types as everything else.  [Assets](/concepts/asset) describe the systems and data stores; [actor profiles](/features/people-roles-organizations/overview) describe the people, teams and organizations; [digital products](/concepts/digital-product) describe what is offered; [locations](/types/0/0025-Locations) describe where things are, physically and digitally.  Because these are ordinary metadata elements, a person can be linked to the role that makes them responsible for an asset, and an asset can be linked to the location and the business capability it serves.

**Reference data** is managed as [valid values and reference data sets](/features/reference-data-management/overview), so the code set exists once and every use of it points at the same definition.  A [data class](/concepts/data-class) describes the kind of value a field holds, which allows values encountered in real data to be recognized against the reference set rather than eyeballed.

**Metadata** is the connective tissue: the schemas describing the structure of each store, the [lineage](/features/lineage-management/overview) describing how data moves between them, the [information supply chains](/concepts/information-supply-chain) describing those flows in business terms, and the governance definitions describing how each must be handled.

**Analytics and insight** come back into the graph rather than accumulating outside it.  [Survey reports](/concepts/survey-report) hold the measurements and profiles produced by analysing resources, and their annotations attach to the assets they describe, so the analysis of a data set is found next to the data set.

## The joins that make it work

Linking categories requires something to join on.  Egeria provides several, and they are worth knowing because they are the mechanisms that make cross-boundary questions answerable:

* **Glossary terms and data classes** are the semantic join.  When the same term is attached to a field in an operational store, a field in a warehouse table and a data field in a project's [data specification](/egeria-solutions/building-data-specifications/overview), those three things are known to mean the same thing - even though nothing about their names or types agrees.
* **Data fields in a data dictionary** are the field-level join across stores.  This is what a [data sharing hub](/patterns/harvest-and-publish/overview) is built on: one data field identifies similar data wherever it appears, so a consumer describes what they want once rather than once per store.
* **[External identifiers](/features/external-identifiers/overview)** are the identity join across tools.  The same resource is known by different names in different systems; recording those names against one asset means an automated process can look up whichever identifier the tool it is calling expects.
* **Reference values** are the coding join.  Shared code sets let data from different sources be compared and combined without a translation step being invented each time.
* **Lineage and information supply chains** are the flow join, connecting a transactional source to the analytics eventually derived from it, through every hop in between.

## What this makes possible

Once the links exist, questions that used to require an investigation become queries:

* Which digital products depend on data originating in a particular country - and therefore which are affected by a change in that jurisdiction's rules?
* Which analytics and reports are built on a data set that has just been reclassified as confidential?
* Which teams and roles need to be told when a system is retired, because they own something downstream of it?
* Where else does this data field appear, and do those copies agree with the authoritative source?

The same links are what allow [automation](/patterns/active-governance/overview) to act.  A governance action can navigate from a classification to the resources it applies to, and from those resources to the people responsible, without any of that navigation being hard-coded.

## Sharing across the boundary in both directions

Linking descriptions is one half; moving data across the boundary is the other.  The [Harvest and Publish](/patterns/harvest-and-publish/overview) pattern packages open metadata - including the master data, reference data and insight described above - into [digital products](/concepts/digital-product) delivered as tabular data sets into whatever the consuming team already uses: a CSV file, a database table, a Kafka topic.  Reference data curated in Egeria can therefore be distributed to the applications that need it, and insight derived from the ecosystem can be delivered to the analysts who will act on it.

The graph below is one such family from Egeria's own product catalog - the master data of the ecosystem, published as products that other tools can subscribe to:

--8<-- "snippets/collections/digital-products/actor,-places-and-product-master-data-mermaid-graph.md"

!!! info "Related information"

    * [Reference data management](/features/reference-data-management/overview) - representing, distributing and governing reference data.
    * [External identifiers](/features/external-identifiers/overview) - correlating the same resource across different tools.
    * [Information Exchange](/patterns/information-exchange/overview) - the automation that keeps metadata synchronized between tools and platforms.
    * [Harvest and Publish](/patterns/harvest-and-publish/overview) - data sharing hubs and the digital product catalog.

--8<-- "snippets/abbr.md"
