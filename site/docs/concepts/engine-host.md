<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Engine Host

An *engine host* is an [OMAG Server](/concepts/omag-server) that hosts one or more [governance engines](/concepts/governance-engine). Governance engines define collections of [governance services](/concepts/gpvernance-service) used to automate governance activity in the digital landscape. The governance services within the governance engines may access third party technology to perform their responsibilities or implement their behavior directly.

The engine host uses a [metadata access server](/concepts/metadata-access-server) to retrieve the [definitions of the governance engines](/concepts/governance-engine-definition) and the governance services within them. These definitions are retrieved through the [Governance Server OMAS](/services/omas/governance-server/overview). The Governance Server OMAS also manages the definition of [governance action processes](/concepts/governance-action-process) that choreograph calls to the services in a governance engine in order to implement technical controls in the governance program.

![Engine host in an OMAG Server ecosystem](engine-host.svg)

Multiple engine hosts may run the same governance engine to provide horizontal scalability.

## Governance Services

Governance services execute a single task.  They are short running.

--8<-- "snippets/concepts/governance-service-types.md"


!!! education "Further information"

    - The capabilities of each of the engine services are described in the [engine services](/services/omes).
    - Configuring an engine host is described in the [Administration Guide](/guides/admin/servers/by-server-type/configuring-an-engine-host).

--8<-- "snippets/abbr.md"
