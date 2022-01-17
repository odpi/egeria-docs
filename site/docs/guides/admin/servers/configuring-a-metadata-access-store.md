<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring a [metadata access store](/egeria-docs/concepts/metadata-access-store)

Each [type of OMAG Server](/egeria-docs/concepts/omag-server/#types-of-omag-server) is configured by creating a [configuration document](/egeria-docs/concepts/configuration-document).

A metadata access store can be run standalone, without connecting to a cohort:

![Standalone metadata access store](standalone-metadata-access-store-config.svg)

Adding the cohort configuration enables the metadata server to communicate with other metadata
servers:

![Connected metadata access store](connected-metadata-access-store-config.svg)

--8<-- "docs/guides/admin/servers/configuring-event-bus.md"

--8<-- "docs/guides/admin/servers/configuring-local-server-url.md"

--8<-- "docs/guides/admin/servers/configuring-omag-server-basic-properties.md"

--8<-- "docs/guides/admin/servers/configuring-the-audit-log.md"

--8<-- "docs/guides/admin/servers/configuring-the-server-security-connector.md"

--8<-- "docs/guides/admin/servers/configuring-the-local-repository.md"

--8<-- "docs/guides/admin/servers/configuring-registration-to-a-cohort.md"

--8<-- "docs/guides/admin/servers/configuring-the-startup-archives.md"

--8<-- "docs/guides/admin/servers/configuring-the-access-services.md"

--8<-- "snippets/abbr.md"
