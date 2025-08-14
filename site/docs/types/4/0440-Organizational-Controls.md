<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

# 0440 Organizational Controls

Organizational controls describe governance controls that are typically implemented through people, organizational structures and responsibilities plus manual procedures and rules.  

![UML](0440-Organizational-Controls.svg)

## GovernanceProcedure entity

*GovernanceProcedure* describes a manual procedure that is performed under certain situations.  An example would be a visual check of a person's government identity document such as a passport or driving license.  The [Actors](/types/1/0110-Actors) that perform this procedure would be linked to a governance responsibility using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.

## Methodology entity

*Methodology* identifies the externally documented methodology (aka method) that is to be used.  For example, software development has the [Agile Software development method](https://en.wikipedia.org/wiki/Agile_software_development).  If this was a key method to govern the software development process, the *Methodology* entity would describe how this method will be used in the organization.  A software development [project](/types/1/0130-Projects) would be linked to the agile methodology entity using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship. 

## GovernanceResponsibility entity

*GovernanceResponsibility* describes a responsibility that is assigned to a person or team.  It could be a requirement to take certain action in specific circumstances, or to make particular types of decisions or to give approvals for particular actions.  An [Actor](/types/1/0110-Actors ) would be linked to a governance responsibility using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.

## TermsAndConditions entity

The *TermsAndConditions* entity identifies the rules relating the use of an element (or the associated real-world [resource](/concepts/resource)). The [GovernedBy](/types/4/0401-Governance-Definitions) relationship attaches the terms and conditions to element that details where these terms and conditions apply. For example, they may be attached to [Agreements](/types/7/0711-Agreements).

*LicenseType* and *CertificationType* are special types of *TermsAndConditions* entities.

### LicenseType entity

The data economy brings licensing to data and metadata.  Even open data typically has a license. The license type defines the permitted uses and other requirements for using the resource. The [GovernedBy](/types/4/0401-Governance-Definitions) relationship is used to link the license type to the resources where the license applies, and the [License](/types/4/0481-Licenses) relationship is used to link the consumers of the resource to the license.  

For example, if the resource was a [Digital Product](/types/7/0710-Digital-Product), it would be linked to the *LicenseType* using the *GovernedBy* relationship. The consumers of the digital product would be granted a license to the digital product using the *License* relationship.


### CertificationType entity

Many regulations and industry bodies define certifications that can confirm a level of support, capability or competence in an aspect of a digital organization’s operation. Having certifications may be necessary to operating legally or may be a business advantage.  Certifications can also be used to communicate that data is of a particular quality level, or a process has completed successfully.

The description of the requirements for particular type of certification is described using a *CertificationType* entity.  It is linked to the elements that require the certification using the [GovernedBy](/types/4/0401-Governance-Definitions) relationship.  The [Certification](/types/4/0482-Certifications) relationship is used to identify the resources that meet the standards laid out in the certification type and so are considered "certified".

## SubjectAreaDefinition entity

[Subject areas](/concepts/subject-area) are topic areas that are important to the organization.  Typically, they cover data that is widely shared across the organization and there is business value in maintaining consistency in the data values in each copy. The role of the subject area definition is to act as a collection point for all the subject area materials. This includes:

* A [glossary of terms](/types/3/0310-Glossary) that describe the key concepts in the subject area.
* Lists and hierarchies of [reference data](/types/5/0545-Reference-Data) that relate to particular data values in the subject area.
* [Quality rules](/types/4/0430-Technical-Controls) for specific data values in the subject area.
* Preferred [data structures and schemas](/types/5/0501-Schema-Elements).

Creating the subject area definition is a declaration that data about this subject area is of significance to the organization and will be receiving special attention.

The subject area definition can be linked to resources where it applies via the [*GovernanceBy*](/types/4/0401-Governance-Definitions) relationship.  Other parts of the subject area definition are described in [model 0425](/types/4/0425-Subject-Areas).

## DataProcessingPurpose entity

Privacy regulations such as the EU's General Data Processing Regulation (GDPR) require data subjects to agree the processing that is permitted on their data. Often the processing is summarized in terms of the outcome (or the "purpose" of the processing) with the option to drill down into the details of how this processing is achieved.

*DataProcessingPurpose* is use to document a particular purpose.  [Model 0485](/types/4/0485-Data-Processing-Purposes) provides additional types to capture the detailed data processing descriptions associated with a *DataProcessingPurpose* and record who or what has permission to perform the specified processing.


--8<-- "snippets/abbr.md"