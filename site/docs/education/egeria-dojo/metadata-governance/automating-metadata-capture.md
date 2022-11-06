<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->


## Automating metadata capture

People are not good at repetitive admin tasks, particularly if they are not the primary focus of their work.  Therefore, the open metadata ecosystem is more complete and accurate is much of the metadata management is automated.  Following our three step model, the automation needs to monitor for triggers that indicate that metadata needs to be updated, drive the necessary changes to metadata and then make those changes visible to downstream processing.

!!! info "Covering ..."
    - How the integration daemon works
    - Using the connector catalog
    - Configuring connectors in the integration daemon
    - Reviewing diagnostics and resulting metadata

??? beginner "Introducing the integration daemon (30 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/introducing-integration-daemon.md"

??? intermediate "Configuring an integration connector (30 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/configuring-integration-daemon.md"

??? intermediate "Validating your integration (30 mins)"
    --8<-- "docs/education/egeria-dojo/metadata-governance/validating-your-integration.md"

!!! education "Further information"
    - [Integrated Cataloguing](/features/integrated-cataloguing/overview)
    - [Open Metadata Integration Services (OMIS)](/services/omis)
    - [Integration Daemon](/concepts/integration-daemon)



--8<-- "snippets/abbr.md"