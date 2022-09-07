---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0482 Certifications

Many regulations and industry bodies define certifications that can confirm a level of support, capability or competence in an aspect of a digital organization’s operation. Having certifications may be necessary to operating legally or may be a business advantage.

The certifications awarded can be captured in the metadata repository to enable both use and management of the certification process.  Details of a type of certification are described in a *CertificationType*. The element that is certified is identified with the *Certification* relationship. This relationship is a *multi-link* relationship so multiple certifications, with different conditions, can be defined at one time.

A *CertificationType* that comes from a regulation can be linked to the [element describing the Regulation](/types/4/0405-Governance-Drivers) using the *RegulationCertificationType* relationship type.


![UML](0482-Certifications.svg)

--8<-- "snippets/abbr.md"