---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0455 Exception Management

Governance is supported by a number of operational logs.  Each operational log is a collection of log records.
In many cases each log record is stored as an individual file for ease of management.
It is not uncommon that the volume of log records is high and the value of the information in
each log record is variable.
As a result individual log records are not catalogued unless they are significant in some way.
(For example, it may be that the log record needs to be kept for regulatory purposes,
or there is stewardship action required.)
As such, the log records are written to storage as the processing that they describe proceeds.
Asynchronous processes then scan and review the content of the log records to ensure the processing is as expected.
They may also purge the log records that are no longer needed.

This log record processing may maintain various counts and other measurements that can be captured in the metadata
or in an external data store.  The **LogAnalysis** classification enables the capture of these measurements
in metadata.  For example,
log records that represent significant events may be catalogued as assets and
the **LogAnalysis** classification attached to the asset.
The results of the log analysis across many records may be rolled up into a
[GovernanceMeasurement](0450-Governance-Rollout.md) attached to the appropriate
[GovernanceDefinition](0401-Governance-Definitions.md).

The types of operational logs and associated processing are:

* Metering captures the usage of resources.  This may be to enforce usage quotas, or for billing.
  A collection of related metering record is represented as a **MeteringLog**.
  
* Operational lineage logging captures the execution path and results of processes.  It is used
  to prove that processes ran, and ran at the right time, processing the
  right quantity of data at appropriate quality.
  A collection of related lineage log records is represented as a **LineageLog**.

* Audit logging records significant events.  This may be successful processing events or detected errors that need action.
  A collection of related audit log records is represented as a **AuditLog**.
  
* Exception management handles errors detected by [verification points](0460-Governance-Execution-Points.md).
  Exception records are managed in one or more **ExceptionBacklog** collections.


![UML](0455-Exception-Management.svg)


--8<-- "snippets/abbr.md"