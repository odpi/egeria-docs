<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Each Java client has two constructors.  The constructors set up the connection to the [OMAG Server Platform](/concepts/omag-server-platform) and control how the client authenticates.  The parameters are:

* `platformName` or `serverName` - the descriptive name of the OMAG Server Platform (for platform-level clients such as `PlatformServicesClient`) or the name of the OMAG Server the client works with.  Some platform-level clients, such as `OMAGServerPlatformConfigurationClient`, take neither.
* `platformRootURL` - the [platform url root](/concepts/platform-url-root) of the OMAG Server Platform.
* `secretStoreProvider`, `secretStoreLocation` and `secretStoreCollection` - the class name of the connector provider for a [secrets store connector](/concepts/secrets-store-connector), the location of the secrets store and the name of the collection of secrets within it.  The client uses these secrets to obtain a bearer token from the platform.  The alternative constructor takes a map of already initialized secrets store connectors (`secretsStoreConnectorMap`) in place of these three parameters.
* `delegatingUserId` - the optional user identifier of the external user that the client is making the request on behalf of.
* `auditLog` - logging destination for audit log messages.

The constructor may throw `InvalidParameterException` if there is an issue setting up the client-side components based on the supplied parameters.

