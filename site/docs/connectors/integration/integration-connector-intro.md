<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->


The [integration connectors](/concepts/integration-connector) support the exchange of metadata with third party technologies.  This exchange may be inbound and/or outbound; synchronous, polling or event-driven. 

An integration connector runs in an [Open Metadata Integration Service (OMIS)](/services/omis) which is in turn hosted in an [Integration Daemon](/concepts/integration-daemon) server.  Each integration service provides a specialist interface designed to aid the integration with a specific type of technology.  The integration connector implementation is therefore dependent on a specific OMIS.

![Deployed Integration Connector](/connectors/integration/integration-connectors.svg)
> An integration connector is shown deployed in an integration service running in an integration daemon.  The connector is linking to a third party technology and also calling the open metadata APIs of Egeria to manage the exchange of metadata.


