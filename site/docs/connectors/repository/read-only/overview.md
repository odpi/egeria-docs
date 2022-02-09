<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


--8<-- "snippets/content-status/released.md"

# Read-only Repository Connector

The read only repository connector provides a compliant implementation of a local repository
that can be configured into a [Metadata Access Store](/concepts/metadata-access-store).
It does not support the interfaces for
create, update, delete.  However it does support the search interfaces and is able to cache metadata.

This means it can be loaded with metadata from an
[Open Metadata Archive](/concepts/open-metadata-archive) and connected
to a cohort.  The content from the archive will be shared with other members of the cohort.


--8<-- "snippets/abbr.md"

