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

# User Documentation

The Asset Lineage OMAS is designed to publish the events that can be used by external tools and engines to build lineage graphs.
These complex events are constructed using the Enterprise Connector in oredr to fetch the full context of the data assets. 

The link between Glossary Terms and Schema Elements/Glossary Categories is named **vertical lineage**.

The **horizontal lineage** traces the path which data flows starting system of records to the point of usage.

Most of the interaction with the Asset Lineage OMAS will be driven by the external tools used to build lineage.

To understand how to configure:

* [Configuring the Asset Lineage OMAS](egeria-docs/guide/admin/configuring-an-open-lineage-server.md)


--8<-- "snippets/abbr.md"
