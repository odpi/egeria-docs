<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Governance Officer API

The Governance Officer API provides the ability to define and maintain
governance definitions, regulations, metrics, and manage licenses and certifications for metadata elements.
It also supports the tracking of implementation resources back to their design elements and exploring
governance action processes.

## Key features

* **Governance Definition Management**: Support for creating, updating, and deleting governance definitions, including the ability to create definitions from templates.
* **Relationship Management**: Capabilities for linking and detaching peer and supporting governance definitions, and associating definitions with metadata elements using the *GovernedBy* relationship.
* **Regulatory Compliance**: Linking regulator organizations to regulation governance definitions.
* **Governance Results Tracking**: Associating governance metrics with the data stores where measurements are located.
* **Licenses and Certifications**: Managing the lifecycle of licenses and certifications for metadata elements, including linking to license/certification types and updating properties.
* **Governance Action Process Exploration**: Visualizing and exploring the structure of governance action processes through process graphs.
* **Implementation and Design Tracking**: Linking design elements to implementation resources and implementation elements to track how governance requirements are realized.

??? info "Further information"

    * [Governance Definition Concept](/concepts/governance-definition/)
    * [Governance Action Concept](/concepts/governance-action/)
    * [Defining a governance program](/guides/planning/governance-program/overview)

----
Sample REST API requests can be found in [Egeria-api-governance-officer.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/governance-officer/Egeria-api-governance-officer.http).

## Defining a governance strategy

??? info "Further information"
    * [Defining the data strategy for Coco Pharmaceuticals](/practices/coco-pharmaceuticals/scenarios/defining-the-data-strategy/overview)




--8<-- "snippets/abbr.md"
