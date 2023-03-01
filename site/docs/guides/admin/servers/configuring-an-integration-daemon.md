<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an [integration daemon](/concepts/integration-daemon)

An *Integration Daemon* is configured by creating a [configuration document](/concepts/configuration-document).  Below is the outline structure of the integration daemon's configuration document.

![Configuration for an integration daemon](integration-daemon-config.svg)

??? info "Configuring the basic properties"
    --8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

??? info "Configuring the audit log"
    --8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

??? info "Configuring the server security connector"
    --8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md"

??? info "Configuring the integration connectors"
    ## Configuring the integration connectors

    The integration connectors that are to run in the integration daemon can be configured one of two ways:

    * Statically in the integration daemon's configuration document using [integration service definitions](#configure-the-integration-services)
    * Dynamically using [integration groups](#configure-dynamic-integration-groups)

    Both approaches can be used in the same integration daemon instance.  However, each integration connector to run should only be configured by

    ??? info "Configuring integration services"
        --8<-- "docs/guides/admin/servers/configuring-the-integration-services.md"
    
    ??? info "Configuring integration groups"
        --8<-- "docs/guides/admin/servers/configuring-the-integration-groups.md"

??? education "Further information"
    - For help in fixing any error you find using the integration daemon, visit the [integration daemon diagnostic guide](/guides/diagnostic/integration-daemon-diagnostic-guide).
    - Link to the [Egeria solutions](/patterns/metadata-integration) to see the integration daemon in action.
    - Link to the [integration daemon services](/services/integration-daemon-services) to understand how the integration daemon is implemented.

--8<-- "snippets/abbr.md"
