<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cohort Registry Store Connector

The *cohort registry store* maintains information about the servers registered in an *[open metadata repository cohort](/egeria-docs/concepts/cohort-member)*.  It resides in each *cohort member* and represents that member's view of the cohort membership.   It contains the registration information sent by this member and the responses received from the other members.

Figure 1 shows a cohort with two members.  Notice that each server has its own cohort registry store - there is no central store.

![Figure 1: Cohort Registry Stores within a Open Metadata Repository Cohort](cohort-registry-stores-in-a-cohort.png)
> Figure 1: Cohort Registry Stores within a Open Metadata Repository Cohort

Figure 2 shows the logical structure inside the cohort registry store.

![Figure 2: Internal structure for the information stored inside a single cohort registry store](cohort-registry-store-contents.png)
> Figure 2: Internal structure for the information stored inside a single cohort registry store.

There is one local registration record describing the information sent to the other members of the cohort and a list of remote registration records received from the other members of the cohort.

## The connector

Egeria uses a cohort registry store connector to implement the cohort registry store to allow different storage methods for different deployment environments.

The default file-based version of this connector is located in the
[adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/cohort-registry-store-connectors)
module.

---8<-- "snippets/abbr.md"
