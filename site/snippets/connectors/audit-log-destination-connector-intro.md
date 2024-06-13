<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

An *[audit log destination connector](/concepts/audit-log-destination-connector)* provides support for a specific *audit log destination*. At least one audit log destination connector is [configured](/concepts/audit-log/#configure-the-audit-log) in every [OMAG Server's](/concepts/omag-server)'s [configuration document](/concepts/configuraton-document) and used by its [audit log](/concepts/audit-log) component when the server runs.

![Audit Log Destination Connector](/connectors/runtime/audit-log-destination-connector.svg)


An audit log destination's purpose may be either to store, process or distribute audit log records to diagnostic systems.  Its associated configuration controls which severities of audit log record it receives.  The implementation for the audit log destination connector can make further choices about how each log record is processed.

