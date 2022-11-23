<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Metadata Exchange

People are not good at repetitive admin tasks, particularly if these tasks are not the primary focus of their work. Therefore, your metadata catalog(s) are more complete and accurate when automation supports these mundane tasks.  The automation needs to:

* monitor for triggers that indicate that metadata needs to be updated,
* drive the necessary changes to metadata and then
* make those changes visible to downstream processing.

The [*Integration Daemon*](/concepts/integration-daemon) is an Egeria [server](/concepts/omag-server) that sits at the edge of the open metadata ecosystem, synchronizing metadata with third party tools.  It is connected to a [Metadata Access Server](/concepts/metadata-access-server) that provides the APIs and events to interact with the open metadata ecosystem.

![Integration Daemon](/services/integration-daemon-in-action.svg)

The integration can be:

* **Triggered by an event from a third party technology** that indicates that metadata needs to be updated in the open metadata ecosystem to make it consistent with the third party technology's configuration.

* **Triggered at regular intervals** so that the consistency of the open metadata ecosystem with the third party technology can be verified and, where necessary, corrected.

* **Triggered by a change in the open metadata ecosystem** indicating that changes need to be replicated to the third party technology.


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

Figure 2 shows Egeria's [Integration Daemon](/concepts/integration-daemon) hosting connectors to passive open technologies.  These connectors are called [integration connectors](/concepts/integration connector).  The integration daemon manages the metadata through an Egeria [Metadata Access Server](/concepts/metadata-access-store).

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


## Next steps?

--8<-- "snippets/getting-started.md"

??? education "Review the planning guide?"
    The [Planning Guide](/guides/planning) describes how to plan the work to introduce Egeria into your organization.

??? education "Review the integration guide?"
    The [Integration Guide](/guides/integration) describes how to integrate third party technology into the open metadata ecosystem.

??? education "Review the administration guide?"
    The [Administration Guide](/guides/admin) describes how to configure OMAG Server Platforms and their servers.

??? education "Learn more about metadata governance?"
    The [Metadata Governance Dojo](/education/egeria-dojo/metadata-concernance/overview) is a self-guided course building on the concepts introduced here.


--8<-- "snippets/abbr.md"