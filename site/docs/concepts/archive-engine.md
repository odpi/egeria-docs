<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2019, 2020. -->

---
hide:
- toc
---

# Archive Engine

The archive engine describes a set of related [archive services](/egeria-docs/guides/developer/archive-services/overview) that dynamically manage [open metadata archives](/egeria-docs/concepts/open-metadata-archives).

An archive engine is hosted in the [Archive Manager Open Metadata Engine Service (OMES)](/egeria-docs/services/omes/archive-manager/overview) running on one or more [Engine Host OMAG Servers](/egeria-docs/concepts/engine-host).

When an archive engine is called, it is passed a governance request type and request parameters. This is mapped to a call to an archive service through the [archive engine definition](/egeria-docs/concepts/governance-engine-definition).

![Archive Engine Definition Structure](/egeria-docs/guides/developer/open-metadata-archives/archive-engine-definition.svg)
> Logical structure of an archive engine definition showing how the governance request types map to the archive service definitions

??? education "Further information"

    The Open Metadata Types used to define the archive engines are located in model **[0461 Governance Engines](/egeria-docs/types/4/0461-Governance-Engines)**.




--8<-- "snippets/abbr.md"