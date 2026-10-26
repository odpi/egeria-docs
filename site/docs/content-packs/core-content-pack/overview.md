<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Core Content Pack

The *CoreContentPack* contains the definitions for the file and open lineage connectors supplied in this distribution along with the valid metadata values for the technologies they support and useful governance action processes. 

This content pack is designed to provide a good starting point for a new Egeria deployment. It is loaded automatically in the *active-metadata-store* sample server.
As it loads, the integration connectors defined in its content start up in the *integration-daemon* server, and the governance engines it defines will start up in the *engine-host*.


It also contains standard security definitions that are small and widely used: the six [STRIDE](/egeria-solutions/threat-modelling/overview#threat-elicitation) *Threat* definitions (`Threat::STRIDE::Spoofing`, `Threat::STRIDE::Tampering`, `Threat::STRIDE::Repudiation`, `Threat::STRIDE::InformationDisclosure`, `Threat::STRIDE::DenialOfService` and `Threat::STRIDE::ElevationOfPrivilege`), and the *CertificationType* for ISO/IEC 27001:2022 (`CertificationType::ISO/IEC 27001:2022`).  Larger security control catalogs are in the separate [Security Content Pack](/content-packs/security-content-pack/overview).

This content pack is built by the [core-content-pack](https://github.com/odpi/egeria/tree/main/open-metadata-resources/open-metadata-archives/) module.

--8<-- "snippets/blueprints/content-packs/core-content-pack-solution-blueprint-mermaid-graph.md"

--8<-- "snippets/abbr.md"