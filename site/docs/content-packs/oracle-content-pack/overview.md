<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Oracle Database Content Pack

The *OracleContentPack* contains the reference data, templates, connector definitions and governance services for working with an Oracle Database Server.  These connectors are supplied in the *omag-server-platform* distribution.  This content pack is designed to provide a good starting point for connecting Egeria to Oracle Database.

It provides templates for Oracle Database servers and pluggable databases, along with the function to survey the contents of Oracle pluggable databases and catalog their schemas.

## What it defines

* The *Egeria:IntegrationGroup:Oracle* [integration group](/concepts/integration-group), which supplies the [integration connectors](/concepts/integration-connector) that catalog Oracle pluggable databases and their schemas.
* The *OracleSurvey* [governance engine](/concepts/governance-engine) - *Oracle Database Server Survey Engine* - which provides the specialist [survey action services](/concepts/survey-action-service) for Oracle Database Servers.
* The *OracleGovernance* governance engine - *Oracle Database Server Governance Engine* - which provides the specialist [governance services](/concepts/governance-service) for Oracle Database Servers.
* The [templates](/concepts/template) and [valid metadata values](/guides/planning/valid-values/overview) for Oracle Database servers, pluggable databases, schemas and tables.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

--8<-- "snippets/abbr.md"
