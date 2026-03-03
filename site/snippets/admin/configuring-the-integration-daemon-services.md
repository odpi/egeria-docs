<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


The *Integration Daemon Services* are configured with a list of [integration group](/concepts/integration-group) names.  Each integration group name identifies an integration group stored in the open metadata repositories.  Linked from the integration group are definitions of the integration connectors that are part of the group.  When an integration daemon is configured with the name of the integration group, it reads the definition of the integration group from the open metadata repositories and runs the connectors that are part of the group.

The integration daemon constantly monitors the integration groups, adjusting the running integration connectors as the definitions change.  The integration daemon also monitors the running integration connectors themselves, restarting them if they fail or if their configuration changes.  This ensures that the integration daemon is always running the latest and most up-to-date integration connectors.
    
??? info "Configuring integration groups"
    --8<-- "snippets/admin/configuring-the-integration-groups.md"
