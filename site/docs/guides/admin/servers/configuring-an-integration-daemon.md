<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an integration daemon

An [*Integration Daemon*](/concepts/integration-daemon) runs [integration connectors](/concepts/integraton-connector) that are exchanging metadata with third party technologies.  For example, an integration connector may catalog files from a file system, or the tables and columns in a database.  Alternatively, it may be gathering lineage information or distributing security information to LDAP.

Integration connectors are typically long-running.  Their implementation calls one of the [Open Metadata Integration Services (OMISs)](/services/omis) to maintain open metadata and access other useful integration utilities.  The integration daemon needs information about which integration connectors to run along with details of the services they need to operate successfully.  The information needed to bootstrap the integration daemon is configured by creating a [configuration document](/concepts/configuration-document) which is passed to the integration daemon when it starts up.

## Overview

Below is the outline structure of the integration daemon's configuration document.

![Configuration for an integration daemon](integration-daemon-config.svg)

The *Local Server URL Root* shown in light grey can be optionally configured to provide the [platformURLRoot](/concepts/platform-url-root) for the default [OMAG Server Platform](/concepts/omag-server-platform) where this integration daemon is to be deployed to.  It is only used if the deploy command does not include the destination platformURLRoot.

The properties shown in blue are standard properties for an [OMAG Server](/concepts/omag-server).

The properties shown in green are specific to integration daemons and they identify which integration connectors to run.  There are two approaches.   An integration daemon can be configured with either approach or both: 

* The *Integration Services* section provides details of the integration connectors that are statically configured into the integration daemon.  They are organized by the integration services that each integration connector is using.  These integration connectors will be automatically started with the integration daemon.  Any changes to these integration connectors need to be made in the configuration document and then the integration daemon needs to be restarted for the changes to take effect.
* The *Dynamic Integration Groups* section points to lists of integration connectors defines using open metadata elements store in the open metadata repositories.  The integration daemon monitors these lists to determine which integration connectors to run.  It dynamically updates the connectors it is running based on the values in the open metadata elements.


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
    - Link to the [integration daemon services](/services/integration-daemon-services) to understand how the integration daemon is implemented.  It also describes the integration daemon's REST API calls to restart and refresh integration connectors; and to make temporary changes to an integration connector's configuration.  These changes are only made in-memory and they are lost when the integration connector restarts. 


--8<-- "snippets/abbr.md"
