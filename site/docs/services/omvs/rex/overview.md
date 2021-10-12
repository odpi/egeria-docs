---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Repository Explorer View Service

The Repository Explorer (Rex) View Service is an Integration View Service that supports Repository Explorer UI operations
that retrieve metadata type and instance information from metadata repositories.

The purpose of this interface is to enable a technical user (such as an Enterprise Architect) to 
retrieve metadata instances from repositories and explore the connectivity of those instances to other metadata objects. 
The interface enables retrieval and search and the construction of a visualization of a graph of connected objects. 

This view service calls a remote server using the [repository services client](/egeria-docs/services/omrs).

---8<-- "snippets/abbr.md"