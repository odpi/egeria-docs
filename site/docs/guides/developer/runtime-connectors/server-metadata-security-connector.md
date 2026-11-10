<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Server Metadata Security Connectors

The [server metadata security connector](/concepts/server-metadata-security-connector) provides authorization support for the requests made to a specific [OMAG Server](/concepts/omag-server).  It is part of Egeria's [metadata security](/features/metadata-security/overview) support.  Each OMAG Server has its own instance of the connector, configured in the `serverSecurityConnection` property of its [configuration document](/concepts/configuration-document).  The connection is set with a `POST` request to `/open-metadata/admin-services/servers/{serverName}/security/connection`.

## Interfaces and Base Classes

The interfaces for the metadata security connectors are defined in the [metadata-security-apis :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/common-services/metadata-security/metadata-security-apis){ target=gh } module in the `org.odpi.openmetadata.metadatasecurity` Java package.  A server metadata security connector implements one or more of these interfaces, depending on which authorization decisions it wishes to make:

| Interface | Authorization decisions |
|---|---|
| `OpenMetadataServerSecurity` | Access to the server as a whole: `validateUserForServer`, `validateUserAsServerAdmin`, `validateUserAsServerOperator` and `validateUserAsServerInvestigator`. |
| `OpenMetadataServiceSecurity` | Access to a specific service, and an operation on that service: `validateUserForService` and `validateUserForServiceOperation`. |
| `OpenMetadataElementSecurity` | Access to individual open metadata elements and their anchors, for example `validateUserForElementRead`, `validateUserForElementDetailUpdate`, `validateUserForAnchorMemberAdd`, `selectConnection` and `getReadableZonesForUser`. |
| `OpenMetadataRepositorySecurity` | Access to types and instances through the repository services, for example `validateUserForTypeCreate`, `validateUserForEntityRead`, `validateUserForRelationshipUpdate`, `validateEntityReferenceCopySave`. |
| `OpenMetadataEventsSecurity` | Filtering of the instance events sent to and received from a cohort: `validateInboundEvent` and `validateOutboundEvent`. |
| `OpenMetadataUserSecurity` | Within a server, the verifier uses this interface to set the zones for a user's elements: `getDefaultZonesForUser` and `getPublishZonesForUser`.  The interface also maintains user accounts and security access controls, which the platform uses. |

The server creates the connector from its connection using the `OpenMetadataServerSecurityVerifier` class in the *metadata-security-server* module.  The verifier checks which of the interfaces above the connector implements and only passes it the matching requests.  **A request covered by an interface that the connector does not implement is not checked by the connector, and is allowed.**  Similarly, if no server security connection is configured, the requests are not checked.

The base classes are in the [metadata-security-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/common-services/metadata-security/metadata-security-connectors){ target=gh } module in the `org.odpi.openmetadata.metadatasecurity.connectors` Java package:

* `OpenMetadataSecurityConnector` - the common base class for the platform and server security connectors.  The connector must extend this class, since the verifier calls its `setServerName`, `setLocalServerUserId` and `start` methods when the server starts.  It provides a protected implementation of each validation method that rejects the request, along with protected methods such as `throwUnauthorizedServerAccess`, `throwUnauthorizedServiceAccess`, `throwUnauthorizedInstanceAccess` and `throwUnauthorizedZoneChange` that log a well-defined audit log message and throw the appropriate exception.
* `OpenMetadataServerSecurityConnector` - extends `OpenMetadataSecurityConnector` and implements `AuditLoggingComponent`.  It is the starting point for a server metadata security connector.  Add the interfaces you need to your subclass and implement their methods as `public`, calling the inherited methods from the base class when access is to be denied.
* `OpenMetadataServerSecurityProvider` - the base class for the connector provider.  It extends `OpenConnectorProviderBase`.

## Example Implementation

An example implementation of a server metadata security connector is located in the [metadata-security-connectors :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-implementation/adapters/open-connectors/metadata-security-connectors){ target=gh } module.  The `OpenMetadataAccessSecurityConnector` implements `OpenMetadataPlatformSecurity`, `OpenMetadataRepositorySecurity`, `OpenMetadataServerSecurity`, `OpenMetadataServiceSecurity`, `OpenMetadataElementSecurity` and `OpenMetadataUserSecurity`, so the same connector can be used as the [platform metadata security connector](/guides/developer/runtime-connectors/platform-metadata-security-connector) and as the server metadata security connector for each server.  It uses an embedded [secrets store connector](/concepts/secrets-store-connector) to supply the user accounts and security groups, and uses [governance zones](/concepts/governance-zone) to control the visibility of elements.  Its connector provider, `OpenMetadataAccessSecurityProvider`, extends `OpenMetadataServerSecurityProvider`.

## Writing the Connector Provider

--8<-- "docs/guides/developer/implementing-a-connector-provider.md"

The connector provider for a server metadata security connector extends `OpenMetadataServerSecurityProvider`.

--8<-- "snippets/abbr.md"
