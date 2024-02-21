<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring a Lineage Warehouse

The [Lineage Warehouse](/concepts/lineage-warehouse) captures lineage from the open metadata ecosystem and maintains an optimized historical record of lineage for reporting.  It is designed for use in regulated industries where lineage must be captured and retained.

The configuration for a lineage warehouse requires knowledge of the [metadata access server](/concepts/metadata-access-server) that supplied open metadata via the [Asset Lineage OMAS](/services/omas/asset-lineage/overview) and the location of its store.

![Configuration for a lineage warehouse](/concepts/lineage-warehouse.svg)

--8<-- "snippets/admin/configuring-standard-sections.md"

??? info "Configuring the Lineage Warehouse Services"
    --8<-- "snippets/admin/configuring-the-lineage-warehouse-services.md"
  
 ### Start up information
 
 !!! info "Runtime consideration"
     It is important to consider that, to operate, Lineage Warehouse depends on the availability of its Metadata Access Server (with Asset Lineage OMAS) being up and running. This is the case because Lineage Warehouse discovers the event bus connectivity and the topic address from asset lineage during start-up. Consequently, it will always wait and retry until this condition is met, and it starts up successfully.
    
--8<-- "snippets/abbr.md"
