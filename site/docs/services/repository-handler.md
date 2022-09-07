---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Repository handler 

The Repository Handler module provides services over the enterprise repository connector.

![Repository Handler call stack](repository-handler-call-stack.svg)

The repository handler supports the following features:

* Conversion of OMRS exceptions into common services exceptions.
* Selection of elements to return based on their [effectivity dates](/features/effectivity-dates/overview).
* [Deduplication](/features/duplicate-management/overview) both for entities and relationships.
* Validation of whether elements with the [Memento](/concepts/memento) classification should be returned.
* [Metadata provenance](/features/metadata-provenance/overview) validation.

--8<-- "snippets/abbr.md"