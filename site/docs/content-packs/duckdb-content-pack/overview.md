<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# DuckDB Content Pack

The *DuckDBContentPack* contains the reference data, templates, connector definitions and governance services for working with a DuckDB database.  These connectors are supplied in the *omag-server-platform* distribution.  This content pack is designed to provide a good starting point for connecting Egeria to DuckDB.

It provides a template for DuckDB databases, along with the function to survey the contents of a DuckDB database - including its attached and federated data sources - and catalog its schemas.

## What it defines

* The *Egeria:IntegrationGroup:DuckDB* [integration group](/concepts/integration-group), which supplies the [integration connectors](/concepts/integration-connector) that catalog DuckDB databases and their schemas.
* The *DuckDBSurvey* [governance engine](/concepts/governance-engine) - *DuckDB Survey Engine* - which provides the specialist [survey action services](/concepts/survey-action-service) for DuckDB databases.
* The *DuckDBGovernance* governance engine - *DuckDB Governance Engine* - which provides the specialist [governance services](/concepts/governance-service) for DuckDB databases.
* The [templates](/concepts/template) and [valid metadata values](/guides/planning/valid-values/overview) for DuckDB databases, schemas and tables.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

--8<-- "snippets/abbr.md"
