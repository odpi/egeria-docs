<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *event action service* is a component that performs event management around a [context event](/concept/context-event).

??? info "Runtime for an event action service"
    Event action services are packaged into [Event Action Engines](/concepts/event-action-engine) that run in the [Event Action OMES](/services/omes/event-action/overview) hosted in an [Engine Host](/concepts/engine-host).  

    The event management interface is implemented by the [Stewardship Action OMAS](/services/omas/stewardship-action/overview) that runs in a [Metadata Access Server](/concepts/metadata-sccess-server).

    An event action service may be triggered via an [Engine Action](/concepts/engine-action) or as part of a [governance action process](/concepts/governance-action-process).

    ![Event Action Service](/connectors/event-action/event-action-service.svg)

