<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


An *open metadata archive* is a portable collection of open metadata [type definitions](/introduction/key-concepts/#metadata-types) and [instances](/introduction/key-concepts/#metadata-instances).  It can be [loaded each time a metadata access server starts up](/guides/admin/servers/configuring-a-metadata-access-store/#configure-metadata-to-load-on-startup) or [added to a running metadata access server](/guides/operations/adding-archive-to-running-server).

The open metadata archive has three types that are used to signal how the archive is intended to be used:

- A *content pack* contains standard metadata that is generally useful. It may come from the Egeria community or third parties.  It can be loaded into many repositories, whether these repositories are connected or not via [cohorts](/concepts/cohort-member).  This is a useful way to distribute [open metadata types](/types) or definitions for a standard.
- A *metadata export* contains a collection of metadata elements that have been extracted from a specific open metadata repository to load into another. It is used to transfer metadata between repositories that are not connected via [cohorts](/concepts/cohort-member).
- A *repository backup* contains a collection of metadata elements  that is intended to act as a backup for a server.  It typically contains metadata instances from the server's [local metadata collection](/concepts/metadata-collection). This archive is expected to be loaded back into the same repository.  This can be done at any time.  If the repository contains more recent content, the older content in the archive is ignored.


--8<-- "snippets/abbr.md"
