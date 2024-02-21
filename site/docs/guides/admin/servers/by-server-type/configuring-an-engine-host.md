<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Configuring an Engine Host

An *[Engine Host](/concepts/engine-host)* is responsible for hosting [Governance Engines](/concepts/governance-engine).  Its configuration needs to include the location of the [Metadata Access Server](/concepts/metadata-access-server) that provides access to the open metadata repositories and the names of the governance engines it is to host. 

![Configuration for an engine host](/concepts/engine-host.svg)


--8<-- "snippets/admin/configuring-standard-sections.md"

??? info "Configuring the Engine Host Services"
    --8<-- "snippets/admin/configuring-the-engine-host-services.md"

??? deprecated "Configuration for an engine host prior to release 5.0"
    Prior to release 5.0, the list of engines to run in an engine host was configured under each engine service.  It was necessary to align the type of governance engine with the correct engine service.
    ![Configuration for an engine host prior to release 5.0](engine-host-config-old.svg)

??? example "Example configuration of an engine host"
    This is an example of the configuration for an engine host called `engine-host`.  It is configured to run 3 engines called `FileProvisioning`, `AssetSurvey` and `AssetGovernance`.  It makes calls to the `active-metadata-store` [Metadata Access Store](/concepts/metadata-access-store).
    
    --8<-- "snippets/admin/by-server-type/engine-host-config-doc-example.md"

    This configuration document is shipped as one of the sample configurations in the `omag-server-platform` assembly.

--8<-- "snippets/abbr.md"
