<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Governance Service

A governance service is a specialized [connector](/egeria-docs/concepts/connector) that implements a specific [type of governance action](/egeria-docs/concepts/governance-action).

There are six types of governance services:

* [Open Discovery Service](open-discovery-service.md) for analysing the content of an [Asset's](asset.md) real-world counterpart in the digital landscape. (For example, if the asset describes a file, the discovery service analyses the data stored in the file).
  
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
  decisions on how to handle a specific situation or incident.  Often this involves a human decision maker.
  
* [Remediation Governance Service](/egeria-docs/guides/developer/governance-action-services/remediation-governance-service) for
  correcting errors in open metadata or the digital landscape it represents.
   
* [Provisioning Governance Service](/egeria-docs/guides/developer/governance-action-services/provisioning-governance-service) for
  configuring, enabling, provisioning resources in the digital landscape.  Often these provisioning
  services manage the cataloguing of new assets and the lineage between them.

The [Governance Action Open Metadata Engine Service (OMES)](/egeria-docs/services/omes/governance-action/overview)
supports the execution of the governance action service.
It supports the specialist REST APIs and event handling needed for the specific type of governance action service.


| Governance Service | Engine Service |
| :----------------- | :------------- | 
| Open Discovery Service | [Asset Analysis OMES](/egeria-docs/services/omes/asset-analysis/overview) |
| Watchdog Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Verification Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Triage Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Remediation Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |
| Provisioning Governance Service | [Governance Action OMES](/egeria-docs/services/omes/governance-action/overview) |


## Support for implementing governance services

The interface for the Open Discovery Service is defined by
the [Open Discovery Framework (ODF)](/egeria-docs/frameworks/odf/overview)
and the rest are defined by the [Governance Action Framework (GAF)](/egeria-docs/frameworks/gaf/overview).

These frameworks provide the guidance to developers of new governance services.

## Support for running governance services

Related governance services are configured together as a
[governance engine](governance-engine.md) and they run in
the appropriate [Open Metadata Engine Service (OMES)](/egeria-docs/services/omes).

The [Governance Engine OMAS](/egeria-docs/services/omas/governance-engine/overview) provides:
* The API to create [governance engine definitions](governance-engine.md) for the governance services.
* The API to link governance services together into [governance action processes](governance-action-process.md).
* The metadata support for the [Engine Host Services](/egeria-docs/services/engine-host-services)
  to drive the governance services in an [Engine Host](/egeria-docs/concepts/engine-host)
  OMAG Server.


--8<-- "snippets/abbr.md"