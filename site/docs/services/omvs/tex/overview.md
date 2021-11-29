---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"
  
# Type Explorer Open Metadata View Services (OMVS)

Develop an explorer interface to support the Type Explorer UI, which enables a technical user (such as an Enterprise Architect) to 
retrieve open metadata type information from repositories and explore the attributes of each type and the possible combinations of 
entities, relationships and classifications. The interface retrieves the type information and display it both visually, as graphs
of entity type inheritance and the possible relationships in which each entity type can participate; the display also includes a 
detailed textual description of the attributes and possible relationships and classification for each entity type. The textual
display also shows the attributes and entity types for each relationship.

This OMVS calls a remote server using the [repository services client](/egeria-docs/services/omrs).

---8<-- "snippets/abbr.md"
