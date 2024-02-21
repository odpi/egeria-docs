<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring a Metadata Access Point

A [Metadata Access Point](/concepts/metadata-access-point) provides [Open Metadata Access Services (OMASs)](/services/omas) to [Governance Servers](/concepts/governance-server) and [View Servers](/concepts/view-server).  It does not have its own local metadata repository and so needs to connect to an [open metadata repository cohort](/concepts/cohort-member) to get access to the open metadata repositories.

![Configuration document for a metadata access point](/concepts/metadata-access-point.svg)

--8<-- "snippets/admin/configuring-standard-sections.md"

??? info "Registering the server with a cohort"
    --8<-- "snippets/admin/configuring-registration-to-a-cohort.md"

??? info "Configuring the access services"
    --8<-- "snippets/admin/configuring-the-access-services.md"

--8<-- "snippets/abbr.md"
