<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Planning Runtime Deployment Guide

Egeria is highly flexible and configurable and so the first piece of advice is to start small and simple and then expand as your experience and understanding of your workloads grows.

## Platforms and servers

Egeria exchanges metadata between many types of tools distributed across different data centers and cloud platforms.

![Egeria integrating different tools distributed over many locations](/introduction/egeria-distributed-operation.svg)

The green clouds represent each of the deployment locations. The different technologies are shown as grey boxes and Egeria itself is shown in blue and orange.

The blue rounded boxes are Egeria's [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform). This platform is the heart of Egeria's implementation.  Typically you would expect to have at least one OMAG Server Platform deployed in each location. However,
when you are experimenting with Egeria, it is often sufficient to start with one OMAG Server Platform and expand the number of platforms as you expand the technologies being integrated.

The OMAG Server Platform is capable of hosting one or more [Open Metadata and Governance (OMAG) Servers](/concepts/omag-server). The OMAG Servers are the orange circles in the illustration above. They manage the connectors to third party technology as well as the frameworks and intelligence that Egeria brings to distributed metadata management.

It is a simple command to move an OMAG Server from one platform instance to another. This means you can start experimenting with a single platform and then add more as your deployment grows. The platform can also run as a node in container technologies such as Docker and Kubernetes.

![OMAG Server deployment choices](/concepts/egeria-operations-server-choices-no-description.svg)

Different types of technology need different types of integration and Egeria has OMAG Servers to match. Each type of OMAG Server is focused on the integration of a specific type of tool, engine or platform:

![Types of OMAG Servers](/concepts/types-of-omag-servers.svg)

The way to understand the diagram is that the arrows should be read as **is a**.  For example, the *repository proxy* **is a** *cohort member* and the *cohort member* **is a** *OMAG Server*. This means that everything documented about a particular type of server is also true for all server types that point to it through the **is a** arrow, all the way down the hierarchy.

Object-oriented software engineers would know of this type of relationship as *behavior inheritance*.

## OMAG Server interactions

![How the OMAG Servers interact](/concepts/omag-server-ecosystem.svg)

- The [cohort members](/concepts/cohort-members) communicate with one another via an [open metadata repository cohort](/services/omrs/cohort). This means that they exchange metadata through a low level, fine-grained API supported by the [Open Metadata Repository Services (OMRS)](/services/omrs).
- The [Open Metadata Access Services (OMAS)](/services/omas) are built on top of the repository services. They live in the [metadata access store](/concepts/metadata-access-store). They offer more course-grained interfaces, specialized for particular types of technology.
- The [governance servers](/concepts/governance-server) are again specialized for particular types of metadata integration or additional governance activity. They connect to a metadata access point / metadata server.
- Finally, the [view servers](/concepts/view-server) support the services for the solution user interfaces. They also connect to a metadata access point / metadata server.

## Suggested incremental deployment approach

The servers' integration can be viewed as a series of nested spheres. The inner sphere involves the cohort members and provides metadata exchange between metadata repositories (and conformance test the integrations). The next level out adds the governance servers to automate the exchange of metadata between the metadata repositories and third party tools, engines and platforms. Finally, adding the view server and user interfaces delivers a governance solution to an organization.

![Spheres of interaction between OMAG Servers](omag-server-integration-spheres.png)

This architecture means that you can incrementally add function to your deployment. Here is a suggested approach:

1. Start with creating an Egeria graph [metadata server](/guides/admin/servers/configuring-a-metadata-access-store). This will provide a metadata repository that can store any type of open metadata.
2. Decide on a name for an [open metadata repository cohort](/services/omrs/cohort) and configure your graph metadata repository to join it.
3. If you want to have other third party metadata repositories that you want to share metadata with, configure [repository proxies](/guides/admin/servers/configuring-a-repository-proxy) for each including registering them to the same cohort as the metadata server.
4. If you then want to add in metadata synchronization with other types of technology beyond metadata repositories, work out which [integration daemons](/concepts/integration-daemon) you need and [configure them to connect to the metadata server](/guides/admin/servers/configuring-an-integration-daemon). Make sure the appropriate [access services](/services/omas) for these integration daemons are enabled in the metadata server.
5. If you want to use the discovery or governance action services then these run in an [engine host server](/concepts/engine-host) and connect to the metadata server via the [Discovery Engine OMAS](/services/omas/discovery-engine) and [Governance Engine OMAS](/services/omas/governance-engine) respectively.
6. Finally, if you want to deploy the user interfaces, make sure you have at least one [view server](/concepts/view-server) for the [presentation server](/concepts/presentation-server) that hosts the UI application.

Working through this exercise gives you an understanding of the Egeria technology that you need for your deployment and how it connects together. The [Solutions Guide](/introduction/patterns) describes different solutions that you can build with Egeria, how they work and the configuration that you will need.

## Building connectors

If you discover that there is a third party technology that is not currently supported by Egeria then you need to [build a connector](/guides/developer/guide) to translate between the APIs and events of that technology and the open metadata APIs and events.

## Identify the scope of the metadata integration

Another useful planning exercise is to identify the community of users and the tools that they use that need to share metadata. This gives you a view of the technology that needs to be integrated. If each community is fairly self-contained with their own tools deployment then you may want to consider deploying an OMAG Server platform for this community and deploying the servers they need onto it. This means they can control  their access to open metadata along with the delivery of open metadata to the rest of the organization.

More importantly, it helps with the definition of the organization's [governance zones](/concepts/governance-zone).

## Deployment checklist

This is a checklist of planning tasks for the deployment of your OMAG Server Platforms and OMAG Servers:

- [ ] [Set up unique certificates](/guides/admin/configuring-the-omag-server-platform/#transport-layer-security-tls) for your OMAG Server Platforms.
- [ ] [Use an encrypted configuration document store](/guides/admin/configuring-the-omag-server-platform/#configuration-store) for your platforms since configuration documents can have certificates and passwords in them.
- [ ] [Implement the metadata security connectors for your organization](/features/metdata-security/overview) to ensure only authorized users access metadata.
- [ ] Choose and [configure the audit log destinations](/guides/admin/servers/configuring-a-metadata-access-store/#configure-the-audit-log) for your OMAG Servers.
- [ ] Ensure you have at least one [Egeria metadata access store](/guides/admin/servers/configuring-a-metadata-access-store/#configure-the-local-repository) in each of your [open metadata repository cohorts](/services/omrs/cohort).
- [ ] [Assign a separate user id for each of your servers](/guides/admin/servers/configuring-a-metadata-access-store/#set-the-servers-user-id-and-optional-password) and ensure they are defined in your user directory and are authorized users according to the metadata security connectors.
- [ ] Consider where you need to have [multiple instances of the same server running to give continuous availability](/guides/admin/guide).
- [ ] Plan your use of the [event bus](/concepts/event-bus): which technology to use (Apache Kafka is the default) and the names of the topics that your OMAG Servers will use.
- [ ] Design the [governance zones](/concepts/governance-zone) that you want to use to control the visibility of assets to different communities of users - or processes.

## More detail to follow...

The text above is a very high level overview of the planning process. More detail will be added to this guide as time permits.

--8<-- "snippets/abbr.md"
