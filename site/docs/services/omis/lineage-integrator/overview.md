---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Lineage Integrator Open Metadata Integration Service (OMIS)

The Lineage Integrator OMIS supports the loading lineage information
from a third party technology.  Specifically this include process structure, ports,
schemas and the data assets they are working with.

## Module Implementation

The modules are as follows:

* [lineage-integrator-api](lineage-integrator-api) - defines the interface for an integration
connector that is supported by the Lineage Integrator OMIS. This includes the implementation
of the context that wraps the Asset Manager OMAS's clients.

* [lineage-integrator-server](lineage-integrator-server) - implements the context manager for
the Lineage Integrator OMIS.

* [lineage-integrator-spring](lineage-integrator-spring) - implements a rest API for validating that a specific
integration connector is able to run under this service.

* [lineage-integrator-client](lineage-integrator-client) - implements a Java client for the REST API.

This integration service is paired with the [Asset Manager](/egeria-docs/services/omas/asset-manager/overview)
Open Metadata Access Service (OMAS).

--8<-- "snippets/abbr.md"