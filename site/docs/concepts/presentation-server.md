---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Presentation server

The **presentation server** is the reverse proxy that protects the open metadata ecosystem from the vagaries of external user traffic and hosts the static JavaScript that provides the [interactive browser-based user interface for Egeria](/user-interfaces/general/overview). It also routes calls to the REST API services running in a [view server](/concepts/view-server) to retrieve information and perform operations relating to open metadata.

![A presentation server in the open metadata ecosystem](view-server.svg)

!!! education "Further information"
    [Setting up the presentation server](/guides/admin/user-interfaces/configuring-the-presentation-server)

--8<-- "snippets/abbr.md"
