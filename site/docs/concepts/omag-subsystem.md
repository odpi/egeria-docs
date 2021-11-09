---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata and Governance (OMAG) Subsystems

A subsystem is a collection of components within a software server that supports one or more related services. Subsystems can be organized in a hierarchy where course-grained subsystems can be decomposed into more fine-grained subsystems.

The [OMAG Server](omag-server.md) is a flexible software server whose subsystems can be activated (or not) through the presence (or absence) of the subsystem's configuration properties in the OMAG Server's [configuration document](/egeria-docs/concepts/configuration-document).

The potential subsystems within an [OMAG Server](omag-server.md) are as follows:

- [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) for supporting access to metadata stored in metadata repositories and the exchange of metadata between repositories via an [open metadata repository cohort](/egeria-docs/concepts/cohort-member). The repository services are further divided into [OMRS subsystems](/egeria-docs/services/omrs/#omrs-subsystems) that can be activated independently.
- [Integration daemon services](/egeria-docs/services/integration-daemon-services) for running integration connectors that exchange metadata with third party technologies.
- [Connected Asset Services](/egeria-docs/services/ocf-metadata-management) for supporting the `ConnectedAsset` interface of a connector.  
- Dynamically registered services provide specialist APIs for particular technologies and user roles. Each of these services runs in their own subsystem independent of the other registered services. The implementation may come from Egeria or a third party. The links are to Egeria provided dynamic services.
    - [Open Metadata Access Services (OMASs)](/egeria-docs/services/omas) for supporting domain-specific services for metadata access and governance. Access services run in the [metadata access server](metadata-access-server.md).
    - [Open Metadata Engine Services (OMESs)](/egeria-docs/services/omes) for supporting specialized governance engines that drive governance activity in the open metadata ecosystem. The engine services run in the [engine host](engine-host.md) server.
    - [Open Metadata Integration Services (OMISs)](/egeria-docs/services/omis) for supporting specific types of [integration connectors](integration-connector.md). The integration services run in the [integration daemon](integration-daemon.md) server.
    - [Open Metadata View Services (OMVSs)](/egeria-docs/services/omvs) for supporting REST services for a User Interface (UI). The view services run in a [view server](view-server.md).

--8<-- "snippets/abbr.md"
