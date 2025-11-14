---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Leveraging your Unity Catalog estate

--8<-- "snippets/work-in-progress.md"

Unity Catalog is an operational metadata catalog that supports controlled access to data and models. It provides metadata to describe the organization of the data, and the status of the model versions on a data platform. It overlays a security model to control access to these data sets and models.

Often an organization has multiple Unity Catalog servers, each co-located with a data platform.  These data platforms may have been deployed on premises and/or across various cloud platforms depending on the project dynamics and funding at the time of deployment.  As data accumulates on these platforms, its sheer size makes it difficult to move, and so these platforms have a long life and are rarely consolidated.

Egeria's *Leveraging your Unity Catalog estate* solution gives you oversight across all of your Unity Catalog servers.  This includes:

* Ongoing surveys to give you a view of the types of data and models you have, where they are deployed, and how this is changing over time.
* Selective metadata synchronization between Unity Catalog servers.
* Creation of a full inventory of all of your data and models managed by your Unity Catalog estate, irrespective of their deployment location.  This inventory can be searched, classified and used to drive governance of your Unity Catalog resources.
* Coordination of the deployment of definitions to multiple destinations including Unity Catalog servers.


--8<-- "snippets/abbr.md"