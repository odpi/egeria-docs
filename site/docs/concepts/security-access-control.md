---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Security Access Control

A security access control defines the permissions to perform specific operations on a particular [digital resource](/concepts/digital-resource).

## Common Access Control Models

The security profession defines a number of approaches to managing access to digital resources:

* Role-Based Access Control (RBAC): Assigns permissions based on user roles, simplifying management and following the principle of least privilege.
* Attribute-Based Access Control (ABAC): Uses user attributes such as location, job title, or time of access to dynamically determine permissions.
* Discretionary Access Control (DAC): Allows resource owners to decide who can access their resources.
* Mandatory Access Control (MAC): Enforces strict policies set by administrators, often used in high-security environments.
    
Each of these are possible in Egeria using [metadata security](/features/metadata-security/overview) and [governance zones](/features/governance-zoning/overview).

??? info "Further information"

    * The *SecurityAccessControl* open metadata type is described in [Model 0423 Security Definitions](/types/4/0423-Security-Definitions).
    * Security access controls are stored in a [secrets store collection](/concepts/secrets-store-connector).
    * The [Security Officer API](/services/omvs/security-officer/overview) is used to maintain security access controls.


--8<-- "snippets/abbr.md"