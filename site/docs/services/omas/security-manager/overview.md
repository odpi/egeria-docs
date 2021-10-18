<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

--8<-- "snippets/content-status/in-development.md"

# Security Manager Open Metadata Access Service (OMAS)

The Security Officer Open Metadata Access Service (OMAS) provides access to metadata for policy enforcement frameworks such as Apache Ranger.  This API simplifies the internal models and structures of the open metadata type model and related structure for the consumers.

As an example, Apache Ranger needs to know how a particular entity is classified so that the classification can be used within a policy (rule). The [Open Metadata Types](/egeria-docs/types) define a complex graph-oriented model, within which classifications can be multi level - for example a column may be classified as `employee_salary` whilst `employee_salary` itself may be classified as `SPI`. Ranger however just needs to know that the column is SPI, not how we got there. So we convert this complex model into something much more operationally-focused in the form of [SecurityTags](/egeria-docs/types/4/0423-Security-Tags) and deliver that over the API. The implementation will follow this graph, and build up a list of all tags that are appropriate to use. Note that in the case of Ranger it is actually the tagsync process that will call the Security Manager OMAS for this classification information

Ranger can do this today, but via a large number of individual requests to retrieve types and entities. Rather than these lower level queries to the metadata repository services, the Security Manager OMAS offers result sets to make queries more efficient, and more appropriate notifications.

More details on Apache Ranger's [Tag Propagation Process](../security-manager/TagPropogation/TagPropogation.md) is found in the docs directory by following the link.


The caller of this interface may be the security manager itself, or via an integration connector hosted inthe [Security Integrator OMIS](/egeria-docs/services/omis/security-integrator) running in an [integration daemon](/egeria-docs/concepts/integration-daemon) if the security manager does not support open metadata directly.



--8<-- "snippets/abbr.md"
