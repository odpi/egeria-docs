---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Governance server

A *Governance Server* is a specialized [OMAG Server](/concepts/omag-server). It is designed to host specific governance services that manage metadata in different technologies or perform specific active [governance actions](/concepts/governance-actions).

![Governance server](governance-server.svg)

The governance servers each have a specific subsystem that contains its services. They are also paired with the [Open Metadata Store Services](/services/open-metadata-store) that supports access to open metadata.

The governance servers are themselves controlled by open metadata.  Their configuration points to the root metadata element(s) that they should use.  They are notified of any changes to this metadata.  Therefore, a governance server's behaviour can be dynamically controlled by extending and updating this metadata.  This means that one governance server can modify either its own behaviour or the behaviour of another governance server.

The table below shows the different types of governance servers and the OMASs they are paired with.

| Governance Server                                  | Description                                                              | Supported by subsystem                                               |
|:---------------------------------------------------|:-------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [Integration Daemon](/concepts/integration-daemon) | Manages the capture of metadata through configured integration services. | [Integration Daemon Services](/services/integration-daemon-services) | 
| [Engine Host](/concepts/engine-host)               | Manages governance engines.                                              | [Engine Host Services](/services/engine-host-services)               |


--8<-- "snippets/abbr.md"
