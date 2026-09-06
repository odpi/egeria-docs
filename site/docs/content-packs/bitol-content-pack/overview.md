<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Bitol Content Pack

The *BitolContentPack* contains the connector definitions for the integration connectors that work with the [Bitol](https://bitol.io) open standards - the *Open Data Contract Standard (ODCS)* and the *Open Data Product Standard (ODPS)* - supplied in the *omag-server-platform* distribution, along with the valid metadata values for the file types they read and write.  It is designed to provide a good starting point for exchanging data contracts and data product descriptors between Egeria's [digital product](/concepts/digital-product) catalog and the teams that publish them as YAML documents.

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

## Contents

The content pack defines the *BitolIntegrationGroup* and registers six integration connectors with it:

| Connector | Role |
| --- | --- |
| Bitol Files Receiver | Monitors file directories (by default `loading-bay/bitol`, or a git checkout attached as a catalog target) and publishes new and changed ODCS/ODPS documents to the Bitol listeners in the integration daemon. |
| Bitol Event Receiver | Receives ODCS/ODPS documents from the Apache Kafka topics attached as catalog targets. |
| Bitol Data Product Cataloguer | Catalogs each ODPS document as a *DigitalProduct* with *SolutionPort*s for its input and output ports. |
| Bitol Data Contract Cataloguer | Catalogs each ODCS document as an *Agreement* classified as a *DataSharingAgreement*, with its schema, quality rules, service levels, servers and security roles. |
| Bitol Document Publisher | Generates ODPS and ODCS documents from the digital products and data sharing agreements in open metadata whenever they change, and for the members of the *DigitalProductCatalog*s attached as catalog targets. |
| Bitol File Store | Writes every document published in the integration daemon to the file system (by default `logs/bitol`), organized by kind, identifier and version, ready to be committed to a git repository. |

The receivers, cataloguers, publisher and store are linked through the integration daemon's Bitol listener mechanism in the same way as the [Open Lineage connectors](/content-packs/open-lineage-content-pack/overview).  Documents may also be published to the daemon through its REST API and through the [Product Manager OMVS](/services/omvs/product-manager/overview).

The mapping between the documents and open metadata is described in the [digital product management](/features/digital-product-management/overview) feature, and in the [connectors' README :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/adapters/open-connectors/integration-connectors/bitol-integration-connectors/README.md){ target=gh }.

--8<-- "snippets/abbr.md"
