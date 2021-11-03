---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Event mapper connectors

The *event mapper connector* provides a common API for
specific implementations of OMRS event mappers to implement.

Event mappers are needed in [repository proxy](/egeria-docs/concepts/repository-proxy)
servers if the third party technology that it is
integrating into the open metadata repository cohort
also has its own mechanisms for maintaining metadata.

The event mapper's role is to notify the cohort of any changes to
the metadata mastered in the third party repository
that has occurred through the third party technology's own mechanisms.

Since each event mapper is tied to a third party
technology, core Egeria does not supply any implementations of
this connector. There are, however, the following
implementations available:

- [Event mapper for Apache Atlas :material-github:](https://github.com/odpi/egeria-connector-hadoop-ecosystem){ target=gh }
- [(Experimental) event mapper for IBM Information Governance Catalog :material-github:](https://github.com/odpi/egeria-connector-ibm-information-server){ target=gh }

--8<-- "snippets/abbr.md"
