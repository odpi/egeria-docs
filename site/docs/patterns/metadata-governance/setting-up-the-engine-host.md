<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

## Setting up the governance engine

**Recap:** A [governance engine](/concepts/governance-engine) runs in an [Engine Host](/concepts/engine-host) on an [OMAG Server Platform](/concepts/omag-server-platform).

Like all types of [OMAG Servers](/concepts/omag-server), the engine host is configured through Egeria's [Administration Service](/services/admin-services) and the result is a [configuration document](/concepts/configuration-document) for the server.

The configuration document is loaded when the engine host is started.  It contains a list of the governance engines that it is to run.  The configuration document also identifies the [metadata access server](/concepts/metadata-access-server) that engine host is paired with, and where the [governance engine definitions](/concepts/governance-engine-definition) have been loaded.  

For each governance engine name listed in the *configuration document*, the engine host calls its metadata access server to retrieve its governance engine definition.  Based on the contents of the governance engine definition, the engine host starts up the appropriate [Open Metadata Engine Services (OMESs)](/services/omes) that hold the logic to run the different types of [governance services](/concepts/governance-service) defined in the governance engine definition.


![Engine Host Configuring](/patterns/metadata-governance/engine-host-configuring.svg)

The governance engine definition does not need to be loaded directly into the metadata access server paired with the engine host.  It just needs to be in one of the metadata access stores connected to the same [cohort](/features/cohort-operation/overview).  A federated query is used to retrieve the governance engine definition.  This searches in across all the connected metadata access stores.  In fact, different parts of the governance engine definition could be in different metadata access stores.  The team that build the governance services may publish their governance service definitions to their local metadata store.  An architect team responsible for building the governance engine definition may have their own metadata access store that holds the GovernanceEngine entity and the relationships to the GovernanceService entities in the governance services team's metadata access store.  As long as they are all connected by a cohort, they can all operate as if all the metadata was in a single repository.


![Engine Host Remote Configuring](/patterns/metadata-governance/engine-host-remote-configuring.svg)

**Recap:** calls to a governance engine are made by initiating a [Governance Action](/concepts/governance-action).  This can be directly through an API call to the Governance Engine OMAS running in a [Metadata Access Store](/concepts/metadata-access-store), or via a [Governance Action Process](/concepts/governance-action-process).

A governance action is an entity in open metadata.  When it is created in the metadata access store, it sends an event to all connected engine hosts.  If it is for a [governance request type](/concepts/governance-request-type) that one of its governance engine's supports, it claims the governance action and passes the request to its governance engine to run.

The nature of Egeria's open metadata ecosystem means that a governance action that requests to run a governance service in the governance engine can be issued to the paired metadata access store ...

![Local Governance Action](/patterns/metadata-governance/engine-host-local-governance-action.svg)

... or to a connected metadata access store.  Therefore, the governance services are available to any member of the open metadata ecosystem.

![Remote Governance Action](/patterns/metadata-governance/engine-host-remote-governance-action.svg)


!!! education "Further information"
    [Configuring an Engine Host](/guides/admin/servers/configuring-an-engine-host)

--8<-- "snippets/abbr.md"