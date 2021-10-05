<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Daemon

An *integration daemon* is an [OMAG Server](omag-server.md) that provides metadata exchange services between third party technology and the open metadata ecosystem.

The integration daemon interacts with the open metadata ecosystem through [Open Metadata Access Services (OMAS)](/egeria-docs/services/omas) running in a [metadata access point](/egeria-docs/concepts/metadata-accces-point) or [metadata server](/egeria-docs/concepts/metadata-server).

![Integration daemon sitting between a third party technology and a metadata access point](integration-daemon.png)

Inside the integration daemon are one or more [Open Metadata Integration Services (OMIS)](/egeria-docs/services/omis) that each focus on metadata exchange with a specific type of technology. They are paired with a specific [Open Metadata Access Service (OMAS)](/egeria-docs/services/omas) running in the metadata access point / metadata server.

To understand how an integration daemon works, it is necessary to look in a bit more detail at how technologies can be connected together to exchange metadata.

## Integration mechanisms

### Closed technology

*Closed technology* describes technology that is only accessible through a user interface.

!!! danger "Not considered"
    Egeria does not provide any particular consideration for these technologies, given they provide no
    integration mechanisms.

### Active and passive open technology

*Passive open technology* offers open APIs that can be called to configure and operate the technology, while *active open technology* provides active, ongoing exchange of information with another technology that covers its operation and specific situations it has detected.

The integration daemon provides support for both **active** and **passive** open technologies:

![Integrating both passive and active open technology into the open metadata ecosystem](open-technology-pattern-implementations.png)

For passive open technology, an integration service will continuously poll the connector to allow it to repeatedly call the technology's API to determine if anything has changed and then pass any changes to the metadata access point / metadata server.

The active open technology support is similar except that rather than polling for changes in the third party technology, the connector listens on the third party technology's event topic and translate the events it receives and passes the information onto the access service via calls to the integration service.

The integration service also listens for events from its access service's [Out Topic](/egeria-docs/services/omas/client-server/#out-topic). If there is new metadata that is of interest to the third party technology, the access service publishes the information and it is picked up by the integration service and passed on to the connector. The connector may then push metadata to the third party technology.

Thus, the integration services of the integration daemon enable metadata to flow both in and out of the open metadata ecosystem.

### Integrated technology

*Integrated technology* describes technology that integrates with open metadata APIs to events "out of the box." Where an Egeria conformance test exists, this technology has a conformance mark.

An integrated technology is able to interact directly with a [metadata access point](/egeria-docs/concepts/metadata-access-point) or [metadata server](/egeria-docs/concepts/metadata-server) by calling the open metadata services or consuming them directly:

![Integrated technology can call the open metadata services or consume the open metadata services directly](integrated-technology-pattern-implementation.png)

## Integration connectors

The code that manages the specific APIs and formats of the third party technology is encapsulated in a special type of connector called an [integration connector](/egeria-docs/connectors/integration-connector).

The specific interface that the integration connector needs to implement is defined by the [integration service](/egeria-docs/services/omis). This interface enables the integration service to pass a context object to the connector before it is started. The context enables the connector to register a listener with the associated access service's [Out Topic](/egeria-docs/services/omas/client-server/#out-topic), or call its REST API, or to push events to the access service's [In Topic](/egeria-docs/services/omas/client-server/#in-topic). By default, the context uses the integration daemon's userId for requests to the access service which means that the metadata created by the integration connector will be credited to this user. If you want to use a different userId for metadata from each connector, the server's userId can be overridden in the connector's configuration.

--8<-- "snippets/abbr.md"
