<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *context event service* is a component that performs event management around a [context event](/concepts/context-event).

??? info "Runtime for an context event service"
    Context event services are packaged into [Context Event Engines](/concepts/context-event-engine) that run in the [Context Event OMES](/services/omes/contex-event/overview) hosted in an [Engine Host](/concepts/engine-host).  

    The event management interface is implemented by the [Stewardship Action OMAS](/services/omas/stewardship-action/overview) that runs in a [Metadata Access Server](/concepts/metadata-sccess-server).

    An context event service may be triggered via an [Engine Action](/concepts/engine-action) or as part of a [governance action process](/concepts/governance-action-process).

    ![Context Event Service](/connectors/context-event/context-event-service.svg)

