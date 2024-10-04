<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


There are two approaches to configuring the Integration Daemon Services. 

* The *Dynamic Integration Groups* section points to lists of integration connectors stored in the open metadata repositories.  The integration daemon monitors these lists to determine which integration connectors to run.  It dynamically updates the connectors it is running based on the values in the open metadata repositories.
* The *Integration Services* section provides details of the integration connectors that are statically configured into the integration daemon.  They are organized by the integration services that each integration connector is using.  These integration connectors will be automatically started with the integration daemon.  Any changes to these integration connectors need to be made in the configuration document and then the integration daemon needs to be restarted for the changes to take effect.

Both approaches can be used in the same integration daemon instance.

??? info "Configuring integration services"
    --8<-- "snippets/admin/configuring-the-integration-services.md"
    
??? info "Configuring integration groups"
    --8<-- "snippets/admin/configuring-the-integration-groups.md"
