<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Starting and Stopping an OMAG Server

Once a [configuration document](/concepts/configuration-document) has been completed for an [OMAG Server](/concepts/omag-server), the server can be started and stopped in several ways:

* the *Servers* tab of [Egeria Operations](/guides/operations/overview#egeria-operations-in-the-portal);
* the `hey_egeria_ops tell servers` commands;
* pyegeria's `RuntimeManager`;
* the REST APIs.

[Operating servers](/guides/operations/overview#operating-servers) in the Operations Guide compares them.  This page describes the platform services REST calls.  They go straight to one [OMAG Server Platform](/concepts/omag-server-platform) and need no view server, so they suit start-up scripts.

Each call needs a bearer token from the platform's token service (`POST {{baseURL}}/api/token`).  See [REST APIs](/guides/operations/overview#rest-apis) in the Operations Guide.  The token's user must be authorized to operate servers on the platform.

## Starting a server

This call starts a server using the configuration document stored on the platform:

```
###
# @name activateWithStoredConfig
POST {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance
Authorization: Bearer {{token}}
```

A server can also be started with a configuration document supplied in the request body.  This document is not saved to the configuration document store:

```
###
# @name activateWithSuppliedConfig
POST {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance/configuration
Authorization: Bearer {{token}}
Content-Type: application/json

{ ...configuration document... }
```

Servers can also be started automatically when the platform starts - see [Auto-starting servers](/guides/admin/configuring-the-omag-server-platform#auto-starting-servers).

## Checking the server

The configuration document is not changed by starting or stopping a server.  These calls return the configuration that the running server was started with, and its status:

```
###
# @name getActiveConfiguration
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance/configuration
Authorization: Bearer {{token}}

###
# @name getActiveServerStatus
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance/status
Authorization: Bearer {{token}}
```

More status calls are listed in [Diagnostic APIs](/guides/diagnostic/diagnostic-apis#is-a-server-running-and-how-is-it-configured).

## Stopping a server

This call stops a server temporarily.  It stays registered with its [cohorts](/concepts/cohort-member), so it rejoins them cleanly when it is restarted:

```
###
# @name shutdownServer
DELETE {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance
Authorization: Bearer {{token}}
```

This call stops a server and also unregisters it from every cohort it belongs to:

```
###
# @name shutdownAndUnregisterServer
DELETE {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}
Authorization: Bearer {{token}}
```

Only use it if the server is being removed permanently.  It does not delete the server's configuration document.

The same calls without a server name act on every server running on the platform: `DELETE .../server-platform/servers/instance` and `DELETE .../server-platform/servers`.  `DELETE .../server-platform/instance` stops every server and then shuts down the platform itself.

## Removing a server's configuration

The configuration document belongs to the [administration services](/guides/admin), not the platform services.  To clear it once the server has been stopped and unregistered:

```
###
# @name clearConfiguration
DELETE {{baseURL}}/open-metadata/admin-services/servers/{{serverName}}/configuration
Authorization: Bearer {{token}}
```

--8<-- "snippets/abbr.md"
