---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Repository Proxy

A *repository proxy* is an [OMAG Server](/concepts/omag-server) that has been configured to act as a proxy to a third party metadata repository. 

![Repository proxy translating between third party APIs/events and open metadata](repository-proxy.svg)

The repository proxy hosts a repository connector to wrap the third party metadata server's APIs and an optional event mapper connector.  There are two repository connector implementations included with Egeria:

- [Repository connectors for Apache Atlas :material-dock-window:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=atlas }
- [Repository connectors for IBM Information Governance Catalog (IGC) :material-dock-window:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=infosvr }

The value of a repository proxy is that it provides access to the metadata that is being collected by the third party metadata repository.  For example, in the picture below, Apache Atlas is running in a Hadoop environment and cataloguing the data it contains.  Through the repository proxy, this metadata is then visible to all of the other users connected via the [cohort](/features/cohort-operation/overview).

![Connecting to Apache Atlas](repository-proxy-atlas.svg)


--8<-- "snippets/abbr.md"
