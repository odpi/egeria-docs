<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0482 Certifications

Many regulations and industry bodies define certifications that can confirm a level of support, capability or competence in an aspect of a digital organization’s operation. Having certifications may be necessary to operating legally or may be a business advantage.

The description of a particular type of certification is described using a [*CertificationType*](/types/4/0440-Organizational-Controls) entity.

The certifications awarded can be captured in the metadata repository to enable both use and management of the certification process.  



![UML](0482-Certifications.svg)

## Certification relationship

An element that meets the requests laid out in a certification type is said to be "certified".  This is represented by the *Certification* relationship. This relationship is a *multi-link* relationship so multiple certifications, with different conditions, can be defined at one time.

## RegulationCertificationType relationship

A [*CertificationType*](/types/4/0430-Technical-Controls) that comes from a regulation can be linked to the [element describing the Regulation](/types/4/0405-Governance-Drivers) using the *RegulationCertificationType* relationship type.

--8<-- "snippets/abbr.md"