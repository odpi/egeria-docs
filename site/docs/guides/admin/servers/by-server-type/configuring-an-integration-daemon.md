<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an integration daemon

An [*Integration Daemon*](/concepts/integration-daemon) runs [integration connectors](/concepts/integraton-connector) that are exchanging metadata with third party technologies.  For example, an integration connector may catalog files from a file system, or the tables and columns in a database.  Alternatively, it may be gathering lineage information or distributing security information to LDAP.

![Configuration for an integration daemon](/concepts/integration-daemon.svg)

Integration connectors are typically long-running.  The integration daemon needs information about which integration connectors to run and the location of the [Metadata Access Server](/concepts/metadata-access-server) that provides access to the open metadata repositories via the [Open Metadata Access Services (OMASs)](/services/omas).  

--8<-- "snippets/admin/configuring-standard-sections.md"

??? info "Configuring the Integration Daemon Services"
    --8<-- "snippets/admin/configuring-the-integration-daemon-services.md"


??? education "Further information"
    - For help in fixing any error you find using the integration daemon, visit the [integration daemon diagnostic guide](/guides/diagnostic/integration-daemon-diagnostic-guide).
    - Link to the [Egeria solutions](/patterns/metadata-integration) to see the integration daemon in action.
    - Link to the [integration daemon services](/services/integration-daemon-services) to understand how the integration daemon is implemented.  It also describes the integration daemon's REST API calls to restart and refresh integration connectors; and to make temporary changes to an integration connector's configuration.  These changes are only made in-memory and they are lost when the integration connector restarts. 


--8<-- "snippets/abbr.md"
