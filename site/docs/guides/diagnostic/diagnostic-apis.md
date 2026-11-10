<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Diagnostic APIs

These REST calls return the state of a platform, its servers and their connectors.  They are what the portal's Egeria Operations, the `hey_egeria` monitors and pyegeria's `RuntimeManager` use, so they give the same answers - but calling them directly is useful when a user interface is itself part of the problem, or when you want the raw detail.

All calls need a bearer token from the platform's token service (`POST {{baseURL}}/api/token`); see [REST APIs](/guides/operations/overview#rest-apis) in the Operations Guide.

## Is the platform running?

The platform services go straight to one platform and do not need a view server, so they work even when other servers are down.

```
###
# @name platformOrigin
# Returns a string naming the platform and its version - the simplest "are you there?" check.
GET {{baseURL}}/open-metadata/platform-services/server-platform/origin
Authorization: Bearer {{token}}

###
# @name platformStartTime
GET {{baseURL}}/open-metadata/platform-services/server-platform/start-time
Authorization: Bearer {{token}}

###
# @name knownServers
# Servers that have run on this platform since it started.
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers
Authorization: Bearer {{token}}

###
# @name activeServers
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/active
Authorization: Bearer {{token}}
```

For example, the quickstart platform returns:

```
Egeria OMAG Server Platform (version 6.3-SNAPSHOT)
```

```json
{
  "class" : "ServerListResponse",
  "relatedHTTPCode" : 200,
  "serverList" : ["qs-engine-host", "qs-integration-daemon", "qs-metadata-store", "qs-view-server", "qs-nanny-daemon"]
}
```

## Is a server running, and how is it configured?

```
###
# @name serverStatus
# Type, start time and whether the server is active.
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/status
Authorization: Bearer {{token}}

###
# @name serverServices
# The services running in an active server.
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/services
Authorization: Bearer {{token}}

###
# @name runningConfiguration
# The configuration document the running server was started with.
GET {{baseURL}}/open-metadata/platform-services/server-platform/servers/{{serverName}}/instance/configuration
Authorization: Bearer {{token}}
```

```json
{
  "class" : "ServerStatusResponse",
  "relatedHTTPCode" : 200,
  "serverName" : "qs-nanny-daemon",
  "serverType" : "Integration Daemon",
  "serverStartTime" : "2026-11-10T10:38:21.598+00:00",
  "active" : true
}
```

The running configuration can differ from the stored configuration document if the document has been changed since the server started - comparing the two is a quick way to spot a change that needs a restart.

The [Runtime Manager](/services/omvs/runtime-manager/overview) gives a fuller report through the view server, combining the server's status, services, history and connectors: `GET {{baseURL}}/servers/{{viewServer}}/api/open-metadata/runtime-manager/omag-servers/{{serverGUID}}/instance/report` (pyegeria: `RuntimeManager.get_server_report()`).

## Connectors and governance engines

```
###
# @name integrationDaemonStatus
# Every integration group and connector, with status, last refresh time and refresh interval.
GET {{baseURL}}/servers/{{integrationDaemon}}/open-metadata/integration-daemon/status
Authorization: Bearer {{token}}

###
# @name integrationGroupSummary
GET {{baseURL}}/servers/{{integrationDaemon}}/open-metadata/integration-daemon/integration-groups/{{integrationGroupName}}/summary
Authorization: Bearer {{token}}

###
# @name governanceEngineSummaries
# Every governance engine in the engine host, with its status and request types.
GET {{baseURL}}/servers/{{engineHost}}/open-metadata/engine-host/governance-engines/summary
Authorization: Bearer {{token}}
```

The meaning of each connector status, and what to do about it, is in [Connector status](/guides/operations/overview#connector-status).

## The audit log

```
###
# @name auditLogReport
# Which components are logging, the severities they have logged and how many of each.
GET {{baseURL}}/servers/{{serverName}}/open-metadata/repository-services/audit-log/report
Authorization: Bearer {{token}}

###
# @name auditLogSeverities
GET {{baseURL}}/servers/{{serverName}}/open-metadata/repository-services/audit-log/severity-definitions
Authorization: Bearer {{token}}
```

The report is a tree of components, each with a `severityCount` (keyed by [severity code](/concepts/audit-log/#audit-log-records)) and its child components.  A component with a count against severity 5 (`Error`) or 6 (`Exception`) is the place to start reading the audit log records themselves.

## Cohorts

These calls show the [cohorts](/concepts/cohort-member) a server belongs to and the members it knows about.

```
###
# @name cohortDescriptions
GET {{baseURL}}/servers/{{serverName}}/open-metadata/repository-services/metadata-highway/cohort-descriptions
Authorization: Bearer {{token}}

###
# @name localRegistration
GET {{baseURL}}/servers/{{serverName}}/open-metadata/repository-services/metadata-highway/cohorts/{{cohortName}}/local-registration
Authorization: Bearer {{token}}

###
# @name remoteMembers
GET {{baseURL}}/servers/{{serverName}}/open-metadata/repository-services/metadata-highway/cohorts/{{cohortName}}/remote-members
Authorization: Bearer {{token}}
```

If a server's list of remote members is missing a server that should be there, see [Cohort errors](/guides/diagnostic/examples-of-cohort-errors).

## The repository

The repository services can be called directly on a metadata access store to check what its repository holds, bypassing the view services and their filtering.  For example, this lists soft-deleted entities, which normal queries do not return:

```
###
# @name findDeletedEntities
POST {{baseURL}}/servers/{{metadataStore}}/open-metadata/repository-services/users/{{userId}}/instances/entities
Authorization: Bearer {{token}}
Content-Type: application/json

{
  "class" : "EntityFindRequest",
  "limitResultsByStatus" : ["DELETED"],
  "offset" : 0,
  "pageSize" : 10
}
```

Use these calls with care: they work below the view and access services, so they skip the validation, anchor maintenance and filtering those services apply.  The local metadata collection identifier, which must match the one stored in the repository, is returned by `POST .../repository-services/users/{{userId}}/metadata-collection-id` with the body `{"class" : "GetRequest"}`.

--8<-- "snippets/abbr.md"
