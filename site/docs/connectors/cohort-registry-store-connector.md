---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Cohort registry store connector

The **cohort registry store** stores information about the repositories registered in
the [open metadata repository cohort](/egeria-docs/services/omrs/cohort).  

Each server in the open metadata repository cohort has
a [cohort registry](/egeria-docs/services/omrs/cohort/#cohort-registry) component to manage
its registration with the cohort and maintain the contents of
its local cohort registry store.

The following diagram shows a cohort with two members: notice that each server has its own
cohort registry store - there is no central store.

![Cohort registry stores within an open metadata repository cohort](cohort-registry-stores-in-a-cohort.png)

The logical structure within the cohort registry store is as follows:

![Internal structure for the information stored inside a single cohort registry store](cohort-registry-store-contents.png)

There is one local registration record describing the information sent to
the other members of the cohort and a list of remote registration records received from
the other members of the cohort.

An implementations of this type of connector is located in the
[adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors){ target=gh }
module.

--8<-- "snippets/abbr.md"
