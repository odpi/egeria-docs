---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Security Integrator Open Metadata Integration Service (OMIS)

The Security Integrator OMIS supports distribution of security
parameters to access control enforcement engines such as Apache Ranger.
Its API simplifies the internal models and structures of
the open metadata type model and related structure for the consumers.

This integration service will ultimately be paired with the [Security Manager](/services/omas/security-manager/overview)
Open Metadata Access Service (OMAS).  However, it is currently calling the 
[Asset Manager OMAS](/services/omas/asset-manager/overview) while the Security Manager OMAS is implemented.
This means it is only monitoring security tags for assets rather than data fields.

--8<-- "snippets/abbr.md"