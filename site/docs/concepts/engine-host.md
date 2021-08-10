<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Governance engine hosting servers

An **engine host** is an [OMAG server](/egeria/concepts/omag-server) that hosts one or more governance engines.
Governance engines provide collections of services used to support the governance of the digital
landscape and the metadata that describes it.
The services within the governance engines may access third party technology to
perform their responsibilities or implement their behavior directly.

The engine host uses a [metadata server](/egeria/concepts/metadata-server) to store the definitions of the governance
engines and the services within them.  These definitions are retrieved through the
[Governance Engine OMAS](/egeria/services/omas/governance-engine).
The Governance Engine OMAS also manages the definition of 
[governance action processes](../../../access-services/governance-engine/docs/concepts/governance-action-process.md)
that choreograph calls to the services in a governance engine in order to implement
technical controls in the governance program.

![Engine host in an OMAG server ecosystem](engine-host.png)

Typically, an engine host is deployed close to where the artifacts/resources/data are stored
because it can generate a lot of network traffic when its services are running.

The metadata interfaces needed by the governance engines are provided by the
[Open Metadata Engine Services (OMES)](/egeria/services/omes) (or engine services for short).
The engine services also run in the engine host OMAG server.

The engine services are:

* **Asset Analysis** - For running [Open Discovery Services](../../../frameworks/open-discovery-framework/docs/discovery-service.md) 
                       that analyse the content of an asset's real world counterpart in the digital landscape, generates annotations
                       in an open discovery analysis report that is attached to the asset in the open metadata repositories.

* **Governance Action** - For running [Governance Action Services](../../../frameworks/governance-action-framework/docs/governance-action-service.md).
                        There are five types of governance action services:                
    * **Watchdog Governance Service** - Monitors changes in the open metadata repositories and initiates governance activity as a result.
        This is typically by creating a 
        [Governance Action](../../../frameworks/governance-action-framework/docs/governance-action.md), a 
        [Governance Action Process](../../../frameworks/governance-action-framework/docs/governance-action-process.md) or an
        [Incident Report](../../../frameworks/governance-action-framework/docs/incident-report.md).
        One example of a watchdog governance service is to monitor for the addition of a new asset.
  
    * **Verification Governance Service** - Runs checks on the metadata properties to ensure they are complete and correct.
   One example of a verification governance service is detection for metadata
   elements with the same qualified name, or an asset without an owner.
                      
    * **Triage Governance Service** - Runs triage tasks to determine how to manage an incident or situation.
    For example, it could initiate an external workflow, assign a task to a steward, wait for manual
    decision or initiate a remediation request.
                   
    * **Remediation Governance Service** - Makes updates to the open metadata or the digital landscape.
    An example of a remediation governance service could be to link or consolidate metadata elements with the same
   qualified name. Another remediation governance service may move assets between zones when a particular date is reached.
   
    * **Provisioning Governance Service** - Invokes a provisioning service whenever a provisioning request is made.  Typically the
   provisioning service is an external service.  It may also create lineage metadata to
   describe the work of the provisioning engine.                

An engine service is paired with a specific [access service](../../../access-services) running in either a 
[metadata access point](metadata-access-point.md) or a [metadata server](metadata-server.md).
The specific access services are:

* [Discovery Engine OMAS](../../../access-services/discovery-engine) for Asset Analysis OMES.
* [Governance Engine OMAS](../../../access-services/governance-engine) for Governance Engine OMES.

The name and URL root of the server where the access service is running
is needed to configure an engine service.

The metadata server used by the engine services does not need to be the same metadata server
as the one used by the engine host server.
This enables the management of metadata about the assets to be maintained close to the assets,
and the definitions of the governance engines, services and processes to be maintained
close to the governance team.  This separation is shown in Figure 2.


![Figure 2](distributed-engine-services-config.png#pagewidth)
> Figure 2: Distribution of metadata managed by the engine host



The engine host services have an REST API to query the status of the governance engines
running in the engine services.  The engine services also have a REST API to query specific details of their
governance engines.  All of these REST APIs may be called by a view server as part of the
support for a user interface.

## Further information

More information on the governance engines are available below:

* The capabilities of each of the engine
services are described in the [engine services](../../../engine-services) module.

* Details of how to create the definitions of the governance engines and governance services are 
  described in the [Governance Engine OMAS](../../../access-services/governance-engine) documentation.

--8<-- "snippets/abbr.md"
