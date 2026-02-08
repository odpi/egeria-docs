<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Integration Daemon

An *integration daemon* is an [OMAG Server](/concepts/omag-server) that provides metadata exchange services between third party technology and the open metadata ecosystem.

The integration daemon interacts with the open metadata ecosystem through [Open Metadata Access Services (OMASs)](/services/omas) running in a [metadata access server](/concepts/metadata-accces-server).

Typically, an integration daemon is deployed close to  the artifacts/resources/data it is synchronizing because it can generate a lot of network traffic when its services are running. Multiple integration daemons may connect to the same metadata access server to provide horizontal scalability.

![Integration daemon sitting between a third party technology and a metadata access point](integration-daemon.svg)

Inside the integration daemon are the [Open Metadata Integration Services (OMISs)](/services/omis) that each focus on metadata exchange for a specific type of technology (databases, files, other catalogs etc). An OMIS is paired with a specific [Open Metadata Access Service (OMAS)](/services/omas) running in the metadata access server.


## Integration connectors

The code that manages the specific APIs and formats of the third party technology is encapsulated in a special type of connector called an [integration connector](/concepts/integration-connector).

Integration connectors are long-running.  The integration daemon periodically calls each running integration connector in turn.  This is called *refreshing the connector*.  The time period between refresh calls to an integration connector is controlled by the integration connector's configuration.  During the refresh call, an integration connector checks for changes to both the open metadata and the third party metadata they are responsible for.  They make updates to correct any discrepancies.  Typically, metadata changes are flowing in one direction, but two-way synchronization is also possible.

An integration connector may also register to receive event notification changes from open metadata and/or the third party technology it is working with.  This allows the metadata synchronization to occur immediately without waiting for the refresh.  In this style, the refresh period is much longer and the refresh processing is used to check that no metadata changes have been missed.

The specific interface that the integration connector needs to implement is defined by the [open integration framework](/frameworks/oif/overview) it is using. This interface enables the integration daemon to pass a context object to the connector before it is started. The context enables the connector to register a listener with the associated metadata access server's [Out Topic](/concepts/out-topic) to listen for open metadata change notifications, or to call its REST API. By default, the context uses the integration daemon's userId for requests to the metadata access server, which means that the metadata created by the integration connector will be credited to this user. If you want to use a different userId for metadata from each connector, the server's userId can be overridden in the [connector's configuration](/types/4/0464-Dynamic-Integration-Groups/).

The integration connectors that run inside the integration daemon are managed dynamically as open metadata using [integration groups](/concepts/integration-group).  Integration connectors are able to modify the integration groups dynamically, and also initiate [governance actions](/concepts/governance-action), create [to dos](/concepts/to-do) and raise [incident reports](/concepts/incident-report).  

Each time the integration connector is called (refreshed) by the integration daemon, it produces an [integration report](/concpets/integraiton-report) listing the metadata elements it has created, updated or deleted.  The integration report is stored in the open metadata repository.  It is possible to disable this function in the integration connector's configuration.

!!! education "Further information"

    - Configuring an integration daemon is described in the [Administration Guide](/guides/admin/servers/by-server-type/configuring-an-integration-daemon).
    - The integration daemon is implemented by the [Integration Daemon Services](/services/integration-daemon-services).

--8<-- "snippets/abbr.md"
