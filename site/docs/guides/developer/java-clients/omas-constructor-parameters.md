<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


Each Java client has multiple constructors.  The constructors set up the connection to the [metadata access server](/concepts/metadata-access-server). The parameters are passed in different combinations to control security and logging.

* `serverName` - the name of the metadata access server.
* `serverPlatformURLRoot` - the [platform url root](/concepts/platform-url-root) of the OMAG Server Platform where the metadata access server is running.
* `auditLog` - logging destination for audit log messages.
* `userId` - this is the optional userId that is embedded in all REST calls.  Think of it as the client's user Id rather than the userId of the end user.
* `password` - this is the password that goes with the client's userId.  The userId and password should both be supplied or neither.
* `maxPageSize` - controls the maximum number of results that can be returned on any call.  If this is not set, the max page size is controlled server-side.
* `restClient` - inside the java client is a [REST API connector](/concepts/rest-client-connector) that manages the marshalling and de-marshalling of the requests into the HTTP protocol used by REST.  Normally this connector is created by the client, but this parameter enables an externally created connector to be used instead.
* `callerId` - found on clients that support registering a listener for [out topic events](/concepts/out-topic).  It is used to maintain a pointer to the next event to receive that is specific to the caller Id.  It should be unique for each independent receiver.  Alternatively, if you have a number of clients that are sharing the processing load for the out topic, all of there callerIds should be the same, and the events will be distributed amongst them.

The constructor may throw `InvalidParameterException` if there is an issue setting up the client-side components based on the supplied parameters. Pick the constructor that matches the parameters you have.  For example, if you call the constructor that supports the client's userId and password and you pass null in these parameters, the exception is thrown.


