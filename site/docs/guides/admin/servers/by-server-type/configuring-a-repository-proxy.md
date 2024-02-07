<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring a [repository proxy](/concepts/repository-proxy)

A *Repository Proxy* is configured by creating a [configuration document](/concepts/configuration-document).  Below is the outline structure of the server's configuration document.

![Configuration for a repository proxy](repository-proxy-config.svg)

??? info "Configuring the default values used in subsequent configuration commands"
    --8<-- "snippets/admin/configuring-event-bus.md"
    --8<-- "snippets/admin/configuring-local-server-url.md"

??? info "Configuring the basic properties"
    --8<-- "snippets/admin/configuring-omag-server-basic-properties.md"

??? info "Configuring the audit log"
    --8<-- "snippets/admin/configuring-the-audit-log.md"

??? info "Configuring the server security connector"
    --8<-- "snippets/admin/configuring-the-server-security-connector.md"

??? info "Registering the server with a cohort"
    --8<-- "snippets/admin/configuring-registration-to-a-cohort.md"

??? info "Configuring the connectors to the third party metadata repository"
    --8<-- "snippets/admin/configuring-the-repository-proxy-connector.md"


--8<-- "snippets/abbr.md"
