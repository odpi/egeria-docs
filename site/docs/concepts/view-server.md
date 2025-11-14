---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# View Server

A *view server* is an [OMAG Server](/concepts/omag-server) that hosts the REST API services called [Open Metadata View Services (OMVSs)](/services/omvs).  These APIs provide access to the full capability of Egeria.  Examples of their use include:

* Third party technology platforms that are integrating directly into with open metadata ecosystem. 
* Javascript browser-based UIs.
* The [pyegeria](/concepts/pyegeria) libraries that support a wide rage of additional capability for the python world. For example, Apache Airflow could be providing a python runtime for metadata exchange jobs.  This approach provides a python option for writing metadata synchronization logic, that is typically implemented as an [integration connector](/concepts/integration-connector) in Java.

![A view server in the open metadata ecosystem](view-server.svg)

The view services are accessed using bearer tokens.  The [OMAG Server Platform](/concepts/omag-server-platform) that hosts the view server includes a default token service with an associated authentication function.  If you wish to use your own token service, the authentication approach can be changed by replacing the [platform metadata security connector](/features/metadata-security/overview) that calls a third party token authentication service.

--8<-- "snippets/abbr.md"
