<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# Cohort Registry Store

The *Cohort Registry* resides in each *[cohort member](/egeria-docs/concepts/cohort-member)*.   It is responsible for registering a member with a specific cohort and maintaining a list of the other members of this cohort.

The registration process is managed by exchanging [Registry Events](/egeria-docs/cohort-events#registry-events) over the [Cohort Topic](/egeria-docs/cohort-events#cohort-topics).

The cohort registry maintains its record of the membership of the cohort in a
[Cohort Registry Store](../component-descriptions/connectors/cohort-registry-store-connector.md).

## Further information

* [Configuring the cohort registry in an OMAG Server](../../../admin-services/docs/concepts/cohort-member.md)
* [Overview of a cohort](../open-metadata-repository-cohort.md)


--8<-- "snippets/abbr.md"