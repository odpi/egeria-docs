<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Egeria project. -->

# Restore from Backup Profile

The technology under test supports the receipt of events from a backup archive.  In normal operating situations, a repository only receives instance events for elements from other repositories.  The exception is when a backup archive is loaded, when the repository receives metadata instances from any repository represented in the archive.

## Restore metadata element

???+ assertion "Assertions"
    | ID | Description |
    |---|---|
    | [`restore-from-backup-01` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-conformance-suite/open-metadata-conformance-suite-server/src/main/java/org/odpi/openmetadata/conformance/tests/repository/instances/TestRestoreFromBackup.java){ target=gh } | entity restored. This tests the [`saveReferenceCopy` :material-github:](https://github.com/odpi/egeria/blob/main/open-metadata-implementation/repository-services/repository-services-apis/src/main/java/org/odpi/openmetadata/repositoryservices/connectors/stores/metadatacollectionstore/OMRSMetadataCollection.java){ target=gh } method of the `OMRSMetadataCollection` interface. | 

