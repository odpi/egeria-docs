<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

An *archive service* is a [specialized connector](/concepts/connector) that maintains an [open metadata archive](/concepts/open-metadata-archive). It is hosted in the [Archive Manager OMES](/services/omes/archive-manager/overview) which is, in turn, running in an [engine host](/concepts/engine-host) OMAG server.

![Archive Services](/connectors/archive/archive-service.svg)
> **Figure 1:** Archive Services

An archive service can:

- Register a listener with the Enterprise OMAS Topic to receive notifications from any of the repositories connected via [Open Metadata Repository Cohorts](/concepts/cohort-member).
- Issue requests to find and retrieve metadata instances from any of the repositories connected via Open Metadata Repository Cohorts.
- Incrementally build and store an open metadata archive.

--8<-- "snippets/abbr.md"
