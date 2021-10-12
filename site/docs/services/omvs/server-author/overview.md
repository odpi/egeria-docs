---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"
  
# Server Author Open Metadata View Service (OMVS)


The Server Author Open Metadata View Service (OMVS) is an Integration View Service that supports Server Author UI operations
that retrieve, author and deploy server configurations.

The purpose of this interface is to enable an IT Infrastructure Architect to author servers in the Egeria eco-system.


This view service offers authoring capabilities; OMAG server configurations are accumulated on the
platform root url that is identified in the Server Author View configuration by the 'omagServerPlatformRootURL'.

While authoring servers, the caller is  not aware of where the server configurations are being accumulated.

In addition to server authoring capabilities, this view service exposes a query that returns the known platforms,
as defined in the view, each platform that is returned continues the servers are stored on them. The caller can
then deploy a server that has been configured onto a particular platform.

In this view server API, platforms and servers are referred to by name, to ease consumption by a user interface.

This view service calls a remote platform using the [admin client](/egeria-docs/services/admin-services).

---8<-- "snippets/abbr.md"