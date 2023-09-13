<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Starting and Stopping an OMAG server

Once a [configuration document](/concepts/configuration-document) has been completed for an [OMAG Server](/concepts/omag-server), it can be started using the following REST call:

```
POST {platformURLRoot}/open-metadata/platform-services/users/{adminUserId}/server-platform/servers/{serverName}/instance
```

and stopped, as follows:

```
DELETE {platformURLRoot}/open-metadata/platform-services/users/{adminUserId}/server-platform/servers/{serverName}/instance
```

The configuration document is not changed by these calls. It is possible to query the running server's configuration using the following REST API:

```
GET {platformURLRoot}/open-metadata/platform-services/users/{adminUserId}/server-platform/servers/{serverName}/instance/configuration
```

If you want to delete the server's configuration document then issue:

```
DELETE {platformURLRoot}/open-metadata/platform-services/users/{adminUserId}/server-platform/servers/{serverName}
```

If the OMAG server is running, this command also unregisters the named server from the cohorts it is connected to.  Only use this command if the server is being permanently removed.

--8<-- "snippets/abbr.md"