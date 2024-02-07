---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Governance server

Governance servers host specific integration or governance connectors for technology that does
not integrate directly with open metadata.

![Governance server](governance-server.svg)

These are the different types:

- [Engine hosts](/concepts/engine-host) - host governance engines for active management of the open metadata ecosystem.
- [Integration daemons](/concepts/integration-daemon) - manage the exchange of metadata with third party technologies.
- [Data engine proxy](/concepts/data-engine-proxy) - captures information about processes and the data sources that they work with and catalogs them in open metadata.
- [Lineage warehouse](/concepts/lineage-warehouse) - accumulates lineage information to provide a comprehensive historical reporting service for lineage.

--8<-- "snippets/abbr.md"
