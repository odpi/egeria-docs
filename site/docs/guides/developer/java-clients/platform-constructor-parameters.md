<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Each Java client has multiple constructors. The constructors set up the connection to the [OMAG Server Platform](/concepts/omag-server-platform). The parameters are passed in different combinations to control security and logging.

* `serverPlatformURlRoot` - the [platform url root](/concepts/platform-url-root) of the OMAG Server Platform.
* `auditLog` - logging destination for audit log messages.
* `userId` - this is the optional userId that is embedded in all REST calls.  Think of it as the client's user Id rather than the userId of the end user.
* `password` - this is the password that goes with the client's userId.  The userId and password should both be supplied or neither.
* `maxPageSize` - controls the maximum number of results that can be returned on any call.  If this is not set, the max page size is controlled platform-side.
* `restClient` - inside the java client is a [REST API connector](/concepts/rest-client-connector) that manages the marshalling and de-marshalling of the requests into the HTTP protocol used by REST.  Normally this connector is created by the client, but this parameter enables an externally created connector to be used instead.

The constructor may throw `InvalidParameterException` if there is an issue setting up the client-side components based on the supplied parameters. Pick the constructor that matches the parameters you have.  For example, if you call the constructor that supports the client's userId and password and you pass null in these parameters, the exception is thrown.


