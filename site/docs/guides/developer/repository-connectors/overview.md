<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Writing Repository Connectors

Egeria provides a number of pre-built [cohort members](/egeria-docs/concepts/cohort-members).

One of them, the [repository proxy](/egeria-docs/concepts/repository-proxy) provides a simple way to integrate a third party server into a cohort by creating an [OMRS Repository Connector and optional Event Mapper Connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh } to map between the third party APIs/events and the repository service's equivalents

A more bespoke integration involves:

- Creating an [OMRS repository connector and optional event mapper connector :material-github:](https://github.com/odpi/egeria/tree/master/open-metadata-implementation/adapters/open-connectors/repository-services-connectors/open-metadata-collection-store-connectors){ target=gh }
- Designing how to configure the OMRS Services for your metadata repository. Typically, this is done by extending the existing administration services of the metadata repository, but Egeria also offers some pre-built [administration services](/egeria-docs/guides/admin/guide) that can be used or modified.
- Plugging the OMRS and any administration services into the metadata repository's security module so that requests to the server can be secured against unauthorized access.
- Integrating the OMRS, administration and security capability into your product.

There are different integration patterns available to help you choose the best approach for your product. Each method is optimized for specific use cases and so the metadata repository can only play a full role in the open metadata use cases if it supports all integration methods. These are:

- Support for an OMRS repository connector to allow open metadata API calls to the repository to create, query, update and delete metadata stored in the repository.
    - The OMRS connectors support the [Open Connector Framework (OCF)](/egeria-docs/frameworks/ocf) to provide a call interface to the metadata repositories.
    - The OMRS Repository Connector API is a standard interface for all metadata repositories. This enables services such as the Enterprise OMRS Repository Connector to interact with 1 or many metadata repositories through the same interface.  
    - The connection configuration it passes to the OCF determines which type of OMRS connector is returned by the OCF.
- Support for the OMRS event notifications that are used to synchronize selective metadata between the metadata repositories.


[^1]: You may want to see the [OMRS metamodel](/egeria-docs/guides/developer/metamodel/overview) for more details on the granularity of metadata exchange.

--8<-- "snippets/abbr.md"
