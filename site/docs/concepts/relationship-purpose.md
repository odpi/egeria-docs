---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Relationship Purpose

Every relationship type in the [open metadata types](/types) has a *relationship purpose*.  The purpose says why the relationship type exists: whether the element at the other end is part of the element, information attached to it, or something independent that it is linked to.

The purpose is stored in the `relationshipPurpose` attribute of the relationship type's definition (`RelationshipDef`).  For the metadata repositories it is informational: they store it and return it with the type, but nothing in the repository depends on it.  The Open Metadata Framework (OMF) defines the values in the `OpenMetadataRelationshipPurpose` enumeration, records them against each relationship type in `OpenMetadataType`, and returns them in the `relationshipPurpose` property of `OpenMetadataRelationshipDef` when a type is retrieved through the APIs.

## Values

| Purpose | Meaning | Followed from an anchored element? |
|---|---|---|
| [STRUCTURAL](#structural) | Part of what the element is: the attributes of a schema, the endpoint of a connection, the steps of a process. | Yes |
| [ATTACHMENT](#attachment) | Information attached to, and owned by, the element: comments, notes, ratings, search keywords. | Yes |
| [ASSIGNMENT](#assignment) | Links the element to independent information that describes or governs it: an owner's role, a catalog template, a governance definition. | No |
| [MEMBERSHIP](#membership) | Groups or organizes elements without owning them, such as collection membership. | No |
| [ASSOCIATION](#association) | Relates elements that keep their own identity, often in one direction, such as a foreign key between columns. | No |
| [PEER](#peer) | A purely peer link between elements of equal standing, such as related glossary terms. | No |
| [DEFINITION](#definition) | Links a design or specification to its implementation. | No |
| [DEPLOYMENT](#deployment) | Where something runs or is stored. | No |
| [DESIGN_LINEAGE](#design_lineage) | LineageRelationship and its subtypes: how data and control are designed to flow. | No |
| [ACTION](#action) | Information gathered so that action can be taken, such as the targets of a governance action or the subscribers to a notification. | No |
| [ACTIVITY](#activity) | A record of action that took place. | No |

## How the purpose is used

### Operations that start on an anchored element

An [anchor](/concepts/anchor) is the root of a group of elements that are managed as one object.  Each member of the group carries the anchor's unique identifier in its `Anchors` classification.  When an operation starts on the anchor itself, it takes the whole group: every element anchored to it, whatever relationships link them.  The purpose does not come into it.

The purpose matters when an operation starts on an element that is anchored to something else, such as one table in a database schema.  The operation must take the element and the parts that belong to it, but not its parent, its siblings or the things it happens to be linked to.  All of these carry the same anchor identifier, so the Anchors classification alone cannot tell them apart.  Egeria uses the direction and purpose of each relationship instead:

* It follows a relationship only to the element at end 2 (downstream of the starting element).  Its parent and anything else upstream are never taken.
* It follows only relationships whose purpose is **STRUCTURAL** or **ATTACHMENT**.  An element linked for any other purpose is independent of the starting element, even when it shares the same anchor.
* It only takes elements that share the starting element's anchor.  The anchor itself is never taken.
* An element whose Anchors classification names an element that has already been taken is always taken too, whichever end of the relationship it is at.  For example, an endpoint is anchored to its connection.

This rule applies to three operations:

* **Delete** - deleting a table also deletes its columns and the comments attached to them.  It does not delete a column in another table that one of its columns refers to with a foreign key, or the role of a person assigned to it.
* **Archive** - archiving uses the same rule to decide which elements receive the [Memento](/concepts/memento) classification.  All of them get one shared archive suffix on their qualified names.
* **Create from template** - when the [template](/concepts/template) is a member of another element's group, the new element copies only the template's downstream structure.  Relationships into the rest of the template's group are not reproduced.

Elements that are their own anchor, such as most assets, are not affected: they are not taken by these operations whatever the purpose of the relationship.  A [cascaded delete](/concepts/cascade-delete) is the way to remove a hierarchy of independent elements, such as a folder and its files.

### Inheritance

A relationship type that has no purpose of its own uses the purpose of its nearest super type.  A relationship type with no purpose at all is treated as independent and is never followed.  If you add relationship types in an extension archive, set the purpose explicitly.

### Visualization and tools

The purpose groups the relationships around an element by meaning: what it is made of, what is attached to it, who and what governs it, and where it runs.  User interfaces and tools can read it from the type definition to lay out or filter a view of the element.

## Relationship types by purpose

Each relationship type links to the page of the type model that defines it.

### STRUCTURAL

Part of what the element is: the attributes of a schema, the endpoint of a connection, the steps of a process.  There are 30 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [APIHeader](/types/5/0536-API-Schemas/) | APIOperation | SchemaType |
| [APIOperations](/types/5/0536-API-Schemas/) | APISchemaType | APIOperation |
| [APIRequest](/types/5/0536-API-Schemas/) | APIOperation | SchemaType |
| [APIResponse](/types/5/0536-API-Schemas/) | APIOperation | SchemaType |
| [ArchiveContents](/types/2/0226-Archive-Files/) | ArchiveFile | Collection |
| [AssetConnection](/types/2/0205-Connection-Linkage/) | Asset | Connection |
| [AttributeForSchema](/types/5/0505-Schema-Attributes/) | ComplexSchemaType | SchemaAttribute |
| [ConceptBeadAttributeLink](/types/5/0571-Concept-Models/) | ConceptBead | ConceptBeadAttribute |
| [ConceptBeadRelationshipEnd](/types/5/0571-Concept-Models/) | ConceptBeadRelationship | ConceptBead |
| [ConnectToEndpoint](/types/2/0201-Connectors-and-Connections/) | Connection | Endpoint |
| [DataClassComposition](/types/5/0541-Data-Classes-and-Data-Grains/) | DataClass | DataClass |
| [DetailedProcessingAction](/types/4/0485-Data-Processing-Purposes/) | DataProcessingAction | DataProcessingAction |
| [EmbeddedConnection](/types/2/0205-Connection-Linkage/) | VirtualConnection | Connection |
| [GovernanceActionProcessFlow](/types/4/0462-Governance-Action-Processes/) | GovernanceActionProcess | GovernanceActionProcessStep |
| [LinkedExternalSchemaType](/types/5/0507-External-Schema-Type/) | SchemaElement | SchemaType |
| [MapFromElementType](/types/5/0511-Map-Schema-Elements/) | SchemaElement | SchemaType |
| [MapToElementType](/types/5/0511-Map-Schema-Elements/) | SchemaElement | SchemaType |
| [MemberDataField](/types/5/0580-Data-Dictionaries/) | DataStructure | DataField |
| [NestedDataField](/types/5/0581-Data-Field-Implementation/) | DataField | DataField |
| [NestedSchemaAttribute](/types/5/0505-Schema-Attributes/) | SchemaAttribute | SchemaAttribute |
| [PortDelegation](/types/2/0217-Ports/) | Port | Port |
| [ProcessHierarchy](/types/2/0215-Software-Components/) | Process | Process |
| [ProcessPort](/types/2/0217-Ports/) | Process | Port |
| [RelationalDBSchema](/types/5/0534-Relational-Schemas/) | RelationalDBSchemaTypeList | RelationalDBSchemaType |
| [ResourceConnection](/types/2/0205-Connection-Linkage/) | Referenceable | Connection |
| [Schema](/types/5/0503-Asset-Schema/) | Referenceable | SchemaType |
| [SchemaTypeOption](/types/5/0501-Schema-Elements/) | SchemaElement | SchemaType |
| [SolutionComponentPort](/types/7/0735-Solution-Ports-and-Wires/) | SolutionComponent | SolutionPort |
| [SolutionComposition](/types/7/0730-Solution-Components/) | SolutionComponent | SolutionComponent |
| [SolutionPortDelegation](/types/7/0735-Solution-Ports-and-Wires/) | SolutionPort | SolutionPort |

### ATTACHMENT

Information attached to, and owned by, the element: comments, notes, ratings, search keywords.  There are 15 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [AnnotationExtension](/types/6/0610-Annotations/) | Annotation | Annotation |
| [AssociatedAnnotation](/types/6/0610-Annotations/) | OpenMetadataRoot | Annotation |
| [AttachedComment](/types/1/0150-Feedback/) | Referenceable | Comment |
| [AttachedLike](/types/1/0150-Feedback/) | Referenceable | Like |
| [AttachedNoteLog](/types/1/0160-Notes/) | Referenceable | NoteLog |
| [AttachedNoteLogEntry](/types/1/0160-Notes/) | NoteLog | Action |
| [AttachedRating](/types/1/0150-Feedback/) | Referenceable | Rating |
| [AttachedTag](/types/1/0150-Feedback/) | Referenceable | InformalTag |
| [ContactThrough](/types/1/0111-Contact-Details/) | ActorProfile | ContactDetails |
| [Contribution](/types/1/0125-Contribution/) | ActorProfile | ContributionRecord |
| [ReferenceableFacet](/types/0/0020-Property-Facets/) | Referenceable | PropertyFacet |
| [SearchKeywordLink](/types/0/0012-Search-Keywords/) | Referenceable | SearchKeyword |
| [SpecificationPropertyAssignment](/types/5/0545-Reference-Data/) | Referenceable | ValidValueDefinition |
| [SupplementaryProperties](/types/3/0395-Supplementary-Properties/) | Referenceable | GlossaryTerm |
| [TranslationLink](/types/0/0022-Translations/) | OpenMetadataRoot | TranslationDetail |

### ASSIGNMENT

Links the element to independent information that describes or governs it: an owner's role, a catalog template, a governance definition.  There are 37 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [AgreementActor](/types/7/0711-Agreements/) | Agreement | Actor |
| [ApprovedPurpose](/types/4/0485-Data-Processing-Purposes/) | Referenceable | DataProcessingPurpose |
| [AssignmentScope](/types/1/0120-Assignment-Scopes/) | Referenceable | Referenceable |
| [AssociatedLog](/types/2/0223-Events-and-Logs/) | Referenceable | Asset |
| [AssociatedSecurityList](/types/4/0423-Security-Definitions/) | SecurityAccessControl | SecurityList |
| [AssociatedSkillSet](/types/1/0145-Perspectives/) | Actor | SkillSet |
| [CatalogTemplate](/types/0/0011-Templates/) | OpenMetadataRoot | OpenMetadataRoot |
| [Certification](/types/4/0482-Certifications/) | Referenceable | CertificationType |
| [CitedDocumentLink](/types/0/0016-Cited-Documents/) | Referenceable | CitedDocument |
| [ContractLink](/types/7/0711-Agreements/) | Agreement | CitedDocument |
| [DataProcessingSpecification](/types/4/0485-Data-Processing-Purposes/) | Referenceable | DataProcessingDescription |
| [DataValueAssignment](/types/5/0540-Data-Value-Specifications/) | Referenceable | DataValueSpecification |
| [DigitalSubscriber](/types/7/0712-Digital-Subscription/) | Referenceable | DigitalSubscription |
| [Exception](/types/4/0455-Exception-Management/) | Referenceable | ExceptionType |
| [ExternalIdLink](/types/0/0017-External-Identifiers/) | OpenMetadataRoot | EXTERNAL_ID |
| [ExternalReferenceLink](/types/0/0014-External-References/) | Referenceable | ExternalReference |
| [GovernanceResults](/types/4/0450-Governance-Rollout/) | GovernanceMetric | Asset |
| [GovernedBy](/types/4/0401-Governance-Definitions/) | Referenceable | GovernanceDefinition |
| [ITInfrastructureProfile](/types/1/0117-IT-Profiles/) | Referenceable | ITProfile |
| [ITProfileRoleAppointment](/types/1/0118-Actor-Roles/) | ITProfileRole | ITProfile |
| [ImplementationResource](/types/7/0737-Solution-Implementation/) | Referenceable | Referenceable |
| [KnownLocation](/types/0/0025-Locations/) | Referenceable | Location |
| [License](/types/4/0481-Licenses/) | Referenceable | LicenseType |
| [MediaReference](/types/0/0015-Linked-Media-Types/) | Referenceable | RelatedMedia |
| [MoreInformation](/types/0/0019-More-Information/) | Referenceable | Referenceable |
| [PersonRoleAppointment](/types/1/0118-Actor-Roles/) | PersonRole | Person |
| [ProfileIdentity](/types/1/0110-Actors/) | ActorProfile | UserIdentity |
| [ReferenceValueAssignment](/types/5/0545-Reference-Data/) | Referenceable | ValidValueDefinition |
| [ResourceList](/types/0/0019-More-Information/) | Referenceable | Referenceable |
| [ResourcePermissions](/types/4/0423-Security-Definitions/) | SecretsCollection | SecurityAccessControl |
| [ScopedBy](/types/1/0120-Assignment-Scopes/) | Referenceable | Referenceable |
| [SecretsCollectionSecurityList](/types/4/0423-Security-Definitions/) | SecretsCollection | SecurityList |
| [SemanticAssignment](/types/3/0370-Semantic-Assignment/) | Referenceable | GlossaryTerm |
| [SolutionComponentActor](/types/7/0730-Solution-Components/) | Actor | SolutionComponent |
| [TeamRoleAppointment](/types/1/0118-Actor-Roles/) | TeamRole | Team |
| [UserAccount](/types/4/0423-Security-Definitions/) | SecretsCollection | UserIdentity |
| [ValidValuesAssignment](/types/5/0545-Reference-Data/) | Referenceable | ValidValueDefinition |

### MEMBERSHIP

Groups or organizes elements without owning them, such as collection membership.  There are 13 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [AgreementItem](/types/7/0711-Agreements/) | Agreement | Referenceable |
| [CollectionMembership](/types/0/0021-Collections/) | Collection | Referenceable |
| [DataValueHierarchy](/types/5/0540-Data-Value-Specifications/) | DataValueSpecification | DataValueSpecification |
| [DependentContextEvent](/types/4/0475-Context-Events/) | ContextEvent | ContextEvent |
| [NestedDesignPattern](/types/5/0595-Design-Patterns/) | DesignPattern | DesignPattern |
| [NestedLocation](/types/0/0025-Locations/) | Location | Location |
| [ProjectHierarchy](/types/1/0130-Projects/) | Project | Project |
| [RegisteredIntegrationConnector](/types/4/0464-Dynamic-Integration-Groups/) | IntegrationGroup | IntegrationConnector |
| [SubjectAreaHierarchy](/types/4/0425-Subject-Areas/) | SubjectArea | SubjectArea |
| [SupportedGovernanceService](/types/4/0461-Governance-Engines/) | GovernanceEngine | GovernanceService |
| [TeamStructure](/types/1/0115-Teams/) | Team | Team |
| [ValidValueMember](/types/5/0545-Reference-Data/) | ValidValueDefinition | ValidValueDefinition |
| [ZoneHierarchy](/types/4/0424-Governance-Zones/) | GovernanceZone | GovernanceZone |

### ASSOCIATION

Relates elements that keep their own identity, often in one direction, such as a foreign key between columns.  There are 29 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [AcceptedAnswer](/types/1/0150-Feedback/) | Comment | Comment |
| [AnnotationMatch](/types/6/0610-Annotations/) | Annotation | OpenMetadataRoot |
| [BusinessCapabilityDependency](/types/7/0715-Digital-Business/) | BusinessCapability | BusinessCapability |
| [ConceptBeadExtension](/types/5/0571-Concept-Models/) | ConceptBead | ConceptBead |
| [ConsistentValidValues](/types/5/0545-Reference-Data/) | ValidValueDefinition | ValidValueDefinition |
| [ConsolidatedDuplicateLink](/types/4/0465-Duplicate-Processing/) | Referenceable | Referenceable |
| [DataProcessingTarget](/types/4/0485-Data-Processing-Purposes/) | DataProcessingAction | Referenceable |
| [DependentSoftwareComponent](/types/2/0282-Released-Software-Components/) | RunnableSoftwareComponent | RunnableSoftwareComponent |
| [ForeignKey](/types/5/0534-Relational-Schemas/) | RelationalColumn | RelationalColumn |
| [GovernanceMechanism](/types/4/0420-Governance-Controls/) | GovernancePolicy | GovernanceControl |
| [GovernanceResponse](/types/4/0415-Governance-Responses/) | GovernanceDriver | GovernancePolicy |
| [GraphEdgeLink](/types/5/0533-Graph-Schemas/) | GraphEdge | GraphVertex |
| [IsAConceptBead](/types/5/0571-Concept-Models/) | ConceptBead | ConceptBead |
| [LabeledRelationship](/types/0/0010-Base-Model/) | OpenMetadataRoot | OpenMetadataRoot |
| [LinkedDataField](/types/5/0581-Data-Field-Implementation/) | DataField | DataField |
| [LinkedMedia](/types/2/0221-Document-Stores/) | MediaFile | MediaFile |
| [PermittedProcessing](/types/4/0485-Data-Processing-Purposes/) | DataProcessingPurpose | DataProcessingDescription |
| [ProjectDependency](/types/1/0130-Projects/) | Project | Project |
| [Regulator](/types/4/0405-Governance-Drivers/) | Regulation | Organization |
| [RelatedContextEvent](/types/4/0475-Context-Events/) | ContextEvent | ContextEvent |
| [RelatedDesignPattern](/types/5/0595-Design-Patterns/) | DesignPattern | DesignPattern |
| [ReportDependency](/types/2/0239-Reports/) | Report | Report |
| [ResourceProfileData](/types/6/0620-Resource-Profiling/) | ResourceProfileLogAnnotation | Asset |
| [RoledRelationship](/types/0/0010-Base-Model/) | OpenMetadataRoot | OpenMetadataRoot |
| [SampleData](/types/0/0010-Base-Model/) | Referenceable | Asset |
| [SoftwarePackageDependency](/types/0/0030-Operating-Platforms/) | Asset | Collection |
| [UsedInContext](/types/3/0360-Contexts/) | GlossaryTerm | Referenceable |
| [ValidValueAssociation](/types/5/0545-Reference-Data/) | ValidValueDefinition | ValidValueDefinition |
| [ValidValuesMapping](/types/5/0545-Reference-Data/) | ValidValueDefinition | ValidValueDefinition |

### PEER

A purely peer link between elements of equal standing, such as related glossary terms.  There are 12 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [AdjacentLocation](/types/0/0025-Locations/) | Location | Location |
| [Antonym](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |
| [GovernanceControlLink](/types/4/0420-Governance-Controls/) | GovernanceControl | GovernanceControl |
| [GovernanceDriverLink](/types/4/0405-Governance-Drivers/) | GovernanceDriver | GovernanceDriver |
| [GovernancePolicyLink](/types/4/0415-Governance-Responses/) | GovernancePolicy | GovernancePolicy |
| [ISARelationship](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |
| [Peer](/types/1/0112-People/) | Person | Person |
| [PeerDuplicateLink](/types/4/0465-Duplicate-Processing/) | Referenceable | Referenceable |
| [PreferredTerm](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |
| [RelatedTerm](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |
| [ReplacementTerm](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |
| [Synonym](/types/3/0350-Related-Terms/) | GlossaryTerm | GlossaryTerm |

### DEFINITION

Links a design or specification to its implementation.  There are 18 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [ConceptDesign](/types/5/0571-Concept-Models/) | Referenceable | ConceptModel |
| [ConnectionConnectorType](/types/2/0201-Connectors-and-Connections/) | Connection | ConnectorType |
| [DataDescription](/types/5/0580-Data-Dictionaries/) | Referenceable | Collection |
| [DataStructureDefinition](/types/5/0580-Data-Dictionaries/) | CertificationType | DataStructure |
| [DataValueDefinition](/types/5/0540-Data-Value-Specifications/) | Referenceable | DataValueSpecification |
| [DigitalSupport](/types/7/0715-Digital-Business/) | BusinessCapability | Referenceable |
| [ImplementedBy](/types/7/0737-Solution-Implementation/) | Referenceable | Referenceable |
| [RegulationCertificationType](/types/4/0482-Certifications/) | Regulation | CertificationType |
| [ReusableTechniqueUse](/types/2/0280-Software-Development-Assets/) | Referenceable | Referenceable |
| [SchemaAttributeDefinition](/types/5/0581-Data-Field-Implementation/) | DataField | SchemaAttribute |
| [SchemaTypeDefinition](/types/5/0581-Data-Field-Implementation/) | DataStructure | SchemaType |
| [SemanticDefinition](/types/3/0370-Semantic-Assignment/) | Referenceable | GlossaryTerm |
| [SmartQuery](/types/7/0725-Smart-Collections/) | ResultsSet | SavedQuery |
| [SoftwareSource](/types/2/0282-Released-Software-Components/) | Asset | SoftwareComponent |
| [SolutionDesign](/types/7/0740-Solution-Blueprints/) | Referenceable | SolutionBlueprint |
| [SpecializedDesignPattern](/types/5/0595-Design-Patterns/) | DesignPattern | DesignPattern |
| [TypedByConceptBead](/types/5/0571-Concept-Models/) | ConceptBeadAttribute | ConceptBead |
| [ValidValuesImplementation](/types/5/0545-Reference-Data/) | ValidValueDefinition | Referenceable |

### DEPLOYMENT

Where something runs or is stored.  There are 16 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [APIEndpoint](/types/2/0212-Deployed-APIs/) | DeployedAPI | Endpoint |
| [AttachedStorage](/types/0/0036-Storage/) | Referenceable | StorageVolume |
| [CapabilityAssetUse](/types/0/0045-Servers-and-Assets/) | SoftwareCapability | Asset |
| [DeployedOn](/types/0/0035-Complex-Hosts/) | ITInfrastructure | Asset |
| [FolderHierarchy](/types/2/0220-Files-and-Folders/) | FileFolder | FileFolder |
| [HostClusterMember](/types/0/0035-Complex-Hosts/) | HostCluster | Host |
| [LinkedFile](/types/2/0220-Files-and-Folders/) | FileFolder | DataFile |
| [MetadataCohortPeer](/types/0/0057-Software-Services/) | CohortMember | MetadataRepositoryCohort |
| [NestedFile](/types/2/0220-Files-and-Folders/) | FileFolder | DataFile |
| [NetworkGatewayLink](/types/0/0070-Networks-and-Gateways/) | NetworkGateway | Network |
| [OperatingPlatformManifest](/types/0/0030-Operating-Platforms/) | OperatingPlatform | Collection |
| [OperatingPlatformUse](/types/0/0030-Operating-Platforms/) | OperatingPlatform | ITInfrastructure |
| [ServerEndpoint](/types/0/0026-Endpoints/) | ITInfrastructure | Endpoint |
| [StoredOn](/types/2/0210-Data-Stores/) | DataStore | StorageVolume |
| [SupportedSoftwareCapability](/types/0/0042-Software-Capabilities/) | ITInfrastructure | SoftwareCapability |
| [VisibleEndpoint](/types/0/0070-Networks-and-Gateways/) | Endpoint | Network |

### DESIGN_LINEAGE

LineageRelationship and its subtypes: how data and control are designed to flow.  There are 14 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [ControlFlow](/types/7/0750-Data-Passing/) | Referenceable | Referenceable |
| [DataFlow](/types/7/0750-Data-Passing/) | Referenceable | Referenceable |
| [DataLineageRelationship](/types/0/0010-Base-Model/) | Referenceable | Referenceable |
| [DataMapping](/types/7/0770-Lineage-Mapping/) | Referenceable | Referenceable |
| [DataSetContent](/types/2/0210-Data-Stores/) | DataSet | Referenceable |
| [DerivedSchemaTypeQueryTarget](/types/5/0512-Derived-Schema-Elements/) | SchemaElement | SchemaElement |
| [DigitalProductDependency](/types/7/0710-Digital-Products/) | DigitalProduct | DigitalProduct |
| [InformationSupplyChainLink](/types/7/0720-Information-Supply-Chains/) | Referenceable | Referenceable |
| [LineageMapping](/types/7/0770-Lineage-Mapping/) | Referenceable | Referenceable |
| [LineageRelationship](/types/0/0010-Base-Model/) | OpenMetadataRoot | OpenMetadataRoot |
| [ProcessCall](/types/7/0750-Data-Passing/) | Referenceable | Referenceable |
| [SolutionLinkingWire](/types/7/0735-Solution-Ports-and-Wires/) | Referenceable | Referenceable |
| [UltimateDestination](/types/7/0755-Ultimate-Source-Destination/) | Referenceable | Referenceable |
| [UltimateSource](/types/7/0755-Ultimate-Source-Destination/) | Referenceable | Referenceable |

### ACTION

Information gathered so that action can be taken, such as the targets of a governance action or the subscribers to a notification.  There are 7 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [CatalogTarget](/types/4/0464-Dynamic-Integration-Groups/) | IntegrationConnector | OpenMetadataRoot |
| [GovernanceActionExecutor](/types/4/0462-Governance-Action-Processes/) | GovernanceActionType | GovernanceEngine |
| [MonitoredResource](/types/4/0451-Notifications/) | NotificationType | Referenceable |
| [NextGovernanceActionProcessStep](/types/4/0462-Governance-Action-Processes/) | GovernanceActionProcessStep | GovernanceActionProcessStep |
| [NotificationSubscriber](/types/4/0451-Notifications/) | NotificationType | Referenceable |
| [RequestForActionTarget](/types/6/0690-Request-For-Action/) | RequestForAction | Referenceable |
| [TargetForGovernanceAction](/types/4/0462-Governance-Action-Processes/) | GovernanceAction | OpenMetadataRoot |

### ACTIVITY

A record of action that took place.  There are 12 relationship types with this purpose.

| Relationship type | End 1 | End 2 |
|---|---|---|
| [ActionRequester](/types/0/0013-Actions/) | Referenceable | Action |
| [ActionTarget](/types/0/0013-Actions/) | Action | OpenMetadataRoot |
| [Actions](/types/0/0013-Actions/) | Referenceable | Action |
| [ContextEventEvidence](/types/4/0475-Context-Events/) | ContextEvent | Referenceable |
| [ContextEventForTimelineEffects](/types/4/0475-Context-Events/) | Referenceable | ContextEvent |
| [ContextEventImpact](/types/4/0475-Context-Events/) | Referenceable | ContextEvent |
| [CrowdSourcingContribution](/types/1/0155-Crowd-Sourcing/) | Referenceable | Actor |
| [ImpactedResource](/types/4/0470-Incident-Reporting/) | Referenceable | IncidentReport |
| [ReportOriginator](/types/2/0239-Reports/) | Referenceable | Report |
| [ReportSubject](/types/2/0239-Reports/) | OpenMetadataRoot | Report |
| [ReportedAnnotation](/types/6/0610-Annotations/) | SurveyReport | Annotation |
| [SourcedFrom](/types/0/0011-Templates/) | OpenMetadataRoot | OpenMetadataRoot |

!!! education "Further information"

    - [Anchor](/concepts/anchor) describes the anchor grouping.
    - [Relationship Category](/concepts/uni-multi-link) describes the cardinality rules for relationships.
    - [Cascade Delete](/concepts/cascade-delete) describes deleting a hierarchy of independent elements.

--8<-- "snippets/abbr.md"
