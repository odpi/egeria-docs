<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Digital Resource

A *digital resource* is a [resource](/concepts/resource) that is implemented in software - a database, a file, a topic, an API, a report, a machine learning model, a running application.

The distinction from a physical resource matters because a digital resource can be reached programmatically.  Egeria can not only describe it, it can connect to it: to survey its contents, to check it is still there, to read its schema, or to move data in and out of it.

Two elements are involved, and keeping them apart is central to how Egeria works:

* The **digital resource** is the real thing, sitting in the technology that hosts it.
* The [**asset**](/concepts/asset) is the metadata element that catalogues it.  This is where the ownership, classifications, governance requirements, glossary links and lineage are recorded.

The bridge between the two is the [digital resource connector](/concepts/digital-resource-connector).  Its [connection](/concepts/connection) is attached to the asset, so any process holding the asset can obtain a connector to the resource itself without needing to know what technology it runs on or where the credentials are kept.

Physical resources - buildings, equipment, people - are also catalogued using assets, but they have no connector, because there is nothing to connect to.

???+ info "Additional information"
    * [Asset](/concepts/asset) describes how digital resources are catalogued and governed.
    * [Digital resource connector](/concepts/digital-resource-connector) describes how a running process gains access to the resource behind an asset.
    * [Digital product](/concepts/digital-product) describes how digital resources are packaged for consumption by others.

--8<-- "snippets/abbr.md"
