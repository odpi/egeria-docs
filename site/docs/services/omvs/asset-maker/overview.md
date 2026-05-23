

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/stable.md"

# Asset Maker API

The Asset Maker API provides APIs for user interfaces that support the creation and maintenance of digital assets and their related properties, such as software capabilities, deployment relationships, and governance actions.

## Key Features

- **Asset Management**: Create, update, and delete different types of assets. Support for creating assets from templates.
- **Software Capability Management**: Define and maintain software capabilities, representing software components, services, or engines.
- **IT Asset Deployment**: Manage the deployment of software capabilities and assets to infrastructure, including linking and detaching implementation details.
- **Data Asset Management**: Organize data assets into data sets and manage their content relationships.
- **Governance Action Management**: Create and track governance actions, assign them to actors, and manage their targets.
- **Catalog Target Management**: Manage the association between integration connectors and the metadata elements they are responsible for cataloguing.
- **Search and Exploration**: Find assets, processes, and software capabilities using search strings and filters.

## Further information

- [Asset Concept](https://egeria-project.org/concepts/asset/)
- [Software Capability Concept](/concepts/software-capability/)
- [Governance Action Concept](/concepts/governance-action/)

----
Sample REST API requests:

- [Egeria-api-asset-maker.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/asset-maker/Egeria-api-asset-maker.http)
- [Egeria-jacquard-actions.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/asset-maker/Egeria-jacquard-actions.http)
- [Egeria-metadata-collections.http](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/view-server-generic-services/asset-maker/Egeria-metadata-collections.http)

---8<-- "snippets/abbr.md"






