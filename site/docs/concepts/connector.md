---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Connector

A connector is a client library for accessing a [resource](/egeria-docs/conceepts/resource) and its associated [asset](/egeria-docs/concepts/asset) metadata.

Egeria provides a framework called the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf/overview) that defines the generic interfaces for [writing](/egeria-docs/guides/developer), [configuring](/egeria-docs/concepts/connection) and [using connectors](/egeria-docs/guides/developer/using-connectors). A connector has two main APIs:

- An standard API called `getConnectedAssetProperties` for retrieving metadata.  This API is defined by the OCF.
- An API for working with the resource itself.  This interface is specialized for the type of resource and the use it is being put to.

It is configured using a [connection](/egeria-docs/concepts/connection)

## Specialist connectors

Various Egeria services provide specific interfaces for connectors to specific types of resources.  For example, the [Open Metadata Integration Services (OMIS)](/egeria-docs/services/omis) define the interfaces for [integration-connectors](/egeria-docs/concepts/integration-connector) used to [exchange metadata between Egeria and third party technologies](/egeria-docs/patterns/metadata-exchange/overview).

## Virtual connectors

OCF connectors are not limited to representing Assets as they are physically implemented. An OCF connector can represent a simplified logical (virtual) asset, such as a data set, that is designed for the needs of a specific application or tool. This type of connector delegates the requests it receives to one or more physical data resources.  It is called a *virtual connector* and us created using a [*virtual connection*](/egeria-docs/concepts/connection/#virtual-connections).

## Further Information

The [connector catalog](/egeria-docs/connectors) describes the connectors that are pre-built for the Egeria ecosystem.

The [Egeria Developer Guide](/egeria-docs/guides/developer/#what-is-a-connector) describes how to write your own connectors.

--8<-- "snippets/abbr.md"




