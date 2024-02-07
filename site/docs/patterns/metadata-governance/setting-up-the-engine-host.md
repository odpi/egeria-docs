<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

## Setting up the governance engine

**Recap:** A [governance engine](/concepts/governance-engine) runs in an [Engine Host](/concepts/engine-host) on an [OMAG Server Platform](/concepts/omag-server-platform).

Like all types of [OMAG Servers](/concepts/omag-server), the Engine Host is configured through Egeria's [Administration Service](/services/admin-services/overview) and the result is a [configuration document](/concepts/configuration-document) for the server.

The configuration document is loaded when the Engine Host is started.  It contains a list of the governance engines that it are to run in the Engine Host.  The configuration document also identifies the [metadata access server](/concepts/metadata-access-server) that Engine Host is paired with, and where the name [Governance Engine Definitions](/concepts/governance-engine-definition) will be retrieved from.  

For each governance engine name listed in the *configuration document*, the Engine Host calls its metadata access server to retrieve its Governance Engine Definition.  Based on the contents of the Governance Engine Definition, the Engine Host starts up the appropriate [Open Metadata Engine Services (OMESs)](/services/omes) that hold the logic to run the different types of [Governance Services](/concepts/governance-service) defined in the Governance Engine Definition.


![Engine Host Configuring](/patterns/metadata-governance/engine-host-configuring.svg)

The *Governance Engine Definition* does not need to be loaded directly into the metadata access server paired with the Engine Host.  It just needs to be in one of the Metadata Access Stores connected to the same [cohort](/features/cohort-operation/overview).  A federated query is used to retrieve the Governance Engine Definition.  This searches in across all the connected Metadata Access Stores.  In fact, different parts of the Governance Engine Definition could be in different Metadata Access Stores.  The team that build the Governance Services may publish their Governance Service Definitions to their local metadata store. An architect team responsible for building the Governance Engine Definition may have their own Metadata Access Store that holds the GovernanceEngine entity and the relationships to the GovernanceService entities in the Governance Services team's Metadata Access Store.  As long as they are all connected by a cohort, they can all operate as if the whole Governance Engine Definition was in a single Metadata Access Store.


![Engine Host Remote Configuring](/patterns/metadata-governance/engine-host-remote-configuring.svg)

**Recap:** calls to a governance engine are made by initiating an [Engine Action](/concepts/engine-action).  This can be directly through an API call to the [Governance Engine OMAS](/services/omas/governance-engine/overview) running in a [Metadata Access Store](/concepts/metadata-access-store), or via a [Governance Action Process](/concepts/governance-action-process).

A Governance Action is an entity in open metadata.  When it is created in the Metadata Access Store, it sends an event to all connected Engine Hosts.  If it is for a [governance request type](/concepts/governance-request-type) that one of its governance engine's supports, it claims the Governance Action and passes the request to its governance engine to run.

The nature of Egeria's open metadata ecosystem means that a Governance Action can be created in the paired Metadata Access Store ...

![Local Governance Action](/patterns/metadata-governance/engine-host-local-governance-action.svg)

... or in a connected Metadata Access Store.  Therefore, the Governance Services are available to any member of the open metadata ecosystem.  They do not need to know where the Engine Hosts are deployed.

![Remote Governance Action](/patterns/metadata-governance/engine-host-remote-governance-action.svg)


!!! education "Further information"
    [Configuring an Engine Host](/guides/admin/servers/by-server-type/configuring-an-engine-host)

