<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *[audit log destination connector](/egeria-docs/concepts/audit-log-destination-connector)* provides support for a specific *audit log destination*. At least one audit log destination connector is [configured](/egeria-docs/concepts/audit-log/#configure-the-audit-log) in every [OMAG Server's](/egeria-docs/concepts/omag-server)'s [configuration document](/egeria-docs/concepts/configuraton-document) and used by its [audit log](/egeria-docs/concepts/audit-log) component when the server runs.

![Audit Log Destination Connector](/egeria-docs/connectors/runtime/audit-log-destination-connector.svg)


An audit log destination's purpose may be either to store, process or distribute audit log records to diagnostic systems.  Its associated configuration controls which severities of audit log record it receives.  The implementation for the audit log destination connector can make further choices about how each log record is processed.



---8<-- "snippets/abbr.md"
