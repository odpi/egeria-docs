<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Coco Pharmaceuticals Content Pack

The *CocoComboArchive* supplies metadata to support the [Coco Pharmaceuticals scenarios](/practices/coco-pharmaceuticals/). It is a useful content pack to load when experimenting with Egeria's capabilities since it provides examples of many types of open metadata.  In addition, this metadata is also available in the following archives that are used in the[Open Metadata Labs](/education/open-metadata-labs/overview/) where different subsets of this metadata are loading into each of the servers.

* *CocoBusinessSystemsArchive* provides a catalog of the business systems and the lineage between them and the load of their data into the data lake.  This archive simulates the type of metadata expected from an ETL tool suite.  It is intended for **cocoMDS5** in the open metadata labs but can be used in any server.

* *CocoOrganizationArchive* - provides the profiles, user identifies and team of the featured personas of Coco Pharmaceuticals.

* *CocoClinicalTrialsTemplatesArchive* - provides the template assets used for onboarding weekly patient measurements during a clinical trial.

* *CocoGovernanceProgramArchive* - provides the metadata to describe Coco Pharmaceuticals governance program.

* *CocoGovernanceEngineDefinitionsArchive* - provides the metadata to describe Coco Pharmaceuticals three governance engines: `AssetGovernance`, `AssetDiscovery` and `AssetQuality`.

* *CocoSustainabilityArchive* - provides the base definitions for Coco Pharmaceutical's sustainability initiative.

* *CocoTypesArchive* - provides additional types for Coco Pharmaceuticals.  These are `BiopsyScope` Enum, `BiopsyReport` Entity, `BiopsySupportingEvidence` Relationship and `ReviewedByClinicalTrials` Classification.


## CocoOrganizationArchive contents

The Coco Pharmaceuticals' department hierarchy:

![The Coco Pharmaceuticals' Department Hierarchy](organization-hierarchy.svg)

The Coco Pharmaceuticals' valid values for defining an employee.

![The Coco Pharmaceuticals' Valid values for defining an employee](organization-valid-values.svg)

## CocoSustainabilityArchive contents

Extensions to the organization structure to support sustainability:

![New organization](sustainability-organization.svg)

New sustainability roles:

![Sustainability Roles](sustainability-roles.svg)

New glossary for sustainability terminology.

![Sustainability Glossary](sustainability-glossary.svg)

## CocoClinicalTrialsTemplatesArchive contents

Clinical trial templates:

![Clinical Trial Templates](clinical-trials-templates.svg)

## CocoGovernanceProgramArchive contents

Governance program definition:

![Governance Program Definition](governance-program.svg)

## CocoGovernanceEngineDefinitionsArchive contents

![Governance Engine Definitions](governance-engines.svg)

--8<-- "snippets/abbr.md"