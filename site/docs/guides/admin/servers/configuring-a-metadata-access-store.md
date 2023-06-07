<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring a [metadata access store](/concepts/metadata-access-store)

A *Metadata Access Store* is configured by creating a [configuration document](/concepts/configuration-document). Below are the outline structures of the server's configuration document.

A metadata access store can be run standalone, without connecting to a cohort:

![Standalone metadata access store](standalone-metadata-access-store-config.svg)

Adding the cohort configuration enables the metadata server to communicate with other metadata servers:

![Connected metadata access store](connected-metadata-access-store-config.svg)

??? info "Configuring the default values used in subsequent configuration commands"
    --8<-- "docs/guides/admin/servers/configuring-event-bus.md"
    --8<-- "docs/guides/admin/servers/configuring-local-server-url.md"

??? info "Configuring the basic properties"
    --8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

??? info "Configuring the audit log"
    --8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

??? info "Configuring the server security connector"
    --8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md"

??? info "Configuring the local repository store"
    --8<-- "docs/guides/admin/servers/configuring-the-local-repository.md"

??? info "Registering the server with a cohort"
    --8<-- "docs/guides/admin/servers/configuring-registration-to-a-cohort.md"

??? info "Configuring the access services"
    --8<-- "docs/guides/admin/servers/configuring-the-access-services.md"

??? info "(Optional) Configuring the open metadata archives to load on server start up"
    --8<-- "docs/guides/admin/servers/configuring-the-startup-archives.md"

--8<-- "snippets/abbr.md"
