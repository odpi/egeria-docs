<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# OMRS Archive Manager

An [open metadata archive](/concepts/open-metadata-archive) provides pre-built definitions
for types and metadata instances.

**OMRSArchiveManager** manages the loading and unloading of open metadata archives for the local OMRS repository.
It is invoked at server start up for a [cohort member](/concepts/cohort-member)
and whenever a new open metadata archive is loaded via a REST API.
 
During server start up, it first calls the [Repository Content Manager](repository-content-manager.md)
to load the types into the local repository (if any) and to maintain the cache of know and active types in the server.

It then calls the [Local Repository Instance Event Processor](local-repository-instance-event-processor.md) to
load the instances. 

## Related information

A description of the utilities for building archives
can be found in the [open-metadata-archives](/concepts/open-metadata-archive)
modules.

Details for configuring a metadata access store to load archives can be found in the
[Administration Guide](/guides/admin/configuring-a-metadata-access-store).

---8<-- "snippets/abbr.md"
