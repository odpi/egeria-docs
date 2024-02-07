---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Archive manager

An [open metadata archive](/concepts/open-metadata-archive) provides pre-built definitions
for types and metadata instances.

`OMRSArchiveManager` manages the loading and unloading of open metadata archives for the local OMRS repository. It is invoked at server start up for a [cohort member](/services/omrs/cohort/#cohort-members) and whenever a new open metadata archive is loaded via a REST API.
 
During server start up, it first calls the [repository content manager](repository-content-manager.md) to load the types into the local repository (if any) and to maintain the cache of know and active types in the server.

It then calls the [local repository instance event processor](/services/omrs/component-descriptions/local-repository-instance-event-processor) to load the instances.

## Related information

A description of the utilities for building archives can be found in the [open-metadata-archives :material-github:](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives){ target=gh } modules.

Details for configuring a metadata server to load archives can be found in the [administration guide](/guides/admin/servers/by-section/repository-services-section/#configuring-the-open-metadata-archives-to-load-on-server-startup).

--8<-- "snippets/abbr.md"
