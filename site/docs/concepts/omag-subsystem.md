<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Open Metadata and Governance (OMAG) subsystems

A subsystem is a collection of components
within a software server that supports one or more related services.
Subsystems can be organized in a hierarchy where course-grained subsystems can be
decomposed into more fine-grained subsystems.

The [OMAG server](omag-server.md) is a flexible software server whose subsystems
can be activated (or not) through the presence (or absence) of the subsystem's configuration
properties in the OMAG server's [configuration document](configuration-document.md).

The potential subsystems within an [OMAG server](omag-server.md) are as follows:

- [Open Metadata Repository Services (OMRS)](../../../../services/omrs) for supporting access
  to metadata stored in metadata repositories and the exchange of metadata between repositories
  via an [open metadata repository cohort](../../../../services/omrs/cohort).
  The repository services are further divided into [OMRS subsystems](../../../../services/omrs/#omrs-subsystems) that
  can be activated independently.
- [Integration daemon services](../../../governance-servers/integration-daemon-services) for running integration
  connectors that exchange metadata with third party technologies.
- [Connected Asset Services](../../../common-services/ocf-metadata-management) for supporting the ConnectedAsset
  interface of a connector.  
- Dynamically registered services provide specialist APIs for particular technologies and user roles.
  Each of these services runs in their own subsystem independent of the other registered services. 
  The implementation may come from Egeria or a third party. The links are to Egeria provided dynamic services.
    - [Open Metadata Access Services (OMAS)](../../../../services/omas.md) for supporting domain-specific services
      for metadata access and governance. Access services run in the [metadata server](metadata-server.md) and
      [metadata access point](metadata-access-point.md) server.
    - [Open Metadata Engine Services (OMES)](../../../../services/engine.md) for supporting specialized governance
      engines that drive governance activity in the open metadata ecosystem.
      The engine services run in the [engine host](engine-host.md) server.
    - [Open Metadata Integration Services (OMIS)](../../../../services/integration.md) for supporting
      specific types of
      [integration connectors](../../../governance-servers/integration-daemon-services/docs/integration-connector.md).
      The integration services run in the [integration daemon](integration-daemon.md) server.
    - [Open Metadata View Services (OMVS)](../../../view-services) for supporting REST
      services for a User Interface (UI). The view services run in a
      [view server](view-server.md).

--8<-- "snippets/abbr.md"
