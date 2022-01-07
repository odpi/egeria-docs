---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Archive Manager Open Metadata Engine Services (OMES)

The Archive Manager Open Metadata Engine Service (OMES) runs in an [Engine Host OMAG Server](/egeria-docs/concepts/engine-host).

It provides access to the open metadata ecosystem for [archive services](/egeria-docs/types/4/0461-Governance-Engines). These are pluggable connectors that maintain [open metadata archives](/egeria-docs/concepts/open-metadata-archive) based on the live metadata in the connected open metadata repositories.

The Archive Manager OMES also provides an API to allow a third party tool to validate that a specific archive service implementation will load in the engine host server, and it returns the usage information encoded in the service's implementation.

## Using the Archive Manager OMES

Archive services are defined and linked to one or more archive engines using the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine). The definitions for both the archive engines and their linked services are stored in a [metadata access server](/egeria-docs/concepts/metadata-access-server).

When the Archive Manager OMES is configured in the engine host, a list of archive engines is supplied. This determines which archive engines and hence archive services that it supports.

The Archive Manager OMES is responsible for initializing the archive engines and providing the context and runtime environment for the archive services when they are requested by third party technologies or through the governance action processing of the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine).

--8<-- "snippets/abbr.md"
