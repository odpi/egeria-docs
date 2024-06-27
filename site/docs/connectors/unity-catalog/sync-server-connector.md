<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# OSS Unity Catalog (UC) Server Synchronizing Connector

The *Unity Catalog OSS Synchronization Connector* exchanges metadata between the open-source version of Unity Catalog and the Open Metadata Ecosystem.

Its work is scoped by the metadata collection that represents Unity Catalog.  This is identified by the *metadataSourceQualifiedName* property in the connector's configuration.
It performs two passes each time it is called.