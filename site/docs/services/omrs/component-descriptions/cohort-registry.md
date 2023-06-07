<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cohort Registry

The OMRS *Cohort Registry* resides in each *[cohort member](/concepts/cohort-member)*. It is responsible for registering a member with a specific *[open metadata repository cohort](../cohort.md)* and maintaining a list of the other members of this cohort.

The registration process is managed by exchanging [Registry Events](/concepts/cohort-events) over the [Cohort Topic](/concepts/cohort-events).

The cohort registry maintains its record of the membership of the cohort in a [Cohort Registry Store](/concepts/cohort-registry-store-connector).

## Further information

* [Configuring the cohort registry in an OMAG Server](/concepts/cohort-member)
* [Overview of a cohort](/features/cohort-operations/overview)


---8<-- "snippets/abbr.md"