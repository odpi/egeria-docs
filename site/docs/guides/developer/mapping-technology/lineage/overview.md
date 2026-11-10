---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Lineage Modeling

The [Open Integration Framework (OIF)](/frameworks/oif/overview) supports the following services for its hosted [integration connectors](/concepts/integration-connector):

- Registering a listener for [OpenLineage events](/features/lineage-management/overview/#the-open-lineage-standard) received either:
    - through the integration daemon's `publish-open-lineage-event` REST API (also available through the [Runtime Manager API](/services/omvs/runtime-manager/overview)), or
    - published by other integration connectors running in the same integration daemon.

- Registering a listener for events from the open metadata ecosystem.  These events notify the integration connector of any changes to open metadata elements that are visible to it.  They can be used to drive the publishing of lineage information to third party technologies.

- Publishing OpenLineage run, job and dataset events to other integration connectors running in the same integration daemon that have registered a listener for these events.

- Cataloguing lineage information from a third party technology.  Specifically this includes process structure, ports, schemas and the data assets they are working with.  The lineage relationships themselves are maintained through the `LineageClient` returned by the integration context's `getLineageClient()` method.

The details of these calls are described in [the integration context](/guides/developer/integration-connectors/integration-context/#open-lineage).

The open metadata types used to represent lineage are described in [0750 Data Passing](/types/7/0750-Data-Passing), [0760 Business Lineage](/types/7/0760-Business-Lineage) and [0770 Lineage Mapping](/types/7/0770-Lineage-Mapping).


!!! education "Further information"
    - [Lineage Management](/features/lineage-management/overview) describes how to set up Egeria to capture, steward, preserve and use lineage.
    - [Building integration connectors](/guides/developer/integration-connectors) describes how to write your own integration connectors.


--8<-- "snippets/abbr.md"