<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Metadata Repository

A *metadata repository* is a store for metadata.

Most organizations have several, and they arrive for different reasons: a database catalog that came with the database platform, a data catalog bought to support an analytics programme, a configuration management database run by the infrastructure team, a modelling tool with its own repository.  Each is authoritative about part of the landscape and knows nothing about the rest.

A metadata repository that supports the open metadata standards is called an [*open metadata repository*](/concepts/open-metadata-repository).  Supporting those standards is what allows repositories to work together: they can exchange metadata, agree on which of them is the master of each element, and present a single view of the landscape to the people and processes that need it.

A repository that does not support the open metadata standards natively can still take part, through a [repository proxy](/concepts/repository-proxy) that translates the open metadata repository API into the repository's own API, or through an [integration connector](/concepts/integration-connector) that keeps a catalog entry in step with it.

???+ info "Additional information"
    * [Open metadata repository](/concepts/open-metadata-repository) describes the two kinds of open metadata repository, and how they store metadata from more than one [metadata collection](/concepts/metadata-collection).
    * [Cohort member](/concepts/cohort-member) describes how repositories are connected together into an [open metadata repository cohort](/concepts/cohort-member).

--8<-- "snippets/abbr.md"
