---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Presentation server

The **presentation server** hosts the JavaScript applications that provide an interactive browser-based
user interface for Egeria.

The JavaScript applications call REST API services running in a [view server](/egeria-docs/concepts/view-server)
to retrieve information and perform operations relating to open metadata.

![A presentation server in the open metadata ecosystem](view-server.svg)

The presentation server supports multi-tenant operation.
Each presentation server tenant is designed to support an organization.
These may be independent organizations or divisions/departments within an organization.  

The tenant is configured with the appropriate view server to use, which in turn routes requests
to its [governance servers](/egeria-docs/concepts/governance-server) and [metadata access servers](/egeria-docs/concepts/metadata-access-server).
Therefore, each tenant sees a different collection of metadata and operates in isolation to the other tenants.

!!! education "Further information"
    The [setup and user guide for the presentation server :material-github:](https://github.com/odpi/egeria-react-ui){ target=gh }
    is held in a separate repository.

--8<-- "snippets/abbr.md"
