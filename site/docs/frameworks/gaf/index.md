<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Governance Action Framework (GAF)
  
The *governance action framework (GAF)* provides the interfaces and base implementations for components (called [governance action services](#governance-action-services)) that take action to:

- detect, report and eventually correct a situation that is harmful to the data or the organization in some way or 
- to enhance the metadata to improve its use.

The governance action framework can be used for three purposes:

- Provide the complete implementation and orchestration of a governance process.
- Provide coordination between processes run by specialized governance systems. For example, coordinating a DevOps pipeline with a data movement and quality process and security incident management.
- Provide contextual metadata plus an audit trail of actions managed by an external governance process.

## Governance action services

A *governance action service* is a specialized [connector](/egeria-docs/concepts/connector) that performs monitoring of metadata changes, validation of metadata, triage of issues, assessment and/or remediation activities on request.

There are five types of governance action services, each of which supports a specialist governance activity:

- [Watchdog governance service](watchdog-governance-service.md) - monitors for specific types of instances, or changes to open metadata and initiates appropriate follow-on governance actions either by creating a [governance action](governance-action.md), a [governance action process](governance-action-process.md) or an [incident report](incident-report.md). For example, a watchdog service may detect a new [asset](/egeria-docs/concepts/asset) and kick off an asset on-boarding governance action process.
- [Verification governance service](verification-governance-service.md) - performs a series of tests around a specific metadata instance and depending on what it finds, it publishes [guards](guard.md) to report on any errors it finds. For example, it may check that a new asset has an owner, is set up with zones and includes a connection and a schema.
- [Triage governance service](triage-governance-service.md) - evaluates a reported situation and makes a choice on the right action to proceed. This may involve a human decision maker, and therefore may initiate an external workflow or create a [ToDo](/egeria-docs/types/1/0137-actions/#todo) for a specific person.
- [Remediation governance service](remediation-governance-service.md) - performs a change to the open metadata (or its counterpart in the real-world). Examples of remediation governance action services are duplicate linking and consolidation.
- [Provisioning governance service](provisioning-governance-service.md) - performs an action that makes a new resource available along with the appropriate open metadata. Typically, the provisioning service is an external service. It may also create lineage metadata to describe the work of the provisioning engine.

These are often used in conjunction with the [open discovery services](/egeria-docs/frameworks/odf/discovery-service) from the [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf). Collectively they are called the *governance services* and they can be linked together into [governance action processes](governance-action-process.md).

Some governance action services invoke functions in external engines that are working with data and related assets. The GAF offers embeddable functions and APIs to simplify the implementation of governance action services, and their integration into the broader digital landscape, whilst being resilient and with good performance.

## Implementing governance action services

Governance action services are [open connectors](/egeria-docs/frameworks/ocf) that support the interfaces defined by the GAF. They may produce [audit log records](/egeria-docs/frameworks/alf) and exceptions, and they may make changes to metadata through the [Open Metadata Access Services (OMAS)](/egeria-docs/services/omas).

A governance action service is passed a *context* as it is started. This provides access to the request type and associated parameters (name-value pairs) used to invoke the governance action service, along with a client to access open metadata through the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine).

![Structure of the governance context](governance-context.png)

This context is then specialized for each type of governance action service. Details of the specific context for each service can be found in the links above to the various governance action service types.

## Configuring governance action services

A collection of related governance action services are grouped into governance action engines for deployment. The governance action engine maps *governance action request types* to the governance action service that should be invoked along with.

![Structure of a governance engine definition](governance-action-engine-definitions.png)

These definitions are created through the [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine) and are stored in the open metadata repositories.

Governance action engines are hosted in an [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes) running on one or more [engine hosts](/egeria-docs/concepts/engine-host). The Open Metadata Types used to define the governance action engines are located in [0461 governance action engines](/egeria-docs/types/4/0461-governance-engines).

## Running governance action services

Governance action engines are hosted by the [Governance Action OMES](/egeria-docs/services/omes/governance-action).

The engine services run in dedicated OMAG server called the [*engine host*](/egeria-docs/concepts/engine-host). You can find [instructions for configuring the engine services in the engine host](/egeria-docs/guides/admin/configuring-an-engine-host/#configure-the-engine-host-services) in the administration guide.

The [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine) provides the services for:

- setting up the definitions of a governance action engine.
- configuring [governance action processes](governance-action-process.md).
- managing [governance actions](governance-action.md) and [incident reports](incident-report.md).

--8<-- "snippets/abbr.md"
