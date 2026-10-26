<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Proactive cataloguing

Most catalogs are filled *reactively*: something is deployed, it runs for a while, and eventually someone discovers it and adds it to the catalog - or nobody does.  Until then it has no recorded owner, nobody knows what data it holds, it is outside the scope of every security and compliance check, and it may not be patched.  Unrecorded systems are one of the most common ways that attackers get in, and one of the main reasons that incidents take a long time to investigate.

*Proactive cataloguing* reverses this.  The catalog entry is created as part of deploying the capability, so the catalog is up to date from the moment a new system, server or software component goes into production, and it is updated each time that capability changes.

## Why it matters for security

An accurate inventory is the foundation for almost every technical security control:

* a system cannot be monitored, scanned or tested if the security team does not know that it exists.
* a vulnerability announced in a software package can only be fixed everywhere if you know where that package is running.
* access cannot be reviewed for a system with no owner.
* an incident cannot be scoped if nobody knows what depends on the affected system.

The same inventory serves the IT infrastructure team, the data governance team (which needs to know where data lives), the privacy team (which needs to know which systems hold personal data) and the business (which needs to know what its information supply chains depend on).  It is worth maintaining it once, in a place they can all use.

## Cataloguing as part of deployment

The most reliable time to capture information about a deployment is when it is happening, because the pipeline doing the deployment already knows what it is deploying, where, and what it was built from.

The [DevOps Pipeline API](/services/omvs/devops-pipeline/overview) lets a deployment pipeline, or the engineer running it, record this as it happens:

* the hosts, operating platforms and software package manifests that make up each standard software stack, and which hosts each stack has been rolled out to.
* the storage volumes attached to hosts and the data stores that use them.
* the networks and gateways through which each service can be reached.
* how each software component was built - its source, its dependencies and the build that produced it.
* which parts of the infrastructure are provided by a cloud provider and so are not completely under the organization's control.

Together these record the *software supply chain*.  The package manifest for each standard deployment is a *software bill of materials* (SBOM): a collection with the [*SoftwarePackageManifest*](/types/0/0030-Operating-Platforms) classification, whose members are *SoftwareArchive* collections containing the *RunnableSoftwareComponent* elements they deliver.  Dependencies between the components are recorded with *DependentSoftwareComponent*, and *SoftwareSource* traces in-house software back to the software components and modules in the source repository.  When a vulnerability is reported in a package, these relationships show which operating platforms and deployed resources include it.

The [*OperatingPlatform*](/types/0/0030-Operating-Platforms) definitions of the standard deployments can also drive the software updater that keeps hosts on the current version.  This makes it possible to run a rolling update of system software, so that security patches are applied systematically across the estate.

[Templates](/features/templated-cataloguing/overview) make it easy to catalog new systems consistently, and [integration connectors](/concepts/integration-connector) can catalog the contents of a new system - its databases, files or topics - as soon as it is running.

## Catching what arrives outside the process

Not every system will come through the pipeline.  Departments buy their own solutions, suppliers install equipment, and acquisitions bring whole estates with them.  [Metadata discovery](/features/metadata-discovery/overview) and survey services can find systems and resources that are running but not catalogued, so that the gap between what is registered and what is actually there can be measured and closed.

## Governing the process

Proactive cataloguing works best when it is a stated obligation rather than a good habit.  Typical governance definitions include:

* an obligation that every system holding company data, or supporting a business process, is recorded in the systems inventory - with its owner, purpose, data holdings, service level and recovery objective - before it enters production.
* an obligation that every change to a production system follows one recorded path, so that what is running can always be explained by what was approved.
* a metric comparing the systems that are registered with the systems that are discovered, broken down by how each was found, so that the route by which unregistered systems arrive can be located and fixed.

!!! summary "Usage"
    Proactive cataloguing moves the effort of maintaining the inventory to the point where the information is already known, and backs it with discovery to catch what is missed.  The result is an inventory that the security team can rely on - and that every other team can use.

## Examples

* [Cataloguing Infrastructure](/practices/coco-pharmaceuticals/scenarios/cataloguing-infrastructure/overview) shows Gary Geeke loading Coco Pharmaceuticals' systems inventory into Egeria, including the systems of two acquired companies.
* [DevOps Cataloguing](/practices/coco-pharmaceuticals/scenarios/devops-cataloguing/overview) shows Lemmie Stage building the cataloguing into the deployment pipelines.
* [Assuring IT Systems Security](/practices/coco-pharmaceuticals/scenarios/assuring-it-systems-security/overview) shows how the security team uses the resulting inventory.

--8<-- "snippets/abbr.md"
