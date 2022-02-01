---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Cohort Member

A *Cohort Member* is an [OMAG Server](/concepts/omag-server) that is capable of joining an *open metadata repository cohort*.

The open metadata repository cohort (or cohort for short) is a group of OMAG servers that are exchanging metadata using a peer-to-peer replication protocol and federated queries.  This is shown in Figure 1.

![Figure 1](cohort-member.svg)
> **Figure 1:** OMAG Servers connected via a cohort

The cohort is self-configuring.  At the heart of it is between one and four shared
[cohort topics](/concepts/cohort-events/#cohort-topics).  Each member publishes a registration request on the appropriate topic when they want to join.  This is picked up by the existing members who add this new server to their registry of members known as the [cohort registry](/concepts/cohort-registry)
and re-send their registration through the same topic to allow the new member to build up its own registry.

When an OMAG server permanently leaves the cohort, it sends an unregistration request. This enables the other members to remove the parting member from their registries.

The purpose of the cohort registry in each member is to configure its federated query capability. The registration information includes the URL Root and server name of the member.  The federation capability in each OMAG server allows it to issue metadata create, update, delete and search requests to each and every member of the cohort.  This is the primary mechanism for accessing metadata.

In addition, any change to metadata made by a member is replicated to the other members of the cohort through the relevant cohort topic.  This gives the other members to opportunity to maintain cached copies of the metadata for performance / availability reasons.  A member may also request that metadata is "refreshed" across the cohort.
The originator of the requested metadata then sends the latest version of this metadata to
the rest of the cohort through the cohort topic.  This mechanism is useful
to seed the cache in a new member of the cohort and is invoked as a result of a
federated query issued from the new member. (A federated query occurs whenever an
[OMAS](/services/omas) make a request for metadata.)

The exchange of metadata is using the [Open Metadata Repository Services (OMRS)](/services/omrs)
interfaces which gives fine-grained metadata notifications and updates.
(See the [OMRS metamodel](/guides/developer/repository-connectors/metamodel/overview) for more details).
The server's [metadata security connector](/features/metadata-security/overview)
provides fine-grained control on which metadata is send, received and/or stored by the server.
This level of control is necessary for metadata repositories that are managing
specific collections of valuable objects such as 
[Assets](/concepts/asset).

Figure 2 shows the different types of cohort members.
Follow the links below the diagram to find out more about each one's purpose.

![Figure 2](cohort-member-types.svg)
> **Figure 2:** Different types of OMAG Servers that can be connected via a cohort

- [Metadata Access Server](/concepts/metadata-access-server)
   - [Metadata Access Store](/concepts/metadata-access-store)
   - [Metadata Access Point](/concepts/metadata-access-point)
- [Repository Proxy](/concepts/repository-proxy)
- [Conformance Test Server](/concepts/conformance-test-server)

## More information

There is more detailed information about the operation of an open
metadata repository cohort in 
[Cohort Operation](/features/cohort-operation/overview).

The administration hands on lab called "**Understanding Cohort Configuration Lab**"
provides an opportunities to query the cohort registries of cohort members as they
exchange metadata for Coco Pharmaceuticals.
Instructions for running the labs [can be found here](/education/open-metadata-labs/overview).

--8<-- "snippets/abbr.md"