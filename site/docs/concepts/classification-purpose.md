---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Classification Purpose

Every classification type in the [open metadata types](/types) has a *classification purpose*.  The purpose says why the classification type exists: whether it helps Egeria manage the element, records statistics about it, describes how it should be governed, or refines what kind of element it is.

The purpose is stored in the `classificationPurpose` attribute of the classification type's definition (`ClassificationDef`).  For the metadata repositories it is informational: they store it and return it with the type, but nothing in the repository depends on it.  The Open Metadata Framework (OMF) defines the values in the `OpenMetadataClassificationPurpose` enumeration, records them against each classification type in `OpenMetadataType`, and returns them in the `classificationPurpose` property of `OpenMetadataClassificationDef` when a type is retrieved through the APIs.

It is the classification counterpart of the [relationship purpose](/concepts/relationship-purpose).

## Values

| Purpose | Meaning |
|---|---|
| [MANAGEMENT](#management) | Used by Egeria to manage the element: its anchor, its zone membership, whether it is a template, a memento, a promise or a known duplicate.  These classifications are mostly maintained by Egeria itself. |
| [ANALYTICAL](#analytical) | Statistics and profiles gathered about the element and its use, typically maintained by Egeria's own services such as the nanny connectors. |
| [GOVERNANCE](#governance) | The governance characteristics of the element - its owner, confidentiality, criticality, retention and so on.  These determine which governance actions are appropriate for the element. |
| [GOVERNANCE_IMPLEMENTATION](#governance_implementation) | Identifies the element as a place where governance is implemented: a control, verification or enforcement point, or a policy management point. |
| [CATEGORY](#category) | Refines the kind of element: the kind of project, collection, location, log, interface or glossary term.  This is the default purpose. |
| [DESCRIPTIVE](#descriptive) | Adds detail about the shape or encoding of the data that the element describes, such as a primary key or a calculated value. |

## How the purpose is used

### Visualization and tools

The purpose groups the classifications on an element by audience.  A user interface can show the GOVERNANCE and CATEGORY classifications to a business user, keep the MANAGEMENT classifications for an administrator, and show the ANALYTICAL classifications on a dashboard.  Tools can read the purpose from the type definition rather than keeping their own lists of classification names.

### Governance

The GOVERNANCE classifications are the ones to consult when deciding which governance actions apply to an element.  The GOVERNANCE_IMPLEMENTATION classifications show where in a process those actions are carried out.

### Inheritance

A classification type that has no purpose of its own uses the purpose of its nearest super type.  For example, a new subtype of *ProjectKind* is a CATEGORY classification.  If you add classification types in an extension archive, set the purpose explicitly.

## Classification types by purpose

Each classification type links to the page of the type model that defines it.

### MANAGEMENT

Used by Egeria to manage the element: its anchor, its zone membership, whether it is a template, a memento, a promise or a known duplicate.  These classifications are mostly maintained by Egeria itself.  There are 10 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [Anchors](/types/0/0010-Base-Model/) |  | OpenMetadataRoot |
| [ConsolidatedDuplicate](/types/4/0465-Duplicate-Processing/) |  | Referenceable |
| [Incomplete](/types/7/0790-Incomplete/) |  | Referenceable |
| [KnownDuplicate](/types/4/0465-Duplicate-Processing/) |  | Referenceable |
| [Memento](/types/0/0010-Base-Model/) |  | OpenMetadataRoot |
| [MetamodelInstance](/types/5/0570-Metamodels/) |  | Referenceable |
| [Promise](/types/0/0010-Base-Model/) |  | OpenMetadataRoot |
| [Template](/types/0/0011-Templates/) |  | OpenMetadataRoot |
| [TemplateSubstitute](/types/0/0011-Templates/) |  | OpenMetadataRoot |
| [ZoneMembership](/types/4/0424-Governance-Zones/) |  | OpenMetadataRoot |

### ANALYTICAL

Statistics and profiles gathered about the element and its use, typically maintained by Egeria's own services such as the nanny connectors.  There are 6 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [GovernanceMeasurements](/types/4/0450-Governance-Rollout/) |  | Referenceable |
| [MemberPopularityProfile](/types/7/0795-Usage-Activity/) |  | Referenceable |
| [RunMetrics](/types/2/0215-Software-Components/) |  | Process, GovernanceActionProcessStep |
| [UsageActivity](/types/7/0795-Usage-Activity/) |  | Referenceable |
| [UserAccountProfile](/types/2/0227-Keystores/) |  | SecretsCollection |
| [ZoneMembershipProfile](/types/4/0424-Governance-Zones/) |  | GovernanceZone |

### GOVERNANCE

The governance characteristics of the element - its owner, confidentiality, criticality, retention and so on.  These determine which governance actions are appropriate for the element.  There are 15 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [AccountingCodes](/types/7/0715-Digital-Business/) |  | Referenceable |
| [BusinessSignificant](/types/7/0760-Business-Lineage/) |  | Referenceable |
| [Confidence](/types/4/0422-Governed-Data-Classifications/) |  | Referenceable |
| [Confidentiality](/types/4/0422-Governed-Data-Classifications/) |  | Referenceable |
| [Criticality](/types/4/0422-Governed-Data-Classifications/) |  | Referenceable |
| [DataScope](/types/2/0210-Data-Stores/) |  | Referenceable |
| [DigitalResourceOrigin](/types/7/0755-Ultimate-Source-Destination/) |  | Referenceable |
| [GeneratedTarget](/types/2/0280-Software-Development-Assets/) |  | Referenceable |
| [GovernanceExpectations](/types/4/0450-Governance-Rollout/) |  | Referenceable |
| [Impact](/types/4/0422-Governed-Data-Classifications/) |  | Referenceable |
| [Ownership](/types/4/0445-Governance-Roles/) |  | Referenceable |
| [ProjectClassification](/types/1/0130-Projects/) |  | Project |
| [Retention](/types/4/0422-Governed-Data-Classifications/) |  | Referenceable |
| [SecurityListMembership](/types/4/0423-Security-Definitions/) |  | UserIdentity |
| [SecurityTags](/types/4/0423-Security-Definitions/) |  | Referenceable |

### GOVERNANCE_IMPLEMENTATION

Identifies the element as a place where governance is implemented: a control, verification or enforcement point, or a policy management point.  There are 10 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [ControlPoint](/types/4/0460-Governance-Execution-Points/) | ExecutionPoint | Referenceable |
| [EnforcementPoint](/types/4/0460-Governance-Execution-Points/) | ExecutionPoint | Referenceable |
| [ExecutionPoint](/types/4/0460-Governance-Execution-Points/) |  | Referenceable |
| [PolicyAdministrationPoint](/types/4/0435-Policy-Management-Capabilities/) | PolicyManagementPoint | Referenceable |
| [PolicyDecisionPoint](/types/4/0435-Policy-Management-Capabilities/) | PolicyManagementPoint | Referenceable |
| [PolicyEnforcementPoint](/types/4/0435-Policy-Management-Capabilities/) | PolicyManagementPoint | Referenceable |
| [PolicyInformationPoint](/types/4/0435-Policy-Management-Capabilities/) | PolicyManagementPoint | Referenceable |
| [PolicyManagementPoint](/types/4/0435-Policy-Management-Capabilities/) |  | Referenceable |
| [PolicyRetrievalPoint](/types/4/0435-Policy-Management-Capabilities/) | PolicyManagementPoint | Referenceable |
| [VerificationPoint](/types/4/0460-Governance-Execution-Points/) | ExecutionPoint | Referenceable |

### CATEGORY

Refines the kind of element: the kind of project, collection, location, log, interface or glossary term.  This is the default purpose.  There are 46 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [AbstractConcept](/types/3/0340-Dictionary/) |  | GlossaryTerm |
| [ActivityDescription](/types/3/0340-Dictionary/) |  | GlossaryTerm |
| [AuditLog](/types/4/0455-Exception-Management/) |  | Asset |
| [Campaign](/types/1/0130-Projects/) | ProjectKind | Project |
| [CanonicalVocabulary](/types/3/0310-Glossary/) | CollectionKind | Glossary |
| [ClassWord](/types/4/0438-Naming-Standards/) |  | Referenceable |
| [CloudPlatform](/types/0/0090-Cloud-Platforms-and-Services/) |  | SoftwareServerPlatform |
| [CloudProvider](/types/0/0090-Cloud-Platforms-and-Services/) |  | Host |
| [CloudService](/types/0/0090-Cloud-Platforms-and-Services/) |  | SoftwareCapability |
| [CloudTenant](/types/0/0090-Cloud-Platforms-and-Services/) |  | SoftwareServer |
| [CollectionKind](/types/0/0021-Collections/) |  | Collection |
| [ContextDefinition](/types/3/0360-Contexts/) |  | GlossaryTerm |
| [CyberLocation](/types/0/0025-Locations/) |  | Location |
| [DataSharingAgreement](/types/7/0711-Agreements/) | CollectionKind | Agreement |
| [DataValueMeaning](/types/3/0340-Dictionary/) |  | GlossaryTerm |
| [EditingCollection](/types/3/0385-Controlled-Glossary-Development/) | CollectionKind | Collection |
| [ElementSupplement](/types/3/0395-Supplementary-Properties/) |  | GlossaryTerm |
| [ExceptionBacklog](/types/4/0455-Exception-Management/) |  | Asset |
| [Experiment](/types/1/0130-Projects/) | ProjectKind | Project |
| [FixedLocation](/types/0/0025-Locations/) |  | Location |
| [GlossaryProject](/types/3/0390-Glossary-Projects/) | ProjectKind | Project |
| [GovernanceProject](/types/4/0417-Governance-Projects/) | ProjectKind | Project |
| [Investigation](/types/1/0130-Projects/) | ProjectKind | Project |
| [LineageLog](/types/4/0455-Exception-Management/) |  | Asset |
| [ListenerInterface](/types/2/0212-Deployed-APIs/) |  | DeployedAPI |
| [LogAnalysis](/types/4/0455-Exception-Management/) |  | Asset |
| [MeteringLog](/types/4/0455-Exception-Management/) |  | Asset |
| [MobileResource](/types/0/0025-Locations/) |  | Referenceable |
| [Modifier](/types/4/0438-Naming-Standards/) |  | Referenceable |
| [NamingStandardsVocabulary](/types/4/0438-Naming-Standards/) | CollectionKind | Glossary |
| [PersonalProject](/types/1/0130-Projects/) | ProjectKind | Project |
| [PrimeWord](/types/4/0438-Naming-Standards/) |  | Referenceable |
| [ProjectKind](/types/1/0130-Projects/) |  | Project |
| [PublisherInterface](/types/2/0212-Deployed-APIs/) |  | DeployedAPI |
| [Question](/types/3/0340-Dictionary/) |  | GlossaryTerm |
| [ReferenceData](/types/5/0545-Reference-Data/) |  | Referenceable |
| [RequestResponseInterface](/types/2/0212-Deployed-APIs/) |  | DeployedAPI |
| [ReusableTechnique](/types/2/0280-Software-Development-Assets/) |  | Referenceable |
| [ScopingCollection](/types/3/0385-Controlled-Glossary-Development/) | CollectionKind | Collection |
| [SecureLocation](/types/0/0025-Locations/) |  | Location |
| [SecurityLog](/types/4/0455-Exception-Management/) |  | Asset |
| [SoftwarePackageManifest](/types/0/0030-Operating-Platforms/) |  | Referenceable |
| [StagingCollection](/types/3/0385-Controlled-Glossary-Development/) | CollectionKind | Collection |
| [StudyProject](/types/1/0130-Projects/) | ProjectKind | Project |
| [Task](/types/1/0130-Projects/) | ProjectKind | Project |
| [Taxonomy](/types/3/0310-Glossary/) | CollectionKind | Glossary |

### DESCRIPTIVE

Adds detail about the shape or encoding of the data that the element describes, such as a primary key or a calculated value.  There are 6 classification types with this purpose.

| Classification type | Super type | Valid for |
|---|---|---|
| [CalculatedValue](/types/5/0512-Derived-Schema-Elements/) |  | SchemaElement |
| [DataAssetEncoding](/types/2/0210-Data-Stores/) |  | DataAsset |
| [InstanceMetadata](/types/5/0550-Instance-Metadata/) |  | Referenceable |
| [ObjectIdentifier](/types/5/0580-Data-Dictionaries/) |  | Referenceable |
| [PrimaryKey](/types/5/0534-Relational-Schemas/) |  | RelationalColumn, DataField |
| [TypeEmbeddedAttribute](/types/5/0505-Schema-Attributes/) |  | SchemaAttribute |

!!! education "Further information"

    - [Relationship Purpose](/concepts/relationship-purpose) describes the purposes of the relationship types.
    - [Anchor](/concepts/anchor) describes the anchor grouping that the *Anchors* classification records.
    - [Governance Zone](/concepts/governance-zone) describes the zones that the *ZoneMembership* classification records.

--8<-- "snippets/abbr.md"
