<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Configuring a [metadata server](/egeria/concepts/metadata-server)

Each [type of OMAG Server](/egeria/concepts/omag-server/#types-of-omag-server) is configured by creating
a [configuration document](/egeria/concepts/configuration-document).

A metadata server can be run standalone, without connecting to a cohort:

![Standalone metadata server](standalone-metadata-server-config.png)

Adding the cohort configuration enables the metadata server to communicate with other metadata
servers:

![Connected metadata server](connected-metadata-server-config.png)

--8<-- "snippets/tasks/configuring-event-bus.md"

--8<-- "snippets/tasks/configuring-local-server-url.md"

--8<-- "snippets/tasks/configuring-omag-server-basic-properties.md"

--8<-- "snippets/tasks/configuring-the-audit-log.md"

--8<-- "snippets/tasks/configuring-the-server-security-connector.md"

--8<-- "snippets/tasks/configuring-the-local-repository.md"

--8<-- "snippets/tasks/configuring-registration-to-a-cohort.md"

--8<-- "snippets/tasks/configuring-the-startup-archives.md"

--8<-- "snippets/tasks/configuring-the-access-services.md"

--8<-- "snippets/abbr.md"
