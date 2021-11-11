<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Entity Proxies Profile

The technology under test is able to store stubs for entities to use on relationships when the full entity is not available.

## Store entity proxies

The technology under test supports the storage of metadata instances that are proxies for instances from other repositories in the cohort.

## Retrieve entity proxies

The technology under test supports the command to retrieve a proxy instance of a metadata instance.

## Entity proxy locking

The technology under test ensures metadata instances that are proxies for instances from other repositories can not be updated.

## Retrieve entity proxies

The technology under test ensures that proxy instances are removed from its repository with integrity when the master copy is deleted.
