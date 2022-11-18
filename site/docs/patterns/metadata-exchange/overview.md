<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Metadata Exchange Patterns

To understand how Egeria's metadata exchange works, it is helpful to look at the patterns used to connect technologies together to exchange information.

The table below shows the four major integration patterns supported by technologies today.

| Pattern | Description |
|---|---|
| Closed Technology | The technology is only accessible through a user interface. |
| Passive Open Technology | The technology offers open APIs that can be called to configure and operate the technology. |
| Active Open Technology | The technology provides active, on-going exchange of information with another technology that covers its operation and specific situations it has detected. |
| Integrated Technology | The technology consumes the open APIs and events supported by another technology. |

## Integrated technology

Egeria does not provide any particular consideration for *closed technology*. However, it does offer a wide range of APIs and event services called [Open Metadata Access Services (OMASs)](/services/omas) to enable a third party technology to become an *integrated technology*, as shown in Figure 1.  The OMASs run in a [metadata access server](/concepts/metadata-access-server).

![Figure 1](integrated-technology-pattern-implementation.svg)
> **Figure 1:** Integrated technology can call the OMASs to consume the open metadata directly

Where a technology does not have direct support for open metadata, Egeria offers hosting of connectors that act as intermediaries to translate API calls and events between the third party technology's APIs and events and Egeria's.

## Passive open technology

For *passive open technology*, Egeria will continuously poll the connector to allow it to repeatedly call the technology's API to determine if anything has changed and then pass any changes to Egeria.  The connector is also able to register a listener for events from Egeria and issue calls to the third party technologies to keep it in synchronization with Egeria.

Figure 2 shows Egeria's [integration daemon](/concepts/integration-daemon) hosting connectors to passive open technologies.  These connectors are called [integration connectors](/concepts/integration connector).  The integration daemon manages the metadata through an Egeria [metadata access server](/concepts/metadata-access-store).

![Figure 2](passive-open-technology-pattern-implementation.svg)
> **Figure 2:** Integration connectors running in an integration daemon polling a third party technology

## Active open technology

The support for *active open technology* is similar to passive open technology except that rather than polling for changes in the third party technology, the connector listens for the third party technology's events and translates them into calls to Egeria.

There are two choices for active open technology.  Any third party technology can be called through an integration connector as above, or, specifically for third party metadata servers, it is possible to integrate them using a [repository connector](/concepts/repository-connector) running in a [repository proxy](/concepts/repository-proxy).  

This is shown in Figure 3.

![Figure 3](active-open-technology-pattern-implementation.svg)
> **Figure 3:** Using either the integration daemon or repository proxy to integrate active open technology into the open metadata ecosystem

The choice of which approach to use depends on the sophistication of the third party metadata server.  Using the repository proxy connects the metadata server into the *[Open Metadata Repository Cohort](/concepts/cohort-member)* (or **Cohort** for short).  It will have access to all metadata exchanged through the cohort and will be called as part of federated queries across the cohort members.  The connector interface is low-level but it does provide the greatest control over the metadata received and shared.  It makes the metadata repository an integrated member of the open metadata ecosystem.

Using the integration daemon connects the third party metadata server on the edge of the open metadata ecosystem.  A two-way exchange is possible, but its metadata must be stored in an Egeria metadata access store that is connected to the appropriate cohorts before its metadata is visible to other members of the cohort.

## Metadata exchange example

Third party technologies are typically integrated in incremental stages. This metadata server exchange example shows an example of this process.  It begins with the *cohort* integration.

A cohort uses a peer-to-peer exchange protocol. Servers that implement the protocol's open metadata APIs and event exchange sequences can become a member of one or more cohorts.  Each member of a cohort can send notifications about updates to its metadata to the other members of the cohort as well as query/update metadata from all of the member repositories.

Since the cohort protocols are open, they can be implemented by any technology.  However this pattern focuses on integrating third party metadata servers that use Egeria to implement the protocol.

### Introducing the repository proxy

Third party metadata servers that do not directly support any of the open metadata APIs and protocols need an adapter to convert their events and APIs into open metadata events and APIs as well as manage the protocol event sequencing.

This first option uses the [Repository Proxy](/concepts/repository-proxy) as the adapter for third party metadata servers. Inside the repository proxy are plug points for two connectors:

- The *OMRS Repository Connector* - translates calls to the OMRS Repository REST API to calls to the third party  metadata server's API.
- The *OMRS Event Mapper* - translates events from the third party metadata server to open metadata events. 
 
The repository proxy represents the third party metadata server in the cohort and calls the connectors as required.  You need one repository proxy for each third party metadata server that you want to be in the solution.

Figure 1 shows the repository proxy in action:

![Figure 1](/concepts/repository-proxy.svg)
> **Figure 1:** showing a repository proxy acting as an adapter for a third party metadata server

You can [create your own implementation of the repository connectors](https://wiki.lfaidata.foundation/display/EG/Implement+an+Open+Metadata+Repository+Connector) for your favorite metadata server. Alternatively Egeria provides repository connector implementations for two third party metadata servers:

  * [IBM Information Governance Catalog (IGC)](https://github.com/odpi/egeria-connector-ibm-information-server)
  * [Apache Atlas](https://github.com/odpi/egeria-connector-hadoop-ecosystem)

We will use these implementations to illustrate how the repository proxies work. We are also assuming that in this example, glossary terms are being maintained in IGC and the organization wants to connect these terms to the Hadoop data sources described in Apache Atlas.

### Working with read-only third party metadata repository connectors

Most third party metadata servers do not support the storing of metadata from other metadata servers.  The sticking point is typically that it can not store information about [where the metadata came from](/features/metadata-provenance/overview) and it can not guarantee that metadata from another metadata server is not updatable through its APIs and user interfaces.  There can also be more subtle issues in the the scale (size) of metadata descriptions or or errors caused by unexpected values they contain.

This is why it is common that the repository connectors for third party metadata servers only support what we call read-only operation.  They can publish information about metadata stored in the third party metadata servers, and support open metadata queries to that repository. However, they do not pass metadata from other metadata servers to the third party metadata server.  

Both IGC's and Atlas's repository connectors are read-only.  Figure 2 shows them connected to their repository proxies and how the operate.

![Figure 2](connecting-read-only-repository.svg)
> **Figure 2:** Read only repository connector operation

Because of their read-only nature, if we just connected them together in a cohort, it would be like two people talking and no-one listening. There would be no value to the solution.

### Creating an enterprise view 

Figure 3 shows a possible extension using an OMAG Server called the [Metadata Access Point](/concepts/metadata-access-point). This provides specialist APIs and events for retrieving and maintaining open metadata.  The metadata access point can be augmented with a [View Server](/concepts/view-server) to support a UI, or provide services to other third party tools.

![Figure 3](enterprise-view.svg)
> **Figure 3:** Using a metadata access point to create an enterprise view

With this approach it is possible to issue queries that return metadata content content from both Atlas and IGC as if they were one metadata repository.   However, there is no support for updates or linking this metadata together.

### Linking metadata from different metadata servers

Figure 4 adds an Egeria [metadata access store](/concepts/metadata-access-store) to the cohort enabling the storage of new metadata.  This means that the APIs of the metadata access point can be used to link glossary terms from IGC to asset definitions from Atlas. These links (called relationships) are stored in the metadata access store.  When queries for metadata are made through the metadata access point, the IGC glossary terms are shown linked to the Atlas assets as if all of the metadata is stored in a single repository.


![Figure 4](enterprise-linking.svg)
> **Figure 4:** Using a metadata access store to provide storage for relationships between IGC and Atlas metadata

### Expanding the scope of metadata being captured

With the metadata access store in place, it is possible to connect an [Integration Daemon](/concepts/integration-daemon) to the metadata access store to provide metadata synchronization to/from additional third party technologies as shown in figure 5.

![Figure 5](enterprise-catalog.svg)
> **Figure 5:** Using a metadata server to provide storage for new metadata

With the above capabilities deployed, there is now a rich source of metadata visible through the metadata access point. Metadata from the IGC and Atlas repositories can be retrieved, combined together and used in new ways without needing to change their implementation.

However, there is no additional metadata being made available through either the IGC or Atlas UIs since they only access metadata stored in their own private metadata repositories. 

### Integrating third party metadata servers through the integration daemon

There is an alternative integration path for third party metadata servers to integrate into the open metadata ecosystem even when they do not meet the requirements to have their repository connectors write metadata into their private metadata repository.

Figure 6 shows IGC connected using this alternative approach.  IGC is now connecting through an integration daemon in a similar way to the other third party technologies shown in Figure 5.  Storing metadata from other repositories is now possible because IGC is no longer providing metadata services to the broader metadata ecosystem as part of the cohort federated queries, removing the requirement to store information about [where the metadata came from](/features/metadata-provenance/overview). The downside is that the metadata in the IGC's xMeta repository is no longer visible to the metadata access point because IGC is no longer a member of the cohort. IGC's metadata will have to be extracted by the integration daemon and stored in the metadata access store for it to be more broadly used.

With this approach, IGC can update its own metadata, and any metadata created through the metadata access point. However, an attempt to update metadata that originated in Atlas would fail when the integration daemon attempted to publish this update into the metadata access store.  (See [metadata provenance](/features/metadata-provenance/overview) to understand why.)

![Figure 6](enterprise-metadata-ecosystem.svg)
> **Figure 6:** Integrating a third party metadata server through the integration daemon

**Note:** this pattern could be repeated to move Apache Atlas to connect through an integration daemon too.

## Summary

In these patterns, you have seen different mechanisms for integrating third party metadata servers together and then build out the metadata ecosystem to enable new use cases.

There are two main integration approaches:

- Integrating using a repository proxy, brings the third party metadata server into the heart of the open metadata ecosystem, enabling queries to its repository to be made by other open metadata services.
- Integrating via an integration daemon has the third party metadata server on the edge of the open metadata ecosystem.  It is not being queried directly, but can engage in two-way metadata exchange through the integration daemon.

!!! info "Further information"

    More about the different types of [Cohort Members](/concepts/cohort-member)including information on how to configure them.  Specifically 

    - [Repository Proxy](/concepts/repository-proxy) to host repository connectors to a third party metadata repository.
    - [Integration Daemon](/concepts/integration-daemon) to host integration connectors to a third party metadata repository.
    - [Metadata Access Point](/concepts/metadata-access-point) to provide new APIs to the federated metadata.
    - [Metadata Access Store](/concepts/metadata-access-store) to provide the store for new metadata.

    There is also specific configuration information for the IBM Information Governance Catalog (IGC) and Apache Atlas setup below:

    - [IBM Information Governance Catalog (IGC)](https://github.com/odpi/egeria-connector-ibm-information-server)
    - [Apache Atlas](https://github.com/odpi/egeria-connector-hadoop-ecosystem)
  
    These are links to more information about cohorts

    - [Operation of the Open Metadata Repository Cohort](/features/cohort-operation/overview)
    - [Querying the members of an Open Metadata Repository Cohort](/guides/operations/overview)

    This link provides guidance if you are interested in writing your own repository connectors:

    - [Writing repository connectors for a third party metadata repository](https://wiki.lfaidata.foundation/display/EG/Implement+an+Open+Metadata+Repository+Connector)

--8<-- "snippets/getting-started.md"

--8<-- "snippets/abbr.md"