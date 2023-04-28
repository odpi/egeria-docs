<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

An *repository governance service* is a [specialized connector](/concepts/connector) that performs governance on open metadata repository  such as maintaining an [open metadata archive](/concepts/open-metadata-archive). It is hosted in the [Repository Governance OMES](/services/omes/repository-governance/overview) which is, in turn, running in an [engine host](/concepts/engine-host) OMAG server.

![Repository Governance Services](/connectors/repository-governance/repository-governance-service.svg)
> **Figure 1:** Repository Governance Services

A repository governance service can:

- Register a listener with the Enterprise OMAS Topic to receive notifications from any of the repositories connected via [Open Metadata Repository Cohorts](/concepts/cohort-member).
- Issue requests to find and retrieve metadata instances from any of the repositories connected via Open Metadata Repository Cohorts.
- Incrementally build and store an open metadata archive.

