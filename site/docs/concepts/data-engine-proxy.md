---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# Data engine proxy

The *data engine proxy* is a [governance server](/concepts/governance-server) that can capture metadata about data movement processes (such as ETL jobs) from a data engine.  This information results in new [Process](/types/0/0010-Base-Model) being defined in open metadata linked to the data sources that it works with. This is valuable information for [lineage](/features/lineage-management/overview).

![Data Engine Proxy](data-engine-proxy.svg)

The data engine proxy is paired with the [Data Engine OMAS](/services/omas/data-engine/overview). Its connector interfaces are defined in the [data-engine-proxy-connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/governance-servers/data-engine-proxy-services/data-engine-proxy-connector){ target=gh } module.

!!! education "Further information"
    - [Setting up the data engine proxy](/guides/admin/configuring-a-data-engine-proxy-server)

--8<-- "snippets/abbr.md"
