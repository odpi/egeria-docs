<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Asset Lineage Open Metadata Access Service (OMAS)

The Asset Lineage OMAS provides services to query the lineage of business terms and data assets.
This access service is used to build **Vertical Lineage** and **Horizontal Lineage** functionality.
On the output topic, it publishes out events that contains full context of data assets and glossary terms involved in lineage.
These events are consumed by the external tools that build the lineage graph in a specific format.

Also, the Asset Lineage OMAS provides an endpoint that publishes the [lineage events](asset-lineage-api/docs/events/lineage-event.md)
associated with the entities involved in lineage.

## Digging Deeper

* [User Documentation](docs/user)
* [Design Documentation](docs/design)

--8<-- "snippets/abbr.md"
