<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Daemon

An *integration daemon* is an [OMAG Server](/concepts/omag-server) that provides metadata exchange services between third party technology and the open metadata ecosystem.

The integration daemon interacts with the open metadata ecosystem through [Open Metadata Access Services (OMASs)](/services/omas) running in a [metadata access point](/concepts/metadata-accces-point) or [metadata access store](/concepts/metadata-access-store).

![Integration daemon sitting between a third party technology and a metadata access point](integration-daemon.svg)

Inside the integration daemon are one or more [Open Metadata Integration Services (OMISs)](/services/omis) that each focus on metadata exchange with a specific type of technology. They are paired with a specific [Open Metadata Access Service (OMAS)](/services/omas) running in the metadata access point / metadata server.


## Integration connectors

The code that manages the specific APIs and formats of the third party technology is encapsulated in a special type of connector called an [integration connector](/concepts/integration-connector).

The specific interface that the integration connector needs to implement is defined by the [integration service](/services/omis). This interface enables the integration service to pass a context object to the connector before it is started. The context enables the connector to register a listener with the associated access service's [Out Topic](/concepts/out-topic), or call its REST API, or to push events to the access service's [In Topic](/concepts/in-topic). By default, the context uses the integration daemon's userId for requests to the access service which means that the metadata created by the integration connector will be credited to this user. If you want to use a different userId for metadata from each connector, the server's userId can be overridden in the connector's configuration.

The integration connectors that run inside the integration daemon can be configured directly into the integration daemon's [configuration document](/concepts/configuration-document), or managed dynamically as open metadata using [integration groups](/concepts/integration-group).

!!! education "Further information"

    - The capabilities of each of the integration services are described in the [integration services](/services/omis).
    - Configuring an integration daemon is described in the [Administration Guide](/guides/admin/servers/by-server-type/configuring-an-integration-daemon).

--8<-- "snippets/abbr.md"
