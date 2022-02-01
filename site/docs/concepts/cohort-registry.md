---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cohort Registry

The *Cohort Registry* resides in each *[cohort member](/concepts/cohort-member)*.   It is responsible for registering a member with a specific cohort and maintaining a list of the other members of this cohort.

The registration process is managed by exchanging [Registry Events](/concepts/cohort-events#registry-events) over the [Cohort Topic](/concepts/cohort-events#cohort-topics).

The cohort registry maintains its record of the membership of the cohort in a [Cohort Registry Store](/concepts/cohort-registry-store-connector).

## Further information

* [Overview of a cohort](/features/cohort-operation/overview)


--8<-- "snippets/abbr.md"