<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Db2 for Linux, UNIX and Windows Content Pack

The *DB2LUWContentPack* contains the reference data, templates, connector definitions and governance services for working with an IBM Db2 for Linux, UNIX and Windows (LUW / UDB) Server.  These connectors are supplied in the *omag-server-platform* distribution.  This content pack is designed to provide a good starting point for connecting Egeria to Db2 for Linux, UNIX and Windows.

It provides templates for Db2 servers and databases, along with the function to survey the contents of Db2 databases and catalog their schemas.

## What it defines

* The *Egeria:IntegrationGroup:DB2LUW* [integration group](/concepts/integration-group), which supplies the [integration connectors](/concepts/integration-connector) that catalog Db2 databases and their schemas.
* The *DB2LUWSurvey* [governance engine](/concepts/governance-engine) - *Db2 for Linux, UNIX and Windows Server Survey Engine* - which provides the specialist [survey action services](/concepts/survey-action-service) for Db2 servers.
* The *DB2LUWGovernance* governance engine - *Db2 for Linux, UNIX and Windows Server Governance Engine* - which provides the specialist [governance services](/concepts/governance-service) for Db2 servers.
* The [templates](/concepts/template) and [valid metadata values](/guides/planning/valid-values/overview) for Db2 servers, databases, schemas and tables.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

--8<-- "snippets/abbr.md"
