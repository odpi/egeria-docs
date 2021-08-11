---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Connector type

The **connector type** is a set of properties that defines the 
supported capabilities and the identity of the [connector provider](connector-provider.md)
for a [connector](connector.md), and is part of the
[Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf). Its properties are:

| Property | Description |
|---|---|
| `guid` | GUID for the connector type. |
| `url` | External link address for the connector type properties in the metadata repository. |
| `qualifiedName` | The official (unique) name for the connector type. This is often defined by the IT systems management organization and should be used (when available) on audit logs and error messages. |
| `displayName` | A consumable name for the connector type. Often a shortened form of the qualifiedName for use on user interfaces and messages.  The displayName should be only be used for audit logs and error messages if the qualifiedName is not set. |
| `description` | A full description of the connector type covering details of the assets it connects to along with usage and versioning information. |
| `connectorProviderClassName` | The [connector provider](connector-provider.md) is the factory for a particular type of [connector](connector.md). This property defines the class name for the connector provider that the [connector broker](connector-broker.md) should use to request new connector instances.
| `recognizedAdditionalProperties` | These are the [connection](connection.md)'s additional properties recognized by the connector implementation. |
| `recognizedConfigurationProperties` | These are the [connection](connection.md)'s configuration properties recognized by the connector implementation. |
| `recognizedSecuredProperties` | These are the [connection](connection.md)'s secured properties recognized by the connector implementation. |
| `additionalProperties` | Any additional properties that the [connector provider](connector-provider.md) needs to know in order to create [connector](connector.md) instances. |

The connector type is linked to the
[connection](connection.md) objects that request this type of connector.

![Connection Structure](connection.png)

!!! education "Further information"
    - The open metadata type for a connector type is defined in [model 0201](/egeria-docs/types/2/0201-connectors-and-connections).
    - The [open connector archives :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-resources/open-metadata-archives/open-connector-archives){ target=gh }
      module provides an open metadata archive that contains connector types for connectors supported by Egeria.

--8<-- "snippets/abbr.md"
