<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Calling Egeria's REST APIs

Egeria's public REST APIs are the Open Metadata View Services (OMVS).  They run in the [View Server](/concepts/view-server) and are designed to be called by user interfaces, scripts and other tools.  Each view service has its own *URL marker* that appears in the URL path:

```
{{platformURLRoot}}/servers/{{viewServerName}}/api/open-metadata/{{urlMarker}}/...
```

For example, the [My Profile](/services/omvs/my-profile/overview) service uses the URL marker `my-profile`, so its `getMyProfile` request is `GET {{platformURLRoot}}/servers/{{viewServerName}}/api/open-metadata/my-profile`.  The view services that are available in every view server (such as [Asset Maker](/services/omvs/asset-maker/overview) and [Classification Explorer](/services/omvs/classification-explorer/overview)) accept the URL marker of any active view service, so the same request can be issued through the specialist service that suits the caller.  The full list of view services is in the [OMVS catalog](/services/omvs).

## Authentication

Every request to the view services must carry a bearer token in the `Authorization` header.  The token is obtained from the platform's token service by sending the user's userId and password in the request body:

```
POST {{platformURLRoot}}/api/token
Content-Type: application/json

{
  "userId" : "peterprofile",
  "password" : "secret"
}
```

The response body is the token.  It is then passed on each request:

```
GET {{platformURLRoot}}/servers/{{viewServerName}}/api/open-metadata/my-profile
Authorization: Bearer {{token}}
```

The token service is also available at `{{platformURLRoot}}/servers/{{serverName}}/api/token`, and `DELETE {{platformURLRoot}}/api/token/logout` ends the session.

## Internal REST APIs

Egeria also uses REST APIs to issue synchronous calls between its servers and platforms.  These include the [platform services](/services/platform-services/overview) (`/open-metadata/platform-services/...`), the [administration services](/services/admin-services/overview) (`/open-metadata/admin-services/...`), the server operations (`/open-metadata/server-operations/...`), the repository services (`/servers/{{serverName}}/open-metadata/repository-services/...`), the governance server services (for example `/servers/{{serverName}}/open-metadata/engine-host/...`) and the framework services that support the connectors (for example `/servers/{{serverName}}/open-metadata/access-services/open-metadata-store/...`).

These APIs are called via the [Java clients](/guides/developer/java-clients/overview).  They are considered internal to Egeria and there is no guarantee that they remain backward compatible.  For operating Egeria, the [Runtime Manager](/services/omvs/runtime-manager/overview) view service is the recommended entry point - see [REST APIs](/guides/operations/overview#rest-apis) in the Operations Guide.

## Finding the API definitions

All the REST APIs are published through Swagger at this URL:

```

{{platformURLRoot}}/swagger-ui/index.html

```

The default rendering is poor and the Egeria community is looking for help to improve it.

It is also possible to get the raw Open API Specification from this URL:

```

{{platformURLRoot}}/v3/api-docs

```

Most modules also provide IntelliJ HTTP Client collections (`.http` files).  For example, each view service module, such as `open-metadata-implementation/view-services/my-profile`, has an `Egeria-api-<service>.http` file that starts with the token request and then has an example of each call.  These can execute in an IntelliJ environment.  They are also easy to read and so are probably the best documentation of our REST API.


--8<-- "snippets/abbr.md"
