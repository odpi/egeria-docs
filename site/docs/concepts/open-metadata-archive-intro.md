<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


An *open metadata archive* is a portable collection of open metadata [type definitions](/introduction/key-concepts/#metadata-types) and [instances](/introduction/key-concepts/#metadata-instances).  It can be [loaded each time a metadata access server starts up](/guides/admin/servers/configuring-a-metadata-access-store/#configure-metadata-to-load-on-startup) or [added to a running metadata access server](/guides/operations/adding-archive-to-running-server).

The open metadata archive has two types:

- A **content pack** containing reusable definitions that are generally useful. They may come from the Egeria community or third parties.
- A **metadata export** containing an export of metadata from a repository. They are used to transfer metadata between repositories that are not connected to the same [cohort](/services/omrs/cohort).


--8<-- "snippets/abbr.md"
