---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Egeria Workspaces

[**Egeria Workspaces**](https://github.com/odpi/egeria-workspaces) offers a preconfigured, containerized environment that you can quickly download and run.  Once running, Egeria workspaces has a Jupyter notebook, command line and a Markdown environment for activating Egeria's governance solutions and configuring them to work with your organization's digital resources.  There is also a web server, Apache Kafka Event Bus, an Open Lineage Proxy and a PostgreSQL server to play with.

![What is included](egeria-workspaces.svg)

As you activate [Egeria's solutions](/egeria-solutions), the associate runtimes are connected to Egeria.

The following solutions are activated automatically:

* [Leveraging Egeria](/egeria-solutions/leveraging-egeria/overview)
* [Leveraging Your Files](/egeria-solutions/leveraging-files/overview)

In addition, Egeria's *quick start* configuration is active.  This gives you:

* **qs-view-server** providing the [external REST APIs](/services/omvs) for accessing Egeria's services.
* **qs-metadata-store** providing the metadata repository services backed by [PostgreSQL storage](/connectors/repository/postgres/overview).
* **qs-integration-daemon** for running the integration connectors that synchronize metadata with different tools and runtimes.
* **qs-engine-host** for running governance services both on the open metadata and the connected tools and runtimes.

![What is inside](egeria-workspaces-exposed.svg)