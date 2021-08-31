---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Metadata Access Point

A *metadata access point* is an [OMAG Server](omag-server.md) that can be a [member of a cohort](/egeria-docs/services/omrs/cohort/#cohort-members) and supports the [access services](/egeria-docs/services/omas).

![Metadata access point in OMAG Server ecosystem](metadata-access-point.png)

This means it provides specialist metadata APIs to user interfaces and governance servers that embrace metadata from all connected open metadata repository cohorts.

The basic metadata access point has no metadata repository and metadata is retrieved and stored from remote repositories via the [cohort](/egeria-docs/services/omrs/cohort). It can be upgraded to a [metadata server](metadata-server.md) by adding a metadata repository which will enable it to store metadata locally.

--8<-- "snippets/abbr.md"
