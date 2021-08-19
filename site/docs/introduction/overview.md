<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Our solution (overview)

![Distrubted operation](egeria-distributed-operation.svg)

Today's organizations have their tools and technologies distributed across multiple data centres and cloud providers (green clouds). Within each location, we can run a platform (blue boxes) that provides integration services tailored to specific types of tools (orange circles).

!!! tip "Peer-to-peer network of metadata"
    The resulting exchange of metadata (blue arrows) creates a peer-to-peer network that spans both locations and vendor tools.

Egeria implements a set of open [metadata types](/egeria-docs/types), [frameworks](/egeria-docs/frameworks/alf), [connectors](/egeria-docs/connectors), [APIs](/egeria-docs/services/omrs), event payloads and interchange protocols to allow all types of tools and metadata repositories to share and exchange metadata. It also provides this platform and pre-built integration services that can run within it to provide a comprehensive toolkit for integrating and distributing metadata between different tools and technologies.

## OMAG Server Platform

Egeria provides the platform (the blue boxes), called the [*Open Metadata and Governance Server Platform* (or *OMAG Server Platform*)](/egeria-docs/concepts/omag-server-platform).

The OMAG Server Platform is a multi-tenant platform that supports horizontal scale-out in Kubernetes and yet is light enough to run as an edge server on a Raspberry Pi. This platform is used to host the actual metadata integration and automation capabilities.

## OMAG server

Within an instance of the OMAG Server *Platform*, one or more [OMAG servers](/egeria-docs/concepts/omag-server) can be configured (the orange circles). These servers implement the wide range of integration and automation capabilities, for example:

- [Open Metadata Repository Services (OMRS)](/egeria-docs/services/omrs) enable the low-level exchange of metadata between platforms.
- [Open Metadata Access Services (OMAS)](/egeria-docs/services/omas) provide higher-level, consumer-centric APIs for interacting with subsets of metadata.

... and many more:

- The [Services](/egeria-docs/services/omrs) reference provides an exhaustive list and deeper explanations of each type of service that can be hosted in the platform.
- The [Connectors](/egeria-docs/connectors) reference provides a list of types of integrations with various tools that are possible, that implement the interfaces defined by the services.
- The [Frameworks](/egeria-docs/frameworks/alf) reference provides details of the frameworks that both the services and adapters can use to simplify their integrations and provide consistency.

## Summary

Combined, the OMAG Server Platforms and Servers running within them provide an enterprise catalog of data and IT resources that are transparently assessed, governed and consumed through many types of tools and technologies. The enterprise catalog is not a physically-centralized one, but a logical one composed of federated metadata from across this peer-to-peer network.

!!! question "Why open source?"
    Delivering this capability as open source is a critical part of the project, since multiple vendors must buy into this ecosystem. They are not going to do this if one organization dominates the technology base. Thus, the open metadata and governance technology must be freely available with an open source governance model that allows a community of organizations and practitioners to develop and evolve the base, and then use it in their offerings and deployments.

--8<-- "snippets/abbr.md"
