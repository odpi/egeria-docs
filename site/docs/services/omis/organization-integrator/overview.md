---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Organization Integrator Open Metadata Integration Service (OMIS)

The Organization Integrator OMIS supports the loading of teams and
other organization structural information into the open metadata ecosystem.


## Module Implementation

The modules are as follows:

* [organization-integrator-api](organization-integrator-api) - defines the interface for an integration
connector that is supported by the Organization Integrator OMIS. This includes the implementation
of the context that wraps the Community Profile OMAS's clients.

* [organization-integrator-server](organization-integrator-server) - implements the context manager for
the Organization Integrator OMIS.

* [organization-integrator-spring](organization-integrator-spring) - implements a rest API for validating that a specific
integration connector is able to run under this service.

* [organization-integrator-client](organization-integrator-client) - implements a Java client for the REST API.

This integration service is paired with the [Community Profile](/services/omas/community-profile/overview)
Open Metadata Access Service (OMAS).

--8<-- "snippets/abbr.md"