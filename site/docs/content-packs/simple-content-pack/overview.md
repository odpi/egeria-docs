---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Simple Content Pack

The *SimpleCatalog* provides an example of a database, an API and an event structure linked to a glossary term.
It is loaded automatically in the *simple-metadata-store* sample server.
SimpleCatalog is also supplied as four archives for use in a demo showing 4 metadata access servers connected together in a single cohort.
The archives are each loaded into a different server.
It is then possible to show how the cohort integrates metadata from different catalogs.
These archives are used in the *Development labs* which are part of the [Open Metadata Labs](/education/open-metadata-labs/overview/).

* *SimpleAPICatalog* - API metadata typically found in an API catalog.

* *SimpleDataCatalog* - Database metadata typically found in an Data catalog.

* *SimpleEventCatalog* - Event metadata typically found in an API catalog.

* *SimpleGovernanceCatalog* - A glossary term linked to metadata elements in the API, Event, Data catalogs.

This picture shows how the simple catalog's metadata is distributed between the 4 different archives.

![Simple Catalog Data Map](simple-catalog-data-map.svg)

--8<-- "snippets/abbr.md"