<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Introducing the Integration Daemon

The *Integration Daemon* is an Egeria server that sits at the edge of the open metadata ecosystem, synchronizing metadata with third party tools.

The integration can be:

* **Triggered by an event from a third party technology** that indicates that metadata needs to be updated the open metadata ecosystem to make it consistent with the third party technology's configuration.

* **Triggered at regular intervals** so that the consistency of the open metadata ecosystem with the third party technology can be verified and, where necessary, corrected.

* **Triggered by a change n the open metadata ecosystem** indicating that changes need to be replicated to the third party technology.

Inside the integration daemon are [integration connectors](/concepts/integration-connector) that each support the API of a specific third party technology.  The integration daemon starts and stops the integration connectors and provides them with access to the open metadata ecosystem APIs.  Its action is controlled by configuration, so you can set it up to exchange metadata with a wide range of third party technologies.

![Integration Daemon](/services/integration-daemon-in-action.svg)


!!! education "Further information"
    - [Integrated Cataloguing](/features/integrated-cataloguing/overview)
    - [Integration Daemon](/concepts/integration-daemon)


--8<-- "snippets/abbr.md"