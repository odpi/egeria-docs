<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

### Start and stop servers

Servers are started and stopped through the [Platform Services](/services/platform-services/overview).  Return to the `Egeria-platform-services.http` collection, change the `@server` variable at the top of the file to `test-metadata-store`, and run these requests:

* `Start server - using stored configuration` - starts `test-metadata-store` using the configuration document created in the previous step.  The response lists the services that have been started, and the platform's run window shows the server's audit log messages as it starts.
* `Get all active servers` - now includes `test-metadata-store`.
* `Query the status of a specific server` - shows when the server started.
* `Shutdown server` - stops the server.  Its configuration document is kept, so it can be started again.
