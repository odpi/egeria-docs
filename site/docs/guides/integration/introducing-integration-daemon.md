<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Inside the Integration Daemon

**Recap:** The *Integration Daemon* is an Egeria [OMAG Server](/concepts/omag-server) that sits at the edge of the open metadata ecosystem, synchronizing metadata with third party tools.  It is connected to a [Metadata Access Server](/concepts/metadata-access-server) that provides the APIs and events to interact with the open metadata ecosystem.

![Integration Daemon](/services/integration-daemon-in-action.svg)

The integration can be:

* **Triggered by an event from a third party technology** that indicates that metadata needs to be updated the open metadata ecosystem to make it consistent with the third party technology's configuration.

* **Triggered at regular intervals** so that the consistency of the open metadata ecosystem with the third party technology can be verified and, where necessary, corrected.

* **Triggered by a change in the open metadata ecosystem** indicating that changes need to be replicated to the third party technology.

Running in the integration daemon are [integration connectors](/concepts/integration-connector) that each support the API of a specific third party technology.  The integration daemon starts and stops the integration connectors and provides them with access to the open metadata ecosystem APIs.  Its action is controlled by configuration, so you can set it up to exchange metadata with a wide range of third party technologies.

An integration connector is specialized for a particular technology.  The integration daemon provides specialized services based of different types of technology, in order to simplify the work of the integration connector.  These specialized services are called the [Open Metadata Integration Services (OMISs)](/services/omis).  Each integration connector is paired with an OMIS and, the OMIS is paired with a relevant [Open Metadata Access Service (OMAS)](/services/omas) running in the [Metadata Access Server](/concepts/metadata-access-server).

![Inside Integration Daemon](/services/integration-daemon-internals.svg)


--8<-- "snippets/abbr.md"