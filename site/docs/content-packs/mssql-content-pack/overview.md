<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Microsoft SQL Server Content Pack

The *MSSQLContentPack* contains the reference data, templates, connector definitions and governance services for working with a Microsoft SQL Server.  These connectors are supplied in the *omag-server-platform* distribution.  This content pack is designed to provide a good starting point for connecting Egeria to Microsoft SQL Server.

It provides templates for Microsoft SQL Server services and databases, along with the function to survey the contents of Microsoft SQL Server databases and catalog their schemas.

## What it defines

* The *Egeria:IntegrationGroup:MSSQL* [integration group](/concepts/integration-group), which supplies the [integration connectors](/concepts/integration-connector) that catalog Microsoft SQL Server databases and their schemas.
* The *MSSQLSurvey* [governance engine](/concepts/governance-engine) - *Microsoft SQL Server Survey Engine* - which provides the specialist [survey action services](/concepts/survey-action-service) for Microsoft SQL Servers.
* The *MSSQLGovernance* governance engine - *Microsoft SQL Server Governance Engine* - which provides the specialist [governance services](/concepts/governance-service) for Microsoft SQL Servers.
* The [templates](/concepts/template) and [valid metadata values](/guides/planning/valid-values/overview) for Microsoft SQL Server servers, databases, schemas and tables.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

--8<-- "snippets/abbr.md"
