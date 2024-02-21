<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# 0045 Servers and Assets

Many data catalogs capture information about data stores, data sets, APIs and topics.  These [digital resources](/concepts/digital-resource) provide access to data and reusable function which is why they are of interest.  These resources run on IT infrastructure.

![UML](0045-Servers-and-Assets.svg)

## ServerAssetUseType enumeration

The *ServerAssetUseType* describes the different types of dependencies that a software capability has on an asset.

* *OWNS* means that the asset is hosted and controlled by the software capability.  For example, a database server OWNS the databases deployed to it.
* *GOVERNS* means the the asset is monitored and action is taken if the asset moves out of certain boundaries or thresholds.  For example, an archiving service GOVERNS a database by removing records that are past a certain date.
* *MAINTAINS* means that although the software capability does not host the asset, it is responsible for maintaining its contents.  For example, an application may store its data in a database running on a remote database server.  The application MAINTAINS the database.
* *USES* means that the software capability is a consumer of the asset.  For example, an analytical service may read the data in a database to feed an algorithm.  The analytical service USES the database.
* *OTHER* means there is another type of dependency between the software capability and the asset.

## ServerAssetUse relationship

[Assets](/types/0/0010-Base-Model/#asset) are managed or consumed by [SoftwareCapabilities](/types/0/0042-Software-Capabilities/#softwarecapability), which is captured by the *ServerAssetUse* relationship.  The properties characterize the relationship:

* *useType* defines how the software capability depends on the asset as defined by the *SoftwareAssetUseType* enumeration.
* *description* provides a description of the use of the asset by the software capability.
* *minimumInstances* defines the minimum number of instances of the asset connected to the software capability.
* *maximumInstances* defines the maximum number of instances of the asset connected to the software capability.

--8<-- "snippets/abbr.md"
