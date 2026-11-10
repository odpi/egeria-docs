<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### Create test servers

Servers are configured through the [Administration Services](/services/admin-services/overview).  The `Egeria-admin-services-server-configuration.http` collection in the `{install directory}/assembly/opt/http-client-collections` directory has a request for each configuration call.

Open `Egeria-admin-services-server-configuration.http` in IntelliJ and change the `@server` variable at the top of the file to `test-metadata-store`.  Then run these requests in order by clicking on the green triangle next to each one:

1. `Token (RequestBody)` - obtains the bearer token used by the other requests.
2. `Set default audit log destination` - sends the server's audit log messages to the console.
3. `Enable the in-memory repository` - gives the server a local repository that is cleared each time the server stops, which is ideal for testing.
4. `Enable all of the access services with no topics` - adds the access services that provide the metadata APIs, without needing an event bus such as Apache Kafka.

This creates the configuration document for a new [Metadata Access Store](/concepts/metadata-access-store) called `test-metadata-store`.  Run `Get server configuration document` to see the configuration document that has been built up.

The [administration guide](/guides/admin/servers/by-server-type/configuring-a-metadata-access-store) describes the other options for configuring a metadata access store.
