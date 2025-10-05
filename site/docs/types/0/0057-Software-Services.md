<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project 2020. -->

# 0057 Software Services

![UML](0057-Software-Services.svg)

## SoftwareService entity

A *SoftwareService* entity provides a well-defined software component that can be called by remote clients across the network. They may offer a request-response or an event-driven interface or both.

## CohortMember entity

A *CohortMember* service describes the cohort services provided by the [Open Metadata Repository Services (OMRS)](/services/omrs) that runs in a [cohort member server](/concepts/cohort-member).

## MetadataRepositoryCohort entity

A *MetadataRepositoryCohort* entity describes a peer to peer metadata sharing exchange between open metadata repositories.  This is call an [Open Metadata Repository Cohort](/features/cohort-operation/overview).

## MetadataCohortPeer relationship

A *MetadataCohortPeer* links a cohort member to its cohort(s).


--8<-- "snippets/abbr.md"
