<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->


The *cohort registry store* maintains information about the servers registered in an *[open metadata repository cohort](/concepts/cohort-member)*.  It resides in each *cohort member* and represents that member's view of the cohort membership.   It contains the registration information sent by this member and the responses received from the other members.

![Cohort registry store connector](/connectors/runtime/cohort-registry-store-connector.svg)

Inside the cohort registry store there is one local registration record describing the information sent to the other members of the cohort and a list of remote registration records received from the other members of the cohort.

![Internal structure for the information stored inside a single cohort registry store](/connectors/runtime/cohort-registry-store-contents.svg)

A *[cohort registry store connector](/concepts/cohort-registry-store-connector)* manages the persistence of the cohort registry store.  Egeria uses a connector to allow different storage methods for different deployment environments.  Each member may choose their own implementation of the cohort registry store connector.

---8<-- "snippets/abbr.md"
