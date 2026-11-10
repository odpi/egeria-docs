<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Server Platform Origin Service

The server platform origin service is a simple REST API that returns basic information about an [Open Metadata and Governance (OMAG) Server Platform](/concepts/omag-server-platform).

Operational scripts often call it while starting or shutting down a platform, to find out whether the platform is running.

The service has a single operation:

```
###
# @name platformOrigin
GET {{baseURL}}/open-metadata/platform-services/server-platform/origin
```

`{{baseURL}}` is the platform's network address - typically its host name and port number, such as `https://localhost:9443`.

The origin is one of the few platform calls that does not need a bearer token.  A script can therefore check that the platform is up before it asks for a token.

The response is a single string describing the implementation and version of the platform.  For example:

```bash
curl --insecure https://localhost:9443/open-metadata/platform-services/server-platform/origin
```

```
Egeria OMAG Server Platform (version 6.3-SNAPSHOT)
```

The `--insecure` option is only needed when the platform uses a self-signed certificate, as the samples do.

## Other ways to get the origin

* pyegeria - `get_platform_origin()` on any of its clients.
* `GET {{baseURL}}/api/about` also needs no token.  It returns a JSON description of the platform's build, including `version` and the build `time`.
* Once you have a token, the [Diagnostic APIs](/guides/diagnostic/diagnostic-apis#is-the-platform-running) describe the calls that return the platform's start time and the servers running on it.

--8<-- "snippets/abbr.md"
