---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->
  
# Open Metadata Access Services (OMAS)

The Open Metadata Access Services (OMAS) provide domain-specific services
for data tools, engines and platforms to integrate with open metadata.

The access services are as follows:

| OMAS | Description |
|---|---|
| [analytics-modeling](analytics-modeling) | The Analytics Modeling OMAS configures and manages metadata for modeling analytics and reporting services. |
| [asset-catalog](asset-catalog) | The Asset Catalog OMAS provides search and query capabilities for tools and applications to support an asset catalog function. It supports search requests for assets with specific characteristics and returns summaries of the matching assets, plus methods to allow drill-down into the details of a specific asset to related metadata. |
| [asset-consumer](asset-consumer) | The Asset Consumer OMAS is designed for applications that are using [OCF](/egeria-docs/frameworks/ocf) connectors to access data stores, APIs and functions such as analytics. The Asset Consumer OMAS provides a factory function for the connectors, the ability to retrieve all of the metadata about the asset and the ability to add feedback on the asset. |
| [asset-lineage](asset-lineage) | The Asset Lineage OMAS listens to relevant lineage related events on the enterprise topic level and publishes these on the Asset Lineage OutTopic, combined with relevant context information on the described entities. These events are listened to by the open lineage services governance server. |
| [asset-manager](asset-manager) | The Asset Managner OMAS manages the exchange of metadata with third party metadata catalogs and asset managers. It is typically called by the [Catalog Integrator OMIS](/egeria-docs/services/omis/catalog-integrator) to send and receive asset information, including schemas, profiles, policies and lineage information with a third party asset manager. Typical examples of asset managers include data catalogs that are managing metadata for a collection of data assets for a data-serving solution. |
| [asset-owner](asset-owner) | The Asset Owner OMAS provides services for an asset owner to curate metadata about their asset(s) and understand how these assets are being used and governed. |
| [community-profile](community-profile) | The Community Profile OMAS supports the administration for a community and related user profiles. These communities are involved in reviewing and crowd-sourcing knowledge about the data assets and their use. |
| [data-engine](data-engine) | The Data Engine OMAS provides APIs and events for a data movement/processing engine to record the changes it is making the the data landscape. This information forms a key part of asset lineage. |
| [data-manager](data-manager) | The Data Manager OMAS provides an integration point to enable technologies that manage collections of data such as database servers, file systems, file managers and content managers to publish metadata to the metadata repositories about the changing structures and content stored in the data platform. It is typically called from the [Database Integrator OMIS](/egeria-docs/services/omis/database-integrator) and [Files Integrator OMIS](/egeria-docs/services/omis/files-integrator) integration services. |
| [data-privacy](data-privacy) | The Data Privacy OMAS supports a privacy officer as they manage data privacy in their organization. This includes managing privacy impact assessments and reviews of software services that use personal data as they move through their development, deployment and use. |
| [data-science](data-science) | The Data Science OMAS provides access to metadata for data assets, connections and projects, plus the ability to maintain metadata about data science notebooks and models and log activity during the analytics development process. It is designed for data science and analytics management tools. |
| [design-model](design-model) | The Design Model OMAS provides the ability to manage information from all types of design models. These models may come from tools or be part of a packaged standard. This content is useful for governance, system integration and software development. |
| [dev-ops](dev-ops) | The DevOps OMAS provides services for a DevOps pipeline to query and maintain metadata about systems, processes and software components that are being deployed into the information landscape. |
| [digital-architecture](digital-architecture) | The Digital Architecture OMAS provides the ability to define information standards, definitions, solution blueprints and models for an organization. It is designed for architecture tools. It is able to support the definition and management of a digital service through concept to deployment. |
| [digital-service](digital-service) | The Digital Service OMAS provides services for a managing the lifecycle of an Egeria Digital Service. |
| [discovery-engine](discovery-engine) | The Discovery Engine OMAS provides an API for a discovery engine to access and store metadata from an open metadata repository (or open metadata repository cohort). |
| [governance-engine](governance-engine) | The Governance Engine OMAS provides APIs and events that retrieve and manage metadata for governance engines. Governance engines ensure that the infrastructure supporting the data landscape is operating according to the governance program. For example, the governance engine may be ensuring that individuals and servers only have access to the data they have been authorized to see. |
| [governance-program](governance-program) | The Governance Program OMAS provides the ability to maintain a governance program in the open metadata repositories. It is designed for governance and CDO tools. |
| [it-infrastructure](it-infrastructure) | The IT Infrastructure OMAS provides support for the design and planning of the information infrastructure that supports the data assets. This includes the development of system blueprints that link down to the metadata about real infrastructure components. This metadata helps in the linkage between information governance metadata and IT infrastructure management (ITIL) metadata typically stored in a Configuration Management Database (CMDB). |
| [project-management](project-management) | The Project Management OMAS supports the metadata associated with projects and campaigns. These projects and campaigns may be for governance projects, or generic data use projects. |
| [security-manager](security-manager) | The Security Manager OMAS provides the services to exchange security tags with access control and data protection technology services. It is called by the [Security Integrator OMIS](/egeria-docs/services/omis/security-integrator). |
| [security-officer](security-officer) |The Security Officer OMAS provides the services to support the definition of roles and rules for managing the protection of metadata and assets, plus work with the audit logs captured by the open metadata and governance tools. It is typically used by the security, compliance and auditing teams. |
| [software-developer](software-developer) | The Software Development OMAS provides access to metadata needed to build compliant APIs, data stores and related software components. |
| [stewardship-action](stewardship-action) | The Stewardship Action OMAS provides services for managing exceptions discovered in the information landscape that need correcting. These exceptions may be quality errors, missing or outdated information, invalid licensing, job failures, and many more. The Stewardship Action OMAS also enables the review and triage of the exceptions, simple remediation and status reporting. |
| [subject-area](subject-area) | The Subject Area OMAS is for tools that support subject matter experts who are defining glossaries, reference data and rules around data for a specific subject area, such as "customer data". It supports the development of a comprehensive definition of the subject area and the standards that support it. These definitions can then be folded into the Governance Program, and used by Asset Owner's to improve the findability and understandability of their assets by linking their asset's structure to relevant parts of the subject area definition. |

## Using the OMAS's

![Structure of an Open Metadata Access Service (OMAS)](access-services-overview.png)

The OMAS's run in either a [metadata access point](/egeria-docs/concepts/metadata-access-point)
or a [metadata server](/egeria-docs/concepts/metadata-server).
They can be configured and activated individually or as a complete set.
The [administration services](/egeria-docs/guides/admin/guide) provide
the ability to configure, start and stop the access services.

Each OMAS typically supports a REST API, a topic where it publishes notifications
of interest to its users, and a topic where new metadata requests can be posted to the
OMAS.

It also has a Java client that provides access to its API and topics.
This java client is embedded in the
[governance servers](/egeria-docs/concepts/governance-server) and
[view servers](/egeria-docs/concepts/view-server).
They can also be downloaded and used independently with the 
**[Egeria Client Package](../../open-metadata-distribution/README.md)**.  

--8<-- "snippets/abbr.md"
