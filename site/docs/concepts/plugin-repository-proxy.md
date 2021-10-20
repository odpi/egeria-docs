---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Plugin Repository Proxy

A *plugin repository proxy* is an [OMAG Server](/egeria-docs/concepts/omag-server) that has been configured to act as a pluggable, native Egeria metadata repository backed by a non-Egeria persistent store.

![Plugin repository proxy translating between a back-end persistence layer and open metadata](plugin-repository-proxy.svg)

The plugin repository proxy hosts a repository connector to wrap the non-Egeria back-end with the necessary OMRS-level APIs.

!!! question "Difference vs. a repository proxy?"
    The primary difference between a *plugin* repository proxy and a repository proxy is that the *plugin* repository proxy is a native Egeria repository implementation: there is no separate user interface or set of interactions that the repository in a *plugin* repository proxy will serve other than Egeria itself. With a (non-plugin) repository proxy, there will typically be a non-Egeria user interface and application that are also served by the back-end, in addition to Egeria.

There are two plugin repository connector implementations included with Egeria:

- [XTDB repository connector :material-github:](https://github.com/odpi/egeria-connector-xtdb){ target=xtdb }
- [JanusGraph repository connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors/graph-repository-connector){ target=janus }

--8<-- "snippets/abbr.md"
