---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Repository Governance Open Metadata Engine Services (OMES)

The Repository Governance Open Metadata Engine Service (OMES) runs in an [Engine Host OMAG Server](/concepts/engine-host). It hosts [repository governance engines](/concepts/repository-governance-engine) that consist of one or more related [repository governance services](/guides/developer/repository-governance-services/overview).  Governance repository services are pluggable connectors that perform repository governance services such as maintain [open metadata archives](/concepts/open-metadata-archive) based on the live metadata in the connected open metadata repositories.

![Repository Governance OMES](/services/omes/engine-services-repository-governance-server-side.svg)

The Repository Governance OMES provides access to the open metadata ecosystem for the repository governance services through a context. It also provides an API to allow a third party tool to validate that a specific repository governance service implementation will load in the engine host server, and it returns the usage information encoded in the service's implementation.

## Using the Repository Governance OMES

The definitions for both the repository governance engines and their linked services are stored in a [governance engine definition](/concepts/governance-engine-definition).  The governance metadata definitions are loaded as metadata into the open metadata ecosystem.

When the Repository Governance OMES is configured in the engine host, a list of repository governance engine names is supplied.  These names are used to retrieve the governance engine definitions for the archive engines in order to configure the Repository Governance OMES.

The Repository Governance OMES is responsible for initializing the repository governance engines and providing the context and runtime environment for the repository services when they are requested through the [governance action](/concepts/governance-action) processing of the [Governance Engine OMAS](/services/omas/governance-engine/overview).

--8<-- "snippets/abbr.md"
