---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Resource Use

A *resource use* [metadata valid value](/guides/planning/valid-values/overview) describes the difference values used in the *resourceUse* property found in the [ResourceList](/types/0/0019-More_Information) relationship.

Here are some example values.

| Resource Use             | Description                                                                                                                                                                                             |
|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Survey Resource          | Create a survey report that details the content of the real-world resource that is attached to an asset.                                                                                                |
| Catalog Resource         | Extract metadata from the real-world resource and add it to the open metadata repositories.  Ongoing monitoring means that any changes to the resource are reflected in the open metadata repositories. |
| Provision Resource       | Make a change to the real-world resource such as add or copy data.                                                                                                                                      |
| Improve Metadata Element | Improve the information about an element in the open metadata repositories.                                                                                                                             |
| Watch Metadata Element   | Monitor for changes to a metadata element and its related elements and take action if required.                                                                                                         |
| Supporting Team          | A team assigned to support the work associated with the element.                                                                                                                                        |
| Supporting Person        | A person assigned to support the work associated with the element.                                                                                                                                      |
| Hosted Service           | A type of service that can be hosted on this type of server.                                                                                                                                            |
| Hosted Connector         | A type of connector that can be hosted by this type of service/engine.                                                                                                                                  |
| Hosted Governance Engine | A type of governance engine that can be hosted by this type of service.                                                                                                                                 |
| Called Service           | A type of service that may be called by this service.                                                                                                                                                   |


--8<-- "snippets/abbr.md"
