---
hide:
- toc
---


<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring different types of OMAG Servers

The configuration document controls that startup of services as an [OMAG Server](/concepts/omag-server) starts up.  When you use the configuration commands from the [Administration Services](/services/admin-services/overview) you are building up the properties in the configuration document.

The configuration document is divided into sections.  Some sections contain properties that are needed by all [types of servers](/concepts/omag-server/#types-of-omag-server) and others are specialized for a particular type of server.  The guides that follow show which services are relevant for each type of server and how to configure them.

![Different types of Server](configuration-document-structure-by-server-type.svg)


* [Metadata Access Store](configuring-a-metadata-access-store.md) - this is a metadata server.  It has a metadata repository and REST APIs to access and maintain the metadata.  It may also send metadata change notifications over an event bus such as Apache Kafka and be a member of an [open metadata repository cohort](/concepts/cohort-member).
* [Metadata Access Point](configuring-a-metadata-access-store.md) - this is like a metadata access store in that it has REST APIs to access and maintain open metadata.  It can also send metadata change notifications over an event bus.  However, it must be a member of an open metadata repository cohort because it has no metadata repository of its own and relies on the other members o the cohort to supply it with metadata. 
* [Repository Proxy](configuring-a-repository-proxy.md) - this type of server hosts a connector that translates open metadata repository requests into calls to a third party metadata server.  It is also able to convert metadata change events from the third party metadata server into open metadata change events.
* [Conformance Test Server](configuring-a-conformance-test-server.md) - this type of server is used by developers of the connectors that run in the repository proxy server. It tests that they are able to safely connect to an open metadata repository cohort.
* [View Server](configuring-a-view-server.md) - this server has specialist REST APIs for UIs and other non-Java environments, such as Python.
* [Integration Daemon](configuring-an-integration-daemon.md) - this server hosts integration connectors that synchronize metadata between third party technologies and the open metadata ecosystem.
* [Engine Host](configuring-an-engine-host.md) - this server hosts governance engines that monitor the open metadata ecosystem and take actions as requested/required.
* [Lineage Warehouse](configuring-a-lineage-warehouse.md) - this server provides optimized access to lineage data.  It has its own repository that it maintains by monitoring the open metadata ecosystem.


This is how these types of servers work together.

![Connected OMAG Servers](/introduction/egeria-solution-components.svg)
