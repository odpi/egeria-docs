<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

# Governance Action Service

---8<-- "docs/connectors/governance-action/governance-action-service-intro.md"

## Governance Context

A governance action service is passed a context as it is started. This provides access to the request type and associated parameters (name-value pairs) used to invoke the governance action service, along with a client to access open metadata through the Governance Engine OMAS.

![Structure of the governance context](governance-context.svg)

This context is then specialized for each type of governance action service. Details of the specific context for each service can be found in the links to the various governance action service types.         
  
--8<-- "snippets/abbr.md"