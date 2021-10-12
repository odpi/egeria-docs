<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring a [view server](/egeria-docs/concepts/view-server)

Each [type of OMAG Server](/egeria-docs/concepts/omag-server/#types-of-omag-server) is configured by creating
a [configuration document](/egeria-docs/concepts/configuration-document).

![Configuration for a view server](view-server-config.svg)

--8<-- "snippets/tasks/configuring-omag-server-basic-properties.md"

--8<-- "snippets/tasks/configuring-the-audit-log.md"

--8<-- "snippets/tasks/configuring-the-server-security-connector.md"

--8<-- "snippets/tasks/configuring-the-view-services.md"

## Configure the presentation server

The [presentation server](/egeria-docs/concepts/presentation-server) is a multi-tenant web application that calls
view services running in a [view server](/egeria-docs/concepts/view-server) to retrieve information and perform operations
relating to metadata servers.

A presentation server tenant is designed to support an organization. These may be independent organizations
or divisions/departments within an organization. The tenant routes requests to the appropriate
view server and then on to the metadata servers behind. Therefore, each tenant sees a different collection of
metadata.

Information for configuring the presentation server is provided [in a separate GitHub repository :material-dock-window:](https://github.com/odpi/egeria-react-ui){ target=react }.

--8<-- "snippets/abbr.md"
