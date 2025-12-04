---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project 2020. -->

--8<-- "snippets/content-status/stable.md"

# Integration Daemon Services

The *integration daemon services* provide the implementation of the [Integration Daemon](/concepts/integration-daemon) OMAG Server which is responsible for operating the [integration connector](/concepts/integration-connector).


![Figure 1](/services/integration-daemon-in-action.svg)
> **Figure 1:** Integration daemon exchanging metadata with many types of third party technologies


Inside the Integration Daemon, the [integration connectors](/concepts/integration-connector) manage the exchange of metadata with third party technology. 

![Figure 2](/services/integration-daemon-internals.svg)
> **Figure 2:** Inside the integration daemon showing the context object that provides the specialist API to the integration connectors


## Further information

* [Trouble shooting issues](/guides/diagnostic/integration-daemon-diagnostic-guide) with the integration daemon
* [Configuring](/concepts/integration-daemon) the integration daemon
* Learning more about [integration connectors](/concepts/integration-connector)
* [Solutions](/solutions/data-manager-integration) using the integration daemon

--8<-- "snippets/abbr.md"