<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

## Configuring the integration daemon

The [integration daemon's configuration](/guides/admin/servers/by-server-type/configuring-an-integration-daemon) contains a list of integration connectors that the integration daemon is to run.  The configuration for each integration connector describes the connector implementation to use, how often to call it and the open metadata services that it needs.

The [connector catalog](/connectors/#integration-connectors) lists the integration connectors that are part of Egeria.  They are organized by technology type.  In addition, you can write your own integration connectors for third party technologies currently not supported in the catalog.  The catalog entry for each integration connector provides the information needed to configure it in an integration daemon.  This includes details of the integration service it uses, where the implementation is located and the configuration options it supports.  See the [Data Files Monitor Integration Connector](/connectors/integration/data-files-monitor-integration-connector) entry as an example. 

??? education "Further information"
    - [Configuring the integration daemon](/guides/admin/servers/by-server-type/configuring-an-integration-daemon)
    - [Writing integration connectors](/guides/developer/integration-connectors/overview)

