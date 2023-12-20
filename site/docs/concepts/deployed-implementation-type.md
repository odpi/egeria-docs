---
hide:
- toc
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Deployed Implementation Type

A *deployed implementation type* is a type of reference data that describes a class of technology that is deployed in an organization's IT landscape.  Its purpose is to describe how technology of this class should be governed and the resources available to do so.  For example:

* An instance of this technology is likely to be catalogued in the open metadata ecosystem using an [asset](/concepts/asset).  The deployed implementation type can define the subtype of the asset to use.  It is also possible to define a template for creating the asset and associate it with the deployed implementation type.
* The governance action processes, governance services and connectors that support this type of technology can be identified.
* The *deployedImplementationType* attribute found in many open metadata types can be set from the matching deployed implementation type reference value.  Having consistent values for the deployedImplementationType attribute makes it possible to retrieve lists of all catalogued technology of a particular class.  The following type definitions include the *deployedImplementationType*:

    * [*Infrastructure*](/types/0/0010-Base-Model)
    * [*DataSet*](/types/0/0010-Base-Model)
    * [*DataStore*](/types/2/0210-Data-Stores)
    * [*DeployedAPI*](/types/2/0212-Deployed-APIs)
    * [*DeployedSoftwareComponent*](/types/2/0215-Software-Components)
    * [*DataFeed*](/types/2/0223-Events-and-Logs)
    * [*SoftwareCapability*](/types/0/0042-Software-Capabilities)
    * [*CloudPlatform*](/types/0/0090-Cloud-Platforms-and-Services)
    * [*ServerPurpose*](/types/0/0041-Server-Purpose)

## Examples of Deployed Implementation Types

--8<-- "snippets/content-packs/deployed-implementation-types.md"

--8<-- "snippets/abbr.md"
