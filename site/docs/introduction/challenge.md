<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Building the intelligent enterprise

Every week we hear of new tools, data platforms and opportunities for organizations to embrace advanced digital technologies such as artificial intelligence. Yet despite investment and the focus of smart people, few organizations succeed in making wide and systematic use of their data.

Today's IT is at the heart of the problem. 

Many teams use tools and data platforms that recognize the value of metadata, but this metadata is managed in a siloed, proprietary way that assumes each tool/platform is the sole guardian of this key resource. The result is that knowledge is not shared across teams that use different tool sets, creating artificial barriers to sharing and collaboration.

## What is Egeria? 

**Egeria** is an open source project dedicated to enabling teams to collaborate by making metadata, and related business context, both open and interoperable between tools and platforms, no matter which vendor they come from.

It provides a set of unified capabilities that can be flexibility deployed to support a small team, or incrementally scaled-up to cover the whole enterprise.  It embraces both greenfield and brownfield development; and the more common mixture of the two :).  It scales from a [Raspberry Pi](https://www.raspberrypi.com/) to a multi-tenant enterprise-grade deployment. Its distributed nature makes it cloud-native; locally deployable and distributable across multiple cloud platforms and on-premises.  Egeria puts you in the driving seat.

--8<-- "snippets/getting-started.md"

## Why do we focus on metadata?

The term *metadata* can be misleading.  For those with a database background, it conjures up images of database schemas, tables and columns.  The photographer sees it as the properties captured by their camera to record their camera settings, location and date/time.  

The Egeria community agree with these definitions, but take it much further.  We see it as the description of the structure and linkages of everything.  It has been suggested that we should use the term *meta-information*, but that is more likely to create greater confusion :).

To help, we captured the range of metadata we work with in [Categories of Metadata](/patterns/metadata-manager/categories-of-metadata/).  You will notice that it covers the *who, what, why, where, when* and *how* of an organization's operation, and most importantly, the linkage between.  This is to ensure an organization builds a knowledge base that provides the foundation of its ability to flex to meet the challenges of the future.

With that idea in place, you are ready to understand why we devote our free time to building this technology.

## Open metadata and governance manifesto

Our guiding beliefs, listed below, were formed when the project started in 2019, and beyond the odd phrasing tweak, it has remained the same:

- The maintenance of metadata must be automated to scale to the sheer volumes and variety of data involved in modern business. Similarly, metadata should be used to drive the exploitation of data and create a business-friendly logical interface to the data landscape.
- The availability of metadata management must become ubiquitous across all data platforms, regardless of deployment environment, so that the processing engines on these platforms can rely on its availability and build capability around it.
- Metadata access must become open and remotely accessible so that tools from different vendors can work with metadata located on different platforms. This implies unique identifiers for metadata elements, some level of standardization in the types and formats for metadata and standard interfaces for manipulating metadata.
- Wherever possible, discovery and maintenance of metadata has to be an integral part of all tools that access, change and move information.

The project is [constantly evolving](/release-notes/roadmap/#history). As a community, we have needed to invent new techniques to enable heterogeneous metadata capture and interoperability.  We have taken self-service to a new level and created options for capturing knowledge from subject-matter experts who hate traditional browser-based UIs.

Given this experience, we would add that delivering on this manifesto takes attention to detail (because that is where the devil is), a willingness to embrace new standards and technologies, and the strength of conviction to forge a new path away from the approach of the traditional metadata catalogs.

??? info "Want to join the Egeria Community?"
    We are an open friendly group, interesting to hear from you.  We have developer work in Java, python and UI development.  We are working on enabling Egeria for AI.  In addition, we have roles for writers, advocates and those willing to contribute their knowledge of tricky problems in this space, experience of techniques that worked, and other war stories.  Alternatively, if you just like solving complex problems, please give us some consideration.

    * [Becoming a member of the Egeria community](/guides/community)


--8<-- "docs/introduction/open-metadata-ecosystem.md"

!!! tip "Summary - What is included in Egeria?"
    Egeria provides [Apache 2.0 licensed standards and technology](/introduction/overview) to support the deployment of the open metadata ecosystem.  This is augmented with reference data, connectors and services to provide [out-of-the-box solutions](/egeria-solutions) to common data management and governance problems.


--8<-- "snippets/abbr.md"
