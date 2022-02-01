<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the ODPi Egeria project. -->

  
# Open Metadata and Governance Frameworks

The open metadata and governance frameworks define the interfaces for pluggable components.  These
components provide much of the customization and technology integration points offered by the open metadata and governance
implementation.  

The open metadata and governance frameworks supported by Egeria are as follows:
  
* *[Audit Log Framework (ALF)](/frameworks/alf/overview)* provides interfaces and classes to
enable connectors of all types to support natural language diagnostic messages for both
exceptions and the audit log.

* *[Open Connector Framework (OCF)](/frameworks/ocf/overview)* provides the interfaces and base implementations for components
(called [connectors](/concepts/connector)) that access data-related assets.
OCF connectors also provide detailed metadata about the assets they access.

* *[Governance Action Framework (GAF)](/frameworks/gaf/overview)* provides the interfaces and base implementations for components
(called governance action services) that take action to assess and correct a situation that is harmful to the data,
or the organization in some way.

* *[Open Discovery Framework (ODF)](/frameworks/odf/overview)* provides the interfaces and base implementations for components
(called discovery services) that access data-related assets and extract characteristics 
about the data that can be stored in an open metadata repository.

**Note:** Both the discovery services and the governance actions are specialized OCF connectors, making the OCF the *only* plug-in mechanism in the open metadata and governance technology.

--8<-- "snippets/abbr.md"
