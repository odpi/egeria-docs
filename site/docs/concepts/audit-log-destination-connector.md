<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Audit Log Destination Connector

The audit log destination connector implements a common interface to an audit log destination.  It is used by the *[Audit Log](/egeria-docs/concepts/audit-log)* to pass audit log records to various locations either to store, process or distribute further.

![Audit Log Destination Connector](/egeria-docs/connectors/runtime/audit-log-destination-connector.svg)

An [OMAG Server](/egeria-docs/concepts/omag-server) can have [multiple audit log destinations](/egeria-docs/guides/admin/configuring-an-integration-daemon/#configure-the-audit-log) configured.  This configuration can control which severities of audit log record are sent to each destination.

The implementation for the audit log destination connector can make further choices about how each log record is processed.

The interface for audit log destination connectors is located in the
[repository-services-apis](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/auditlogstore) module.  The audit log destination connectors implemented by Egeria are described in the [connector catalog](/egeria-docs/connectors/#audit-log-destination-connectors).


---8<-- "snippets/abbr.md"
