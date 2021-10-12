<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


# Governance Engine

A governance engine is responsible for executing requests to a collection of related
[governance services](governance-service.md).

The implementation of a governance engine is
handled by an [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes)
running in an [Engine Host](/egeria-docs/concepts/engine-host) OMAG Server.

There is a specific engine service for each type of governance engine/service pair.

## Governance Engines

Governance engines define a collection of related governance
services.  Governance services are specialized connectors that
implement a single specialized governance activity.
There are six types of governance service:

* [Open Discovery Service](/egeria-docs/concepts/open-discovery-service) for
  analysing the content of an [Asset's](/egeria-docs/concepts/asset) real-world counterpart
  in the digital landscape. (For example, if the asset describes a file, the discovery service
  analyses the data stored in the file).
  
* [Watchdog Governance Service](/egeria-docs/guides/developer/governance-action-services/watchdog-governance-service) for
  monitoring changes to open metadata elements and when certain changes occur
  (such as the creation of a new [Asset](/egeria-docs/concepts/asset))
  the watchdog service requests action from
  other governance services by creating either a
  [Governance Action](/egeria-docs/concepts/governance-action),
  a [Governance Action Process](/egeria-docs/concepts/governance-action-process)
  or an [Incident Report](/egeria-docs/concepts/incident-report).
  
* [Verification Governance Service](/egeria-docs/guides/developer/governance-action-services/verification-governance-service)
  for testing the properties of specific open metadata elements  
  to ensure they are set up correctly or
  do not indicate a situation where governance activity is required.
  The [results](/egeria-docs/concepts/guard) returned from the verification service
  can be used to trigger other governance services as part of a
  [Governance Action Process](/egeria-docs/concepts/governance-action-process).
  
* [Triage Governance Service](/egeria-docs/guides/developer/governance-action-services/triage-governance-service) for making
  decisions on how to handle a specific situation or incident.  Often this involves
  a human decision maker.
  
* [Remediation Governance Service](/egeria-docs/guides/developer/governance-action-services/remediation-governance-service) for
  correcting errors in open metadata or the digital landscape it represents.
   
* [Provisioning Governance Service](/egeria-docs/guides/developer/governance-action-services/provisioning-governance-service) for
  configuring, enabling, provisioning resources in the digital landscape.  Often these provisioning
  services manage the cataloguing of new assets and the lineage between them.

There is a different [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes)
depending on the type of governance service.  The engine services support
the specialist REST APIs and event handling needed for the specific
type of governance service.


| Governance Service | Engine Service |
| :----------------- | :------------- | 
| Open Discovery Service | [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis/overview) |
| Watchdog Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Verification Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Triage Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Remediation Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Provisioning Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |


Each governance engine has a unique name. 
A **governance engine definition** for this unique name
is created using the
[Governance Engine OMAS API](/egeria-docs/services/omas/governance-engine/overview).

Figure 1 shows the structure of a governance engine definition.
The open metadata types for this definition are in
model [0461 - Governance Engines](/egeria-docs/types/4/0461-Governance-Engines)
(see **Governance Engine**, **GovernanceService** linked by the **SupportedGovernanceService** relationship.


![Figure 1](/egeria-docs/concepts/governance-request-type.png)
> **Figure 1:** The structure of a governance engine definition


When a governance engine is called, it is passed a request type
and request parameters.  This is mapped to a call to a [governance service](governance-service.md).



--8<-- "snippets/abbr.md"