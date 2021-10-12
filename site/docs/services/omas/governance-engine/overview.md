<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Governance Engine Open Metadata Access Service (OMAS)

The **Governance Engine OMAS** supports the implementation of a [governance program](../governance-program)
by providing the metadata services for running
**[governance engines](/egeria-docs/concepts/governance-engine)**.

A governance engine is a collection of related 
**[governance services](/egeria-docs/concepts/governance-service)** that provide pluggable
governance functions.  The governance services are implemented as 
specialist [connectors](/egeria-docs/frameworks/ocf/overview) that are defined by:

 * [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview) for Open Discovery Services
   that analyse the content of resources in the digital landscape.
 * [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf/overview) of Governance Action Services
   that monitor, assess and maintain metadata.

The governance services run in the [Engine Host OMAG Server](/egeria-docs/concepts/engine-host)
supported by the [Open Metadata Engine Services (OMES)](/egeria-docs/services/omes).
   
The Governance Engine OMAS has the following capabilities:

* Creating the definitions for [governance engines](/egeria-docs/concepts/governance-engine) and
  their [governance services](/egeria-docs/concepts/governance-service).
* Providing the APIs and events that enable the Engine Host OMAG Server to retrieve the definitions
  of the governance engines and services and be notified of any changes to them.
* Creating the definitions for [governance action processes](/egeria-docs/concepts/governance-action-process)
  that control the sequencing of [governance actions](/egeria-docs/concepts/governance-action).
* Providing APIs to create [governance actions](/egeria-docs/concepts/governance-action) explicitly and
  [incident reports](/egeria-docs/concepts/incident-report).
* Initiation and choreography of governance actions based on the template provided by 
  a [governance actions process](/egeria-docs/concepts/governance-action-process).
* Notification of new [governance actions](/egeria-docs/concepts/governance-action) to the 
  Engine Host OMAG Servers that then invoke the appropriate governance services to action them.
* Supporting the metadata requirements for many of the [engine services](/egeria-docs/services/omes).
* Linking the governance actions, governance action processes and governance services
  to the governance definitions supported by the [Governance Program OMAS](/egeria-docs/services/omas/governance-program/overview).
* Providing APIs to query the status of the governance capabilities implemented through the governance engines.



## Documentation

Governance Engine OMAS has a [User Guide](docs/user) that covers the Governance Engine OMAS's APIs and
events.  

The documentation for writing governance services is located:

* [Open Discovery Framework (ODF)](../../frameworks/open-discovery-framework) for Open Discovery Services.
* [Governance Action Framework (GAF)](../../frameworks/governance-action-framework) for the
Governance Action Services: Watchdog Governance Services, Triage Governance Services, Verification Governance Services,
Remediation Governance Services
and Provisioning Governance Services. 


--8<-- "snippets/abbr.md"
