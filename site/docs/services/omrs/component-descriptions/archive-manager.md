<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Archive Manager

An [open metadata archive](../open-metadata-archive.md) provides pre-built definitions
for types and metadata instances.

**OMRSArchiveManager** manages the loading and unloading of open metadata archives for the local OMRS repository.
It is invoked at server start up for a [cohort member](../cohort-member.md)
and whenever a new open metadata archive is loaded via a REST API.
 
During server start up, it first calls the [Repository Content Manager](repository-content-manager.md)
to load the types into the local repository (if any) and to maintain the cache of know and active types in the server.

It then calls the [Local Repository Instance Event Processor](local-repository-instance-event-processor.md) to
load the instances. 

## Related information

A description of the utilities for building archives
can be found in the [open-metadata-archives](/egeria-docs/concepts/open-metadata-archives)
modules.

Details for configuring a metadata server to load archives can be found in the
[Administration Guide](/egeria-docs/guides/admin).

---8<-- "snippets/abbr.md"
