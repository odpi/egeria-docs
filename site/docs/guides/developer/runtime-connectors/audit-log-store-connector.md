---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Audit Log Store Connectors

The *audit log store connectors* provide a common interface to an audit log destination. It is used by the [OMAG Server's](/egeria-docs/concepts/omag-server)'s [audit log](/egeria-docs/concepts/audit-log).

The audit log supports multiple instances of the audit log store and will pass audit log records to each configured instance of the audit log store connectors.

Implementations of this type of connector are located in the [adapters/open-connectors/repository-services-connectors/audit-log-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/audit-log-connectors){ target=gh } module.

--8<-- "snippets/abbr.md"
