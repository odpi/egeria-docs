---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Display Integrator Open Metadata Integration Service (OMIS)

The Display Integrator OMIS supports the exchange of displayed data such as reports and forms along with their related
schema and
connection information between an external system supporting the data display
and the open metadata ecosystem.

It supports a type of [integration connector](/egeria-docs/concepts/integration-connector)
that are able to create assets representing forms, reports and queries
along with their associated display schema .

## Forms and Reports

Figure 1 shows the types of metadata for forms and reports that integrators connectors can create with this integration service.


![Figure 1 - Form](/egeria-docs/services/omas/data-manager/form-model.svg)
<br><br>
![Figure 1 - Report](/egeria-docs/services/omas/data-manager/report-model.svg)
> **Figure 1:** Forms and Reports metadata supported by the Display Integrator OMIS 

Either can be represented as a set of nested **DataContainers** with specific input and output
**DataFields** use to represent the individual data items. 


## Queries

Integrators connectors can also create queries that support forms and reports with this integration service.
Figure 2 shows the types of metadata for the queries.

![Figure 2 - InformationView](/egeria-docs/services/omas/data-manager/information-view-model.svg)
> **Figure 2:** Query metadata supported by the Display Integrator OMIS 

Queries can also be represented as a set of nested data containers and data fields.

## Open Metadata Types

Figure 3 shows the open metadata types used to represent the metadata for forms, reports and queries
created through this service.

![Figure 3 - Form](/egeria-docs/services/omas/data-manager/form-open-metadata-types.svg)
<br><br>
![Figure 3 - Report](/egeria-docs/services/omas/data-manager/report-open-metadata-types.svg)
<br><br>
![Figure 2 - InformationView](/egeria-docs/services/omas/data-manager/information-view-open-metadata-types.svg)
> **Figure 3:** Form and Report open metadata types supported by the Display Integrator OMIS 

The principle asset types are
[Form](/egeria-docs/types/2/0239-Reports),
[Report](/egeria-docs/types/2/0239-Reports) and
[InformationView](/egeria-docs/types/2/0235-Information-View)
for forms, reports and queries respectively.

If a SoftwareServerCapability such as an
[Application](/egeria-docs/types/0/0050-Applications-and-Processes) or 
[ReportingEngine](/egeria-docs/types/0/0055-Data-Processing-Engines) is defined,
any asset created is automatically linked to it using the
[ServerAssetUse](/egeria-docs/types/0/0045-Servers-and-Assets)
relationship.

When a **DataContainer** is created for a report or a form, it is represented as a
[DisplayDataContainer](/egeria-docs/types/5/0537-Display-Schemas) entity.
**DataFields** are created as
[DisplayDataField](/egeria-docs/types/5/0537-Display-Schemas) entities.

The **DataContainers** and **DataFields** for a queries are represented as
[QueryDataContainer](/egeria-docs/types/5/0537-Display-Schemas) and
[QueryDataField](/egeria-docs/types/5/0537-Display-Schemas) respectively.

All of these types are subtypes of schema attributes that
the [TypeEmbeddedAttribute](/egeria-docs/types/5/0505-Schema-Attributes)
classification [method for defining the schema type](/egeria-docs/guides/developer/mapping-technology/modelling-schemas).

The different subtypes enable metadata searches to narrow the results to this type of display metadata.

When a data container or a data field is attached to a form or report asset, the service automatically inserts the
[AssetSchemaType](/egeria-docs/types/5/0503-Asset-Schema) relationship,
[DisplaySchemaType](/egeria-docs/types/5/0537-Display-Schemas) entity and
[AttributeForSchema](/egeria-docs/types/5/0505-Schema-Attributes) relationship
in between the asset entity and the data container/field entity if not already in place.

Similarly, the combination of
[AssetSchemaType](/egeria-docs/types/5/0503-Asset-Schema) relationship,
[QuerySchemaType](/egeria-docs/types/5/0537-Display-Schemas) entity and
[AttributeForSchema](/egeria-docs/types/5/0505-Schema-Attributes.svg) relationship
is inserted between a query and a data container/field.

When a data field/container is nested inside another, it is 
linked to the structure using the
[NestedSchemaAttribute](/egeria-docs/types/5/0505-Schema-Attributes.svg) relationship.


This integration service is paired with the [Data Manager OMAS](/egeria-docs/services/omas/data-manager/overview).

--8<-- "snippets/abbr.md"