---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0481 Licenses

The data economy brings licensing to data and metadata.  Even open data typically has a license.

The license will define the permitted uses and other requirements for using the asset.

Details of a type of license are described in a *LicenseType*. Terms and conditions for the license are attached to the *LicenseType* using the [AttachedTermsAndConditions](/types/4/0483-Terms-And-Conditions) relationship.

The element that is licensed is identified with the *License* relationship. This relationship is a *multi-link* relationship so the same license type, with different dates, can be linked to the same element.

![UML](0481-Licenses.svg)



--8<-- "snippets/abbr.md"